import scrapy
import re
import json
import os

def get_phone_number(html_text):
    list_phones = []
    frt_ptr = re.findall(r'\+\d{2}\s?0?\d{10}', html_text)
    for phone in frt_ptr:
        list_phones.append(phone)

    scd_ptr = re.findall(r'\d{4}[\-]\d{3}[\-]\d{4}', html_text)
    for phone in scd_ptr:
        list_phones.append(phone)
    return list_phones


def check_absolute_url(src, url):
    if src:
        if "http:" not in src and "https:" not in src:
            return f"{url}{src}"
        return src
    pass


class DNBSpider(scrapy.Spider):
    name = "PageInfoSpider"
    sites = open("sites.txt")
    start_urls = [site for site in sites.readlines()]
    array = []

    def parse(self, response, **kwargs):
        self.array.append(
            {
                "logo": check_absolute_url(response.xpath('//img/@src').get(), response.url),
                'phones': get_phone_number(response.text),
                'website': response.url,
            }
        )
        with open(f"{os.environ.get('HOME')}/Desktop/return.json", "w", encoding="UTF8") as returnFile:
            json_parse = json.dumps(
                self.array
            )
            returnFile.write(json_parse)

        yield {
            "logo": check_absolute_url(response.xpath('//img/@src').get(), response.url),
            'phones': get_phone_number(response.text),
            'website': response.url,
        }
