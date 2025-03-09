a= list(map(int,input().split()))
t=int(input())
b=[]
for i in a:
  j=i+1
  for j in a:
    if(i+j==t):

      b.append(i)
      b.append(j)
      print(b)
  break