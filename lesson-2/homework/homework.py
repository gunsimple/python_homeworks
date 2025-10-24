@@ -0,0 +1,41 @@
# Homework Exercises

## 1. Yosh kalkulyatori
Foydalanuvchining ismi va tug'ilgan yilini so'rash uchun Python dasturini yozing, 
so'ngra ularning yoshini hisoblang va ko'rsating. 

name= input("Ismingizni kiriting: ")
tugilgan_yil= int(input("Yilinigizni kiriting: ")) 
joriy_yil=2025
age=tugilgan_yil-joriy_yil
print(f"Salom,{name}! Siz{age} yoshdasiz")


## 2. Extract Car Names
Extract car names from the following text:
```python
txt = 'LMaasleitbtui' 
``
txt = 'LMaasleitbtui'
mashina=txt[1::2]
print(mashina)


## 3. Extract Car Names
Extract car names from the following text:
```python
txt = 'MsaatmiazD'
``` 
txt='MsaatmiazD'
mashina=txt[::2]
print(mashina)

## 4. Extract Residence Area
Extract the residence area from the following text:
```python 
txt = "I'am John. I am from London" 

txt="I'am Jonh. I am from London"
start=txt.find ("L")
city=txt[start:]
print(city)


## 5. Reverse String
Write a Python program that takes a user input string and prints it in reverse order.

gap=input("Matni kiriting: ")
teskari=gap[::-1]
print("Teskari mant: ", teskari)


## 6. Count Vowels
Write a Python program that counts the number of vowels in a given string. 

txt="Matimatika"
vowels='aieou'
txt_lower=txt.lower()
count=0
for vowel in vowels:
    count += txt_lower.count(vowel)
print("Unli xarflarni soni: ", count) 


## 7. Find Maximum Value
Write a Python program that takes a list of numbers as input and prints the maximum value. 

numbers=[2,8,6,7,3,1]
print("Katta son: ", max(numbers))

## 8. Check Palindrome
Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).  

word=input("Matni kiriting: ")
if word==word [::-1]:
    print("Bu so'z palindor!")
else:
    print("Bu so'z palindor emas.") 

## 9. Extract Email Domain
Write a Python program that extracts and prints the domain from 
an email address provided by the user. 

email=input("Email manzil kiriting: ")
try:
    domain=email.split('@')[1]
    print("Email domeni:", domain)
except IndexError:
    print("Notog'ri email manzil kiritildi!")   


## 10. Generate Random Password
Write a Python program to generate a random password containing letters, digits, and special characters.

import random
import string

def generate_password(length=12):
    # Harflar, raqamlar va maxsus belgilar to'plamini yaratish
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Tasodifiy parol yaratish
    password = ''.join(random.choices(all_characters, k=length))
    
    return password

# Parol uzunligini foydalanuvchidan olish
length = int(input("Parol uzunligini kiriting: "))
print("Yaratilgan parol:", generate_password(length))
