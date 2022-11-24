'''
Given a text file file.txt, print just the 10th line of the file.

Example:

Assume that file.txt has the following content:
'''
# Read from the file file.txt and output the tenth line to stdout.
awk 'NR==10{print; exit}' file.txt
