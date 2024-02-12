
# import psutil
# # print(psutil.cpu_count())
# processes = psutil.process_iter()
#
# for process in processes:
#     print(process.cmdline())
#     print(f"Process ID: {process.pid}, Name: {process.name()}")
#

import os
import psutil

# def find_procs_by_name(name):
#     "Return a list of processes matching 'name'."
#     ls = []
#     for p in psutil.process_iter(["name", "exe", "cmdline"]):
#         if name == p.info['name'] or \
#                 p.info['exe'] and os.path.basename(p.info['exe']) == name or \
#                 p.info['cmdline'] and p.info['cmdline'][0] == name:
#             ls.append(p)
#     return ls
#
# a = find_procs_by_name('python.exe')
# print(a)


import psutil

# Iterate over all running processes
for proc in psutil.process_iter():
    try:
        # Get process information
        process_info = proc.as_dict(attrs=['pid', 'name', 'cmdline'])

        # Check if process has command line arguments
        if process_info['cmdline']:
            if process_info['name']=="python.exe":  # print only python's proccess list
                print(
                f"PID: {process_info['pid']}, Name: {process_info['name']}, Command Line: {' '.join(process_info['cmdline'])}")
    except psutil.NoSuchProcess:
        pass
    except psutil.AccessDenied:
        pass
