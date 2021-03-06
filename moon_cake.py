# Author:Vanyo
import requests
import re
#下载网页
def get_html_text(url):
    try:
        res = requests.get(url,timeout=30)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        return res.text
    except:
        return ""

#解析网页并保存数据
def parse_page(html):
    try:
        #下面四个变量得到的都是列表，plt是一个列表，tlt也是一个列表....
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        loc = re.findall(r'\"item_loc\"\:\".*?\"', html)
        sale = re.findall(r'\"view_sales\"\:\".*?\"', html)
        print(plt)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            location = eval(loc[i].split(':')[1])
            location = location.split(' ')[0]
            sales = eval(sale[i].split(':')[1])
            sales = re.match(r'\d+', sales).group(0)
            #print(price)
            with open("月饼数据.txt", 'a', encoding='utf-8') as f:
                f.write(title + ',' + price + ',' + sales + ',' + location + '\n')
    except:
        print("")

def main():
    goods = "月饼"
    depth = 100
    start_url = 'https://s.taobao.com/search?q=' + goods
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = get_html_text(url)
            parse_page(html)
        except:
            continue

main()