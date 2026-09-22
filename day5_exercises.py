

temperature = 89

if temperature > 30:
    print("it's hot")
elif temperature >= 20 and temperature <=30:
    print("it's warm")
else:
    print("it's cold")

#exericise 2

has_umbrella = True
is_raining = False

if has_umbrella and is_raining:
    print("you'll stay dry")

elif not has_umbrella and is_raining:
    print("you'll get wet")
else:
    print("no need for umbrella")

#exercise 3

user ={
    'name': 'vanessa',
    'email': ''
}

if user.get('email'):
     print("email on file: " + user.get('email'))
else:
    print('no email provided')




