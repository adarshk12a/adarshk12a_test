##Lists
print("hello")
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

new_list=list()
for i in range(len(first_list)):
    element= first_list[i],second_list[i]
    new_list.append(element)
print(new_list)

##  Get all values from the dictionary and add them to a list but don’t add duplicates
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

speed_list=list()

for i in speed.values():
    if i not in speed_list:
        speed_list.append(i)
print(speed_list)
##Exercise 5: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

zip(list1,list2)
for x,y in zip(list1,list2):
    print(x,y)