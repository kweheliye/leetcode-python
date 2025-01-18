import re

names = ["Kamal", "hel"]


for s in names:
    if re.search(r'^hel$', s):
        print(f"Found in: {s}")
    else:
        print(f"Not found in: {s}")



def my_func(*args,**kwargs):
    print("Hello world", args, kwargs )

my_func("abc", "def", key=123, abc=123)

student = ['Kamal', "Hashi", 'Weheliye']

for x, num in enumerate(student):
    print("x", num)
