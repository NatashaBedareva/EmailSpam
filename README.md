# EmailSpam

Determines whether the email is spam. 

### Features

- It works on the basis of a naive Bayesian classifier.
- Creates a dictionary of spam and non-spam words
- Visual interface on tkinter

### Principle of operation algorithm.
- Text processing. Removing punctuation marks, converting to lowercase
- Creating dictionaries with the probability that the word is spam
- To determine whether an email is spam, we consider the full probability according to Bice's theorem

For training, you need to use a set of files from this site https://www2.aueb.gr/users/ion/data/enron-spam/
