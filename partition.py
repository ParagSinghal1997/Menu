#!/usr/bin/python36

print("content-type: text/html")
print()

import subprocess as sb
import cgi

data = cgi.FieldStorage()

device = data.getvalue("device")
size = data.getvalue("size")
fs = data.getvalue("fs")
path = data.getvalue("path")

def create_partition(device,size,fs,path):
    create_part = 'sudo ansible-playbook  part.yml --extra-vars "host={} disk={} end={}"'.format("localhost",device,size)
    formate_part = 'sudo ansible-playbook  mkfs.yml --extra-vars "host={} dev1={}1 type1={}"'.format("localhost",device,fs)
    mount_part = 'sudo ansible-playbook  mount.yml --extra-vars "host={} state=mounted device={}1 type={} point={}"'.format("localhost",device,fs,path)

    print(mount_part)
    output = sb.getoutput(create_part)
    print(output)
    if 'failed=0' not in output and 'unreachable=0' not in output:
        return output
    else:
        output = sb.getoutput(formate_part)
        if 'failed=0' not in output and 'unreachable=0' not in output:
            return output
        else:
            output = sb.getoutput(mount_part)
            if 'failed=0' in output and 'unreachable=0' in output:
                return output
            else:
                return "failed=1"


output = sb.getoutput(create_partition(device,size,fs,path))

