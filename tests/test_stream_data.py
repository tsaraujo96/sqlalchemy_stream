import pytest

from conftest import SetupTest, TearDownTest
from main import use_case


@pytest.fixture
def resource():
    try:
        SetupTest()
        yield "resource"
    finally:
        TearDownTest()


@pytest.mark.asyncio
async def test_query_of_stream_data(resource):
    await use_case()
