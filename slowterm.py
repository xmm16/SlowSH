import os
import subprocess
import time

git_commands = ("git pull && git add . && git commit -m input && git push")
subprocess.run(git_commands, shell=True, text=True, capture_output=True)

first_time = True

while True:
    subprocess.run("git pull", shell=True, text=True, capture_output=True)

    if not first_time:
        os.system("cat std.out")
        print('\n')

    with open("run.bash", 'w') as f:
        f.write(input("<slow>> ").strip())

    subprocess.run(git_commands, shell=True, text=True, capture_output=True)
    
    while subprocess.run("git fetch --dry-run", text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True).stdout == '':
        time.sleep(1)

    if first_time:
        first_time = False
