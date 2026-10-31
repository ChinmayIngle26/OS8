import subprocess

print("1. Display Running Processes")
subprocess.run(["tasklist"])

print("\n2. Display Python Processes")
subprocess.run(
    ["tasklist", "/FI", "IMAGENAME eq python.exe"]
)

print("\n3. Process Management Demonstration")
print("Use taskkill /PID <PID> /F to terminate a process.")