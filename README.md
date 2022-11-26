# Guess-the-Number

## osX and Linux fix:
1. open file in an editor
2. go to line 7
3. change 'cls' to 'clear'

## Why youneed to change it:
This clears the screen after every round, cls is the batch (.bat) command for clearing the screen, but on Linux and MacOS X there is not batch (.bat) so the command os different (cls).

## Requirments
1. python

## How it works
1. generates a number between 0 and 1000
2. asks user for their guess
3. compares numbers and says if you are correct or not
