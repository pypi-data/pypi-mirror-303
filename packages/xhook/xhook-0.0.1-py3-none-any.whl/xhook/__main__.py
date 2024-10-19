import asyncio
import json
import uuid
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional

import aiohttp


@dataclass
class WebhookRequest:
    id: str
    created_at: str
    http_url: str
    http_method: str
    http_content_type: str
    http_headers: Dict[str, str]
    http_query_params: Dict[str, str]
    data: Any


WebhookRequestHandler = Callable[[WebhookRequest], None]


class WebhookRequestWorker:
    def __init__(
        self,
        channel_id: str,
        request_handler: WebhookRequestHandler,
        batch_size: Optional[int] = None,
        worker_id: Optional[str] = None,
    ):
        self.channel_id = channel_id
        self.api_base_url = "https://omni.mrfxyz.workers.dev/"
        self.request_handler = request_handler
        self.batch_size = batch_size or 5
        self.worker_id = worker_id or str(uuid.uuid4())
        self.is_running = False
        self.current_requests: List[WebhookRequest] = []
        self._session: Optional[aiohttp.ClientSession] = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def fetch_requests(self) -> List[WebhookRequest]:
        try:
            session = await self._get_session()
            url = f"{self.api_base_url}/api/requests/{self.channel_id}"
            params = {"batchSize": str(self.batch_size), "workerId": self.worker_id}

            async with session.get(url, params=params, timeout=2) as response:
                if response.status == 404:
                    return []
                if response.status == 429:
                    await asyncio.sleep(5)
                    return []
                if not response.ok:
                    raise aiohttp.ClientError(f"HTTP error! status: {response.status}")

                data = await response.json()
                return [WebhookRequest(**request) for request in data]

        except asyncio.TimeoutError:
            print("Timeout while fetching requests, will retry")
            return []
        except aiohttp.ClientError as e:
            print(f"Network error while fetching requests, will retry: {e}")
            return []
        except Exception as e:
            raise e

    async def process_request(self, request: WebhookRequest) -> None:
        try:
            print(f"Starting request {request.id}")

            # Execute the user-provided request handler
            await self.request_handler(request)

            # Mark request as completed
            await self.mark_request_complete(request.id)

            print(f"Completed request {request.id}")
        except Exception as e:
            print(f"Error processing request {request.id}: {e}")
            await self.release_lock(request.id)
            raise e

    async def mark_request_complete(self, request_id: str) -> None:
        session = await self._get_session()
        url = f"{self.api_base_url}/api/request/{request_id}/ack"

        async with session.post(
            url, json={"workerId": self.worker_id}, timeout=5
        ) as response:
            if not response.ok:
                raise Exception(
                    f"Failed to mark request {request_id} as complete: {response.status}"
                )

    async def release_lock(self, request_id: str) -> None:
        try:
            session = await self._get_session()
            url = f"{self.api_base_url}/api/request/{request_id}/no-ack"

            async with session.post(
                url, json={"workerId": self.worker_id}, timeout=5
            ) as response:
                if not response.ok:
                    print(
                        f"Failed to release lock for request {request_id}: {response.status}"
                    )
        except Exception as e:
            print(f"Error releasing lock for request {request_id}: {e}")
            # Don't raise here as this is called in error handling

    async def start(self) -> None:
        if self.is_running:
            print("Worker is already running")
            return

        self.is_running = True
        print(f"Worker {self.worker_id} started")

        while self.is_running:
            try:
                # Fetch new batch of requests
                self.current_requests = await self.fetch_requests()

                if not self.current_requests:
                    # No requests available, wait before trying again
                    await asyncio.sleep(1)
                    continue

                # Process requests sequentially
                for request in self.current_requests:
                    if not self.is_running:
                        break
                    await self.process_request(request)

            except Exception as e:
                print(f"Error in request processing loop: {e}")
                # Wait before retrying
                await asyncio.sleep(2)

    async def stop(self) -> None:
        self.is_running = False
        # Release locks for any current requests
        for request in self.current_requests:
            await self.release_lock(request.id)
        self.current_requests = []

        if self._session and not self._session.closed:
            await self._session.close()

        print(f"Worker {self.worker_id} stopped")

    async def handle_shutdown(self) -> None:
        print("Shutting down worker gracefully...")
        await self.stop()
