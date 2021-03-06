import urllib
import urllib.request as request_
from http import cookiejar
import re
import json
import sys 
import base64
import binascii
import rsa

class weiboLogin:
    def getCookies(self):
        #获取一个保存cookies的对象
        cj = cookiejar.LWPCookieJar()
        #将一个保存cookies对象和一个HTTP的cookie的处理器绑定
        cookie_support = request_.HTTPCookieProcessor(cj)
        #创建一个opener,设置一个handler用于处理http的url打开
        opener = request_.build_opener(cookie_support, request_.HTTPHandler)
        #安装opener，此后调用urlopen()时会使用安装过的opener对象
        request_.install_opener(opener)
        


    #预登陆获得 servertime, nonce, pubkey, rsakv
    def getServerData(self):
        url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=MTg3MDE3NzAzMTM%3D&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)&_=1449841204179'
        data = urllib.request.urlopen(url).read().decode('utf-8')
        p = re.compile('\((.*)\)')
        data = p.search(data).group(1)
        try:
            json_data = json.loads(data)
            servertime = json_data['servertime']
            nonce = json_data['nonce']  
            pubkey = json_data['pubkey']  
            rsakv = json_data['rsakv']
            pcid = json_data['pcid']
            print(json_data) 
            return servertime, nonce, pubkey, rsakv
        except:
            print("get Server Data error")
            return 0

    #base64加密用户名
    def getUsername(self, username):
        username_ = urllib.parse.quote_plus(username)
        username = base64.encodebytes(username_.encode('utf-8'))[:-1] 
        return username

    #RSA2加密密码
    def getPassword(self, password, servertime, nonce, pubkey):  
        rsaPublickey = int(pubkey, 16)  
        key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥  
        message = str(servertime) + '\t' + str(nonce) + '\n' + str(password) #拼接明文js加密文件中得到
        passwd = rsa.encrypt(message.encode('utf-8'), key) #加密
        passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。          
        return passwd

    #获取需要提交的表单数据     
    def getFormData(self,userName,password,servertime,nonce,pubkey,rsakv):  
        userName = self.getUsername(userName)  
        psw = self.getPassword(password,servertime,nonce,pubkey)            
        form_data = {  
            'entry':'weibo',  
            'gateway':'1',  
            'from':'',  
            'savestate':'7',  
            'useticket':'1',  
            'ssosimplelogin': '1',  
            'vsnf':'1',  
            'su':userName,  
            'service':'miniblog',  
            'servertime':servertime,  
            'nonce':nonce,  
            'pwencode':'rsa2',  
            'rsakv':rsakv,  
            'sp':psw,  
            'sr':'1366*768',  
            'encoding':'UTF-8',  
            'prelt':'115',  
            'url':'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',  
            'returntype':'META'  
            }  
        formData = urllib.parse.urlencode(form_data)  
        return formData.encode()

    def login(self,username,psw):  
        self.getCookies()  
        url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'  
        servertime,nonce,pubkey,rsakv = self.getServerData()  
        formData = self.getFormData(username,psw,servertime,nonce,pubkey,rsakv)  
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'}  
        req  = urllib.request.Request(  
            url = url,  
            data = formData,  
            headers = headers,
            method = 'POST'  
        ) 
        #print(req.data) 
        result = urllib.request.urlopen(req) 
        s = result.read().decode('gbk')
        print(s)  
        #还没完！！！这边有一个重定位网址，包含在脚本中，获取到之后才能真正地登陆    
        try:  
            login_url = re.findall("location.replace\(.(.*?).\);" , s)[0]  
            print(login_url)
            #由于之前的绑定，cookies信息会直接写入  
            res = urllib.request.urlopen(login_url)  
            print("Login success!")  
        except:  
            print('Login error!')  
            return 0

    def postMsg(self):
         
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0','Referer':'http://weibo.com/u/5108659863/home?topnav=1&wvr=6'}
        url = 'http://weibo.com/aj/mblog/add?_wv=5'
        formData = {
            'location':'v6_content_home',
            'appkey':'',
            'style_tpye':'1',
            'pic_id':'',
            'text':'hello chen da cong !',
            'pdetail':'',
            'rank':'0',
            'rankid':'',
            'module':'stissue',
            'pub_tpye':'dialog',
            '_t':'0'
            }
        formData = urllib.parse.urlencode(formData)     
        req = urllib.request.Request(
            url = url,
            data = formData.encode(),
            headers = headers,
            method = 'POST'
        )
        result = urllib.request.urlopen(req)
        print(result.read())


test = weiboLogin()

test.login('18701770313', '1914346128')
test.postMsg()
