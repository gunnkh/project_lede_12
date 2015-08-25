# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime import Text

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open('/Users/gunnkh/Desktop/lede/test_both_file.txt', 'rb')
# Create a text/plain message
msg = Text.MIMEText(fp.read())
fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Test'] = 'The contents of %s' % textfile
msg['gunnkh@vg.no'] = me
msg['gunnkarihegvik@gmail.com'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()


