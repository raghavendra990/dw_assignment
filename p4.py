from lxml import html
import requests
import json

def scrapper():
    url = "http://www.shopclues.com/computers/desktops%C2%ADand%C2%ADmonitors/monitors.html"
    page = requests.get(url)
    tree = html.fromstring(page.text)

    data  = {"items":[]}

    for i in range(10):
        items  = {}
        items["url"] = tree.xpath('//div[@class="products-grid"]/div[%s]/a/@href'%(i+1))
        items["thumbnails"] = tree.xpath('//div[@class="products-grid"]/div[%s]/a/input/@value'%(i+1))
        items["title"] = tree.xpath('//div[@class="products-grid"]/div[%s]//div[@class="details"]/a/text()'%(i+1))
        items["price"] = tree.xpath('//div[@class="products-grid"]/div[%s]//span[@class="price"]/text()'%(i+1))

        data["items"].append(items)

    return json.dumps(data)

print scrapper()

