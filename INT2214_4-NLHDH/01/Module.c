#include <linux/init.h>
#include <linux/list.h> // list
#include <linux/module.h>
#include <linux/slab.h> // malloc, free

const int TOTAL_PERSON = 5;

struct birthday {
  int day;
  int month;
  int year;
  struct list_head list;
};

static LIST_HEAD(birthday_list);
struct birthday *person;

static int hello_init(void) {
  // Insert 5 new birthday instance to the list
  for (int i = 0; i < TOTAL_PERSON; i++) {
    person = kmalloc(sizeof(struct birthday), GFP_KERNEL);
    person->day = i;
    person->month = 7;
    person->year = 2003;
    INIT_LIST_HEAD(&person->list);
    list_add_tail(&person->list, &birthday_list);
  }
  // Traverse and print the content out
  struct birthday *ptr;
  list_for_each_entry(ptr, &birthday_list, list) {
    printk(KERN_INFO "Birthday : %d/%d/%d\n", 
           ptr->day, ptr->month, ptr->year);
  }

  return 0;
}

static void hello_exit(void) {
  struct birthday *ptr, *next;
  // Traverse and release entry
  list_for_each_entry_safe(ptr, next, &birthday_list, list) {
    printk(KERN_INFO "Delete birthday: %d-%d-%d\n", 
           ptr->day, ptr->month, ptr->year);
    list_del(&ptr->list);
    kfree(ptr);
  }
}

module_init(hello_init);
module_exit(hello_exit);

MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("Hello World Module");
MODULE_AUTHOR("ANY");
