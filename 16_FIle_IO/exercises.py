
file = open("file.txt")
contents = file.read()
print(contents)
file.close()  # once file is opened we need to close it to save resources

with open("file.txt") as file:  # no longer need to close the file manually
    contents = file.read()
    print(contents)

with open("file.txt", mode='a') as file:  # 'w' for write, 'a' for append
    file.write("\nText added.")

with open('data.txt') as data:
    high_score = int(data.read())

with open('data.txt', mode='w') as data:
    data.write(f'{high_score}')

