# Naive Bayes Language Classifier

This Python program can tell whether the input text file is written in English or Spanish. It uses a multinomial Naive Bayes classifier based on letter frequencies.
It works by first reading in predefined probability distributions for each letter A–Z in both English (e.txt) and Spanish (s.txt), then analyzing the input text file to count how often each letter appears.
Using these counts, the program calculates the log-likelihood of the text under each language model by summing the product of each letter’s count and the logarithm of its corresponding probability. 
It then applies Bayes' Rule to convert these likelihoods into posterior probabilities, outputting the probability that the text is English or Spanish. 

##  Demo
![Demo](Demo.gif)

## How to run / Use yourself

1. **Clone the repository and navigate to folder**:
   ```bash
   git clone https://github.com/JackHatlestad/naivebayes-language-classifier.git
   cd naivebayes-language-classifer
2. **Run Program**:
   ```bash
   Python classifier.py [input.txt]
