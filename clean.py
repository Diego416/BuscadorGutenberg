infile = open('outtemp', 'r')

for line in infile:
      print ''.join([i for i in line if (not i=='"' and not i=='\t' and not i=='[' and not i==']' and not i==' ')])[:-1]
      
infile.close()
