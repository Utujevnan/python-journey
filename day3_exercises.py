#exercise one

fav_food =['chips','rice','eggs','chicken','salad']
print(fav_food[0])
print(fav_food[-1])
print(fav_food[1:3])
print(fav_food[::-1])

#exercise two

numbers = [4, 8, 15, 16, 23, 42]
numbers.append(100)
numbers.insert(0,1)
numbers.remove(15)
poped = numbers.pop(-1)
print(poped)
print(numbers)

#exercise three


tasks =['sports', 'work','shower','bedtime']
tasks.sort()
print(tasks)

number = len(tasks)
print('you have '+str(number)+' tasks to complete')