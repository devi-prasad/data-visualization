from __future__ import print_function
import re
import io
import contextlib
import mmap

keywords = ['from', 'to', 'date', 'content-type', 'subject', 'cc', 'bcc']
multiline_keywords = ['to', 'cc', 'bcc', 'subject']
punctuations = [' ', '\t', '\n', ',', ';', '<', '>', '/', '\"', '\'', '&', '#', '=']
fence = '++##++\n'

###
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
    l = r = -1
    mid = s.find('@', cur) # abcd@wxyz
    if (mid >= 0):
      l = r = mid
      slen = len(s)
      while (l >= 0 and s[l] not in punctuations):
        l = l - 1
      while (r < slen and s[r] not in punctuations):
        r = r + 1
      eid = (s[l+1: r].split())[0]
  ##
    assert (eid != None or l == -1 or r == -1 or s.find('@', cur) == -1)
  ##
  return (r, eid)

###
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

###
## 'run' looks like this: 'Fri, 8 Nov 2013 22:00:14 +0530'
def parse_line_content(row, kw, run):
  #
  if kw == 'from':
    eids = grep_email_ids(run)
    if (len(eids) == 1):
      row['from'] = eids[0]
    else: row['from'] = ' '
  if kw == 'to':
    to = grep_email_ids(run)
    if (len(to) >= 1):
      row['to'] = to
    else: row['to'] = ' '
  if kw == 'cc':
    cc = grep_email_ids(run)
    if (len(cc) == 0):
      row['cc'] = cc
    else: row['cc'] = ' '
  if kw == 'bcc':
    bcc = grep_email_ids(run)
    if (len(bcc) == 0):
      row['bcc'] = bcc
    else: row['bcc'] = ' '
  if kw == 'date':
  	daydate = run.split()
  	row['day'] = daydate[0][0:3]
  	row['date'] = daydate[1:4]
  if kw == 'content-type':
    row['content-type'] = run.split()[0][:-1]
  if kw == 'subject':
    row['subject'] = run.strip('\'\" ')
  ##
  return row

###
def table_write(row):
  if 'from' in row:
    print(row)

###
def make_table(f):
  pattern = re.compile("^(?P<keyword>[-\w]*):(?P<run>.*$)",
                       re.IGNORECASE | re.DOTALL)
  row = {}
  nextline = None
  ##
  while True:
    if nextline is None:
      l = f.readline()
    else:
      l = nextline
      nextline = None
    ##
    if l == '' or l is None:
      table_write(row);
      break
    if (l == fence):
      table_write(row);
      row = {}
    else:
      m = pattern.match(l)
      if m is not None:
        kw = m.group('keyword').lower()
        run = m.group('run').lower()
        if kw in keywords:
          if kw in multiline_keywords:
            for nl in f:
              m = pattern.match(nl)
              if m is None:
                nlp = nl.find('=')
                if (nlp > -1): nl = nl[nlp:]
                run = run + nl.lower()
                #print(run)
              else:   ## we consumed an additional line; make a note!
                nextline = nl
                break
          ##
          ## we got hold of the run text - even the multi-line ones.
          row = parse_line_content(row, kw, run)

###
def main(mail_headers_path):
  f = io.open(mail_headers_path, 'rt', encoding='utf-8')
  make_table(f)
  f.close()

###
main('gmheaders.txt')
