BOT_NAME = 'conisterbank'

SPIDER_MODULES = ['conisterbank.spiders']
NEWSPIDER_MODULE = 'conisterbank.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'conisterbank.pipelines.ConisterbankPipeline': 100,

}