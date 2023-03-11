import argparse
from _datetime import datetime
import json
from models import Author, Quotes

"""
py main.py --action -a load or find
"""

parser = argparse.ArgumentParser(description='load or find')

parser.add_argument('-a', '--action')


def load_json():
    with open('json-files/authors.json', 'r', encoding='utf-8') as fh:
        rez = json.load(fh)
        for itr in rez:
            new_author = Author()
            new_author.description = itr['description']
            new_author.born_date = datetime.strptime(itr['born_date'], '%B %d, %Y').date()
            new_author.born_location = itr['born_location']
            new_author.fullname = itr['fullname']
            new_author.save()

    with open('json-files/qoutes.json', 'r', encoding='utf-8') as fh:
        rez = json.load(fh)
        for itr in rez:
            authors = Author.objects(fullname=itr['author'])
            if len(authors) > 0:
                cur_author = [0]
            new_quote = Quotes(author=cur_author)
            new_quote.quote = itr['quote']
            new_quote.tags = itr['tags']
            new_quote.save()


def find_in_db():
    while True:
        command = input('insert command and volume:')
        if command[:4] == 'exit':
            break
        else:
            agr = command.split(':')
            f_name = agr[0]
            if f_name == 'name':
                authors = Author.objects(fullname=agr[1])
                for author in authors:
                    print(author.to_mongo().to_dict())
            elif f_name == 'tag':
                quotes = Quotes.objects(tags=agr[1])
                for quote in quotes:
                    print(quote.to_mongo().to_dict())
            elif f_name == 'tags':
                quotes = Quotes.objects(tags__in=agr[1].split(' '))
                for quote in quotes:
                    print(quote.to_mongo().to_dict())


if __name__ == '__main__':
    if 'load' == vars(parser.parse_args()).get('action'):
        load_json()
    else:
        find_in_db()

