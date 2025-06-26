import sys
import string
import math
import os

def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish)

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    X = {letter: 0 for letter in string.ascii_uppercase}

    with open(filename, encoding='utf-8') as f:
        for line in f:
            for char in line:
                if char.isalpha():
                    char = char.upper()
                    if char in X:
                        X[char] += 1
    return X

def main():
    if len(sys.argv) != 2:
        print("Usage: python classifier.py [letter file]")
        return

    text_file = sys.argv[1]

    if not os.path.isfile(text_file):
        print(f"Error: Can't find text file")
        return

    e, s = get_parameter_vectors()

    X = shred(text_file)
    X_counts = [X[char] for char in string.ascii_uppercase]

    F_english = math.log(0.5) 
    F_spanish = math.log(0.5) 

    for i in range(26):
        xi = X_counts[i]
        e_i = e[i]
        s_i = s[i]

        if e_i > 0:
            F_english += xi * math.log(e_i)
        if s_i > 0:
            F_spanish += xi * math.log(s_i)

    if F_spanish - F_english >= 100:
        p_english_given_X = 0.0
    elif F_spanish - F_english <= -100:
        p_english_given_X = 1.0
    else:
        p_english_given_X = 1 / (1 + math.exp(F_spanish - F_english))

    p_spanish_given_X = 1.0 - p_english_given_X

    print("The probability that this text is English is: " + f"{p_english_given_X:.4f}" )
    print("The probability that this text is spanish is: " + f"{p_spanish_given_X:.4f}" )
    if p_english_given_X >= 0.5:
        print("The text was written in English.")
    else:
        print("The text was written in Spanish.")
main()