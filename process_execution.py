import subprocess
import os

print("Parent Process ID:", os.getpid())

print("\nExecuting child process...\n")

process = subprocess.Popen(
    ["cmd", "/c", "dir"],
    shell=False
)

print("Child Process ID:", process.pid)

process.wait()

print("\nChild Process Completed")
print("Exit Code:", process.returncode)