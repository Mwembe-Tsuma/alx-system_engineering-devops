#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>


int infinite_while(void);

/**
  *infinite_while- Runs an infinite loop
  *
  *Return: 0 success
  */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
  *main- Entry point
  *
  *Return: 0 success
  */

int main(void)
{
	char counter = 0;
	pid_t pid;

	while (counter < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			counter++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
