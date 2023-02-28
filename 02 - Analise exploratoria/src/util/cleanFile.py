
import time
import unicodedata
import re

f = open("02 - Analise exploratoria/src/util/idhm2010.csv", "r", encoding='UTF-8')

g =  open("02 - Analise exploratoria/src/util/idhm2010-norm.csv", "w", encoding='UTF-8')
#time at the start of program is noted
start = time.time()
  
#keeps a track of number of lines in the file
count = 0
for lines in f:
    nfkd_form = unicodedata.normalize('NFKD', lines)
    lines =  u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
    g.writelines(lines)
  
#time at the end of program execution is noted
end = time.time()
  
#total time taken to print the file
print("Execution time in seconds: ",(end - start))
print("No. of lines printed: ",count)