#Remove Index
numbers=[1,2,3,4,]
for x in numbers:
    if x%2==0: #means no remaining
        numbers.remove(x)
print(numbers)


#Select Index
text="python"
print(text[1:4]+text[-1]) #means 1 to 3 and plus last


#Boolean Trick
a=True
b=False
c=True
if a or b and c: #means and execute priority
    print("pass")
else:
    print("fail")


#Scope & Global
count=5 #Global variable
def update_count():
    global count #for change in global variable
    count=10 #Local variable_no affect to Global variable
    return count
update_count()
print(count)