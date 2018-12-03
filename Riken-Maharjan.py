#!/usr/bin/env python3

'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 

The API consists of 10 functions that you must implement.

Guidelines:
1) Edit the file to match your first name and last name with the format shown.

2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.

3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.

4) We believe in self commenting code, however, provide comments to your solutions
and be organized.

5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.

6) Plagiarism is a serious issue, avoid it at all costs.

7) Don't import external libraries which are not python native

8) Don't change the parameters or returns, follow the directions.

9) Assignment is optional, but totally recommend to achieve before Monday for practice.

Happy Scripting!

© 2018 Revature. All rights reserved.
'''

'''
use the main function for testing purposes and to show me results for all functions.
'''
def main():
	print("Reverse of Hello: ",reverse("Hello"))
	print("Acronym for Deoxyribo Nucleic Acid: ",acronym("Deoxyribo Nucleic ACid"))
	print("Triangle (1,2,1) is: ",whichTriangle(1,2,1))
	print("score for the word scrabble is: ",scrabble("scrabble"))
	print("Is 9 an amstrong number: ",armstrong(9))
	print("Prime Factors of 15: ",primeFactors(15))
	print("Is The quick brown fox jumps over the lazy dog a pangram? ",pangram("The quick brown fox jumps over the lazy dog"))
	print("Sort([1,2,5,4]): ",sort([1,2,5,4]))
	print("rotate abcdefghijklmnopqrstuvwxyz with shift key 13 : ",rotate(13, "abcdefghijklmnopqrstuvwxyz"))
	evenAndOdds()
'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"

Rules:
- Do NOT use built-in tools
- Reverse it your own way

param: str
return: str
'''
def reverse(string):
	revString = ""
	for c in string:
		revString =  c + revString
	return revString	
'''
2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).

param: str
return: str
'''
def acronym(phrase):
	acronym = ""
	isSpaceBefore = False

	for i in range(len(phrase)):
		if(i==0):
			acronym += phrase[i]
		if(isSpaceBefore):
			acronym += phrase[i]

		isSpaceBefore = True if (phrase[i] == " " or phrase[i] == "-") else False 
	return acronym.upper()  

'''
3. Determine if a triangle is equilateral, isosceles, or scalene. An
equilateral triangle has all three sides the same length. An isosceles
triangle has at least two sides the same length. (It is sometimes specified
as having exactly two sides the same length, but for the purposes of this
exercise we'll say at least two.) A scalene triangle has all sides of
different lengths.

param: float, float, float
return: str -> 'equilateral', 'isoceles', 'scalene'
'''
def whichTriangle(sideOne, sideTwo, sideThree):
	if(sideOne == sideTwo and sideTwo == sideThree):
		return 'equilateral'
	elif(sideOne == sideTwo or sideTwo == sideThree or sideOne == sideThree):
		return 'isosceles'
	elif(sideOne != sideTwo and sideTwo != sideThree and sideOne != sideThree):
		return 'scalene'		



'''
4. Given a word, compute the scrabble score for that word.

--Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
"cabbage" should be scored as worth 14 points:

3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
point for E And to total:

3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14

param: str
return: int
'''
def scrabble(word):
	
	dictionary = {
	'A':1,
	'E':1,
	'I':1,
	'O':1,
	'U':1,
	'L':1,
	'N':1,
	'R':1,
	'S':1,
	'T':1,	
	'G':2,
	'B':3,
	'C':3,
	'M':3,
	'P':3,	
	'F':4,
	'H':4,
	'V':4,
	'W':4,
	'Y':4,	
	'K':5,	
	'J':8,
	'X':8,	
	'Q':10,
	'Z':10
		
	}
	answer = 0
	capString = word.upper()
	for c in capString:  
		answer = answer + dictionary[c]	
	return answer;



'''
5. An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9 10 is not an Armstrong number,
because 10 != 1^2 + 0^2 = 2 153 is an Armstrong number, because: 153 = 1^3 +
5^3 + 3^3 = 1 + 125 + 27 = 153 154 is not an Armstrong number, because: 154
!= 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190 Write some code to determine whether
a number is an Armstrong number.

param: int
return: bool
'''
def armstrong(number):
	assert(type(number) == int)
	letterArray = [int(x) for x in str(number)]
	answer = 0.0
	for i in range(len(letterArray)):
		answer += pow(letterArray[i],len(letterArray))
	return answer == int(number)
'''
6. Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.
 
Note that 1 is not a prime number.

param: int
return: list
'''
def primeFactors(number):
	finalAnswer = []
	i = 2
	while(i <= number ):
		if(number % i == 0):
			finalAnswer.append(i)
			number = number / i
			i = i - 1 
		i = i + 1
	return finalAnswer	
'''
7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
gramma, "every letter") is a sentence using every letter of the alphabet at
least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.
 
The alphabet used consists of ASCII letters a to z, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
 
param: str
return: bool
'''
import string

def pangram(sentence):
	dictionary = {}
	

	letters = list(string.ascii_lowercase)

	for c in sentence:
		dictionary[c] = 10
	
	for c in letters:
		if(not c in dictionary):
			return False
	return True	

'''
8. Sort list of integers.
f([2,4,5,1,3,1]) = [1,1,2,3,4,5]

Rules:
- Do NOT sort it with .sort() or sorted(list) or any built-in tools.
- Sort it your own way

param: list
return: list
'''
def sort(numbers):
	'''Bubble sort'''
	
	for i in range(len(numbers)):
		for j in range(len(numbers)-i-1):
			if numbers[j+1] < numbers[j]:
				temp = numbers[j]
				numbers[j] = numbers[j+1]
				numbers[j+1] = temp
	return numbers	

'''
9. Create an implementation of the rotational cipher, also sometimes called
the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the
letters in the alphabet using an integer key between 0 and 26. Using a key of
0 or 26 will always yield the same output due to modular arithmetic. The
letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly
used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain: abcdefghijklmnopqrstuvwxyz Cipher: nopqrstuvwxyzabcdefghijklm It is
stronger than the Atbash cipher because it has 27 possible keys, and 25
usable keys.

Ciphertext is written out in the same formatting as the input including
spaces and punctuation.

Examples: ROT5 omg gives trl ROT0 c gives c ROT26 Cool gives Cool ROT13 The
quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire
gur ynml qbt. ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The
quick brown fox jumps over the lazy dog.

param: int, str
return: str
'''
def rotate(key, string):
	alphabhets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	answer = ""
	for c in string:
		if c.isalpha():
			lower = c.lower()
			i = alphabhets.index(c)
			index = (i + key) % 26
			newChar = alphabhets[index]
			answer += newChar
	return answer
	  

'''
10. Take 10 numbers as input from the user and store all the even numbers in a file called even.txt and
the odd numbers in a file called odd.txt.

param: none, from the keyboard
return: nothing
'''
def evenAndOdds():
	yourInput = input("Please insert 10 numbers separated by commas: ")
	#print yourInput
	numbers = list(map(int, yourInput.split(",")))
	for numb in numbers:
	
		if(numb % 2 == 0):
			with open("even.txt", 'a') as f:
				f.write(str(numb)+'\n')
		elif(numb % 2 != 0 ):
			with open("odd.txt", 'a') as f:
				f.write(str(numb)+'\n')


if __name__ == "__main__":
	main()
