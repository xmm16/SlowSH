import os
import subprocess

while True:
    os.system("git pull")
    os.system("cat std.out")

    with open("run.bash", 'w') as f:
        f.write(input("<slow>> ").strip())

    git_commands = ("git add . && git commit -m input && git push")
    subprocess.run(git_commands, shell=True, text=True, capture_output=True)
