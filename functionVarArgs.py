#Passing numerous args with *args
def total(*nums):
    return sum(nums)

print(total(1,3,4,6,2,19))

#Passing named arguements i.e like a dictionary eg. (a=1, b=2) ==> {a:1, b:2}
def dictprep(**kwargs):
    print(kwargs)

dictprep(a=2, b=3)