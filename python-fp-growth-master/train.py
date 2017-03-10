from fp_growth import find_frequent_itemsets
import csv

with open('examples/april2008.csv','r') as f:
       reader=csv.reader(f)
       w=[]
       count=0;
       for row in reader:
               w.append(row[1:])
               count+=1
               if count==1000:
                      break

finalResult=[]
for i in w:
       col=1
       itemCount=[]
       for eachItem in i:
              #print(type(eachItem))
              if eachItem!=str(0):
                     itemCount.append(col)
              col+=1
       finalResult.append(itemCount)
              

#print (finalResult)
minimum_support=10
#print(w)
#for i in w:
  # print(i)
   

result = []
for itemset, support in find_frequent_itemsets(finalResult, minimum_support, True):
      result.append((itemset,support))

result = sorted(result, key=lambda i: i[0])
for itemset, support in result:
    print (str(itemset) +' '  + str(support))
                

