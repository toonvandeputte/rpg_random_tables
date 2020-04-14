# D100 random tables
This is a simply Python script to generate random items for your tabletop or virtual RPGs, based on a number of D100 tables that are available online.

## Basic usage

The script picks a random or specific item from the available lists. It returns this either as simple text, or a json object with some additional data (like the item nr that was chosen).

### Some examples

`python3 pick_item.py --mylist trinkets --format=json`

will return:

`{"desc":"A tuning fork that produces the most satisfying note anyone that hears it has ever heard","nr":93}`

As you can see, the JSON data also includes the number of the item. Knowing this, you can easily get the same item again with:

`python3 pick_item.py --mylist trinkets --format json --item 93`

If you just want the text description of that item, you'd do:

`python3 pick_item.py --mylist trinkets --format simple --item 93`

to get:

`A tuning fork that produces the most satisfying note anyone that hears it has ever heard`

For complete instructions, do `python3 pick_item.py -h`.


## Requirements
This script requires Python 3.
The only external library required is Pandas, it is used for parsing the CSV files and selecting the (randomly) requested item from them

## Sources

* Mundane Treasure: https://400billionsuns.blogspot.com/2016/02/random-tables-100-mundane-treasures.html
* Trinkets: https://www.reddit.com/r/d100/comments/6zx05f/d100_trinkets/
* Flawed Utopias: https://elfmaidsandoctopi.blogspot.com/2017/02/d100-flawed-utopias.html
