import csv
import os
from ../api_main/models import Team

def run():
    # this refers to the csv file that should be read
    # file = open(INSERT_FILE_PATH_HERE)
    read_file = csv.reader(file)

    # avoid header values
    count = 1

    for team in read_file:
        if count == 1:
            pass
        else:
            print(team)
            Team.objects.create(series=team[0], name=team[1], year=team[2], era=team[3], colors=[4], actors=[5])