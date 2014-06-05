#coding:utf-8
"""
Copyright (c) 2014. Kensuke Kousaka

This software is released under the MIT License

http://opensource.org/licenses/mit-license.php
"""
__author__ = 'Kensuke Kousaka'

import sys
import os


def main(argv):
    if len(argv) < 3:
        print 'Designate Arguments'
        print 'python search.py WhereToFind FileName'
        sys.exit(1)

    print '---------- SEARCHING ----------'
    for dpath,dnames,fnames in os.walk(argv[1]):
        for fname in fnames:
            if argv[2] in fname:
                print dpath, ":", fname
    print '---------- FINISHED ----------'

if __name__ == '__main__':
    main(sys.argv)