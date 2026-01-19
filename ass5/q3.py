import csv

#  1. Read a file and display its contents 
print("\n1. Read file and display contents")
with open("data.txt", "r") as file:
    print(file.read())

#2. Count number of lines in a file
print("\n2. Count number of lines")
with open("data.txt", "r") as file:
    lines = file.readlines()
    print("Total lines:", len(lines))


# 3. Count how many times each word appears 
print("\n3. Word count in file")
with open("data.txt", "r") as file:
    text = file.read().lower()

words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)


# 4. Write 5 user-entered sentences to a file 
print("\n4. Write 5 sentences to file")
with open("sentences.txt", "w") as file:
    for i in range(5):
        sentence = input("Enter sentence: ")
        file.write(sentence + "\n")

print("Sentences saved successfully.")


#  5. Append a list of strings to an existing file 
print("\n5. Append list to file")
data = ["Apple\n", "Banana\n", "Mango\n"]

with open("data.txt", "a") as file:
    file.writelines(data)

print("Data appended successfully.")


#  6. Print only lines containing a specific word 
print("\n6. Search word in file")
search_word = input("Enter word to search: ")

with open("data.txt", "r") as file:
    for line in file:
        if search_word in line:
            print(line.strip())


#  7. Replace a word in file 
print("\n7. Replace word in file")
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open("data.txt", "r") as file:
    content = file.read()

content = content.replace(old_word, new_word)

with open("data.txt", "w") as file:
    file.write(content)

print("Word replaced successfully.")


#  8. Merge two text files 
print("\n8. Merge two files")

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as f3:
    f3.write(f1.read())
    f3.write("\n")
    f3.write(f2.read())

print("Files merged into merged.txt")


#  9. Read CSV file and display content 
print("\n9. Read CSV file")

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


#  10. Backup a file 
print("\n10. Backup file")

with open("data.txt", "r") as source, open("backup.txt", "w") as backup:
    backup.write(source.read())

print("Backup created as backup.txt")
