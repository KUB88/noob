from switcher import Switcher

switcher = Switcher('9.9.9.1', 'Qzxt@1088', 'yanghua')
switcher.login()
ip, version = switcher.get_version()
print(ip+' '+version)
#buff = switcher.send_cmd('sh run', 'More', 'test error')
#print(buff)b