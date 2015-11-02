import yaml
import json

# create a list

my_list = range(10)
print type(my_list)

# add a dictionary to the list
my_list.append({})

# add some key/value pairs to dict
my_list[-1] ['attribs'] = range(7)
my_list[-1] ['ip_address'] = '10.10.10.129'
my_list[-1] ['net_mask'] = '255.255.255.255'
#for item in my_list:
#        print item
length = len(my_list)

print 'Length of this list is: %i  ' %length 

# create yaml structure style 1

dumped = yaml.dump(my_list)
print dumped

# create yaml structure  style 2
dumped2 = yaml.dump(my_list, default_flow_style=True)
print dumped2

# write yaml to files using different styles
with open("some_file.yml" , "w") as f:
	f.write(yaml.dump(my_list)  )
with open("some_file2.yml","w") as f:
	f.write( yaml.dump(my_list, default_flow_style=True) )
with open("some_file3.yml","w") as f:
        f.write( yaml.dump(my_list, default_flow_style=False) )	


# Now create JSON 

with open("test_file.json" , "w") as g:
	json.dumps(my_list)

with open("test_file2.json" , "w") as g:
        json.dump(my_list , g)

