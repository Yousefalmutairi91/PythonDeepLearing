# Lecture-1:

#Question 1
# Initialize "Python" as a String
word = "Python"

# Delete 2 letters
del_chr = word[:-2]
# print (del_chr) = Pyt

# Reverse the string
print(del_chr[::-1])



#Question2
#Take two numbers from user:
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Add num1 to num2
result_sum = int(num1) + int(num2)
print("\nTotal of the Addition is: %d" % result_sum)

# Subtract num1 from num2
result_sub = int(num1) - int(num2)
print("\nTotal of of the Subtraction is: %d" % result_sub)

# Divide num1 by num2
result_div = int(num1) / int(num2)
print("\nTotal of the Division is: %d" % result_div)

# Multiplication num1 on num2
result_multipl = int(num1) * int(num2)
print("\nTotal of the Multiplication is: %d" % result_multipl)




#Question3
# Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’
str = input("Write this Sentance (I love playing with python): ")

# Replace ‘python’ with ‘pythons’
print(str.replace("python", "pythons"))



#lecture -2

# Take the number of the students from the user
n = input("How many students: ")

# Convert input to integer
n = int(n)

# Create two lists, one list to save inputs in Pound and another one to list calculated values in Kilogram
listpound = []
listkg =[]

# Loop to insert input from user and calculated values
i = 0
while i < n:
    # Insert function into lbs
    listpound.insert(i, float(input("Enter the student's weights in lbs: ")))
    # Insert function into Kg
    listkg.insert(i, format(listpound[i] * 0.453592, '.2f'))
    # Loop until students number equals number of lists
    i+=1

# Print users input of weights
print(listpound)
# Print the weights in kg
print(listkg)



#2
#In Python, defining the function works as follows. def is the keyword for defining a function.
#The function name is followed by parameter(s) in (). The colon : signals the start of the function body,
#which is marked by indentation. Inside the function body, the return statement determines the value to be returned.

def string_alternative(string):
    return string[::2]

# '__main__' for function call
if __name__ == '__main__':
    
    str = input("Enter your sentance: ")
    str_altr = string_alternative(str)
    
    print(str_altr)
    
    
    
#3
# Open the file
file = open("word_counts.txt", "r+")
dict_count = dict()
# This function loops inside the file
def readFile():
    for line in file:
        line = line.strip()
        words = line.split(" ")
        countWords(words)

# Looping to check if the word was added to dictionary or add it
def countWords(words):
    for word in words:
        if word in dict_count:
            dict_count[word] = dict_count[word] + 1
        else:
            dict_count[word] = 1
# Looping to print all words
def printResult():
    for result in list(dict_count.keys()):
        print(result, ":", dict_count[result])

# Run functions
readFile()
printResult()
file.close()

file = open('word_counts.txt', 'w+')

def writeinFile():
    for wr in dict_count:
        file.write(wr)
        file.write(": ")
        file.write(str(dict_count[wr]))
        file.write("\n")

# Run function to write over word_counts.txt file
writeinFile()
file.close()