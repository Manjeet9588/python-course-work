'''Given the names and grades of students in a class:
Store them in a nested list.
Find the second lowest grade.
Print the names of all students who have that second lowest grade.
Print the names in alphabetical order.
Each name should be printed on a new line.'''
result = []
for _ in range(int(input())):
    name = input("Enter your name : ")
    score = float(input("Enter your score : "))
    result.append([score,name])

result = sorted(result)

score_sorted = [value[0] for value in result]
unique_score = sorted(list(set(score_sorted)))
second_highest = unique_score[1]

output = []
for score , name in result:
    if score == second_highest:
        output.append(name)

final_output = sorted(output)

for n in final_output:
    print(n)
