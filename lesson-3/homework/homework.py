Homework: List and Tuple Exercises

## 1. Create and Access List Elements
Create a list containing five different fruits and print the third fruit.  

mevalar=["ananas", "banan", "shaftoli", "uzum", "qulpunay"] 

print(mevalar[2]) 

## 2. Concatenate Two Lists
Create two lists of numbers and concatenate them into a single list. 

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

lists=list1+list2

print(lists)

## 3. Extract Elements from a List
Given a list of numbers, extract the first, middle, and last elements and 
store them in a new list. 

numbers=[10,15,20,25,30]  

first=numbers[0]
middle=numbers[len(numbers)//2] 
last=numbers[-1]

new_number=[first,middle,last] 

print(new_number)

## 4. Convert List to Tuple
Create a list of your five favorite movies and convert it into a tuple.  

favorite_movies=["Twilight","Dracula","Fifty shades of Grey","Istanbullik kelin","Qora deniz"]
movies_tuple= tuple(favorite_movies) 

print(movies_tuple)

## 5. Check Element in a List
Given a list of cities, check if "Paris" is in the list and print the result. 

cities=["Bali","Turkiya","Moskova","New York","Yaponiya","Parij","Dubay","Afrika","Misr"] 

result= "Parij" in cities 

print(result)

## 6. Duplicate a List Without Using Loops
Create a list of numbers and duplicate it without using loops.  

numbers=[1,2,3,4,5,6]

duplicate= numbers *2 

print(duplicate)

## 7. Swap First and Last Elements of a List
Given a list of numbers, swap the first and last elements.

numbers = [10, 20, 30, 40, 50]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

## 8. Slice a Tuple
Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7. 

numbers_tuple=(1,2,3,4,5,6,7,8,9,10) 
slice_tuple=numbers_tuple[3:8]
print(slice_tuple)


## 9. Count Occurrences in a List
Create a list of colors and count how many times "blue" appears in the list.  

colors=["Red","Blue","Green","Yellow","Blue","Blue","Black","Blue"]
colors_count=colors.count("Blue")
print(colors_count)

## 10. Find the Index of an Element in a Tuple
Given a tuple of animals, find the index of "lion". 

animals=("cat","dog","hoerse","lion","jerafa","fil")
animals_tuple=animals.index("lion") 
print(animals_tuple)

## 11. Merge Two Tuples
Create two tuples of numbers and merge them into a single tuple. 

tuple1=(1,2,3,4,5)
tuple2=(6,7,8,9,10)

merge_tuple=tuple1+tuple2
print(merge_tuple)

## 12. Find the Length of a List and Tuple
Given a list and a tuple, find and print their lengths. 

my_list=[1,2,3,4,5,]
my_tuple=(10,20,30,40,50,60)

list_len=len(my_list)
tuple_len=len(my_tuple)

print(list_len)
print(tuple_len)

## 13. Convert Tuple to List
Create a tuple of five numbers and convert it into a list. 

my_tuple=(1,2,3,4,5,)
my_list=list[my_tuple]

print(my_list)

## 14. Find Maximum and Minimum in a Tuple
Given a tuple of numbers, find and print the maximum and minimum values. 

my_tuple=(24,56,74,36,28,64,45)

min_tuple=min(my_tuple)
max_tuple=max(my_tuple)

print("Tupledagi minimum son:",min_tuple)
print("Tupledagi maxsimal son:", max_tuple)

## 15. Reverse a Tuple
Create a tuple of words and print it in reverse order  

numbers=(1,2,3,4,5,6,7,8,9,10)

numbers_rev=tuple(reversed(numbers))

print(numbers_rev)
