""" def language(x):
    print("do something")
    
language("Cadee computer never seems to work in the morning.") """

""" def english_or_french():

    N = int(input("How many lines are there in the piece of writing?: "))
    line = input("Give me a piece of writing: ")
    t_count = 0
    s_count = 0

    for _ in range(N):
        t_count += line.count('t') + line.count('T')
        s_count += line.count('s') + line.count('S')

    if t_count > s_count:
        print("English")
    else:
        print("French")
english_or_french()
 """
""" def parked_spots_today_and_yesterday():

    N = int(input("How many parking spots are there?: "))
    yesterday = input("Use C to indicate an occupied spot and . to indicate a free spot from yesterday:  ")
    today = input("Use C to indicate an occupied spot and . to indicate a free spot for today: ")

    parked_today_and_yesterday = 0
    for i in range(N):
        if yesterday[i] == 'C' and today[i] == 'C':
            parked_today_and_yesterday +=1
    print(parked_today_and_yesterday)
parked_spots_today_and_yesterday() """

""" def english_or_french():
    N = int(input("How many lines are there?: "))
    line = input("Give me the line(s): ")
    t_count = 0
    s_count = 0
    
    for _ in range(N):
        t_count += line.count('t') + line.count('T')
        s_count += line.count('s') + line.count('S')
    
    if t_count > s_count:
        print("English")
    else:
        print("French")
english_or_french() """

""" def parked_today_and_yesterday():
    N = int(input("How many parking spots are there?: "))
    yesterday = input("Use C to indicate an occupied spot and a . to indicate a free spot: ")
    today = input("Use C to indicate an occupied spot and a . to indicate a free spot: ")
    parked_today_and_yesterday = 0

    for i in range(N):
        if yesterday[i] == 'C' and today[i] == 'C':
            parked_today_and_yesterday += 1
    print(parked_today_and_yesterday)
parked_today_and_yesterday() """

""" def lang(x):
    t = 0
    s = 0
    for char in x:
        if char == "t" or char == "T":
            t+=1
        elif char == "s" or char == "S":
            s+=1
    if t>s:
        print("Eng")
    else:
        print("French") """

""" def spaces(y, t):

spaces("CCC..", ".C.C.C") """

""" def lang():
    t_count = 0
    s_count = 0
    x = input("Give me the line(s): ")
    for char in x:
        if char == "t" or char == "T":
            t+=1
        elif char == "s" or char == "S":
            s+=1

    if t>s:
        print("English")
    else:
        print("French")
lang() """

""" def english_or_french():
    
    x = input("Give me the line(s): ")
    t_count = 0
    s_count = 0
    
    for _ in range():
        t_count += x.count('t') + x.count('T')
        s_count += x.count('s') + x.count('S')
    
    if t_count > s_count:
        print("English")
    else:
        print("French")
english_or_french()  """

""" def lang():
    line_or_lines = input("Give me the line(s): ")
    t = 0
    s = 0
    for char in line_or_lines:
        if char == "t" or char == "T":
            t+=1
        elif char == "s" or char == "S":
            s+=1

    if t>s:
        print("English")
    else:
        print("French")
lang() """

""" def parking_spaces():
    yesterday = input("Use C to indicate an occupied space and use . to indicate a free space from yesterday: ")
    today = input("Use C to indicate an occupied space and . to indicate a free space for today: ")
    parked_spaces = 0

    for i in range(len(yesterday)):
        if yesterday[i] == 'C' and today[i] == 'C':
            parked_spaces +=1
    print(f"There are {parked_spaces} spaces that were parked today and yesterday.")
parking_spaces() """

""" def lang():
    line_or_lines = input("Give me the line(s): ")
    t_count = 0
    s_count = 0
    for char in line_or_lines:
        if char == 't' or char == 'T':
            t_count +=1
        elif char == 's' or char == 'S':
            s_count +=1
    
    if t_count > s_count:
        print("English")
    else:
        print("French")
lang() """

""" def parking_spaces():
    yesterday = input("Use C to indicate an occupied space and . to indicate a free space from yesterday: ")
    today = input("Use C to indicate an occupied space and . to indicate a free space for today: ")
    parked_spaces = 0

    for i in range(len(yesterday)):
        if yesterday[i] == 'C' and today[i] == 'C':
            parked_spaces +=1
    print(parked_spaces)
parking_spaces() """

""" def lang():
    line_or_lines = input("Give me the line(s): ")
    t_count = 0
    s_count = 0

    for char in line_or_lines:
        if char == 't' or char == 'T':
            t_count+=1
        elif char == 's' or char == 'S':
            s_count+=1
    
    if t_count > s_count:
        print("English")
    else:
        print("French")
lang() """

""" def parking_spaces():
    yesterday = input("Use C to indicate an occupied space and . to indicate a free space from yesterday: ")
    today = input("Use C to indicate an occupied space and . to indicate a free space for today: ")
    parked_spaces = 0

    for i in range(len(yesterday)):
        if yesterday[i] == 'C' and today[i] == 'C':
            parked_spaces +=1
    print(f"There are {parked_spaces} spaces occupied from yesterday and today.")
parking_spaces()

#Conditional statements and looping through characters. """

""" def lang():
    line_or_lines = input("Give me the line(s): ")
    t_count = 0
    s_count = 0

    for char in line_or_lines:
        if char == 'T' or char == 't':
            t_count +=1
        elif char == 'S' or char == 's':
            s_count +=1
    
    if t_count > s_count:
        print("English")
    else:
        print("French")
lang() """

""" def occupied(n,y,t):
    both = 0
    for i in range(n):
        if (y[i] == "C" and t[i] == "C"):
            both +=1
    return both
print(occupied(5, "CCC..", "C.C.C")) """

""" def occupied():
    n = int(input("How many parking spaces are there?: "))
    yesterday = input("Use C to indicate an occupied space and . to indicate a free space from yesterday: ")
    today = input("Use C to indicate an occupied space and . to indicate a free space: ")
    both = 0

    for i in range(n):
        if yesterday[i] == 'C' and today[i] == 'C':
            both +=1
    print(both)
occupied() """

""" def honi_count():
    word = input("Give me the word: ")
    need_word = "HONI"
    x = 0
    y = 0

    for char in word:
        if char == need_word[x]:
            x+=1
            if x == 4:
                y+=1
                x = 0
    print(y)
honi_count() """

""" def add(x,y):
    return x+y
result = add(5,8)
print(result) """

""" def integer_check():
    x = int(input("Give me a number: "))
    if x > 0:
        return "Positive number"
    return "Negative number"
print(integer_check())
integer_check() """

""" def MC(n, s a):
    correct = 0
    for i in range(n):
        if s[i] == a[i]:
            correct+=1 """

""" def password(x):
    upper = 0
    lower = 0
    digits = 0
    if len(x) > 6 and len(x) < 13:
        for char in x:
            if char.isdigit():
                lower +=1
        if upper >3 and lower >2 and digits>1 """

""" student = {
    'name': 'Cadee',
    'age': 15,
    'grades': (80, 90, 100)
}
print(student['name']) """

""" def wizard(o, n, duels):
    owner = o
    number_of_owners = 1
    for i in duels:
        #"BA"
        if duels[1] == owner:
            owner = duels[0]
            number_of_owners +=1
        for i in range(n):
            duels[i][1] == owner """

""" student = {'name': "Steve", "school": "computing"}

lists and arrays """

N = int(input("How many duels are there?: "))
def wizard():
    wand = input("Which wizard first held the wand? Enter an uppercase letter: ")
    duel = input("Enter all duels between 2 uppercase letters separated by a space")
    duel = []
    duel_count = 0

    for char in duel