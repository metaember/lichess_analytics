# lichess_analytics
Small scripts to stalk and occasionally troll [Lichess](https://en.lichess.org) players.

## Running
To run, first set up a file called `local_data.txt` in the root folder, and write the name of the desired user on the first line. Then, proceed to running the python file. 

Important note: Do not run too frequently, we like Lichess, we do not want to spam their servers. The code currenty does not check for [429 status](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#429)!

## Todo:
- Maintain some form of history of the evolution of the number of games, perhaps the api lets us get that
- Email the player if thay are on a winning/loosing streak, or if they are abusing of Lichess


Disclaimer: This is intended for use on friends only, and for motivation :).
