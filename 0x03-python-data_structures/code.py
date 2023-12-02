courses = ['History', 'Math', 'Physics', 'compSci']

# Instead to doing that
for index in range(len(courses)):
    print(index, courses[index])

# You just can do that
print("=" * 10)
for index, course in enumerate(courses, 1): # or: start=1
    print(index, course)

print("=" * 10)
# Note that this Way convert list to string
print("Convert to string: ")
course_str = ", ".join(courses)
print(course_str)

# But u can return it to list again Using:
print("\nReturn To List again: ")
new_list = course_str.split(', ')
print(new_list)