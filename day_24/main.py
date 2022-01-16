# Open and read a file
# with open("my_file.txt") as file:
#    content = file.read()
#    print(content)
# /Users/hp/Desktop/my_file2.txt
# Open and write in a file
with open("my_file.txt", mode="w") as file:
    for n in range(5):
        file.write(f"\nThis is a new appended text. {n}")
