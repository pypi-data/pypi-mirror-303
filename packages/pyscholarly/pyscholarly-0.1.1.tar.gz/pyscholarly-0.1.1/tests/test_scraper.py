import pytest
from scholarscraper import ScholarScraper, fetch_scholar_data

@pytest.mark.asyncio
async def test_fetch_scholar_data():
    # Use a known Google Scholar profile
    scholar_id = "u5VcrGgAAAAJ"
    data = await fetch_scholar_data(scholar_id)
    
    assert data is not None
    assert "name" in data
    assert "citations" in data
    assert "h_index" in data
    assert isinstance(data["publications"], list)
