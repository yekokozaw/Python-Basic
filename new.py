num_str = input("Enter number :")

##စစ် ပေးတာ ကောင်းတယ်
## check and recover

# while not num_str.isdigit():
#     num_str = input("Please number :")
# num = int(num_str)
# print("number is ",num)

import dis
a = 10
b = 20
c = 30
def func():
    d = a + b * c
    return d
print (dis.dis(func))   #byte code 