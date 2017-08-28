# proc-explorer

## getatt

gets parameter from all numbered directories in /proc, as in processes.
usage: python getatt.py --get=cmdline

it will get all 'cmdline' from all processes, then one can pipe grep to limit results.


## findproc

finds a parameter in /proc/sys and prints it.

usage: python findproc.py --find=mmap_min_addr (example)
