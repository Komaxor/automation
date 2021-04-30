#import scraper
from heapq import nlargest
import csv


def sort_top(cast):
    with open(file=cast, mode='r') as file:
        file.readline()  # remove column title
        cast_dict = {}
        while True:
            actor = str(file.readline()).strip('\n')
            if actor == '':
                break
            if actor not in cast_dict:
                cast_dict[actor] = 1
            else:
                cast_dict[actor] += 1
        top_cast = nlargest(5, cast_dict, key=cast_dict.get)
        return top_cast


def top_cast(cast):
    top_cast = sort_top(cast)
    file_name = 'imdbcast/top-cast.csv'
    with open(file=file_name, mode="w") as csvfile:
        writer = csv.writer(csvfile)
        for actor in top_cast:
            writer.writerow([actor])
    return file_name
