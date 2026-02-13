# ------ Web Scraping ------

# The internet is full of a huge amount of data which can be used for different purposes.
# To collect this data we need to know how to scrape data from a website. Web scraping is the process of
# extracting and collecting data from websites and storing it on a local machine or in a database.
# In this section, we will use beautifulsoup and requests package to scrape data. The package version
# we are using is beautifulsoup 4. To start scraping websites you need requests, beautifulSoup4 and a website.

# >>> pip install requests
# >>> pip install beautifulsoup4

# To scrape data from websites, basic understanding of HTML tags and CSS selectors is needed.
# We target content from a website using HTML tags, classes or/and ids.
# Let us import the requests and BeautifulSoup module:
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import json
import re


url = 'https://quotes.toscrape.com/'

# Use the requests get method to fetch the data from url
response = requests.get(url)
# Check the status
status = response.status_code
print('Status Code:', status) # 200 means the fetching was successful

# Use beautifulsoup4 to scrape the page
content = response.content  # get content from page
soup = BeautifulSoup(content, 'html.parser')  # parse html content
print('Title:', soup.title.string)
print('Body:', soup.body)
quotes = soup.find_all('span', class_='text')  # save quotes from website
authors = soup.find_all('small', class_='author')  # save authors of quotes from website

for i in range(len(quotes)):
    print(quotes[i].text)
    print('-',authors[i].text)


#tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
#table = tables[0] # the result is a list, we are taking out data from it
#for td in table.find('tr').find_all('td'):
#    print(td.text)

# ------ Exercises ------

# 1: Scrape the following website and store the data as json file.
print('1:')
url = "https://webscraper.io/test-sites/e-commerce/allinone"

def scrape_ecommerce(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # FIXED selector
    products = soup.select("div.thumbnail")

    data = []

    for product in products:
        # Title
        title_tag = product.select_one("a.title")
        title = title_tag.get_text(strip=True) if title_tag else None

        # Price
        price_tag = product.select_one("h4.pull-right.price")
        price = price_tag.get_text(strip=True) if price_tag else None

        # Description
        desc_tag = product.select_one("p.description")
        description = desc_tag.get_text(strip=True) if desc_tag else None

        # Product URL
        product_url = None
        if title_tag and title_tag.get("href"):
            product_url = "https://webscraper.io" + title_tag["href"]

        # Reviews
        reviews_tag = product.select_one(".ratings .pull-right")
        reviews = int(reviews_tag.get_text(strip=True).split()[0]) if reviews_tag else None

        # Rating (count stars)
        rating = len(product.select(".glyphicon-star"))

        data.append({
            "title": title,
            "price": price,
            "description": description,
            "reviews": reviews,
            "rating": rating,
            "url": product_url
        })

    return data


# Run scraper
products = scrape_ecommerce(url)

# Save JSON
with open("full_ecommerce_data.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print("Saved full_ecommerce_data.json ✔")

# 2:
print('2:')

# 3: Scrape the presidents table and store the data as json.
print('3:')
URL = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

def clean(text):
    """Remove brackets, references, and normalize whitespace."""
    text = re.sub(r"\[[^\]]*\]", "", text)  # Remove [1], [a], etc.
    text = text.replace("\xa0", " ")       # Convert non-breaking spaces
    text = text.replace("–", "-")          # Normalize dashes
    return text.strip()

def extract_vp(cell):
    """Extract VP names from the VP cell, handling links and text."""
    # Prefer names from <a> links
    a_tags = cell.find_all("a")
    names = [clean(a.get_text()) for a in a_tags if clean(a.get_text())]

    # If no links found, fallback to plain text
    if not names:
        text = clean(cell.get_text(" ", strip=True))
        if text not in ["", "-", "—"]:
            names = [text]

    return names

def scrape_presidents():
    resp = requests.get(URL, headers=HEADERS)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    table = soup.find("table", class_="wikitable")
    rows = table.find_all("tr")

    # Find VP column index dynamically
    header = [clean(h.get_text()) for h in rows[0].find_all("th")]
    vp_idx = None
    for i, h in enumerate(header):
        if "vice" in h.lower():
            vp_idx = i
            break

    if vp_idx is None:
        raise Exception("Vice President column not found")

    presidents = []
    last_vp = []

    for row in rows[1:]:
        cols = row.find_all(["td", "th"])
        if len(cols) <= vp_idx:
            continue

        no   = clean(cols[0].get_text())
        name = clean(cols[2].get_text())
        term = clean(cols[3].get_text())
        party = clean(cols[4].get_text())
        election = clean(cols[5].get_text())

        vp_raw = extract_vp(cols[vp_idx])

        # Handle rowspan (VP cell spanning multiple rows)
        if vp_raw:
            last_vp = vp_raw
        vp_final = vp_raw if vp_raw else last_vp

        presidents.append({
            "No": no,
            "Name": name,
            "Term": term,
            "Party": party,
            "Election": election,
            "Vice President": vp_final
        })

    return presidents

# RUN
data = scrape_presidents()

with open("us_presidents.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved! Example output:")
print(json.dumps(data[0], indent=2))  # George Washington
print(json.dumps(data[39], indent=2))  # Ronald Reagan


