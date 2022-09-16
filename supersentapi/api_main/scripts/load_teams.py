import csv
import os
from ..models import Team

def run():
    # this refers to the csv file that should be read
    file = open('api_main/scripts/sentapi_seed_data.csv')
    read_file = csv.reader(file)

    # avoid header values
    count = 1

    for team in read_file:
        if count == 1:
            pass
        else:
            print(team)
            Team.objects.create(series_number=team[0], name=team[1], year=team[2], era=team[3], colors=team[4], actors=team[5])
        count = count + 1