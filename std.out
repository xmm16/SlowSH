import os
import subprocess
import time

os.system("git pull && git add . && git commit -m init && git push")

shell = subprocess.Popen("/bin/bash", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

while True:
    if subprocess.run("git fetch --dry-run", text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True).stdout != '':
        os.system("git pull")
        with open("run.bash", 'r') as f:
            new_bash = f.read()

        if new_bash:
            with open("std.out", 'r') as f:
                old_out = f.read()

            shell.stdin.write(new_bash + ' > std.out 2>&1\n')
            shell.stdin.flush()
            while True:
                with open("std.out", 'r') as f:
                    new_out = f.read()

                if old_out == new_out:
                    break
                    
                time.sleep(1)

            os.system("git pull && git add . && git commit -m output && git push")

    time.sleep(1)
