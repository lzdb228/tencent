# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentItem

class TencentPositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['tencent.com']
    url='https://hr.tencent.com/position.php?&start='
    offset=0
    start_urls = [url+str(offset)]

    def parse(self, response):
        content=response.xpath("//tr[@class='even']|//tr[@class='odd']")
        for each in content:
            item=TencentItem()
            name = each.xpath("./td[1]/a/text()").extract()
            detailLink = each.xpath("./td[1]/a/@href").extract()
            positionInfo = each.xpath("./td[2]/text()").extract()
            peopleNumber = each.xpath("./td[3]/text()").extract()
            workLocation = each.xpath("./td[4]/text()").extract()
            publishTime = each.xpath("./td[5]/text()").extract()

            item['name']=name
            item['detailLink']=detailLink
            item['positionInfo']=positionInfo
            item['peopleNumber']=peopleNumber
            item['workLocation']=workLocation
            item['publishTime']=publishTime

            yield item

        if self.offset<3930:
            self.offset += 10

        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)


