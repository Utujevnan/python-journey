#exercise one

numbers = [1,56,90,24,19]

for number in numbers:

    if number % 2 == 0:
        print(number, "even")
    else:
        print(number, "odd")

#exercise two

student ={
    'name':'utuje',
    'age':18,
    'course':'python',
    'is_enrolled':True

}

for key,value in student.items():
    print(key, value)

#exercise three

counter =0

while counter<5:
    print("still going")
    counter +=1
print("done")

for i in range(10):
    if i == 7:
        break
    if i%2==0:
        continue
    else:
        print(i)



