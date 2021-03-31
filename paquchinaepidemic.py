import requests
from lxml import etree
import json

if __name__ == "__main__":
    '''chinaepidemicdata = []    
    tmp = {'地区':0,'现有':0,'累计':0,'治愈':0,'死亡':0}
    url = "https://news.qq.com/zt2020/page/feiyan.htm#/"
    headers = {
        "cookie":"__Secure-3PSID=7gfNykUzkC6cjuxBXQAmxBG1MWgfop6Ay8MwE3XW78RQzjPkWSd-9H5aQhzuU27FNmkWjw.; __Secure-3PAPISID=exmTGKZ_ldiiYV9t/AntgRX4lFGw4dbIGe; NID=211=NsX6pjiMdgdIK1hj8XRgJLTYZqe_Xo874AStYwX3Pycud9h6f6uVuO_C_gxOaNqm6SXxUigF6-hsdSbcPribBnGMmcfZZd95Zs1jHhnLKVjF9TRKffUB0T5_u9AmTRQRAB0bBkJuQbfLnHPwZCbCj9pZeLgsbEJ30vnhzvkIXyV27xEeqdjH3RprpFc7CbwhPaFAC1WfKaE-3YD_OZqeZMGs7ObpNgZwTcrUq7hqFusT2tlEnWcKkCrX7BxPJSKT6DXM0x83ITdKMQ; 1P_JAR=2021-03-20-13; __Secure-3PSIDCC=AJi4QfHNOYhpPX9fls2-Qjfs70OpHYWCInS33Q-sx1w_BtSHmswBaGjQxqL7EF_yvgSf8XnnoMM",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54"
    }
    page_data = requests.get(url = url,headers = headers).text
    tree = etree.HTML(page_data)
    with open('test.txt','w',encoding='utf-8') as fp:
        fp.write(page_data)
    tbody_list = tree.xpath('//div[@class = "listWraper"]/table[2]/tbody')
    print(tbody_list)
    for tbody in tbody_list:
        city_name = tbody.xpath('./tr[1]/th[1]/p[1]/span/text()')[0]
        xianyou = tbody.xpath('./td[1]/p[1]/text()')[0]
        leiji = tbody.xpath('./td[2]/p[1]/text()')[0]
        zhiyu = tbody.xpath('./td[3]/p[1]/text()')[0]
        siwang = tbody.xpath('./td[4]/p[1]/text()')[0]
        tmp['地区'] = city_name
        tmp['现有'] = xianyou
        tmp['累计'] = leiji
        tmp['治愈'] = zhiyu
        tmp['死亡'] = siwang
        chinaepidemicdata.append(tmp)
    print(chinaepidemicdata)'''
    url = "http://139.9.119.40/api/coviddata/%E6%B2%B3%E5%8D%97?format=json&date=2021-03-18"
    headers = {
        "X-CSRFTOKEN" : "aCSZHgMNMRUYDDQNk1ZRaha4pTepoWqNQnarrC1ZMwM7JsnH3EPmpfciOFogCmAU",
        "cookie":"__Secure-3PSID=7gfNykUzkC6cjuxBXQAmxBG1MWgfop6Ay8MwE3XW78RQzjPkWSd-9H5aQhzuU27FNmkWjw.; __Secure-3PAPISID=exmTGKZ_ldiiYV9t/AntgRX4lFGw4dbIGe; NID=211=NsX6pjiMdgdIK1hj8XRgJLTYZqe_Xo874AStYwX3Pycud9h6f6uVuO_C_gxOaNqm6SXxUigF6-hsdSbcPribBnGMmcfZZd95Zs1jHhnLKVjF9TRKffUB0T5_u9AmTRQRAB0bBkJuQbfLnHPwZCbCj9pZeLgsbEJ30vnhzvkIXyV27xEeqdjH3RprpFc7CbwhPaFAC1WfKaE-3YD_OZqeZMGs7ObpNgZwTcrUq7hqFusT2tlEnWcKkCrX7BxPJSKT6DXM0x83ITdKMQ; 1P_JAR=2021-03-20-13; __Secure-3PSIDCC=AJi4QfHNOYhpPX9fls2-Qjfs70OpHYWCInS33Q-sx1w_BtSHmswBaGjQxqL7EF_yvgSf8XnnoMM",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54"        
    }
    page_data = requests.post(url = url,headers = headers).text
    '''page_data = page_data.split('(')[1].split(')')[0]'''
    print(page_data)