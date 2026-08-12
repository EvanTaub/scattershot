import asyncio
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("worker")


async def main() -> None:
    log.info("worker starting")
    while True:  # noqa: ASYNC110 -- placeholder; Day 8 will replace this
        await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
