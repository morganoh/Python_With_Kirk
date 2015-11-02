import ciscoconfparse


from ciscoconfparse import CiscoConfParse


cisco_input = CiscoConfParse('cisco_ipsec.txt')

cisco_crypto2 = cisco_input.find_objects_w_child(parentspec = r"^crypto map CRYPTO", childspec = r"pfs group2") 

#print type (cisco_crypto2)

for i in cisco_crypto2:
	print i.text
	for child in i.children:
		print child.text

