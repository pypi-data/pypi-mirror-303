import asyncio

try:
    from redis import Redis
except ImportError:
    Redis = None


class AsyncRedisPipe:
    """
    A utility class for executing Redis commands concurrently and efficiently using pipelines in the backend.

    This class is designed for high-loaded applications that rely on Redis non-pipeline calls. By using pipelines to batch together multiple Redis commands, it can achieve significantly higher throughput than traditional non-pipeline Redis calls.

    Example:
    >>> redis = Redis()
    >>> pipe = AsyncRedisPipe(redis)
    >>> await pipe.set("key", "value")
    >>> await pipe.get("key")
    >>> redis_calls = [pipe.get("key") for i in range(100000)]
    >>> await asyncio.gather(*redis_calls) # 100K Concurrent redis calls

    """

    def __init__(
        self,
        redis: Redis,
        pipe_max_size: int = 200,
        workers: int = 8,
        loop: asyncio.AbstractEventLoop = None,
    ) -> None:
        """
        Args:
            redis (``Redis``):
                The Redis client

            pipe_max_size (``int``, *optional*):
                The maximum number of commands in a single pipeline. Defaults to ``200``.

            workers (``int``, *optional*):
                The number of workers processing the pipeline. Defaults to ``8``.

            loop (:py:class:`asyncio.AbstractEventLoop`, *optional*):
                The event loop to use. Defaults to :py:class:`asyncio.get_event_loop()`.
        """

        if not Redis:
            raise RuntimeError("Redis is not installed. Try pip install redis")

        self.redis = redis
        self.pipe_max_size = pipe_max_size
        self.__queue = asyncio.Queue()
        self.__loop = (
            asyncio.get_event_loop()
            if not isinstance(loop, asyncio.AbstractEventLoop)
            else loop
        )
        self.is_running = True
        self.__worker_tasks = [
            self.__loop.create_task(self.__worker()) for _ in range(workers)
        ]

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return

    async def __worker(self):
        while self.is_running:
            pipe = self.redis.pipeline(False)
            futures = []
            count = 0

            while count <= self.pipe_max_size:
                try:
                    if count == 0:
                        data = await self.__queue.get()
                    else:
                        data = self.__queue.get_nowait()
                        await asyncio.sleep(0)
                except asyncio.QueueEmpty:
                    break
                else:
                    pipe.execute_command(*data[1])
                    futures.append(data[0])
                    count += 1

            self.__loop.create_task(self.__handle_pipe_line(futures, pipe))

    async def __handle_pipe_line(self, futures: list, pipe):
        results = await pipe.execute(False)
        for x, result in enumerate(results):
            if isinstance(result, BaseException):
                futures[x].set_exception(result)
            else:
                futures[x].set_result(result)

    def __getattr__(self, name):
        if name == "delete":
            name = "del"

        def wrapper(*args):
            fut = asyncio.Future()
            args = (name,) + args
            self.__queue.put_nowait((fut, args))
            return fut

        return wrapper

    def close(self):
        """Close the AsyncRedisPipe instance"""
        self.is_running = False
        for worker in self.__worker_tasks:
            worker.cancel()
