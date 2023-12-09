#!/usr/bin/python3

# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault():     method returns the value of the item with the specified key.
#                   If the key does not exist, insert the key, with the specified value, see example below

print("setdefault():")
user = {
  "name": "Osama"
}
print(user)
print(user.setdefault("age", 36))
print(user)

print("=" * 40)
print("Popitem():")
# popitem():    remove the last item that was last inserted, and return it

member = {
  "name": "Osama",
  "skill": "PS4"
}
print(member)
member.update({"age": 36})
print(member.popitem())     # this  print the last
item = list(member.popitem())
print(f"item = {item}")
print(type(item))

print("=" * 40)

# items() :      method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

print("items()")
view = {
  "name": "Osama",
  "skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 36    # Note: The view object will reflect any changes done to the dictionary, see example below.

print(allItems)

print("=" * 40)


# fromkeys()

print("fromkeys()")
a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"

print(dict.fromkeys(a, b))