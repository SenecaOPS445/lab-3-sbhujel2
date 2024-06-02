#!/usr/bin/env python3
#Author ID: sbhujel2 (180147217)

import subprocess

def free_space():
    p1 = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', '/$'], stdin=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(['awk', '{print $4}'], stdin=p2.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    p2.stdout.close()

    output = p3.communicate()[0]
    stdout = output.decode('utf-8').strip()
    return stdout
if __name__ == "__main__":
    print(free_space())
