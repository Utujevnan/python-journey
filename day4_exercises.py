

#exercise one
student ={
    'name':'utuje',
    'age':18,
    'course':'python',
    'is_enrolled':True

}

print(student['name'])
print(student['course'])

student['age'] = 21
print(student)
student['graduation_year'] = 2025
print(student)

#exercise two

print(student.get('phone_number', 'not provided'))
del student['is_enrolled']
print(student)
#exercise three
print(student.keys())
print(student.values())
print('utuje' in student.values())
print(len(student))


