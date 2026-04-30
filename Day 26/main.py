numbers = [1, 2, 3, 4, 5]
squared_numbers = [n ** 2 for n in numbers]

name = "Pranav"
letters = [n for n in name]

double_no = [n * 2 for n in range(1, 11)]
print(double_no)

names = ["Peter", "Paul", "Mary", "John", "Jane", "Jack", "Jill", "James", "Jenny", "Joe"]
short_names = [n.upper() for n in names if len(n) < 5]
print(short_names)
