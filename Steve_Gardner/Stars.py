x = [4,6,1,3,5,7,25]
def draw_starsI(num_list):
    for num in num_list:
        output = ''
        for i in range(num):
            output += '*'
        print output

draw_starsI(x)

y = [4,'Tom',1,'Michael',5,7,'Jimmy Smith']
def draw_stars2(my_list):
    for item in my_list:
        output = ''
        if type(item) is int:
            for i in range(item):
                output += '*'
        elif type(item) is str:
            first_letter = item[0].lower()
            for i in range(len(item)):
                output += first_letter
        print output

draw_stars2(y)
