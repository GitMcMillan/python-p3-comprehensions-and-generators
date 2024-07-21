#!/usr/bin/env python3


# squared_minus_one = list()

# for n in range(1, 11):
#     squared_minus_one.append((n ** 2) -1)
    
# print(squared_minus_one)

# List Comprehension: Uses []
# squared_minus_one = [(n ** 2) -1 for n in range(1, 11)]


# Generator Expression: uses () 
# one_to_three = range(1,4)
# List Comprehension: squared_lc = [n ** 2 for n in one_to_three]
#Generator Expression: squared_ge = (n ** 2 for n in one_to_three)

# looping through each sdhows identical values:
# for n in squared_lc:
#     print(n)

# 1
# 4
# 9

# for n in squared_ge:
#     print(n)

# 1
# 4
# 9
# 

# But the objects are NOT identical
#print(squared_lc)
# [1, 4, 9]
#print(squared_ge)
# <generator object <genexpr>>


def return_evens(num_list):
    #num_list = [n % 2 == 0 for n in range(1, 10, 2)]
    evens = [n for n in num_list if n % 2 == 0 ]
    return evens

def make_exclamation(sentence_list):
    
    return [sentence + "!" for sentence in sentence_list]