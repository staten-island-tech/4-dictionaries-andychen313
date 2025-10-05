""" def language(x):
    print("do something")
    
language("Cadee computer never seems to work in the morning.") """

line = input("Give me a piece of writing: ")
N = int(input("How many lines are there in the piece of writing?: "))
t_count = 0
s_count = 0

for _ in range(N):
    t_count += line.count('t') + line.count('T')
    s_count += line.count('s') + line.count('S')

if t_count > s_count:
    print("English")
else:
    print("French")

""" N = int(input("How many parking spots are there?: "))
yesterday = input("Use C to indicate an occupied spot and . to indicate a free spot from yesterday:  ")
today = input("Use C to indicate an occupied spot and . to indicate a free spot for today: ")

parked_today_and_yesterday = 0
for i in range(N):
    if yesterday[i] == 'C' and today[i] == 'C':
        parked_today_and_yesterday +=1
print(parked_today_and_yesterday) """
