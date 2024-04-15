from sqlalchemy import Table, select
from sqlalchemy.ext.asyncio import AsyncConnection


class QueryRepository:

    @classmethod
    async def query_generator(cls, connection: AsyncConnection, metadata):

        my_table = Table("mock_table", metadata)
        query = select(my_table)

        stream_rows = connection.stream(query)
        return await stream_rows
