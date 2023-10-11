# Level 6
Given Prompt: The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7
owned by group bandit6
33 bytes in size

Setup
`ssh bandit6@bandit.labs.overthewire.org -p 2220`

`cd` to the root directory 
run `find ./ -user bandit7 -group bandit6 -size 33c`
- `-user bandit7` to specify user bandit7
- `-group bandit6` to specify group bandit6
- `-size 33c` to specify files with size 33 bytes

Going through the displayed files, we can find a file without permission denied:
`./var/lib/dpkg/info/bandit7.password`

run `cat ./var/lib/dpkg/info/bandit7.password`
