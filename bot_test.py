import csv
import codecs
import os

# Read in the old content

if os.path.isfile("/Users/gunnkh/Desktop/lede/test_both_file.txt"):
	with codecs.open("/Users/gunnkh/Desktop/lede/test_both_file.txt", 'rU', encoding="utf-8") as inputfile:
		old_lines = [s.strip() for s in inputfile.readlines()]
else:
	old_lines = []

# scraper - Do whatever to create new_lines
import urllib2
from bs4 import BeautifulSoup
url = 'http://hoyre.no/Presse/%C3%98konomiske-bidrag/%C3%98konomiske-bidrag-2015'
connection = urllib2.urlopen(url)
page = BeautifulSoup(connection.read())
div_tag = page.find('div', attrs={'class':'articlebody small-12 medium-12 large-12 large-centered column'})

p_tag = div_tag.find_all('p')

donor15 = []
for p in p_tag:
    donors = p.getText()

    donor15.append(donors)
#    print donor15


# new line is list of sentencenses
#new_lines = ['mm','ss']
donor15

# Find all of the changes
changes = [line for line in donor15 if line not in old_lines]

print "Changes are"
print changes

# Save new lines to the output file
with codecs.open("/Users/gunnkh/Desktop/lede/test_both_file.txt", "wb", encoding="utf-8") as outfile:
    for line in donor15:
        # For some reason you need to add a newline so
        # it doesn't all run together
        outfile.write(line + '\n')


# import csv

# with open("input.txt") as file: 
#     reader = csv.reader(file, delimiter=' ')
#     for row in reader:
#         # print row

