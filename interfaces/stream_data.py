import csv
from aiofiles import open as io_open


class ManageStream:

    @classmethod
    async def upload_stream(cls, rows):

        async with io_open("output.csv", 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'Nome', 'Idade', 'Cidade']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            await writer.writeheader()

            async for item in rows:
                await writer.writerow(item._mapping)

