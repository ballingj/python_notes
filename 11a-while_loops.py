# while loop - stop when user answer hi
#
answer = input("Please say hi to me ")
#
while answer != "hi":
    answer = input("Rude...Please say hi to me... ")
print("Thank you, Hi to you too.")
#
# while loop
# 
num = 10
while num > 0:
    print(f"NUMBER is: {num}")
    num -= 1
#
count = 1
while count < 8:
    print("*"*count)
    count+=1
while count > 0:
    print("*"*count)
    count-=1

#  while True and breaking
while True:
    count1 = 0
    while count1 != 10: 
        print(count1)
        count1 += 1
    break
