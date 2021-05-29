r1=[3,1,2,3,6,2,3,6,2,3,6,3,2,3,6,2,3,4,3,2,5,4,2,1,2,1,2,3,1,2,6,2,3,6,2,3,6,3,2,3,1,5,3,2,1,2,4,2,1,8,1,2]
#r1=[10,7,12,2,4,7,2,4,1,2,6,6,3,2,1,4,7,2,7,3,1,3,11,4,2,1,5,2,3,3,6,1,3,9,5,2,1,2,11,9,2,3,8,2,5,1,2,7,2,4,11,2,12]
b=sum(r1)

m=[]
n=0
l=[]
for i in range(len(r1)+1):
  a =[]
  for j in range(b*2):
    a.append(" ")  
  m.append(a)
l3=[]

for k in range(len(r1)):
  if (k==0 or k%2==0):
    l3.append("/"*r1[k])
  else:
    l3.append("\\"*r1[k])

a=0
b=0
l=[]
l2=[0]
r=[]
for j in l3:
  for k in j:
    r.append(k)

for i in range(len(r)):
  if i+1<len(r)+1:
    if r[i-1]=="/"and r[i]=="/":
      a+=1
      l.append(a)
      b+=1
      l2.append(b)
    if r[i-1]=="/"and r[i]=="\\":
      l.append(a)
      b+=1
      l2.append(b)
    if r[i-1]=="\\"and r[i]=="/":
      l.append(a)
      b+=1
      l2.append(b)
    if r[i-1]=="//"and r[i]=="\\":
      a+=1
      l.append(a)
      b+=1
      l2.append(b)
    if r[i-1]=="\\"and r[i]=="\\":
      a-=1
      l.append(a)
      b+=1
      l2.append(b)
t=0
n=max(l)
for y in range(len(l)):
    m[l[y]][l2[y]]=r[y]
    if l[y]==n:
      x,z=l[y],l2[y]



'''  
m[1][0]="/"
m[2][1]="/"
m[3][2]="/"
m[3][3]="\\"
m[3][4]="/"
m[4][5]="/"
m[4][6]="\\"
m[3][7]="\\"
m[2][8]="\\"
m[2][9]="/"
m[3][10]="/"
m[4][11]="/"
m[5][12]="/"
m[6][13]="/"
m[7][14]="/"
m[7][15]="\\" 
m[6][16]="\\"
m[5][17]=="\\"
'''
m[x+1][z-1]="< >"
m[x+2][z-1]="/|\\"
m[x+3][z-1]=" O"

for f in range(len(r1)//2-1,0,-1):
    t=len(r1)*2
    for e in range(t+len(r1)):
        print(m[f][e],end="")
    print()
