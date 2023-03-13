#Shell i/o Redirections and Filters
0. echo "Hello, World"  :Write a script that prints “Hello, World”, followed by a new line to the standard output.
1. echo ""(Ôo)'" :  Write a script that displays a confused smiley "(Ôo)'.
2. cat /etc/passwd: Dsiplay contents of file /etc/passwd
3. cat /etc/passwd /etc/hosts: Display the content of /etc/passwd and /etc/hosts
4. tail /etc/passwd: Display the last 10 lines of /etc/passwd
5. head /etc/passwd: Display the first 10 lines of /etc/passwd
6. head -n 3 iacta | tail -n 1 : Write a script that displays the third line of the file iacta.
7. echo "Best School" > \\\*\\\\"'\"Best School\"\\'"\\\\\*\$\\\?\\\*\\\*\\\*\\\*\\\*\:\) : Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.
8. ls -la > ls_cwd_content : Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
9. tail -n 1 < iacta >> iacta : Write a script that duplicates the last line of the file iacta
10. find . -type f -name "*.js" -delete : Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
11. find . -type d -not -name '.' | wc -l : Write a script that counts the number of directories and sub-directories in the current directory.
12. ls -lt | head :  Create a script that displays the 10 newest files in the current directory.
13. sort | uniq | -u : Create a script that takes a list of words as input and prints only words that appear exactly once.
14. grep -i "root" /etc/passwd : Display lines containing the pattern “root” from the file /etc/passwd
15. grep -i  "bin" /etc/passwd | wc -l : Display the number of lines that contain the pattern “bin” in the file /etc/passwd
16. grep -i "root" -A 3 /etc/passwd : Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
17. grep -i -v "bin" /etc/passwd : Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
18. grep -i  '^[a-z]' /etc/ssh/sshd_config : Display all lines of the file /etc/ssh/sshd_config starting with a letter.
19. tr "A" "Z" | tr "c" "e" : Replace all characters A and c from input to Z and e respectively.
20. tr -d "cC" : Create a script that removes all letters c and C from input.
21. rev : Write a script that reverse its input.
22. cut -d:  -f 1,6  /etc/passwd | sort : Write a script that displays all users and their home directories, sorted by users.
23. find . -empty | rev | cut d '/' -f1 | rev : Write a command that finds all empty files and directories in the current directory and all sub-directories.
24. find -type f -name "*.gif" | rev | cut -d "/" -f 1 | cut -d '.' -f 2- | rev | LC_ALL=C sort -f: Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.
25. cut -c 1 | paste -s -d :  Create a script that decodes acrostics that use the first letter of each line.
26. tail -n +2 | cut -f -1 | sort -k 1 | uniq -c | sort -rnk 1 | head -n 11 | rev | cut -d ' ' -f -1 | rev : Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.
