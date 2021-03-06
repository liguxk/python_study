#encoding:utf-8

import urllib
import os

def reporthook(blocks_read,blocks_size,total_size):
    """total_size is reported in bytes.
    block_size is the amount read each time.
    blocks_read is the number of blocks successfully read.
    """
    if not blocks_read:
        print 'connection opened'
        return
    if total_size<0:
        print 'Read %d blocks (%d bytes)' %(blocks_read,blocks_read*blocks_size)
    else:
        amount_read=blocks_read*blocks_size
        print 'Read %d blocks, or %d/%d' %(block_read.amount_read,total_size)
    return
try:
    filename,msg=urllib.urlretrieve(
      'http://blog.doughellmann.com/',
      reporthook=reporthook)
    print
    print 'File:',filename
    print 'Headers:'
    print msg
    print 'File exists before cleanup:',os.path.exists(filename)
finally:
    urllib.urlcleanup()
    print 'File still exists:',os.path.exists(filename)
