import xml.etree.ElementTree as ET
import re

def readFile(fileName):
  with open(fileName, 'r') as f:
    read_data = f.read()

  regex = re.compile(r"\.mp4\?.*?</flv>")
  xmlAfterReplace = regex.sub(".mp4</flv>", read_data)
  return xmlAfterReplace

def parseXML(xmlString):
  root = ET.fromstring(xmlString)
  print(root.tag, root.text)
  allChild(root)

def allChild(root):
  for child in root:
    print (child.tag, child.text)
    allChild(child)

if __name__ == '__main__':
  xmlString = readFile('1345.xml')
  parseXML(xmlString)
  