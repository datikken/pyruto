import asyncio
from playwright.async_api import async_playwright

base_url = 'https://cointelegraph.com'

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(base_url)
        links = await page.query_selector_all('a')
        f = open('result.txt', 'w')
        for link in links:
            text = await link.get_attribute('href')
            if text == '/':
                continue
            if 'void(0)' in text:
                continue
            if 'https' not in text:
                f.write(f"{base_url}{text}\n")
            else:
                f.write(f"{text}\n")
            print(text)
        f.close()
        await browser.close()

asyncio.run(main())