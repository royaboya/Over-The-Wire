# Level 3
Given Prompt: The password for the next level is stored in a hidden file in the inhere directory.

Setup
<code>ssh bandit3@bandit.labs.overthewire.org -p 2220</code>
pass: aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

run `ls` to find the `inhere` directory
`cd inhere` and `ls` to find that nothing is displayed

run `ls -a` to uncover `.hidden` file
`cat .hidden` to get password

password: 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe