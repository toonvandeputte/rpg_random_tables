zip -r ./function.zip pick_item.py pick_item-lambda.py lists
aws lambda update-function-code --function-name pickRandomThings --zip-file fileb://function.zip
exit