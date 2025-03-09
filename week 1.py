a= list(map(int,input("Enter the array separate by space:").split()))
t=int(input("targeted sum :" ))
b=[]
count=0
for i in a:
  j=i+1
  for j in a:
    if(i+j==t):
      count = count +1

      b.append(a.index(i))
      b.append(a.index(j))
      print(b)
  break
if count ==0:
  print("Not found")
 
