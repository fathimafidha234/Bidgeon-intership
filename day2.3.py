list=[]
for i in range(5):
    num =int(input("enter a number:"))
    list.append(num)
largest=max(list)
smallest=min(list)
total=sum(list)
even_count=0
odd_count=0
for num in list:
    if num % 2 == 0:
        even_count+=1
    else:
        odd_count+=1
print("list:",list)        
print("largest number:",largest)
print("smallest number:",smallest)
print("sum of number:",total)
print("even count:",even_count)
print("odd count:",odd_count)
