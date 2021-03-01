word=input()
word1=[]
time=0
position=0
keyboard = input()
a=[i for i in range(26)]
keyboard1=[]
for i in keyboard:
    if i != ' ':            # ignoring space char
        keyboard1.append(ord(i))
for i in word:
    if i!=' ':
        word1.append(ord(i))
for i in range(len(word1)):
    time+=abs(a[word1[i]-97]-position)
    position=a[word1[i]-97]
print(time)
