str1=input()
str2=input()
len1=len(str2)
c=str2[len1-1]
count=0
for i in str1:
    if c==i:
        count+=1
print(count)