#!/usr/bin/python3
#1 # [1, 2, 3, 4]: "Test"       # Unhashable type: 'list'. But Why?: 
   # Key need to be immutable => (Number, str, typle), But list not allowed


# ============================================================================

user = {
    "Name": "Mohamed",
    "Age": 22,
    (1, 2, 3, 4): "Test",       # It's ok, look at note #1
    "Name": "Elhennawy"         # Here Name value's Will Be updatew
}


print(user)
print(user['Name']) # or: use .get()
print(user.get('Age'))

print("=" * 40)
for i in user:
    print(user[i])

# ===========================================================

languages = {
  "One": {
    "name": "Html",
    "progress": "80%"
  },
  "Two": {
    "name": "Css",
    "progress": "90%"
  },
  "Three": {
    "name": "Js",
    "progress": "90%"
  }
}

print(languages)
print(languages['One'])
print(languages['Three']['name'])

# Dictionary Length

print(len(languages))
print(len(languages["Two"]))

# Create Dictionary From Variables

frameworkOne = {
  "name": "Vuejs",
  "progress": "80%"
}

frameworkTwo = {
  "name": "ReactJs",
  "progress": "80%"
}

frameworkThree = {
  "name": "Angular",
  "progress": "80%"
}

allFramework = {
  "one": frameworkOne,
  "two": frameworkTwo,
  "three": frameworkThree
}

print(allFramework)