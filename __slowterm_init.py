import os
import subprocess
import time

with open("run.bash", 'r') as f:
    old_bash = f.read()

shell = subprocess.Popen("/bin/bash", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

while True:
    if subprocess.run("git fetch --dry-run", text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True).stdout != '':
        print("executing")
        with open("run.bash", "r") as f:
            new_bash = f.read()

        if old_bash != new_bash:
            with open("std.out", "w") as f:
                shell.stdin.write(new_bash + '\n')
                shell.stdin.flush()
                f.write(shell.stdout.readline().strip())
            os.system("git pull && git add . && git commit -m output && git push")
            old_bash = new_bash

    time.sleep(1)
