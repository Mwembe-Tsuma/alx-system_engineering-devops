# Shell variables and expansions
0. alias ls="rm *" : Create a script that creates an alias.
1. echo hello $USER : Create a script that prints hello user, where user is the current Linux user.
2. export PATH=$PATH:/action : Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.
3. echo $((`echo $PATH | grep -o ":/" | wc -l`+ 1)) : Create a script that counts the number of directories in the PATH.
4. printenv: Create a script that lists environment variables. 
5. set. : Create a script that lists all local variables and environment variables, and functions.
6. BEST="School" : Create a script that creates a new local variable.
7. export BEST="School" : Create a script that creates a new global variable.
8. echo $(($TRUEKNOWLEDGE + 128)) : Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
9. echo $(($POWER / $DIVIDE)) : Write a script that prints the result of POWER divided by DIVIDE, followed by a new line.
10. echo "$(($BREATH ** $LOVE))": Write a script that displays the result of BREATH to the power LOVE
11. echo $((2#$BINARY)) : Write a script that converts a number from base 2 to base 10.
12. echo {a..z}{a..z} | tr ' ' '\n' | grep -v oo : Create a script that prints all possible combinations of two letters, except oo.
13. printf "%.2f" $NUM | sort : Write a script that prints a number with two decimal places, followed by a new line.
The number will be stored in the environment variable NUM.
14. printf '%x\n' $DECIMAL :  Write a script that converts a number from base 10 to base 16.
15. tr 'a-zA-Z' 'n-za-mN-ZA-M' : Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII. 
16. perl -lne 'print if $. % 2 == 1' : Write a script that prints every other line from the input, starting with the first line.
17.  echo $(printf %o $(($((5#$(echo $WATER | tr 'water' '01234'))) + $((5#$(echo $STIR | tr 'stir.' '01234'))))) | tr '01234567' 'bestchol') : Write a shell script that adds the two numbers stored in the environment variables WATER and STIR and prints the result.
