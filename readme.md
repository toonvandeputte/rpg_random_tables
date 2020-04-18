# D100 random tables
This is a simply Python script to generate random items for your tabletop or virtual RPGs, based on a number of D100 tables that are available online.

## What does it do?

The script picks a random or specific item from the available lists. It returns this either as simple text, or a json object with some additional data (like the item nr that was chosen). You can use this script from the commandline via `pick_item-cli.py` or use it in an API-triggered Lambda function via `pick_item-lambda.py`. The latter is probably the most easily adaptable to other contexts.

## CLI vs Lambda

* pick_item.py contains the main functionality to load lists and pick an item. You would normally not use this from the command line, it is imported in the two other .py files you're more likely to use.
* pick_item-cli.py is a wrapper that takes command line arguments and passes them on. This is what you should be using for use from the command line.
* pick_item-lambda.py is a wrapper that is built for an API-triggered AWS Lambda function. It takes path-based arguments and uses them to generate a proper REST response. If you are building your own integration, this is probably what you should be basing it on.

## Some CLI examples

* `python3 pick_item-cli.py flawed_utopias`
* `python3 pick_item-cli.py mundane_treasure --output simple`
* `python3 pick_item-cli.py ruined_building_contents --item 20`

Let's go through some sample uses. The following call

`python3 pick_item-cli.py trinkets --format=json`

will return:

`{"desc":"A tuning fork that produces the most satisfying note anyone that hears it has ever heard","nr":93}`

As you can see, the JSON data also includes the number of the item. Knowing this, you can easily get the same item again with:

`python3 pick_item-cli.py trinkets --format json --item 93`

If you just want the text description of that item, you'd do:

`python3 pick_item-cli.py trinkets --format simple --item 93`

to get:

`A tuning fork that produces the most satisfying note anyone that hears it has ever heard`

This is handy for cases where you just want to load the text into some dumb application/view that can't handle json. 

For complete instructions, do `python3 pick_item-cli.py -h`.

## Requirements
This script requires Python 3.
The only external library required is Pandas, it is used for parsing the CSV files and selecting the (randomly) requested item from them

## Sources

* Mundane Treasure: https://400billionsuns.blogspot.com/2016/02/random-tables-100-mundane-treasures.html
* Trinkets: https://www.reddit.com/r/d100/comments/6zx05f/d100_trinkets/
* Flawed Utopias: https://elfmaidsandoctopi.blogspot.com/2017/02/d100-flawed-utopias.html
* Ruined Building Contents: https://www.reddit.com/r/d100/comments/6zx6gf/d100_ruined_building_contents/
* Market Stalls: http://beyondtheblackgate.blogspot.com/search?q=d100
* Fairy Tale Equipment: https://violentmediarpg.blogspot.com/2017/07/big-basic-weird-fairytale-equipment.html
* Riddles: https://www.reddit.com/r/d100/comments/6zxes8/d100_riddles/

## Known todos

* Make the whole API REST response generation more DRY.
* Create a help endpoint/method for the API (Lambda) version.
* Lists on S3 or via other easily parametrized source?