import requests
from bs4 import BeautifulSoup

class AbhiScraper:
    def __init__(self, product_url):
        self.product_url = product_url
        self.soup = None
        self._get_page_content()

    def _get_page_content(self):
        """Fetch and parse the product page HTML."""
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
        }
        response = requests.get(self.product_url, headers=headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.content, 'html.parser')
        else:
            raise Exception(f"Failed to retrieve page. Status code: {response.status_code}")

    def get_title(self):
        """Scrape and return the product title."""
        try:
            title = self.soup.find("span", {"class": "VU-ZEz"}).get_text(strip=True)
            return title
        except AttributeError:
            return "Title not found"

    def get_price(self):
        """Scrape and return the product price."""
        try:
            price = self.soup.find("div", {"class": "_30jeq3 _16Jk6d"}).get_text(strip=True)
            return price
        except AttributeError:
            return "Price not found"

    def get_rating(self):
        """Scrape and return the product rating."""
        try:
            rating = self.soup.find("div", {"class": "_3LWZlK"}).get_text(strip=True)
            return rating
        except AttributeError:
            return "Rating not found"

    def get_reviews(self):
        """Scrape and return the product review count."""
        try:
            reviews = self.soup.find("span", {"class": "_2_R_DZ"}).find_all("span")[1].get_text(strip=True)
            return reviews
        except (AttributeError, IndexError):
            return "Reviews not found"

    def get_all_details(self):
        """Return all available product details: title, price, rating, and reviews."""
        return {
            'title': self.get_title(),
            'price': self.get_price(),
            'rating': self.get_rating(),
            'reviews': self.get_reviews()
        }
