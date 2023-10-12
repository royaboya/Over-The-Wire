# Level 8
Given Prompt: The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

Setup
`ssh bandit8@bandit.labs.overthewire.org -p 2220`

`ls` to find a `data.txt` file

run `sort data.txt | uniq -u` to get the unique string
- `sort data.txt` sorts all of the strings in the file in order
- `|` redirects output
- `uniq -u` filters for unique strings
