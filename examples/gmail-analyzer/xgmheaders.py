from __future__ import print_function
import sys
import re
import contextlib
import mmap

####
## The idea is simple. Look for a sequence of lines that begin with 'Received:'
##   and bracketed by 'Content-Type:'
## The RE matches across multiple lines.
## In the output, each group of email headers is separated by 80 '+' chars.
####
def extract_headers(f):
  global count_seen
  pattern = re.compile("^Received: .*?^Content-Type: .*?$", re.DOTALL | re.MULTILINE)
  with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
    matches = re.findall(pattern, m)
    if (matches):
      print('+' * 80)
      for m in matches:
        print(m)
        print('+' * 80)
    #
    #print(len(matches), file=sys.stderr)


def main(mail_archive_path):
  f = file(mail_archive_path, 'r')
  extract_headers(f)
  f.close()


main('dp.mbox')
