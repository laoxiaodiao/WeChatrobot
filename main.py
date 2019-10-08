import requests
import urllib
import urllib.request
import json
import itchat
import re
from bs4 import BeautifulSoup
from itchat.content import *
print('''
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
☆☆☆         微信群多功能机器人V2.0               ☆☆☆
☆☆☆         Desigined  By Laoxiaodiao           ☆☆☆
☆☆☆         Last update:2019-08-21              ☆☆☆
☆☆☆         Email:3220821418@qq.com             ☆☆☆
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
''')
try:
    group=input("你要管理的群昵称(如果要有多个群,请以逗号或空格隔开)：")
    group=re.split('，|,| ',group)#将多个群弄成列表，后面来判断消息是否来自这些群
    zhmm=input("请输入账号和密码\n如果有多个账号密码，对应的账号和密码之间用空格分开，然后在输入另一个账号密码\n如（623708478 007633，687248622 764155）：")
    zhmm=re.split(' |,|，',zhmm)
    # zh = [0 for _ in range(int(len(zhmm)/2))]
    # mm=[0 for _ in range(int(len(zhmm)/2))]
    # for i in range(int(len(zhmm)/2)):
    #     zh[i]=zhmm[2*i]
    #     mm[i]=zhmm[2*i+1]
    # zhmm=dict(zip(zh,mm))
    print('你所输入的账号密码为'+str(zhmm))
except:
    print('输入账号密码环节出现错误，请重新输入')
def GET_SHORTURL(firsturl,i):
    try:
        #以下用到了两个链接，一个是查询文档ID的，另一个是下载的
        url1="http://139.224.236.108/post.php"
        url3="http://139.224.236.108/downdoc.php"
        #将传入的文档链接进行转化
        downloadurl=firsturl.replace("/","%2F").replace(":","%3A")
        #head1查询文档ID的数据头
        #data1是查询的数据内容，其中将docinfo的值转化为链接
        #查询得到结果，截取id的那一段并返回

        def query():
            head1 = {"POST": "/post.php HTTP/1.1",
                     "Host": "139.224.236.108",
                     "Content-Length": "145",
                     "Accept": "*/*",
                     "Origin": "http://139.224.236.108",
                     "X-Requested-With": "XMLHttpRequest",
                     "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                     "Referer": "http://139.224.236.108/1.html",
                     "Accept-Encoding": "gzip, deflate",
                     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                     "Cookie": "usrname="+zhmm[2*i]+"; usrpwd="+zhmm[2*i+1]
                     }
            data1 = 'usrname='+zhmm[2*i]+'&usrpass='+zhmm[2*i+1]+'&docinfo=downloadurl&taskid=up_down_doc1'
            data1 = data1.replace('downloadurl', downloadurl)
            respons=requests.post(url1,data=data1,headers=head1).json()
            id=respons['url']
            id=id[37:]
            return id



        id = query()
        #head3下载文档的数据头
        #data3是请求下载的数据内容，其中vid是查询内容返回的文档id值
        #获取下载链接
        def down():
            Referer = "http://139.224.236.108/nocode.php?id={docid}"
            head3 = {"POST": "/downdoc.php HTTP/1.1",
                     "Host": "139.224.236.108",
                     "Content-Length": "54",
                     "Accept": "*/*",
                     "Origin": "http://139.224.236.108",
                     "X-Requested-With": "XMLHttpRequest",
                     "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                     "Referer": Referer.format(docid=id),
                     "Accept-Encoding": "gzip, deflate",
                     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                     "Cookie": "usrname="+zhmm[2*i]+"; usrpwd="+zhmm[2*i+1]
                     }
            data3 = 'vid={docid}&taskid=directDown'
            data3 = data3.format(docid=id)
            response=requests.post(url3, data=data3, headers=head3).json()
            downurl=response["dlink"].replace("\\",'')
            return downurl

        url5 = down()
        print(url5)
        return url5
    except:
        return 0

#电影解析
def getvideo(vurl):
    jiexiurl1="http://jx.618g.com/?url="
    viedourl=vurl
    url=jiexiurl1+viedourl
    result=requests.get(url)
    ret= re.findall(r'url=(http.*")',result.text)
    ret=ret[0].replace("\"","")
    return ret

def search(search_text):
    session = requests.session()
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
    a = search_text
    a_gb = a.encode('utf-8')
    s = urllib.parse.quote(a_gb)
    search_url = "https://www.yunpanjingling.com/search/" + s
    session.get("https://www.yunpanjingling.com/", headers=head)
    soup = session.get(search_url, headers=head).text
    soup = BeautifulSoup(soup, 'html.parser')
    result = soup.find_all('div', attrs={'class': 'referrer'})
    res_text = re.findall("target=\"_blank\">(.*?) </a>", str(result))
    re_text = []
    for i in res_text:
        re_text.append(str(i).replace("</em>", "").replace("<em>", "").replace(" ", ""))
    res_url = re.findall("href=\"(.*?)\"", str(result))
    search_result = dict(zip(re_text, res_url))  # 列表转字典
    if len(search_result) == 0:
        retur_msg = "抱歉，没有找到你要搜索的资源"
    else:
        return_msg = "搜索的结果如下：\n"
        for key in search_result:
            return_msg = return_msg + str(key) + ':' + "(" + str(search_result[key]) + ")\n"
        return_msg = return_msg + "结果通过爬虫抓取自互联网，会在页面中检测关键字与网盘链接，请在打开的链接中多翻翻，一切会有的"
    return return_msg

def login_req():
    # 图灵接口，返回信息
    apiUrl="http://openapi.tuling123.com/openapi/api/v2"
    def get_info(message):
        data={
            "reqType":0,
            "perception": {
                "inputText": {
                    "text":message
                }
            },
            "userInfo": {
                "apiKey": "你的图灵apikey",
                "userId": "robot"
            }
        }
        try:
            r=requests.post(apiUrl,json=data).json()
            info=r['results'][0]['values']['text']
            return info
        except:
            return

    @itchat.msg_register([itchat.content.TEXT], isGroupChat=True)  # 群消息的处理
    def print_content(msg):
        if msg.User["NickName"] in group:# 这里可以在后面加更多的or msg.User["NickName"]=='你希望自动回复群的名字
            if str(msg['Text'][0:4])=="文库下载":
                huifubdwk=0
                i=0
                while(huifubdwk==0):
                    huifubdwk=GET_SHORTURL(str(msg['Text'].replace("文库下载","")),i)
                    if i>int(len(zhmm)/2):
                        huifubdwk="获取下载链接失败,请检查是否是专业文档或付费文档，或者是没有按规定格式下载"
                        break
                    else:
                        i=i+1;
                print(msg.User['NickName'] + ":" + msg['Text'] )  # 打印哪个群给你发了什么消息
                print("%s+\n"%huifubdwk)  # 打印机器人回复的消息
                itchat.send(u'@%s\u2005 %s' % (msg['ActualNickName'],huifubdwk), msg['FromUserName'])
            elif str(msg['Text'][0:4])=="观看电影":
                huifubdwk=getvideo(str(msg['Text'].replace("观看电影","")))
                print(msg.User['NickName'] + ":" + msg['Text'] )  # 打印哪个群给你发了什么消息
                print("%s+\n"%huifubdwk)  # 打印机器人回复的消息
                itchat.send(u'@%s\u2005 %s' % (msg['ActualNickName'],huifubdwk), msg['FromUserName'])
            elif str(msg['Text'][0:4])=="@机器人":
                huifubdwk=get_info(str(msg['Text'].replace("@机器人","")))
                print(msg.User['NickName'] + ":" + msg['Text'] )  # 打印哪个群给你发了什么消息
                print("%s+\n"%huifubdwk)  # 打印机器人回复的消息
                itchat.send(u'@%s\u2005  %s' % (msg['ActualNickName'],huifubdwk), msg['FromUserName'])
            elif str(msg['Text'][0:2]) == "搜索":
                huifubdwk = search(str(msg['Text'].replace("搜索", "")))
                print(msg.User['NickName'] + ":" + msg['Text'])  # 打印哪个群给你发了什么消息
                print("%s+\n" % huifubdwk)  # 打印机器人回复的消息
                itchat.send(u'@%s\u2005  %s' % (msg['ActualNickName'], huifubdwk), msg['FromUserName'])
            else:# 不是链接直接忽略
                print(msg['Text'])
        else:#不是相应群直接忽略
            pass


    # 登录微信
itchat.auto_login(hotReload=True)
login_req()
itchat.run()
