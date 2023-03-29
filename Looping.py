#for i in range in (100):
#    print(i)

for x in range(100):
    print(x)

for i in range(100):
    if(i%2==0):
      print(i)

for i in range(100):
    if(i%2!=0):
        print(i)

import random as rand
for x in range(10):
    print(rand.randint(1,1000))


import random as rand
sum=0.00
for i in range(5):
    print("i=",i)
    randomNumber=rand.randint(1,5)
    print("Random number=", randomNumber)
    sum=sum+randomNumber
    print("sum=",sum)
print("final sum", sum)
average=sum/5
print(average)3


