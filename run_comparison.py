import subprocess
import sys
from multiprocessing import Process

def run_python(version, script, count):
    cmd = [version, script, "--count", str(count)]
    print(f"\nRunning with {version}:")
    subprocess.run(cmd)

if __name__ == "__main__":
    count = 100_000_000
    if len(sys.argv) > 1:
        count = int(sys.argv[1])

    run_python("python3.13", "gil_comparison.py", count)
    run_python("python3.13t", "gil_comparison.py", count)
