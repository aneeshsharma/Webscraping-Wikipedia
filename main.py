from pyppeteer import launch
from bs4 import BeautifulSoup
import asyncio

import narrate


async def main(keyword):
    # Create a browser instance and goto Wikipedia
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://en.wikipedia.org/wiki/Main_Page')

    # Type in search keyword and press enter
    await page.type('[id=searchInput]', keyword)

    await page.screenshot({'path': 'main_page.png'})

    # Press enter and Wait for results to load
    await page.keyboard.press('Enter')
    await page.waitForNavigation()

    await page.screenshot({'path': 'results.png'})

    # Get all the links from results
    urls = await page.evaluate('''
        () => {
            const links = document.querySelectorAll('.mw-search-results a')
            const urls = Array.from(links).map(link => link.href)
            return urls
        }
    ''')

    print(urls)

    # Goto the first result
    await page.goto(urls[0])

    await page.screenshot({'path': 'article.png'})

    # Get all text in p tags
    data = await page.evaluate('''
        () => {
            const contents = document.querySelectorAll('.mw-parser-output p')
            const ps = Array.from(contents).map(para => para.innerHTML)
            return ps
        }
    ''')

    # Join the result paras with blank space
    allData = ' '.join(data)

    print(allData)

    # Parse it to text from html
    soup = BeautifulSoup(allData)
    text = soup.get_text().strip()

    print(text)

    # remove square brackets
    finalText = ''
    bracket = 0
    for i in range(min(len(text), 500)):
        if text[i] == '[':
            bracket += 1
        elif text[i] == ']':
            bracket -= 1
        elif bracket == 0:
            finalText += text[i]

    print(finalText)

    narrate.narrate(finalText)

    await browser.close()

while True:
    try:
        keyword = input('? ')
        asyncio.get_event_loop().run_until_complete(main(keyword))
    except EOFError:
        print('bye')
        break
