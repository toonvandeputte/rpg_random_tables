import csv
from random import randint
import glob
import os

def pick_item( mylist, item = None ):
	items = list()
	if mylist not in get_available_lists():
		return "List '" + str(mylist) + "' does not exist"
	try:
		with open( 'lists/' + mylist + '.csv' ) as csvfile:
			for row in csv.DictReader(csvfile):
				items.append(row)
	except:
		return "'" + mylist + ".csv' cannot be opened"
	if ( isinstance(item, int) ):
		item = (item-1) % len(items)
	else:
		item = randint(0, len(items)-1)
	return [ items[item], item, mylist ]

def get_available_lists():	
	names = [os.path.basename(x).replace('.csv','') for x in glob.glob("./lists/*.csv")]
	return names