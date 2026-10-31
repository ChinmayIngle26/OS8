import multiprocessing
import os

def child_process():
    print("\nChild Process Created")
    print("Child PID:", os.getpid())
    print("Parent PID:", os.getppid())

if __name__ == "__main__":

    print("Parent Process ID:", os.getpid())

    process = multiprocessing.Process(
        target=child_process
    )

    process.start()
    process.join()

    print("\nParent Process Completed")
    print("Child Process ID:", process.pid)
    print("Exit Code:", process.exitcode)