import scrapy
from scrapy.exceptions import CloseSpider

from scrapy.loader import ItemLoader
from ..items import ConisterbankItem
from itemloaders.processors import TakeFirst


class CapitaliomSpider(scrapy.Spider):
	name = 'conisterbank'
	start_urls = ['https://www.conisterbank.co.im/conister-news-community']
	page = 1
	last_post = ''

	def parse(self, response):
		post_links = response.xpath('//h4/a/@href')
		yield from response.follow_all(post_links, self.parse_post)

		self.page += 1
		next_page = f'https://www.conisterbank.co.im/conister-news-community?page={self.page}'

		if self.last_post == post_links.getall()[-1]:
			raise CloseSpider('no more pages')

		self.last_post = post_links.getall()[-1]

		yield response.follow(next_page, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="large-8 columns main"]/p//text()').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//time/text()').get()

		item = ItemLoader(item=ConisterbankItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
