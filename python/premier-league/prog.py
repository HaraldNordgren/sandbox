#!/usr/bin/env python3

import unidecode

NEXT_YEAR = [
"August",
"September",
"October",
"November",
"December",
]

def plus_one(map, key):
	if key in map:
		map[key] +=1
		return
	map[key] = 1

def normalize_name(name):
	name = name.replace("'", "")
	return unidecode.unidecode(name)

with open("month") as f:
    months = f.readlines()

with open("year") as f:
    years = f.readlines()


yearly_player_of_the_month = {}
player_of_the_year = {}

for m in months:
	columns = m.split("	")

	month = columns[0]
	year = int(columns[1])
	if month in NEXT_YEAR:
		year += 1

	year_string = "%d–%d" % (year-1, year)

	if year_string not in yearly_player_of_the_month:
		yearly_player_of_the_month[year_string] = {}

	name = columns[3]
	name = name.replace("†", "")
	name = normalize_name(name)

	plus_one(yearly_player_of_the_month[year_string], name)

for y in years:
	columns = y.split("	")
	year = columns[0]
	if len(year) == 7:
		year = year[:5] + year[:2] + year[5:]
	
	name = columns[2].strip(" (2)")
	name = normalize_name(name)
	player_of_the_year[year] = name

for year, player in player_of_the_year.items():
	monthly_awards = 0
	if player in yearly_player_of_the_month[year]:
		monthly_awards = yearly_player_of_the_month[year][player]

	max_value = 0
	max_players = []

	for player_per_month, count in yearly_player_of_the_month[year].items():
		if count > max_value:
			max_value = count
			max_players = [player_per_month]
		elif count == max_value:
			if player_per_month not in max_players:
				max_players.append(player_per_month)

	if max_value > 1:
		print("%s %s (%s won PotM most times at %s)" % (year, player, ", ".join(max_players), max_value))
	else:
		print("%s %s (no one won PotM more than once)" % (year, player))
