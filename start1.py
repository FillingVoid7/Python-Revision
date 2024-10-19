### Modifying elements in a list : by accessing them using their index.
fruits = ['apple','orange','banana','tomato']
fruits[1] = 'gava'

### Adding elements to a list 

#append(): Adds an item at the end of the list.
fruits = ['apple','orange','banana','tomato']
fruits.append('mango')

#insert(): Adds an item at a specific position (index,value)
fruits = ['apple','orange','banana','tomato']
fruits.insert(1,'mango')


### Removing Elements from a List

#'del' : deletes an item by its [index]
fruits = ['apple','orange','banana','tomato']
del fruits[1]

#pop(): Removes and returns the last item, or a specified index.
fruits = ['apple','orange','banana','tomato']
last_fruit = pop()
first_fruit = pop(0)
return last_fruit
return first_fruit

#remove(): Removes an item by value.
fruits = ['apple','orange','banana','tomato']
fruits.remove('apple')


### Organizing a list 

# sort() :  modifies the list permanently in ascending or descending order.
numbers = [3,1,1,12,2]
numbers.sort()   #ascending order
numbers.sort(reverse = True)  #descending order

# sorted() : returns a new sorted list without altering the original list.
numbers = [3,1,1,12,2]
sorted_numbers = sorted(numbers)

# reverse() : printing list in reverse order
numbers = [3,1,1,12,2]
number.reverse()

### range() : with list() to generate a list of numbers 
#range(start, stop) function includes the start value but excludes the stop value. 
numbers = list(range(1,11))
print(numbers)     #[1,2,3,4,5,6,7,8,9,10]


## copying a list 
numbers = [3,1,1,12,2]
copied_num = numbers[:]
print(numbers)

