# Exercise 8:
#
# Write a program with a loop that repeatedly
# asks the user to enter a word. The user should
# enter nothing (press Enter without typing
# anything) to signal the end of the loop.
# Once the loop ends, the program should
# display the average length of the words
# entered, rounded to the nearest whole number.
word = ""
total_word = 0
avg_word = 0

while word != "":
    word = input("input your fav")
    words = word_string.split()
    word_count = len(words)
    total_word += word_count
print(word_count)
