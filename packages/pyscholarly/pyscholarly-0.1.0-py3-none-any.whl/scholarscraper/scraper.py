from playwright.async_api import async_playwright
from datetime import datetime
from typing import Dict, List, Optional
import asyncio

class ScholarScraper:
    def __init__(self):
        self._playwright = None
        self._browser = None
        
    async def __aenter__(self):
        self._playwright = await async_playwright().start()
        self._browser = await self._playwright.chromium.launch(headless=True)
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()

    async def _get_page_content(self, url: str) -> str:
        page = await self._browser.new_page()
        try:
            await page.goto(url)
            await page.wait_for_selector("#gsc_rsb_cit")
            content = await page.content()
            return content
        finally:
            await page.close()

    async def get_author_data(self, scholar_id: str) -> Dict:
        url = f"https://scholar.google.com/citations?user={scholar_id}&hl=en"
        content = await self._get_page_content(url)

        page = await self._browser.new_page()
        await page.set_content(content)

        try:
            name = await page.evaluate('() => document.querySelector("#gsc_prf_in")?.innerText || ""')
            
            # Get citation statistics
            stats = {}
            rows = await page.query_selector_all("#gsc_rsb_cit #gsc_rsb_st tbody tr")
            
            for row in rows:
                label_elem = await row.query_selector(".gsc_rsb_sc1 .gsc_rsb_f")
                if label_elem:
                    metric_name = await label_elem.text_content()
                    values = await row.query_selector_all(".gsc_rsb_std")
                    if len(values) >= 2:
                        all_time = await values[0].text_content()
                        recent = await values[1].text_content()
                        stats[metric_name] = {
                            'all': int(all_time),
                            'recent': int(recent)
                        }

            # Get publications
            publications = []
            publication_elements = await page.query_selector_all('#gsc_a_b .gsc_a_tr')
            
            for pub in publication_elements:
                title_elem = await pub.query_selector('.gsc_a_at')
                citations_elem = await pub.query_selector('.gsc_a_ac')
                year_elem = await pub.query_selector('.gsc_a_y .gsc_a_h')

                title = await title_elem.text_content() if title_elem else ''
                citations = await citations_elem.text_content() if citations_elem else '0'
                year = await year_elem.text_content() if year_elem else ''

                publications.append({
                    'title': title,
                    'num_citations': int(citations) if citations.isdigit() else 0,
                    'year': year
                })

            return {
                'name': name,
                'citations': stats.get('Citations', {'all': 0, 'recent': 0}),
                'h_index': stats.get('h-index', {'all': 0, 'recent': 0}),
                'i10_index': stats.get('i10-index', {'all': 0, 'recent': 0}),
                'publications': publications
            }

        finally:
            await page.close()

async def fetch_scholar_data(scholar_id: str) -> Dict:
    """Convenience function to fetch scholar data."""
    async with ScholarScraper() as scraper:
        return await scraper.get_author_data(scholar_id)
