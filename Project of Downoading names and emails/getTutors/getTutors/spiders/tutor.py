import scrapy
from bs4 import BeautifulSoup

from ..items import GettutorsItem
class TutorSpider(scrapy.Spider):
    name = "tutor"
    start_urls = ["https://www.math.harvard.edu/peoples-categories/professors-senior-faculty/"]


    def parse(self, response):
        soup = BeautifulSoup(response.text,'html.parser')
        # Step 3: Find all list items in the page
        list_items = soup.findAll('li')
        abj = GettutorsItem()

        # Step 4: Extract and print professor names (assuming they are within 'a' tags)
        for li in list_items:
            a_tag = li.find('a')
            if a_tag:
                abj['name'] = a_tag.text
                abj['url'] = a_tag['href']
                yield{'title': li.text, 'href': a_tag}

        
