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
