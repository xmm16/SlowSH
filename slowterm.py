import os
import subprocess
import time

while True:
    subprocess.run("git pull", shell=True, text=True, capture_output=True)
    os.system("cat std.out")

    with open("run.bash", 'w') as f:
        f.write(input("<slow>> ").strip())

    git_commands = ("git add . && git commit -m input && git push")
    subprocess.run(git_commands, shell=True, text=True, capture_output=True)
    time.sleep(5)
