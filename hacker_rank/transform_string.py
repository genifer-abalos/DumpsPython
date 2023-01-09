#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    # Write your code here
    words = sentence.split(" ")

    transformed_words = []
    for word in words:
        if len(word) == 1:
            transformed_words.append(word)
        else:
            print(len(word))
            for i in range(len(word)-1):
                if not i == 0:
                    if word[i] < word[i + 1]:
                        print("transform to lowercase")
                    elif word[i] > word[i + 1]:
                        print("transform to uppercase")
                    else:
                        print("no change")
    print(transformed_words)
    return transformed_words


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # sentence = input()
    sentence = "a Blue MOON"

    result = transformSentence(sentence)

    # fptr.write(result + '\n')

    # fptr.close()
