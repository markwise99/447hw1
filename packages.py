# automatically installs the required packages on run
import sys
import subprocess


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    install("flask")
    install("databases")
    install("flask-wtf")
    install("flask-sqlalchemy")
    
    # process output with an API in the subprocess module:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    print(installed_packages)

main()