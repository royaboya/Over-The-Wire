# Level 5
Given Prompt: The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

human-readable
1033 bytes in size
not executable

Setup
`ssh bandit5@bandit.labs.overthewire.org -p 2220`

`cd` into `inhere` and `ls` to get:
```
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
```
run `find -readable -size 1033c -not -executable`
- `-readable` for human readable 
- `-size 1033c` for 1033 bytes
- `-not -executable` for not executable files

returns `./maybehere07/.file2`
`cat ./maybehere07/.file2`to get password
