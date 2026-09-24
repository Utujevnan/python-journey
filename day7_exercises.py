
#exercise one

def describe_person(name, age):

    print(f"{name} is {age} years old")

describe_person("vanessa", 15)
describe_person("chris", 20)


#exercise two

def is_even(num):
    if num % 2 ==0:
        return True
    else:
        return False

result = is_even(5)
print(result)

#exercise three

def calculate_total(*args):
    sum =0
    for i in args:
        sum+=i

    return sum

calculate_total(1,2,3,4,5)
calculate_total(5,7,30,4,9)




