import random, pandas
numbers = [1, 2, 3, 4, 5]
squared_numbers = [n ** 2 for n in numbers]

name = "Pranav"
letters = [n for n in name]

double_no = [n * 2 for n in range(1, 11)]

names = ["Peter", "Paul", "Mary", "John", "Jane", "Jack", "Jill", "James", "Jenny", "Joe"]
short_names = [n.upper() for n in names if len(n) < 5]

name_score = {n: random.randint(1, 100) for n in names}

passed_names = {n: s for n, s in name_score.items() if s >= 60}

student_dict = {
    "student" : ["Pranav", "Alice", "Bob", "Charlie", "David"],
    "score" : [85, 92, 78, 88, 95]
}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    if row.score >= 85:
        print(f"{row.student} passed with a score of {row.score}")
