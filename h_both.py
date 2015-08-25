
# import csv

# # donors = {
# #    'donor': 'Sole Invest', 
# #    'amount': '200000'
# #    }


# donors = list(csv.DictReader(open("/Users/gunnkh/Desktop/h_donor.csv", 'rU'), dialect=csv.excel_tab))

import pandas as pd
donors = pd.read_csv( "/Users/gunnkh/Desktop/lede/h_donors_all.csv" )

#print donors
#[d for d in donors]
#print d

# def h_donor(donor):
#   donor = donors['donor']
#   return donors 


# def h_amount(donor):
#   amount = donors['amount']
#   return donors['amount']

#print donors

#for s in ( donors['donor']+" ga "+donors['amount'].astype( str ) ).values:
#  print s,"kroner til Høyres valgkamp."


def h_sentence(d):
  donor = d['donor']
  amount = d['amount']
  return "{0} ga {1} kroner til Høyres valgkamp.".format(donor, amount)

#def h_sentence(d):
#  return "{donor} ga {amount} kroner til Høyres valgkamp".format(**d)

# #print h_sentence(donors)

# for d in donors:
#   print h_sentence(d)

for index, d in donors.iterrows():
  print h_sentence(d)
