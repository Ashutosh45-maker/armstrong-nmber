num=int(input("enter an integer to check whether it is an armstrong number:"))
sum=0
for i in num:
    sum=sum+i**len(num)
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")