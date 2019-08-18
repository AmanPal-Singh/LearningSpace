"""
Chapter 1 - Arrays and Strings
Aman Singh


Key concepts: Hash tables, arrays, and strings
"""


# Q1: Is Unique


def is_unique(string):
	""" This function determines if string has all unique characters and returns a boolean type """
	chars = []

	for char in string:
		if char in chars:
			return False
		else:
			chars.append(char)
	return True


assert is_unique("ba") == True , "Should be True"
assert is_unique("bab") == False, "Should be False"
assert is_unique("") == True, "Should be True"
assert is_unique("bbbbbbb") == False, "Should be False"
assert is_unique("1231") == False, "Should be False"
assert is_unique("1!3#t") == True, "Should be True"


# Q2: Check Permutation
# Assumed that non alphabetic characters are included

def is_permutation1(string1, string2):
	""" is_permutation1 determines if string1 and string2 are permutations of each other """
	chars = []

	for char in string1:
		chars.append(char.lower())
	for char in string2:
		if char in chars:
			chars.remove(char.lower())

	if len(chars) == 0 and (string1 != "" or string2 != ""):
		return True
	else:
		return False

assert is_permutation1("tacocat", "ttaacco") == True, "Should be True"


#Q3: URLify

def URLify(string, string_length):
	""" URLify returns string as a URl with all spaces replaced by %20 """

	URL = ''.join('%20' if c == ' ' else c for c in string[:string_length])
	return URL
	
assert URLify("Mr John Smith      ", 13) == "Mr%20John%20Smith", "Should be \"Mr%20John%20Smith\""

#Q4: Palindrome Permutation

def palindrome_permutation(string):
	string = string.lower().replace(" ", "")
	print(string)
	if len(string) % 2 == 0:
		chars = []
		for char in string:
			if char in chars:
				chars.remove(char)
			else:
				chars.append(char)
		if len(chars) == 0:
			return True
		else:
			return False
	else:
		chars = []
		for char in string:
			if char in chars:
				chars.remove(char)
			else:
				chars.append(char)
		if len(chars) == 1:
			return True
		else:
			return False

assert palindrome_permutation("taco coa") == True, "Returns True"

#Q5: One Away

def one_away(s1, s2):

	#If there is more than a 1 char difference, then there is no way to make one string another with one edit by definition of question
	if abs(len(s1) - len(s2)) > 1:
		return False
	elif abs(len(s1) - len(s2)) == 1:
		boolean = True
		for char in s1:

	else:


# Q6: String Compression

