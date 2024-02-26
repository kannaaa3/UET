#include <linux/init.h>
#include <linux/sched.h>
#include <linux/list.h> // list
#include <linux/module.h>

static int hello_init(void) {
  struct task_struct *task;
  for_each_process(task) {
    printk("pid = %d\n", task->pid);

  }
  return 0;
}

static void hello_exit(void) {
  // Traverse and release entry
}

module_init(hello_init);
module_exit(hello_exit);

MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("Hello World Module");
MODULE_AUTHOR("ANY");
