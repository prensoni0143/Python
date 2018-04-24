print("How many numbers do you want to print?")
a=int(input())

fab1=0
fab2=1
for b in range(0,a):
    print(fab1)
    sum=fab1+fab2
    fab2=fab1
    fab1=sum

print("Thanks for your using my program")
