import psutil
import os
import time

print("SYSTEM PERFORMANCE ANALYSIS")
print("----------------------------")

# CPU utilization
cpu = psutil.cpu_percent(interval=1)

print("CPU Utilization:", cpu, "%")

# Memory utilization
memory = psutil.virtual_memory()

print("\nTotal RAM:",
      round(memory.total / (1024**3), 2), "GB")

print("Used RAM:",
      round(memory.used / (1024**3), 2), "GB")

print("Available RAM:",
      round(memory.available / (1024**3), 2), "GB")

print("Memory Utilization:", memory.percent, "%")

# Current process information
process = psutil.Process(os.getpid())

print("\nCURRENT PROCESS INFORMATION")

print("Process ID:", process.pid)

print("Memory Used:",
      round(process.memory_info().rss / (1024**2), 2), "MB")

print("Process Status:", process.status())
