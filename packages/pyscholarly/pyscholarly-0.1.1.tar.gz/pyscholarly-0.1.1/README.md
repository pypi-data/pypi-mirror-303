# ScholarScraper

A Python library for scraping Google Scholar profiles using Playwright.

## Installation

```bash
pip install pyscholarly
```

## Usage

```python
from pyscholarly import fetch_scholar_data
import asyncio

async def main():
    # Fetch data for a Google Scholar profile
    data = await fetch_scholar_data("SCHOLAR_ID")
    print(f"Name: {data['name']}")
    print(f"Total citations: {data['citations']['all']}")
    print(f"h-index: {data['h_index']['all']}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Features

- Fetch author information
- Get citation statistics (all-time and recent)
- Get publication list with citations
- Async/await support
- Clean, typed interface

## Requirements

- Python 3.8+
- Playwright

## License

This project is licensed under the MIT License - see the LICENSE file for details.
