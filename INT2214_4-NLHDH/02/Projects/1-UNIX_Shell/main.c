#include <malloc.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define MAX_LINE 80 /* The maximum command length */
#define CMD_BUF_LEN 6

const int MAX_ARGC = MAX_LINE / 2 + 1;

char *recent_cmds[CMD_BUF_LEN];
int cmd_ptr = 0;

int parse_cmdline(char *cmd, char **args) {
  int argc = 0;
  char DELIM[] = " \n";
  char *cur_pos = strtok(cmd, DELIM);
  char *nex_pos = cmd;

  if (cur_pos == NULL) {
    return 0;
  }

  while ((nex_pos = strtok(NULL, DELIM)) != NULL) {
    args[argc++] = cur_pos;
    cur_pos = nex_pos;
  }

  args[argc++] = cur_pos;

  return argc;
}

void add_cmd(char *cmd) {
  if (!recent_cmds[cmd_ptr]) {
    recent_cmds[cmd_ptr] = malloc(MAX_LINE);
  }
  strcpy(recent_cmds[cmd_ptr], cmd);
  // printf("add %s\n", recent_cmds[cmd_ptr]);
  cmd_ptr = (cmd_ptr + 1) % CMD_BUF_LEN;
}

char *get_recent_cmd(int num) {
  if (num > CMD_BUF_LEN)
    return 0;
  int id = (cmd_ptr + CMD_BUF_LEN - num) % CMD_BUF_LEN;
  // printf("get recent: %d %d\n",num, id);
  return recent_cmds[id];
}

int main(void) {
  int i;
  char *args[MAX_ARGC]; /* command line arguments */
  int should_run = 1;
  char *cmdline = malloc(MAX_LINE);
  char buf[MAX_LINE];

  for (i = 0; i < MAX_ARGC; i++)
    args[i] = malloc(0x10);

  while (should_run) {
    printf("osh> ");
    fflush(stdout);

    memset(buf, 0, MAX_LINE);
    read(0, buf, MAX_LINE);

    if (buf[0] == '!') {
      char *find_cmd;
      if (strncmp(buf, "!!", 2) == 0)
        find_cmd = get_recent_cmd(1);
      else if (buf[1] <= '9' && buf[1] >= '0') {
        buf[2] = 0;
        int id;
        sscanf(buf + 1, "%d", &id);
        find_cmd = get_recent_cmd(id);
      } else {
        printf("Invalid command!\n");
        continue;
      }
      if (!find_cmd) {
        printf("No command in history!\n");
        continue;
      }
      strcpy(cmdline, find_cmd);

    } else {
      strcpy(cmdline, buf);
    }

    add_cmd(cmdline);

    int argc = parse_cmdline(cmdline, args);

    if (!argc)
      continue;

    pid_t pid = fork();
    if (pid < 0) {
      printf("Fork failed!\n");
      continue;
    }
    // child process
    if (pid == 0) {
      fflush(stdout);
      for (int i = argc; i < MAX_ARGC; i++)
        args[i] = 0;
      if (execvp(args[0], args) == -1) {
        printf("Failed to execute command!\n");
      }
    }
    if (strcmp(args[argc - 1], "&")) {
      wait(NULL);
    }
  }

  for (int i = 0; i < MAX_ARGC; i++)
    free(args[i]);
}
