from subprocess import call
from os import chdir, getcwd
from sorter import top_cast
from delete_csv import delete_csv
from drive_handler import process

if __name__ == "__main__":
    cast_file = "cast.csv"
    delete_csv(cast_file)
    chdir("imdbcast")
    call(["scrapy", "crawl", "cast", "-o", cast_file])
    print(getcwd())
    chdir("..")
    print(getcwd())
    cast_file = top_cast('imdbcast/cast.csv')
    process(cast_file)
    email_file = 'emails.csv'
    process(email_file)
