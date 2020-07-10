import os
import sys
import subprocess


def all_pids() -> str:
    res = subprocess.run(['ps', '-ef'], stdout=subprocess.PIPE, encoding='utf-8')
    return res.stdout


def pid_information():
    '''
    Также вместо всего этого можно использовать уже изобретенный велосипед:
    os.getpid()
    
    '''
    
    def pid_basic(pid: int=1) -> str:
        res = subprocess.run(['ps', '-Flww', '-p', str(pid)], stdout=subprocess.PIPE, encoding='utf-8')
        return res.stdout

    try:
        print(pid_basic(pid = int(sys.argv[1])))
    except (IndexError, ValueError):
        print(pid_basic())


def list_dirs(path: str):
    if os.path.isdir(path):
        print(f"\nALL FILES IN {path}\n")
        for i in os.listdir(path):
            print(i)
    else:
        raise Exception(f"Path:\n{path} is not exist!")


def curr_dir():
    print(f"\nCURRENT DIRECTORY: {os.getcwd()}\n")
    for i in os.listdir():
        print(i)


def kernel_ver():
    return f"KERNEL VERSION: {os.uname()[2]}\n"


def os_ver():
    return f"OS VERSION: {os.uname()[3]}\n"

if __name__ == "__main__":
    print(all_pids())
    pid_information()
    print(os_ver())
    print(kernel_ver())
    print(curr_dir())
    print(list_dirs(input("\nPlease enter dir for list files:")))

