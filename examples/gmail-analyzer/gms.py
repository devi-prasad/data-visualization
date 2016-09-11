from __future__ import print_function
import sys
import re
import contextlib
import mmap

###
### Lists email ids of those from whom I have emailed.
### NOTE: Assumes ASCII char set. Not tested against UNICODE strings.
###

identities = {}  # email id is the key, and name of the contact is the value.
frequencies = {} # email id is the key, and frequency is the value.
count_seen = 0   # how many emails did we check?

def update_identities(emid, name):
  global identities, frequencies
  # convert the email id to a lowercase string.
  emid = emid.lower()
  if not identities.has_key(emid):
    identities[emid] = name
    frequencies[emid] = 1
  else:
    frequencies[emid] = frequencies[emid] + 1


def split_name_and_email_id(s):
  ilab = s.index('<')
  irab = s.index('>')
  name = s[5:ilab].strip()

  if (name is None or len(name) == 0): name='%nan%'
  else:
    if (name[0] == '\'' or name[0] == '\"'):
      name = name[1:len(name)-1]
  emid = s[ilab+1:irab].strip()
  return (name, emid)


###
# This uses a powerful regular expression to tease out only the 'From' header
# field from each email. It then stores the name and email id in the 
# 'identities' dictionary declared above.
# Note this implementation employs memory mapped file for searching the
# mail archive.
###
def get_senders(f):
  global count_seen
  pattern = re.compile("From:[ \"\'][ .\-\[\]\w\'\"]+<.+@.+>", re.IGNORECASE)
  with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
    matches = re.findall(pattern, m)
    if (matches):
      for m in matches:
        (name, emid) = split_name_and_email_id(m)
        update_identities(emid, name)
        count_seen = count_seen + 1
  #
  return count_seen


###
# writes to 'senders.csv' and 'frequencies.csv'.
#
###
def main(mail_archive_path):
  global identities, frequencies, count_seen
  #
  f = file(mail_archive_path, "r")
  get_senders(f)
  f.close()
  #
  #
  #print("seen: %d" % count_seen, file=sys.stderr)
  f = file("senders.csv", 'w', 32*1024)
  for emid in identities:
    print("%s,%s" % (emid, identities[emid]), file=f)
  f.close()
  f = file("frequencies.csv", 'w', 32*1024)
  for emid in frequencies:
    print("%s,%d" % (emid, frequencies[emid]), file=f)
  f.close()


main("dp.mbox")
