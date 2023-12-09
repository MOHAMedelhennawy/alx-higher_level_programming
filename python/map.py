#!/usr/bin/python3
# def FormatText(text):
#     return f"- {text.strip().capitalize()} -"

# my_list = ["OSaMa", "   AhMED", "moHamED", "ELHENawy "]

# MyFormaterData = list(map(FormatText, my_list))
# print(MyFormaterData)

# MyFormaterData = map(FormatText, my_list)
# print(MyFormaterData)
# for Name in MyFormaterData:
#     print(Name)


# ==================================================
print("=" * 30)
my_list = ["OSaMa", "   AhMED", "moHamED", "ELHENawy "]
x = []
x = map(lambda a: f"- {a.strip().capitalize()}- ", my_list)
for name in x:
    print(name)

print("=" * 30)
x = list(map(lambda a: f"- {a.strip().capitalize()}- ", my_list))
print(x)

# ====================================================================
print("=" * 30)

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

# ====================================================================
print("=" * 30)

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))