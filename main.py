from subprocess import call
from os import chdir

if __name__ == "__main__":
    chdir("imdbcast")
    call(["scrapy", "crawl", "cast", "-o", "cast.csv"])
