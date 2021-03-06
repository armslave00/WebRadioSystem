import requests
import json
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import re

# import pickle   #serilize



# bangumiInfoList = []

# bangumiDOMList = soup.select("li.clr")

# for bangumiDOM in bangumiDOMList:
#   bangumiInfo = {}
#   bangumiInfo['nameKana'] = bangumiDOM['data-kana']
#   bangumiInfo['updateDate'] = bangumiDOM['data-update']
#   bangumiInfo['weekDay'] = bangumiDOM['data-week']
#   bangumiInfo['type'] = bangumiDOM['data-genre']
#   bangumiInfo['ID'] = bangumiDOM['id']
#   bangumiInfo['started'] = "noMovie" in bangumiDOM['class']
#   bangumiInfo['name'] = bangumiDOM.select("h4 > span")[0].get_text()
#   bangumiInfo['navigator'] = bangumiDOM.select("p.navigator > span")[0].get_text()
#   bangumiInfo['thumbnail'] = bangumiDOM.select("p.thumbnail > img")[0]['src']
#   bangumiInfo['programLink'] = bangumiDOM.select("p.programLink > a")[0]['href']
#   bangumiInfo['isLive'] = len(bangumiDOM.select("div.contType > .live")) > 0
#   bangumiDetailResponse = requests.get("http://www.onsen.ag/data/api/getMovieInfo/" + bangumiInfo['ID'] + "?callback=callback")
#   bangumiDetailJSON = bangumiDetailResponse.text[9:-3]
#   bangumiDetail = json.loads(bangumiDetailJSON)
#   bangumiInfo['count'] = bangumiDetail['count']
#   bangumiInfo['personality'] = bangumiDetail['personality']
#   bangumiInfoList.append(bangumiInfo)

# bytes = result.encode(encoding='UTF-8')

regexParameter = re.compile(r"(?<=').+?(?=')")
regexRtmpPre = re.compile(r"\.mp4\?.*?</flv>")

bangumiInfoList = []

for x in range(1,7):
  programRequest = requests.get("http://hibiki-radio.jp/get_program/" + str(x))
  programRequest.encoding = "UTF-8"
  programSoup = BeautifulSoup(programRequest.text, "html.parser")
  programDOMList = programSoup.select("div.hbkProgram > a")
  for programDOM in programDOMList:
    bangumiInfo = {}
    bangumiInfo['thumbnail-small'] = programDOM.select(".hbkProgramBanner")[0]['src']
    bangumiInfo['updateDate'] = programDOM.select(".hbkProgramComment")[0].get_text()
    actionParameters = re.findall(regexParameter, programDOM['onclick'])
    bangumiInfo['ID'] = actionParameters[0]
    bangumiInfo['count'] = actionParameters[2]
    bangumiInfo['parameter1'] = actionParameters[4]
    bangumiInfo['parameter2'] = actionParameters[6]
    RtmpInfoRequest = requests.get("http://image.hibiki-radio.jp/uploads/data/channel/" + bangumiInfo['ID'] + "/" + bangumiInfo['count'] + ".xml")
    RtmpInfoRequest.encoding = "UTF-8"
    RtmpInfoString = regexRtmpPre.sub(".mp4</flv>", RtmpInfoRequest.text)
    RtmpInfoSoup = BeautifulSoup(RtmpInfoString, "html.parser")
    bangumiInfo['protocol'] = RtmpInfoSoup.select('protocol')[0].get_text()
    bangumiInfo['domain'] = RtmpInfoSoup.select('domain')[0].get_text()
    bangumiInfo['dir'] = RtmpInfoSoup.select('dir')[0].get_text()
    bangumiInfo['channel'] = RtmpInfoSoup.select('channel > flv')[0].get_text()
    bangumiInfo['thumbnail'] = RtmpInfoSoup.select('channel > thumbnail')[0].get_text()
    # http://image.hibiki-radio.jp/uploads/data/channel/gate/1748.xml?1443077580731
    descriptionRequest = requests.get("http://image.hibiki-radio.jp/uploads/data/channel/" + bangumiInfo['ID'] + "/description.xml")
    descriptionRequest.encoding = "UTF-8"
    descriptionSoup = BeautifulSoup(descriptionRequest.text, "html.parser")
    bangumiInfo['name'] = descriptionSoup.select('title')[0].get_text()
    bangumiInfo['description'] = descriptionSoup.select('outline')[0].get_text()
    bangumiInfo['link'] = descriptionSoup.select('link')[0].get_text()
    bangumiInfo['castlist'] = []
    nameDOMList = descriptionSoup.select('cast > name')
    for nameDOM in nameDOMList:
      bangumiInfo['castlist'].append(nameDOM.get_text())
    bangumiInfo['cast'] = " / ".join(bangumiInfo['castlist'])
    # http://image.hibiki-radio.jp/uploads/data/channel/gate/description.xml?1443077583936
    bangumiInfoList.append(bangumiInfo)

# with open('workfile-h1.txt', 'w', encoding='UTF-8') as f:
#   f.write(soup.prettify())

with open('workfile-hibiki1.txt', 'w', encoding='UTF-8') as f:
  for info in bangumiInfoList:
    f.write(u"名字: ")
    f.write(info['name'])
    f.write("\n")
    f.write(u"Link: ")
    f.write(info['link'])
    f.write("\n")
    f.write(u"回数: ")
    f.write(str(info['updateDate']))
    f.write("\n")
    f.write(u"Pict: ")
    f.write(info['thumbnail-small'])
    f.write("\n")
    f.write(u"Pict: ")
    f.write(info['thumbnail'])
    f.write("\n")
    f.write(u"ID  : ")
    f.write(info['ID'])
    f.write("\n")
    f.write(u"Coun: ")
    f.write(info['count'])
    f.write("\n")
    f.write(u"Pmt1: ")
    f.write(info['parameter1'])
    f.write("\n")
    f.write(u"Pmt2: ")
    f.write(info['parameter2'])
    f.write("\n")
    f.write(u"protocol: ")
    f.write(info['protocol'])
    f.write("\n")
    f.write(u"domain: ")
    f.write(info['domain'])
    f.write("\n")
    f.write(u"dir: ")
    f.write(info['dir'])
    f.write("\n")
    f.write(u"channel: ")
    f.write(info['channel'])
    f.write("\n")
    f.write(u"thumbnail: ")
    f.write(info['thumbnail'])
    f.write("\n")
    f.write(u"description: ")
    f.write(info['description'])
    f.write("\n")
    f.write(u"cast: ")
    f.write(info['cast'])
    f.write("\n\n")
  

