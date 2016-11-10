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
        items['product_id'] = tree.xpath('//div[@class="products-grid"]/div[%s]/a/input/@id'%(i+1))
        items["url"] = tree.xpath('//div[@class="products-grid"]/div[%s]/a/@href'%(i+1))
        items["thumbnails"] = tree.xpath('//div[@class="products-grid"]/div[%s]/a/input/@value'%(i+1))
        items["title"] = tree.xpath('//div[@class="products-grid"]/div[%s]//div[@class="details"]/a/text()'%(i+1))
        items["price"] = tree.xpath('//div[@class="products-grid"]/div[%s]//span[@class="price"]/text()'%(i+1))
        

        items["availabilty"] = [{"picode":i , "availabilty":json.loads(requests.get("http://www.shopclues.com/nss.php?pincode_no=%s&product_ids=%s"%(i , items['product_id'][0])).text)}for i in [671551 , 575001 , 560070] ]
        data["items"].append(items)
    return json.dumps(data)

print scrapper()

