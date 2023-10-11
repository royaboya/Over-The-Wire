# Level 2
Given Prompt: The password for the next level is stored in a file called spaces in this filename located in the home directory

Setup
<code>ssh bandit2@bandit.labs.overthewire.org -p 2220</code>

run `ls` to find a file named "spaces in this file name"

run <code>cat spaces\ in\ this\ filename</code> or <code>cat "spaces in this filename"</code>
