import asyncio

import pytest
import pathlib

from navability.services import *


@pytest.mark.asyncio
async def test_all_queries_loaded():
    assert len(GQL_OPERATIONS) > 0
    assert len(GQL_FRAGMENTS) > 0


@pytest.mark.asyncio
async def test_mock_queries_loaded():
    fragments, queries = get_operations(
        f"{pathlib.Path(__file__).parent.resolve()}/common_query_test"
    )
    assert len(fragments) == 4
    assert len(queries) == 1
    # Assert: The tree of fragments are correctly appended to the operation.
    # Ew, ugly way to get the original data back, but it's parsed GQL.
    assert "fragment FRAGMENT_C on Var" in queries["QUERY_A"].data.loc.source.body
