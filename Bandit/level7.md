# Level 7
Given Prompt: The password for the next level is stored in the file data.txt next to the word millionth

Setup
`ssh bandit7@bandit.labs.overthewire.org -p 2220`

`ls` to find a file called `data.txt`
running `cat` leads to a large display of random text

run `grep "millionth" data.txt` to get:
`millionth	TESKZC0XvTetK0S9xNwm25STk5iWrBvP`