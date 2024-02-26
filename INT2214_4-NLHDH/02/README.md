### Code on slide
```c
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <unistd.h>

int value = 5;

int main(){
  printf("\n Before fork()");
  pid_t pid;
  pid = fork();
  if (pid < 0) { /* error occurred */
    fprintf(stderr, "\n Fork Failed");
    return 1;
  }
  else if (pid == 0) { /* child process */
    value += 15;
    printf("\n CHILD: value = %d",value);
  /* LINE A */
  return 0;
  }
  else if (pid > 0) { /* parent process */
    wait(NULL);
    printf("\n PARENT: value = %d",value);
    /* LINE B */
    return 0;
  }
}
```

Output:
```
Before fork()
CHILD: value = 20 Before fork()
PARENT: value = 5%                                                                                                                                                                                                                  

```


The child inherited its parent's stdout (which hasn't been `fflush` yet), that's why we see 2 `"Before fork()"`.
After copying the process image from parent, the child added 5 to `value`, whereas the parent didn't.



### Exercises

**3.12**. Call `res[i]` is the number of total created process the loop length `i`. Hence `res[0] = 1`, `res[1] = 2`.

As we can see, `res[i] = 2 * res[i-1]` since after the first `fork()`, there are exactly two equivalent process that run the loop length `i-1`.

Hence, the answer is `2^4 = 16` created process.

**3.14**. Both processes continued to run on the same next piece of code. The only different is the value of `pid` variable: the parent's `pid` is equal to its child created by `fork()`, but the child's `pid` is `0`. 

The output of parent should be:
```
parent: pid = 2603     // C: child pid returned from fork()
parent: pid1 = 2600    // D: actual pid return from getpid()
```
The output of the child:
```
child: pid = 0         // A: pid since fork()
child: pid1 = 2603     // B: actual pid return from getpid()
```

### Project [1]: Unix Shell
```c
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
  cmd_ptr = (cmd_ptr + 1) % CMD_BUF_LEN;
}

void print_history() {
  for (int j = 1; j <= 6; j++) {
    int i = (cmd_ptr - j +CMD_BUF_LEN) % CMD_BUF_LEN;
      if (recent_cmds[i] == 0)  break;
      printf("> %s", recent_cmds[i]);
  }
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

    int res = strcmp(buf, "history\n");
    if (!res) {
      print_history();
      continue;
    }


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

    int conc = !(strcmp(args[argc - 1], "&"));

    pid_t pid = fork();
    if (pid < 0) {
      printf("Fork failed!\n");
      continue;
    }
    // child process
    if (pid == 0) {
      fflush(stdout);
      for (int i = argc - 1*(conc!=0); i < MAX_ARGC; i++)
        args[i] = 0;
      if (execvp(args[0], args) == -1) {
        printf("Failed to execute command!\n");
      }
    }
    if (!conc) {
      wait(NULL);
    }
  }

  for (int i = 0; i < MAX_ARGC; i++)
    free(args[i]);
}

```

Output

```
osh> history
> ls /home
> sleep 20 &
> ls -la /home/kannaaa3

```

### Project [2] DFS Process Tree

```c
#include <linux/init.h>
#include <linux/sched.h>
#include <linux/list.h> // list
#include <linux/module.h>


void dfs(struct task_struct *lst) {
  struct task_struct *task;
  struct list_head* lh;
  list_for_each (lh, &lst->children) {
    task = list_entry(lh, struct task_struct, sibling);
    printk("%-20s   %-4u    %-4d\n", task->comm, task->__state, task->pid);
    dfs(task);
  }
}

static int hello_init(void) {
  struct list_head *list;
  printk("-----------------------------------\n");
  printk("process name          state     pid\n");
  printk("-----------------------------------\n");
  dfs(&init_task);

  return 0;
}

static void hello_exit(void) {
  // traverse and release entry
}

module_init(hello_init);
module_exit(hello_exit);

module_license("gpl");
module_description("hello world module");
module_author("any");

```


