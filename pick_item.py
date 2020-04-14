import pandas as pd
from random import randint
import argparse
import glob
import os
import json

mylist        = 'mundane_treasure'
item_nr       = None
output_format = 'auto'

def pick_item( mylist, item = None ):
	if mylist not in get_available_lists():
		return False
	try:
		items = pd.read_csv( 'lists/' + mylist + '.csv' )
	except:
		return False
	if ( isinstance(item, int) ):
		item = (item-1) % items.shape[0]
	else:
		item = randint(0, items.shape[0]-1)
	#print(items.shape[0])
	#print(item)
	return [ items.iloc[[item]], item ]

def display_item( item_list, output_format = output_format ):
	if 'auto' == output_format:
		if 1 < item_list[0].shape[1]:
			output_format = 'json'
		else:
			output_format = 'simple'

	if isinstance(item_list[0], bool) and False == item_list[0]:
		print (0)
		return False
	if ( 'simple' == output_format ):
		output = item_list[0].iloc[0]['desc']
	else:
		item_list[0]['nr'] = item_list[1] + 1
		output = item_list[0].iloc[0].to_json()
	print( output )

def get_available_lists():	
	names = [os.path.basename(x).replace('.csv','') for x in glob.glob("./lists/*.csv")]
	return names

# create parser
parser = argparse.ArgumentParser()
 
# add arguments to the parser
parser.add_argument("--mylist", choices=get_available_lists(), required=True, help='Required. The list from which you want to choose.')
parser.add_argument("--item", type=int, required=False, default=None, help='Optional. The item you want to pick from the list. 1 is the first item. If this number is larger than the amount of items in the list, the counter will just wrap around. So selecting \'item 120\' from a list with only 100 items, will select the 20th item.')
parser.add_argument("--format", choices=['json','simple','auto'], required=False, default='auto', help='Optional. The output format. \'simple\' will always just return the description, \'json\' will always return a json representation of the item which will always have at least a \'desc\' key. \'auto\' will pick one of the previous formats, based on the number of data columns present. If there is only one (\'desc\') it will just output the value of the \'desc\' column')

# parse the arguments
args = parser.parse_args()

mylist = args.mylist

if args.item:
	item_nr = args.item

if args.format:
	output_format = args.format

display_item( pick_item( mylist, item_nr ), output_format )