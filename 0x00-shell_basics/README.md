0. pwd: print working directory
1. ls : list contents of your directory or file
2. cd ~: Change directory to home
3. ls -l :Displays contents of a directory in a long format
4. ls -al  Display current directory contents, including hidden files (starting with .)
5. ls -al -n: Display current directory contents numerically including hidden files
6. mkdir /tmp/my_first_directory: creates a file named my_first_directory inside a directory named tmp
7. mv /tmp/betty  /tmp/my_first_directory/ : Move the file betty from /tmp/ to /tmp/my_first_directory.
8. rm /tmp/my_first_directory/betty: Removing file betty in my_first_directory directory
9. rm -r /tmp/my_first_directory: Delete the directory my_first_directory that is in the /tmp directory.
10. cd - : A script that changes the working directory to the previous one.
11. ls -al . .. /boot : A  script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
12. file /tmp/iamafile: Prints the type of a file named iamafile.
13. ln -s  /bin/ls  __ls__: Creates a symbolic link named __ls__that  than points to /bin/ls directory
14. cp -un *.html ../ : A  script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
