from __future__ import print_function
import re
import io
import contextlib
import mmap

keywords = ['from', 'to', 'date', 'content-type', 'subject', 'cc', 'bcc']
fence = '+'*80 + '\n'

def new_row():
  return {'from': '', 'to': '', 'date': '', 'day': '', 'cc': '', 'bcc': '', 'subject': ''}

def grep_one_email_id(s, cur=0):
  assert(s is not None and cur >= 0)
  ##
  l = s.find('<', cur)
  r = 0
  eid = None
  if (l >= cur):
    r = s.find('>', l)
    if (r > l and s.find('@', l, r) > -1):
      eid = (s[l+1:r].split())[0]
  ##
  if eid is None: # may be the email id is not surrounded by angle braces < ... >
    mid = s.find('@', cur) # abcd@wxyz
    if (mid >= 0):
      l = r = mid
      slen = len(s)
      while (l >= 0 and s[l] not in [' ', '\t', '\n', ',', ';', '<', '\"', '\'']):
        l = l - 1
      while (r < slen and s[r] not in [' ', '\t', '\n', ',', ';', '>', '\"', '\'']):
        r = r + 1
      eid = (s[l+1: r].split())[0]
  ##
    assert (eid != None or l == -1 or r == -1 or s.find('@', cur) == -1)
  ##
  return (r, eid)


def grep_email_ids(s):
  i = 0
  eid = None
  eids = []
  i, eid = grep_one_email_id(s, i)
  ##
  while (i > 0):
  	eids.append(eid)
  	i, eid = grep_one_email_id(s, i)
  ##
  return eids

##
## 'run' looks like this: 'Fri, 8 Nov 2013 22:00:14 +0530'
def parse_line_content(row, kw, run):
  #
  if kw == 'from':
    eids = grep_email_ids(run)
    if (len(eids) == 0): eids = ['']
    print('from: ', eids[0])
  if kw == 'to':
    to = grep_email_ids(run)
    print('to:', to)
  if kw == 'cc':
    cc = grep_email_ids(run)
    print('cc:', cc)
  if kw == 'bcc':
    bcc = grep_email_ids(run)
    print('bcc:', bcc)
  if kw == 'date':
  	daydate = run.split()
  	row['day'] = daydate[0][0:3]
  	row['date'] = daydate[1:4]
  	print('day and date: ', row['day'], row['date'])
  if kw == 'content-type':
    row['content-type'] = run.split()[0][:-1]
    print('content-type: ', row['content-type'])
  if kw == 'subject':
    row['subject'] = run.strip('\'\" ')
    print('subject: ', row['subject'])
  ##
  return row


def make_table(f):
  pattern = re.compile("^(?P<keyword>[-\w]*):(?P<run>.*$)", 
                       re.IGNORECASE | re.DOTALL | re.MULTILINE)
  row = None
  ##
  with f:
    for l in f:
      if (l == fence):
        row = new_row()
      else:
        m = pattern.match(l)
        if m is not None:
          kw = m.group('keyword').lower()
          if kw in keywords:
            row = parse_line_content(row, kw, m.group('run').lower())
            #print((kw, m.group('run').lower()))
            #print(row)

def make_table_rough_bad(f):
  pattern = re.compile(b"^(?P<keyword>[-\w]*):(?P<run>.*$)",
                       re.IGNORECASE | re.DOTALL | re.MULTILINE)
  row = None
  ##
  with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as mf:
    #while True:
      m = pattern.findall(mf)
      print(m[0][0])
      #if m is not None:
      #  kw = m.group('keyword').lower()
      #  print(kw, m.group('run').lower())
      #  if kw in keywords:
          #row = parse_line_content(row, kw, m.group('run').lower())
      #    print((kw, m.group('run').lower()))
          #print(row)


def main(mail_headers_path):
  f = io.open(mail_headers_path, 'rt', encoding='utf-8')
  make_table(f)
  f.close()

#main('gms.py')
main('gmheaders.txt')
