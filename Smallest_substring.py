# Finding smallest substring with maximum number of distinct characters

s = input()
leng=len(set(s))
# print(leng)
j=0
k=len(s)
def incj(j):
    return j+1
def deck(k):
    return k-1
def inck(k):
    return k+1
def decj(j):
    return j-1
while(1):
    j=incj(j)
    sub1=s[j:k]
    if(len(set(sub1))<leng):
        j=deck(j)
        sub1=s[j:k]
        break
    if(j==len(s)-1):
        break
A = len(sub1)
# print(A)
j=0
while(1):
    k=deck(k)
    sub1=s[j:k]
    if(len(set(sub1))<leng):
        k=inck(k)
        sub1=s[j:k]
        break
    if(k==0):
        break
B = len(sub1)
# print(B)
print(min(A,B))
    