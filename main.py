import asyncio

from memory_profiler import profile
from sqlalchemy import MetaData

from conftest import SetupTest, TearDownTest
from connection import get_connection
from interfaces.stream_data import ManageStream
from repository.repo import QueryRepository


@profile(stream=open('memory_profiler.log', 'w+'))
async def use_case():

    metadata = MetaData()
    engine = get_connection()
    async with engine.connect() as conn:
        await conn.run_sync(metadata.reflect)
        stream_row = await QueryRepository.query_generator(conn, metadata)
        await ManageStream.upload_stream(stream_row)


if __name__ == '__main__':
    try:
        # SetupTest()
        asyncio.run(use_case())
    finally:
        # TearDownTest()
        print("processo finalizado")
