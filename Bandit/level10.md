# Level 10
Given Prompt: The password for the next level is stored in the file data.txt, which contains base64 encoded data

Setup
`ssh bandit10@bandit.labs.overthewire.org -p 2220`

run `ls` to find `data.txt` and `cat data.txt` to find something like:
`VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==`

It is given that the information is base64 encoded

run `base64 -d data.txt` to get something like:
`The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM`