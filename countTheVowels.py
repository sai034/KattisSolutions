#	Count the Vowels
# https://open.kattis.com/problems/countthevowels

c=str(input())
count=0
d='a','e','i','o','u','A','E','I','O','U'
for i in c:
    if i=='a' or i=='e'or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O'or i=='U' in c:
        count=count+1
print(count)
