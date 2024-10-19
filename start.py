#strings and string manipulation 

#Basic string operation 

# 1. concatenation 
first_name = 'jack'
last_name = 'paul'
full_name = first_name + ' ' + last_name
print(full_name)

#2. Indexing 
first_name = 'jack'
char1 = first_name[0]
char2 = first_name[2]
char3 = first_name[-1]    # index -1 refers to the last element, -2 refers to the second-to-last element, and so on.

#3.String Slicing: Extracting a portion of a string using the slicing technique ([start:end])
full_name = 'Jack Paul'
slice_fullName = full_name[0:4]      # extracts 'Jack' 

#String Length: Finding the length of a string using the len() function
full_name = 'Jack Paul'
len_count = len(full_name)


#Basic string methods for manipulation 

# .lower() and .upper():
s = 'Jack Paul'
s.lower()
s.upper()

# .strip(): removes leading and trailing whitespaces from string 
s = '   Jack Paul   '
s.strip()       #'Jack Paul'

#.replace(): replaces occurrences of a substring with another substring(old,new)
s = "I like Paul"
new_s = s.replace("like", "love")
print(new_s)  # 'I love Paul'


#.split(): splits a string into a list where each word is a list item, based on a delimiter:  character or set of characters that define the boundaries between separate elements  (default is whitespace).
sentence = "Hello, how are you?"
words = sentence.split()    #['Hello,', 'how', 'are', 'you?']

         ## using delimeter(,)
         sentence = "apple,banana,cherry"
         fruits = sentence.split(",")        # ['apple', 'banana', 'cherry']



#String Formatting 

#.format() : provides a way to inject variables into a string. 
# named arguments and postional arguments too . 
name = 'Jack'
age = 29
result = "My name is {} and I am {} years old.".format(name,age)     

#Using Format Specifiers in .format()

#for controlling decimal values : 
pi = 3.14159
result = "Pi to 2 decimal places : {:.2f}".format(pi)       # 3.14 

#Padding and Alignment in .format(): left,right,center alignment width 10 
left_aligned = "{:<10}".format("left")            "left      "  
right_aligned = "{:>10}".format("right")          "     right"
center_aligned = "{:^10}".format("center")        "  center  "



x / y  # Division (float)
x // y  # Division (integer)

