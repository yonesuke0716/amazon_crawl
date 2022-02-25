import scrapy
from scrapy_selenium import SeleniumRequest
from time import sleep
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector

class AmazonCrawlSpider(scrapy.Spider):
    name = 'amazon_crawl'

    def start_requests(self):
        yield SeleniumRequest(
            url='http://www.amazon.co.jp/',
            wait_time=3,
            screenshot=False,
            callback=self.parse
        )

    def parse(self, response):
        driver = response.meta['driver']

        # 検索欄の取得
        search_text = driver.find_element_by_xpath('//input[@id="twotabsearchtextbox"]')
        search_text.send_keys('python')
        search_button = driver.find_element_by_xpath('//input[@id="nav-search-submit-button"]')
        search_button.submit()
        sleep(3)

        # タイトルの一覧を取得
        for elem in driver.find_elements_by_xpath('//span[@class="a-size-base-plus a-color-base a-text-normal"]'):
            yield{
                'title': elem.text
            }
