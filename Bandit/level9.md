# Level 9 
Given Prompt: The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters

Setup
`ssh bandit9@bandit.labs.overthewire.org -p 2220`

`ls` to see a `data.txt` file
run `strings data.txt | grep "=="` to see something like:
```
x]T========== theG)"
========== passwordk^
========== is
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
```