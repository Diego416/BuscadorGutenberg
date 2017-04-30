infile = open('out.txt', 'r')

for line in infile:
      print ''.join([i for i in line if (not i=='"' and not i=='\t')])[:-1]
      
infile.close()
