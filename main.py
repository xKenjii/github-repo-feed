from bs4 import BeautifulSoup
import requests

def filterCharsets(input):
    string = str(input)
    
    string = string.replace('&lt;li&gt;', '')
    string = string.replace('&lt;/li&gt;', '')
    string = string.replace('<title>', '')
    string = string.replace('</title>', '')
    string = string.replace('<content>', '')
    string = string.replace('</content>', '')
    string = string.replace('&lt;/ul&gt;', '')
    string = string.replace('&lt;p&gt;&lt;strong&gt;', '')
    string = string.replace('&lt;/strong&gt;', '')
    string = string.replace('<link href="', '')
    string = string.replace('" rel="alternate" type="text/html"/>', '')
    string = string.replace('<content type="html">&lt;ul&gt;', '')
    string = string.replace('<content type="html">', '')
    string = string.replace('&lt;code&gt;', '')
    string = string.replace('&lt;/code&gt;', '')
    string = string.replace('&lt;ul&gt;', '')
    string = string.replace('&lt;p&gt;', '')
    string = string.replace('&lt;/p&gt;', '')
    string = string.replace('&lt;a href="', '')
    string = string.replace('"&gt;', ' ( ')
    string = string.replace('&lt;/a&gt;' , ' )')
    string = string.replace('&lt;/ol&gt;', '')
    string = string.replace('&lt;br&gt;', '')

    return string

url = 'https://github.com/xKenjii/github-repo-feed/releases.atom';

r = requests.get(url, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'})

soup = BeautifulSoup(r.content, features='xml')

releaseData = soup.findAll('entry')
for i in releaseData:
    link = filterCharsets(i.find('link'))
    title = filterCharsets(i.find('title'))
    content = filterCharsets(i.find('content'))

    print(link)
    print(title)
    print(content)
    print('-----')