import requests
from bs4 import BeautifulSoup as bs
import re
import pickle

#LAWSONのスクレイピング関数
def lawson_scraping(url):
    header = {"User-Agent" : "Mozilla/5.0"}
    soup = bs(requests.get(url, headers=header).content, 'html.parser')

    names = []
    #商品リスト
    #商品名をHtmlから抽出
    for i in soup.find_all('div', class_='content'):
        for j in i.find_all('p', class_='caption'):
            j = j.text
            j = j.strip(" ")
            j = j.replace("\u3000", "")
            names.append(j)

    #画像        
    images = []
    for i in soup.find_all('div', class_='box lw-no-shadow'):
        j = i.a.get("href")
        images.append("http://www.lawson.co.jp" + j)
            
            
    #カロリー
    kcals = []
    for i in soup.find_all('div', class_='content'):
        for j in i.find_all('p', class_ ='description'):
            j = j.text
            j = j.split("kcal")[0]
            j = j.strip(" ")
            j = int(j)
            kcals.append(j)
    
    #リストデータ作成
    return list(zip(kcals, names, images))

#セブンのスクレイピング関数
def seven_scraping(url):
    header = {"User-Agent" : "Mozilla/5.0"}
    s = bs(requests.get(url, headers=header).content, 'html.parser')
    
    #名前
    s_names = []
    for i in s.find_all('div', class_='itemName'):
        s_names.append(i.text)

    #画像        
    s_images = []
    for i in s.find_all('div', class_='image'):
        j = i.a.get("href")
        s_images.append("https://www.sej.co.jp"+j)

    #カロリー
    s_kcals = []
    for i in s.find_all('div', class_='summary'):
        j = i.find('li', class_ ='n1')
        j = j.text
        j = j.strip("※地域によりカロリーが異なる場合があります。")
        j = j.split("kcal")[0]
        j = int(j)
        s_kcals.append(j)

    return list(zip(s_kcals, s_names, s_images))


def main():
    bento = lawson_scraping("http://www.lawson.co.jp/recommend/original/bento/index.html")
    rice = lawson_scraping("http://www.lawson.co.jp/recommend/original/rice/index.html")
    sushi = lawson_scraping("http://www.lawson.co.jp/recommend/original/sushi/index.html")
    chilled = lawson_scraping("http://www.lawson.co.jp/recommend/original/chilledbento/index.html")
    sandwich = lawson_scraping("http://www.lawson.co.jp/recommend/original/sandwich/index.html")
    pasta = lawson_scraping("http://www.lawson.co.jp/recommend/original/pasta/index.html")
    noodle = lawson_scraping("http://www.lawson.co.jp/recommend/original/noodle/index.html")
    soup = lawson_scraping("http://www.lawson.co.jp/recommend/original/soup/index.html")
    chukaman = lawson_scraping("http://www.lawson.co.jp/recommend/original/chukaman/index.html")
    gratin = lawson_scraping("http://www.lawson.co.jp/recommend/original/gratin/index.html")
    cupnoodle = lawson_scraping("https://www.lawson.co.jp/recommend/original/select/cupnoodle/index.html")
    salad = lawson_scraping("http://www.lawson.co.jp/recommend/original/salad/index.html")
    #ドレッシングを排除
    only_saldas = []
    for i in salad:
        if 0 <= i[1].find('ドレッシング') :
            continue
        else:
            only_saldas.append(i)

    lawson_list = bento + rice + sushi + chilled + sandwich +  pasta + noodle + soup + chukaman + only_saldas + gratin + cupnoodle

    f = open('lawson_list.txt', 'wb')
    list_row = lawson_list
    pickle.dump(list_row, f)

    seven_url ="https://www.sej.co.jp/i/products/anshin/calorie/"
    seven_list = seven_scraping(seven_url)

    f = open('seven_list.txt', 'wb')
    list_row02 = seven_list
    pickle.dump(list_row02, f)



if __name__ == '__main__':
    main()