import requests
from bs4 import BeautifulSoup as bs
import re
import pickle

def scraping(url):
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
    for i in soup.find_all('div', class_='media-content'):
        for j in i.find_all("img"):
            images.append(j.get("src"))

    pics = []        
    for i in images:
        pics.append("http://www.lawson.co.jp" + i)
            
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
    return list(zip(kcals, names, pics))

def main():
    bento = scraping("http://www.lawson.co.jp/recommend/original/bento/index.html")
    rice = scraping("http://www.lawson.co.jp/recommend/original/rice/index.html")
    sushi = scraping("http://www.lawson.co.jp/recommend/original/sushi/index.html")
    chilled = scraping("http://www.lawson.co.jp/recommend/original/chilledbento/index.html")
    sandwich = scraping("http://www.lawson.co.jp/recommend/original/sandwich/index.html")
    pasta = scraping("http://www.lawson.co.jp/recommend/original/pasta/index.html")
    noodle = scraping("http://www.lawson.co.jp/recommend/original/noodle/index.html")
    soup = scraping("http://www.lawson.co.jp/recommend/original/soup/index.html")
    chukaman = scraping("http://www.lawson.co.jp/recommend/original/chukaman/index.html")
    gratin = scraping("http://www.lawson.co.jp/recommend/original/gratin/index.html")
    cupnoodle = scraping("https://www.lawson.co.jp/recommend/original/select/cupnoodle/index.html")
    salad = scraping("http://www.lawson.co.jp/recommend/original/salad/index.html")
    #ドレッシングを排除
    only_saldas = []
    for i in salad:
        if 0 <= i[1].find('ドレッシング') :
            continue
        else:
            only_saldas.append(i)

    lawson_list = bento + rice + sushi + chilled + sandwich +  pasta + noodle + soup + chukaman + only_saldas + gratin + cupnoodle

    f = open('menu_list.txt', 'wb')
    list_row = lawson_list
    return pickle.dump(list_row, f)




if __name__ == '__main__':
    main()