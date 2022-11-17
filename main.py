def cenzor(filename, some):
    with open(filename, 'r') as file:
        data = file.readlines()
    for h in data:
        for i in some:
            while i in h.lower():
                lower_text = h.lower()
                finder = lower_text.find(i)
                counter = len(i)
                replace = "*" * counter
                find_index = data.index(h)
                h = h[:finder] + replace + h[finder + counter:]
                data[find_index] = h
    new_str = ""
    for k in data:
        new_str += k
    with open("new_text.txt", 'w') as file:
        file.write(new_str)


some_list1 = ['shit', 'ass', 'dick', 'bitch', 'sex', 'nigga', 'niggas']

cenzor('text.txt', some_list1)
