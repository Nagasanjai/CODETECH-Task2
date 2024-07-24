# Grade calculator
'''
100 - 90 = O
89 - 80 = a+
79 - 70 = a
69 - 60 = b
59 - 50 = c
49 - 0 = d
'''

subject = int(input("enter the number of subject > "))
subject_list = []

i = 0
while i < subject:
    user = input("enter the subject name > ")
    subject_list.append(user)
    i+=1

grade_mark = []
for i in subject_list:
    marks = int(input(f"{i} enter the marks : "))
    grade_mark.append(marks)

empty = dict(zip(grade_mark,subject_list))
print(empty)

final_list = {}
final = []

for i in empty:
    if i>=90 and i<=100:
        pass
    elif i>=80 and i<=89:
        pass
    elif i>=70 and i<=79:
        pass
    elif i>=60 and i<=69:
        pass
    elif i>=50 and i<=59:
        pass
    elif i>=0 and i<=49:
        pass
    else:
        print("Invalid Option!")
