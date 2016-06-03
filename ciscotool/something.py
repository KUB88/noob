import re
s = '''

MTU: 1500
Physical Location: QinZhou
Mgmt address(es):
    IPv4 Address: 1.1.1.1
----------------------------------------
Device ID:YB14-BD-Core-I6-N7K-01-BSS-VDC(FXS1841Q1K2)
System Name: YB14-BD-Core-I6-N7K-01-BSS-VDC

Interface address(es):
    IPv4 Address: 10.10.163.146
Platform: N7K-C7010, Capabilities: Router Switch Supports-STP-Dispute
Interface: Ethernet1/37, Port ID (outgoing port): Ethernet10/3
Holdtime: 161 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(8a)

Advertisement Version: 2
Duplex: full

MTU: 1500
----------------------------------------
Device ID:YB14-BD-Core-I6-N7K-01-BSS-VDC(FXS1841Q1K2)
System Name: YB14-BD-Core-I6-N7K-01-BSS-VDC

Interface address(es):
    IPv4 Address: 10.10.163.146
Platform: N7K-C7010, Capabilities: Router Switch Supports-STP-Dispute
Interface: Ethernet1/38, Port ID (outgoing port): Ethernet8/11
Holdtime: 161 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(8a)

Advertisement Version: 2
Duplex: full

MTU: 1500
----------------------------------------
Device ID:YB14-BD-Core-I6-N7K-01-BSS-VDC(FXS1841Q1K2)
System Name: YB14-BD-Core-I6-N7K-01-BSS-VDC

Interface address(es):
    IPv4 Address: 10.10.163.146
Platform: N7K-C7010, Capabilities: Router Switch Supports-STP-Dispute
Interface: Ethernet1/39, Port ID (outgoing port): Ethernet8/3
Holdtime: 161 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(8a)

Advertisement Version: 2
Duplex: full

MTU: 1500
----------------------------------------
Device ID:QC-NEXUS7K-B-BOSS(TBM16416441)
System Name: QC-NEXUS7K-B-BOSS

Interface address(es):
    IPv4 Address: 10.10.161.50
Platform: N7K-C7010, Capabilities: Router Switch Supports-STP-Dispute
Interface: Ethernet1/40, Port ID (outgoing port): Ethernet1/40
Holdtime: 164 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(14)

Advertisement Version: 2
Duplex: full

MTU: 1500
Physical Location: QinZhou
----------------------------------------
Device ID:QC-NEXUS7K-B-BOSS(TBM16416441)
System Name: QC-NEXUS7K-B-BOSS

Interface address(es):
    IPv4 Address: 10.248.180.22
Platform: N7K-C7010, Capabilities: Router Switch IGMP Filtering Supports-STP-Dispute
Interface: Ethernet3/2, Port ID (outgoing port): Ethernet3/2
Holdtime: 164 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(14)

Advertisement Version: 2

Native VLAN: 1
Duplex: full
Physical Location: QinZhou
----------------------------------------
Device ID:JQ-NEXUS7K-A-BOSS(TBM16512173)
System Name: JQ-NEXUS7K-A-BOSS

Interface address(es):
    IPv4 Address: 10.10.161.134
Platform: N7K-C7010, Capabilities: Router Switch Supports-STP-Dispute
Interface: Ethernet3/4, Port ID (outgoing port): Ethernet1/3
Holdtime: 160 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(8a)

Advertisement Version: 2
Duplex: full

MTU: 1500
Physical Location: QinZhou
----------------------------------------
Device ID:QB-N5K-2(SSI174204YY)
System Name: QB-N5K-2

Interface address(es):
    IPv4 Address: 10.10.111.15
Platform: N5K-C5548UP, Capabilities: Switch IGMP Filtering Supports-STP-Dispute
Interface: Ethernet3/26, Port ID (outgoing port): Ethernet1/29
Holdtime: 159 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 5.2(1)N1(8a)

Advertisement Version: 2

Native VLAN: 1
Duplex: full

MTU: 1500
Physical Location: QinZhou
Mgmt address(es):
    IPv4 Address: 1.1.1.2
----------------------------------------
Device ID:QC_BOSS_C6513_13.BOSS
VTP Management Domain Name: SHMCC

Interface address(es):
    IPv4 Address: 10.10.100.12
Platform: WS-C6513, Capabilities: Router Switch IGMP Filtering 
Interface: Ethernet3/39, Port ID (outgoing port): TenGigabitEthernet11/1
Holdtime: 144 sec

Version:
Cisco IOS Software, s72033_rp Software (s72033_rp-IPSERVICESK9_WAN-M), Version 12.2(33)SXH4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2008 by Cisco Systems, Inc.
Compiled Mon 10-Nov-08 08:30 by prod_rel_team

Advertisement Version: 2
Duplex: full
Mgmt address(es):
    IPv4 Address: 10.10.100.12
----------------------------------------
Device ID:QB-CCS-Z7609-1.BOSS
VTP Management Domain Name: SHMCC

Interface address(es):
    IPv4 Address: 10.10.151.12
Platform: CISCO7609, Capabilities: Router Switch IGMP Filtering 
Interface: Ethernet3/40, Port ID (outgoing port): TenGigabitEthernet8/1
Holdtime: 127 sec

Version:
Cisco IOS Software, s72033_rp Software (s72033_rp-IPSERVICESK9_WAN-M), Version 12.2(33)SXH4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2008 by Cisco Systems, Inc.
Compiled Mon 10-Nov-08 08:30 by prod_rel_team

Advertisement Version: 2

Native VLAN: 1
Duplex: full
Mgmt address(es):
    IPv4 Address: 10.10.151.12
'''
a = re.split('-+-',s)
print(a)