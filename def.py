try:
    x = open("msg.txt", "r")
    x_file = x.read()
except FileNotFoundError:
    print("File not found")
else:
    def count_words(w):
        xf = x_file.lower()
        search = xf.count(w)
        return search
print(count_words("ey"))
