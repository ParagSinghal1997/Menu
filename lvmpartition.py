#!/usr/bin/python36

print("content-type: text/html")
print()

import subprocess as sb
import cgi

data = cgi.FieldStorage()

device = data.getvalue("device")
fs = data.getvalue("fs")
path = data.getvalue("path")
vgname = data.getvalue("vg_name")
vgsize = data.getvalue("vg_size")
lvname = data.getvalue("lv_name")
lvsize = data.getvalue("lv_size")

def createlvm_partition(device,vgname,vgsize,lvname,lvsize,fs,path):
    create_vg = 'sudo ansible-playbook vg.yml --extra-vars  "host={} state=present  pvlist={} vgname={} size={}"'.format("localhost",device,vgname,vgsize)
    create_lv = 'sudo ansible-playbook lv.yml --extra-vars  "host={} sta=present  device={} vgname={} lvname={} size={}"'.format("localhost",device,vgname,lvname,lvsize)
    formate_part = 'ansible-playbook ./final_playbooks/mkfs.yml --extra-vars "host={} dev1=/dev/{}/{} type1={}"'.format("localhost",vgname,lvname,fs)
    mount_part =  'sudo ansible-playbook  mount.yml --extra-vars  "host={} state=mounted  device=/dev/{}/{} type={} point={}"'.format("localhost",vgname,lvname,fs,path)
    output = sb.getoutput(create_vg)
    if 'failed=0' not in output and 'unreachable=0' not in output:
        return output
    else:
        output = sb.getoutput(create_lv)
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



output = sb.getoutput(createlvm_partition(device,vgname,vgsize,lvname,lvsize,fs,path))

