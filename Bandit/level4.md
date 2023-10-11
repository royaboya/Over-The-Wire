# Level 4
Given Prompt: The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

Setup
`ssh bandit4@bandit.labs.overthewire.org -p 2220`
pass: 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

1. `cd inhere` 
2. `ls` to find that there are multiple files

Options:
1. By brute force `cat` each individual file or `file` the entire directory
2. Run `strings` and pass all files in

running `file ./` returns:
```
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
```
then `cat ./-file07` to get contents

or

run `strings ./*` to get:
```
HRrtZ
MUb4
eE}:
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
```
password: lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR