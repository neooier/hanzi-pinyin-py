import os
import subprocess
import sys

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode())
    if result.stderr:
        print(result.stderr.decode(), file=sys.stderr)

def main():
    # Clean up previous builds
    run_command("rmdir /s /q dist build & del /q *.egg-info")
    
    # Build the package
    run_command("python setup.py sdist bdist_wheel")
    
    # Upload the package to PyPI
    run_command("twine upload dist/*")

if __name__ == "__main__":
    main()
