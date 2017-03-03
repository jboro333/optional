#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

import urllib2
from bs4 import BeautifulSoup


class Client(object):
    """Getting the name of the book taht's free today"""

    def __init__(self):
        super(Client, self).__init__()

    def get_web(self, html):
        f = urllib2.urlopen(html)
        html = f.read()
        f.close()
        return html

    def lets_parse(self, html):
            soup = BeautifulSoup(html, 'html.parser')
            books = soup.find_all("h2")
            for book in books:
                return book

    def print_book(self, book):
            book.text
            for book in book:
                book = book.strip(' \t\n\r')
            print book

    def run(self):
        web = "https://www.packtpub.com/packt/offers/free-learning"
        html = self.get_web(web)
        free = self.lets_parse(html)
        self.print_book(free)


if __name__ == "__main__":
    client = Client()
    client.run()
    # print get_web("https://www.packtpub.com/packt/offers/free-learning")
