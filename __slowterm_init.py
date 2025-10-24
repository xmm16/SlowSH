import os
import subprocess
import time

old_bash = ""

while True:
    with open("run.bash", "r") as f:
        new_bash = f.read()

    if old_bash != new_bash:
        with open("std.out", "w") as f:
            f.write(subprocess.run("bash run.bash", text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True).stdout)
        os.system("git add . && git commit -m refresh && git push")

    time.sleep(1)
