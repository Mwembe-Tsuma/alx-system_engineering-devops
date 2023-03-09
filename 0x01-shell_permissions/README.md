0. su betty: A script that switches the current user to the user betty.
1. whoami: A script that prints the effective username of the current user.
2. group: A script that prints all the groups the current user is part of.
3. chown betty :  A  that changes the owner of the file hello to the user betty.
4. touch hello: A  script that creates an empty file called hello.
5. chmod u+x hello: Ascript that adds execute permission to the owner of the file hello.
6. chmod ug+x,o+r : A  script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
7. chmod ugo+x: A script that adds execution permission to the owner, the group owner and the other users, to the file hello
8. chmod 007 hello : A script that sets the permission to the file hello to --- --- rwx
9. chmod 753 hello : A script that sets the mode of the file hello to  rwxr-x-wx
10. chmod --reference olleh hello : A  script that sets the mode of the file hello the same as olleh’s mode.
11. chmod -R +X . : A script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.
12. mkdir -m751 my_dir : A  script that creates a directory called my_dir with permissions 751 in the working directory.
13. chgrp school hello : A Write a script that changes the group owner to school for the file hello
14. chown vincent:staff * - A script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.
15. chown -h vincent:staff _helloo : A script that changes the owner and the group owner of _hello to vincent and staff respectively.
16. chown --from=guillaume betty hello: A script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
17. telnet towel.blinkenlights.ln: Write a script that will play the StarWars IV episode in the terminal.
