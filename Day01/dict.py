students = {
    "Tom":90,
    "Alice":95,
    "Bob":88
}
print(students)

#新增
students["Jack"] = 100
print(students)

#删除
del students["Bob"]
print(students)

#遍历
for names, scores in students.items():
    print(names, scores)

#按k排序
for name in sorted(students):
    print(name, students[name])

#按value排序
sorted_students = sorted(
    students.items(),
    key = lambda item: item[1],
    reverse = True
)
print(sorted_students)
print(type(sorted_students))

