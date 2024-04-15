from sqlalchemy.ext.asyncio import create_async_engine


def get_connection():
    engine = create_async_engine('sqlite+aiosqlite:///mock_data.db')
    return engine
