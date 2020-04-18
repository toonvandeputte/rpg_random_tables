import pick_item
import argparse
import json

mylist        = 'mundane_treasure'
item_nr       = None
output_format = 'auto'

# create parser
parser = argparse.ArgumentParser()
 
# add arguments to the parser
parser.add_argument("mylist", choices=pick_item.get_available_lists(), help='Required. The list from which you want to choose.')
parser.add_argument("--item", type=int, required=False, default=None, help='Optional. The item you want to pick from the list. 1 is the first item. If this number is larger than the amount of items in the list, the counter will just wrap around. So selecting \'item 120\' from a list with only 100 items, will select the 20th item.')
parser.add_argument("--format", choices=['object','json','simple','auto'], required=False, default='auto', help='Optional. The output format. \'simple\' will always just return the description, \'object\' will always return the native object (ordereddict). \'json\' will always return a stringified json representation of the item which will always have at least a \'desc\' key. \'auto\' will pick one of the previous formats, based on the number of data columns present. If there is only one (\'desc\') it will just output the value of the \'desc\' column')

# parse the arguments
args = parser.parse_args()

mylist = args.mylist

if args.item:
	item_nr = args.item

if args.format:
	output_format = args.format

def display_item( item_list, output_format = 'auto' ):
	if 'auto' == output_format:
		if 1 < len( item_list[0] ):
			output_format = 'object'
		else:
			output_format = 'simple'
	if isinstance(item_list, str):
		return item_list
	if ( 'simple' == output_format ):
		output = item_list[0]['desc']
	else:
		output = {
			"item" : item_list[0],
			"nr" :  int( item_list[1] ) + 1,
			"list" : item_list[2]
		}
		if 'json' == output_format:
			output = json.dumps( output )
	return output

print( display_item( pick_item.pick_item( mylist, item_nr ), output_format ) )