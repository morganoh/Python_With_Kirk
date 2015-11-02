import ciscoconfparse


from ciscoconfparse import CiscoConfParse


cisco_input = CiscoConfParse('cisco_ipsec.txt')

cisco_crypto = cisco_input.find_objects(r"crypto map CRYPTO") 

#print type (cisco_crypto)

for i in cisco_crypto:
	print i.text
	for child in i.children:
		print child.text

