# Level 11
Given Prompt: The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

Setup
`ssh bandit11@bandit.labs.overthewire.org -p 2220`

run `cat data.txt` to get something like:
`Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi`

We know that this is a ROT13 cipher, lower case [a-z] translated 13 characters would be [n-m]
and upper case [A-Z] would be [N-M]

run `cat data.txt | tr "[A-Za-z]" "[N-ZA-Mn-za-m]"`
- `cat data.txt` takes the content and passes as output
- `tr "[A-Za-z]" "[N-ZA-Mn-za-m]"` replaces text from set one to set two
- `A-Za-z` specifies alphabetical letters in the order of `ABCD...XYZabcd...xyz`
- `N-ZA-Mn-za-m` specifies new order as `NOPQ...XYZAB...LM` and `nopq...xyzab...lm` respectively
- dashes are used to specify the enumeration of letters and `A` or `Z` are used to help specify the location of the beginning/end of the alphabet

End Result is something like: 
`The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv`