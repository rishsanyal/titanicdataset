import csv as csv
import numpy as np


test_file = open('/Users/rsanyal/Documents/Titanic/train.csv','r')
tfo = csv.reader(test_file)
header = next(tfo)


with open("genderbasedmodle.csv",'w') as test2:
    pfo = csv.writer(test2)

    pfo.writerow(["PassangerID","Survived"])
    
    for row in tfo:
        if row[3] == "female":
            pfo.writerow([row[0],'1'])
        else:
            pfo.writerow([row[0],'0'])

test2.close()
test_file.close()


#print(sum(men+women))