import os.path,subprocess
from subprocess import STDOUT,PIPE
import time

def compile_java(java_file):
    subprocess.check_call(['javac', java_file])




compile_java('Hello.java')
os.system('java Hello')