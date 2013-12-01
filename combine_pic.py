#! -*-coding: utf-8-*-

import os
import shutil
import sys

picfile = ['jpg', 'jpeg', 'png']
dstdir = unicode(os.getcwd(), 'gb2312')

def find_pic(arg, dirname, files):
    for filename in files:
        #f = filename.decode('gb2312')
        f = unicode(filename, 'gb2312')
        print 'file name is:', f
        if 1:
            arg['file_count'] += 1
            filetype = os.path.splitext(f)[1][1:]
            print 'filetype is:', filetype
            if filetype in picfile:
                arg['pic_count'] += 1
                try:
                    #print os.path.join(dirname, filename), os.path.join(dstdir, filename)
                    shutil.copy2(os.path.join(dirname, filename), os.path.join(dstdir, filename))
                except:
                    print 'Error ', sys.exc_info()[0]
                    #pass
                #print 'pics number: %d, files number is: %d' % (pic_count, file_count)



def combine_pic():
    pwd = os.getcwd()
    print pwd
    print os.path.join(dstdir, 'test.txt')
    raw_input()
    count = {'pic_count': 0, 'file_count': 0}
    os.path.walk(os.getcwd(), find_pic, count)
    print "pics number: %d, files number is: %d" % (count['pic_count'], count['pic_count'])

if __name__ == '__main__':
    print 'start'
    combine_pic()
