# Level 0 
Given Prompt: The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

SSH username: bandit0
SSH pass: bandit0
port: 2220

run <code>ssh bandit0@bandit.labs.overthewire.org -p 2220</code>
enter password <code>bandit0</code>


# Level 0 > 1
Given Prompt: The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

run <code>ls</code> to find <code>readme</code> file
then <code>cat readme</code> to get password

password: NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL