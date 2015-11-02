# read yaml and json files created and 
# pretty print the datastructyre returned
import json
#import pprint
import yaml



with open("test_file2.json") as f:
	new_list = json.load(f)

#print new_list


#from pprint import pprint as pp
#pp(new_list)


with open('some_file3.yml') as g:
	new_structure = yaml.load(g)

#print new_structure

from pprint import pprint as pp

pp(new_list)
pp(new_structure)
