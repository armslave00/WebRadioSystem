import requests
import json
from bs4 import BeautifulSoup

r = requests.get("http://www.onsen.ag/")
r.encoding = "UTF-8"
soup = BeautifulSoup(r.text, "html.parser")

bangumiInfoList = []

bangumiDOMList = soup.select("li.clr")

for bangumiDOM in bangumiDOMList:
  bangumiInfo = {}
  bangumiInfo['nameKana'] = bangumiDOM['data-kana']
  bangumiInfo['updateDate'] = bangumiDOM['data-update']
  bangumiInfo['weekDay'] = bangumiDOM['data-week']
  bangumiInfo['type'] = bangumiDOM['data-genre']
  bangumiInfo['ID'] = bangumiDOM['id']
  bangumiInfo['started'] = "noMovie" in bangumiDOM['class']
  bangumiInfo['name'] = bangumiDOM.select("h4 > span")[0].get_text()
  bangumiInfo['navigator'] = bangumiDOM.select("p.navigator > span")[0].get_text()
  bangumiInfo['thumbnail'] = bangumiDOM.select("p.thumbnail > img")[0]['src']
  bangumiInfo['programLink'] = bangumiDOM.select("p.programLink > a")[0]['href']
  bangumiInfo['isLive'] = len(bangumiDOM.select("div.contType > .live")) > 0
  bangumiDetailResponse = requests.get("http://www.onsen.ag/data/api/getMovieInfo/" + bangumiInfo['ID'] + "?callback=callback")
  bangumiDetailJSON = bangumiDetailResponse.text[9:-3]
  bangumiDetail = json.loads(bangumiDetailJSON)
  bangumiInfo['count'] = bangumiDetail['count']
  bangumiInfo['personality'] = bangumiDetail['personality']
  bangumiInfoList.append(bangumiInfo)

with open('workfile-t4.txt', 'w', encoding='UTF-8') as f:
  for info in bangumiInfoList:
    f.write(u"名字: ")
    f.write(info['name'])
    f.write("\n")
    f.write(u"Navi: ")
    f.write(info['navigator'])
    f.write("\n")
    f.write(u"Pict: ")
    f.write(info['thumbnail'])
    f.write("\n")
    f.write(u"Link: ")
    f.write(info['programLink'])
    f.write("\n")
    f.write(u"Live: ")
    f.write(str(info['isLive']))
    f.write("\n")
    f.write(u"回数: ")
    f.write(str(info['count']))
    f.write("\n")
    f.write(u"personality: ")
    f.write(str(info['personality']))
    f.write("\n")
    f.write(u"片假: ")
    f.write(info['nameKana'])
    f.write("\n\n")
  

