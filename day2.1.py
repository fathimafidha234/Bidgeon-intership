word=input("Enter a word:")
vowels="aeiou"
count=0
for chr in word:
    if chr in vowels:
        count+=1
print(count)
