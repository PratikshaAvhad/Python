#Write a function which print a dictionary where the keys are numbers between 1 and 20
#(both included) and the values are square of keys

def create_square_dict():
    d = {}
    for i in range(1, 21):
        d[i] = i * i   
    print(d)


create_square_dict()
