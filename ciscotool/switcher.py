import paramiko
import sys,os,time

class ProxyServer(object):
    """docstring for ProxyServer"""
    def __init__(self, host = '10.10.113.28', password = 'ciscoPass0909', username = 'neteagle'):
        self.host = host
        self.password = password
        self.username = username

    def logging(self, path = 'C:\\Users\\yangh\\Desktop\\test.log'):
        paramiko.util.log_to_file(path)

    def login(self, timeout = 6):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname = self.host, username = self.username, password = self.password)
        self.channel = self.ssh.invoke_shell()
        self.channel.settimeout(timeout)
        return self.channel

    def connection_close(self):
        self.channel.close()
        self.ssh.close()


class Switcher(object):
    """docstring for Switcher"""
    def __init__(self, host = None, password = None, username = None, path = None):
        self.host = host
        self.password = password
        self.username = username
        self.path = path
        self.connection = 0
        self.version = None
        try:
            self.proxy = ProxyServer()
            if not self.path: 
                self.proxy.logging()
            else:
                self.proxy.logging(path)
            self.channel = self.proxy.login()
        except:
            print('[-] Error info: proxy server login error!')
            

    def login(self):
        buff = ''
        result = ''
        buff = self.send_cmd('ssh '+self.username+'@'+self.host,'assword: ','connection timeout')
        if not buff.find('yes/no') == -1:
            self.channel.send('yes\n')
            buff = ''
        self.channel.send(self.password+'\n')
        buff = ''
        while not buff.endswith('# '):
            result = self.channel.recv(9999)
            result = result.decode()
            if not result.find('assword') == -1:
                print('[-] Error info: Authentication faild.')
                self.proxy.connection_close()    
            buff += result
        self.connection = 1
        self.version = self.get_version()
        print('[+] login success at '+self.host)

    def get_version(self):
        if connection:
            buff = self.send_cmd('sh version', 'More', 'get version information error.')
            if buff.find('NX-OS') >= 0:
                version = 'NX-OS'
            elif buff.find('Cisco IOS Software') >= 0:
                version = 'IOS'
            else:
                version = 'not cisco device'
            return self.host,version
        else:
            print('[-] not connected to switcher')
            pass

    def send_cmd(self, cmd, keyword, errorinfo, more = None):
        self.channel.send(cmd+'\n')
        buff = ''
        while buff.find(keyword) == -1:
            try:
                result = self.channel.recv(9999)
            except:
                print('[-] '+errorinfo)
                print('[-] connection close')
                self.proxy.connection_close()
            buff += result.decode()
        return buff
        
    def get_neighbours(self, version = None):
        if connection:
            buff = self.send_cmd('sh cdp neighbour detail', '#', 'get cdp neighbour error', more = 'more')