import subprocess

subprocess.call(['dir', '-1'], shell=True)
subprocess.call(['git add .', '-1'], shell=True)
subprocess.call(['git commit -m "kuku"', '-1'], shell=True)
subprocess.call(['git status', '-1'], shell=True)
