#!/usr/bin/python

f = open('workfile', 'rw')

for line in f:
    print line

f.write('This is a test.\nThis is the second line.\nThe third line.')

f.close()


f = open('workfile')
print f

for line in f:
    print line
    
print 'File name is ', f.name
print 'File closed or not ', f.closed
print 'File open mode ', f.mode
print 'File softspace flag ', f.softspace

f.close()
