import json

import scrapy

class MySpider(scrapy.Spider):
    name = "myspider"

    def start_requests(self):
        urls = ['https://joyeroscabranes.com/59-solitarios?page=1&from-xhr=null','https://joyeroscabranes.com/59-solitarios?page=2&from-xhr=null']
        headers = {
            'authority': 'joyeroscabranes.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://joyeroscabranes.com/59-solitarios',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        cookies = {
            'PHPSESSID': '4be0bamhsnac3o1nhto4l6vr9q',
            'cookiesplus': '%7B%22consent_mode%22%3Anull%2C%22C_P_DISPLAY_MODAL%22%3Afalse%2C%22consents%22%3A%7B%22cookiesplus-finality-3%22%3A%22on%22%2C%22cookiesplus-finality-4%22%3A%22on%22%7D%2C%22consent_date%22%3A%222024-05-11%2014%3A58%22%2C%22consent_hash%22%3A%223f12632637c2a9225665e60b69b92af8-b060d431%22%7D',
            'PrestaShop-61d2a98b21f729af7544b0d5f8d64395': 'def5020031aab500e7abac830002eca5149069148f746e05d9aa76416b22327b36e1229f504051ac049aebe5629818025f46ee225c692fd34ef035fc5b16a2af326c619d20345c1831eabd145923dc3058bd289afdbb531efffedeac5985df097be614537ca367b2d191119189104b3e5ec96f145e652577d5c87f81d90cbabb2072b3ee6650f723b8c6d86fca9fce22bfd5ab3289f5d5ef6f19b3d37cb83ab5ffd0952911e307f53e373eff6f0479039291430adf2a6dea65a3d7edcaccb3f0a9f68884d2bade6caaf9e5942e8720e3e471714bfe860651404e31e22907f237239bc8cfaba903a4387d5a895116807c5462b848df505d83843f522ed26a1fe8468008e38720f2016b2c7f89dcced0c37f718c33c65deeba1af26da5c509946df420fabf55b37b0454d2e2a9ba9b8da70e9e9f318330cd1a74409a8c1132f499ce148a1a28d3b1163b47c1ee8847e1f779d7db4c0ea791bc0e6f8324b116a0baf2149173de0331851de61f10eb37ec34f39f3af83ecbfe73cef2ab820755d4c31812be6b327bc6f367a0042b93c4719273a672bb110ce26ead9d3d65722376e75d7d21e299e1cbba8f426cece9859d95b43d1fcb041b8a05defa46f231ffe8ad584c0a152a0ca83233f2d99174c27575824330ed6b4c0b310d3e6944e4cf64c7ea0bcd76d206de5658dbbd0e5bd401de; PHPSESSID=o9lkubp3u23l4uegri7gjm81ia; PrestaShop-61d2a98b21f729af7544b0d5f8d64395=def50200b3dfb094d6e90c875b8ec6357715eb40fc8cfd1c69b0aee4959f4b7f04dd53eb8d0adab91d9ba12095ad897bd285a4c9c61993f7362a12cc53d7c8bd41d0a657709fc32080fd54fa3b4e58be16b6f7a3d9fd88361b4ed1b6395afe12e0accb72149c0e830b7080c1dbfd8719e927f610841199931fc6d54255c9c0489fed807d6f2e48a89cfafa00d88ccffa2cdae0e49434707268a291965b67f8c1c63a69c45d6eaf4881931705cf666f2a63c003205d8dfe399a5f7dd20841a78dff98c663bd2682728c9fca38f5212358c588261f62d522723e450f487ba2298ed4d9cd5450493778e1e3d4e8946359d4cf1f582e2bd383cd263ceb23a3385cdec1fad1530715a4bd7023b54d131a78944c65b93d798044a0809d44f03b36e54b9d4660d8fcde56c182f81c5caa4feaef71646ce1055496404fa5ce1732c38cb80c4ad77e52c5d9ab12135dd217cb04b1f2fa22b8b51fd71caa3c372f97ddfd4ab35f7692ec0a8ae275fd972bb8bb62a5e6bc8327724f688d28b39eaa133e59df39eb457acb0ee1e74cbed75cebdafc9d22c2ee8667d6a4f89844c7ecd9287596b60de4fde8ea01a101c72f2fee7a0c1d161e207254d9f5c7de1dc67f807e99b1ecbac25f16aab0fec4413a93cb7a201a8f4f0ce7502cde875907e51e74e80fd8a4da140d029c86a3153d98b084ded6d4bd9ab472c338; cookiesplus=%7B%22consent_mode%22%3Anull%2C%22C_P_DISPLAY_MODAL%22%3Afalse%2C%22consents%22%3A%7B%22cookiesplus-finality-3%22%3A%22on%22%2C%22cookiesplus-finality-4%22%3A%22on%22%7D%2C%22consent_date%22%3A%222024-05-11%2014%3A58%22%2C%22consent_hash%22%3A%223f12632637c2a9225665e60b69b92af8-b060d431%22%7D'
        }

        for url in urls:
            yield scrapy.Request(url, headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):
        json_data=json.loads(response.text)
        products=json_data['products']
        for product in products:
            data = {}
            data['image_url_1'] = product['cover']['bySize']['large_default']['url']
            data['name'] = product['name']
            data['price'] = product['price']
            data['description_short'] = product['description_short'].replace("<p>","").replace("</p>","")
            data['reference'] = product['reference']
            yield scrapy.Request(url=product['link'], callback=self.product_details, meta={'data': data})

    def product_details(self, response):
        url=response.url
        data=response.meta['data']
        path = response.xpath("//ol/li//span/text()").getall()
        category_list="/".join(path)
        image_url = response.xpath('//*[@id="swiper-wrapper-column-images"]/div[2]/picture/img/@data-image-large-src').get()
        product_info = {}
        texts = response.xpath('//div[@class="elementor-widget-container"]//text()').getall()
        description_title=response.xpath("//div[@class='elementor-widget-container']/h2/span/text()").get()
        data_sheet = response.css('section.product-features dl.data-sheet')
        dt_elements = data_sheet.css('dt.name')
        dd_elements = data_sheet.css('dd.value')
        for dt, dd in zip(dt_elements, dd_elements):
            key = dt.css('::text').get().strip()
            value = dd.css('::text').get().strip()
            product_info[key] = value
        product_info_str = ",".join([f"{key}: {value}" for key, value in product_info.items()])
        cleaned_text = "".join(texts).replace("\r\n            ", "").replace('\t\t\n\t\t\t\n\t\t\n\t\t\t\t', '')
        data["category_list"]=category_list
        data["product_info"]=product_info_str
        data["image_url_2"]=image_url
        data['description_title']="{}: {}".format(description_title, cleaned_text)
        data["url"]=url

        yield data