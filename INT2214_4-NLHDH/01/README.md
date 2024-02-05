This is the code for the exercises in **Operating System Concept, Silberschatz et al. 9th ED (page 96-99)**. 

## Requirements
Remember to update the system (`linux` and `linux-headers` package for Arch user).
To see which version is currently loading, run:
```
uname -r
```
You could see the folder inside `/lib/modules`.

## Run
```
❯ make
❯ sudo insmod Module.ko    #  Insert module to the kernel
❯ sudo dmesg               #  View logs
❯ sudo rmmod Modulo        #  Remove module from the kernel
❯ sudo dmesg               #  View logs
```
## More few things
Check out the exercises in the 10th ED (there are something with `/proc`).

First **2 chapters** were covered during the first lecture.
