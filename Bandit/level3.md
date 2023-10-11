# Level 3
Given Prompt: The password for the next level is stored in a hidden file in the inhere directory.

Setup
<code>ssh bandit3@bandit.labs.overthewire.org -p 2220</code>

run `ls` to find the `inhere` directory
`cd inhere` and `ls` to find that nothing is displayed

run `ls -a` to uncover `.hidden` file
`cat .hidden` to get password
