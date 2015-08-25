$ crontab -e

5****

cron.txt file

python ~/



url = 'http://hoyre.no/Presse/%C3%98konomiske-bidrag/%C3%98konomiske-bidrag-2015'
connection = urllib2.urlopen(url)
page = BeautifulSoup(connection.read())

div_tag = page.find('div', attrs={'class':'articlebody small-12 medium-12 large-12 large-centered column'})

#donors = []
#for p in p_tag:
p_tag = div_tag.find_all('p')

#    print p.getText()
#    donors.append( p.getText() )
#print p_tag

for p in p_tag:
    donors = p.getText()
    print donors
