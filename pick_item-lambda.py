import pick_item
import json

def format_item( item_list ):
	output = {
		"statusCode": 200,
		"body" : {}
	}
	if isinstance(item_list, str) :
		output['statusCode'] = 400
		output['body'] = item_list
		return output
	output['body'] = {
		"message" : "OK",
		"item" : item_list[0],
		"nr": int( item_list[1] ) + 1,
		"list": item_list[2]
	}
	return output

def api_render( item_formatted, output_format='auto' ):
	if 400 == item_formatted['statusCode']:
		return item_formatted
	if 'simple' == output_format:
		item_formatted['body'] = item_formatted['body']['item']['desc']
	else:
		item_formatted['body'] = json.dumps( item_formatted['body'] )
	return item_formatted

def lambda_handler( event, context ):

	#root path
	if None == event['pathParameters']:
		lists = pick_item.get_available_lists()
		returnbody = {
			"message" : "OK",
			"lists" : lists
		}
		return {
			"statusCode" : 200,
			"body" : json.dumps( returnbody )
		}

	#has path parameters
	output_format='auto'
	mylist = 'mundane_treasure'
	item = None

	if 'output_format' in event['pathParameters']:
		output_format = event['pathParameters']['output_format']
	if 'mylist' in event['pathParameters']:
		mylist = event['pathParameters']['mylist']
		if 'item' in event['pathParameters']:
			if int(event['pathParameters']['item']) > 0:
				item = int( event['pathParameters']['item'] )
	return api_render( format_item( pick_item.pick_item( mylist, item ) ), output_format )