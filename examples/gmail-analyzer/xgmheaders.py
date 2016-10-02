from __future__ import print_function
import re
import contextlib
import mmap
import io

####
## The idea is simple. Look for a sequence of lines that begin with 'Received:'
##   and bracketed by 'Content-Type:'
## The RE matches across multiple lines.
## In the output, each group of email headers is separated by 80 '+' chars.
####
def extract_headers(f):
  pattern = re.compile(b"^Received: .*?^Content-Type: .*?$", 
                       re.DOTALL | re.IGNORECASE | re.MULTILINE)
  with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
    matches = pattern.findall(m)
    if (matches):
      print('++##++')
      for m in matches:
        print(m.decode(errors='ignore'))
        print('++##++')


def main(mail_archive_path):
  f = io.open(mail_archive_path, 'r', encoding='utf-8')
  extract_headers(f)
  f.close()


main('dp.mbox')
