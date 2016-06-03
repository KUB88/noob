import paramiko
import os,sys,time

#堡垒机信息
blip = '10.10.113.28'
bluser = 'neteagle'
blpasswd = 'ciscoPass0909'

#主机测试
host_ip = '9.9.9.25'
host_user = 'yanghua'
host_passwd = 'Qzxt@1088'

port = 22
passinfo='assword: '
paramiko.util.log_to_file('C:\\Users\\yangh\\Desktop\\test.log')
file = open('C:\\Users\\yangh\\Desktop\\ip.txt','w+')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip, username=bluser, password=blpasswd)

channel = ssh.invoke_shell()
channel.settimeout(30)

buff = ''
resp = ''
channel.send('ssh '+host_user+'@'+host_ip+'\n')
while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception as e:
        print('Error info:%s connection time' % str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp.decode()
    print(buff)
    if not buff.find('yes/no') == -1:
        channel.send('yes\n')
        buff = ''
print('check point 0')
channel.send(host_passwd+'\n')

buff = ''
#print('check point')
while not buff.endswith('#'):
    resp = channel.recv(9999)
    if not resp.find(passinfo.encode()) == -1:   #输入密码错误重新输入
        print('Error info: Authentication faild.')
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp.decode()

ipadd = ['10.10.100.' + str(i) for i in range(1,256)]
print('check point')

buff = ''
for ip in ipadd:
    channel.send('ping '+ip+'\n')
    while True:
        resp = channel.recv(9999)
        buff += resp.decode()
        #print(buff)
        #print('===========================')
        if not buff.find('!!') == -1:
            file.write(ip+' is alive\n')
        if not buff.find('.....') == -1:
            file.write(ip+' is not alive\n')
        if buff.endswith('#'):
            buff = ''
            file.flush()
            break
file.close()

