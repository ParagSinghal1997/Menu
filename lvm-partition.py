#!/usr/bin/python36

print("content-type: text/html")
print()

import subprocess as sp

a = (sp.getoutput("sudo fdisk -l"))
a = a.split("\n")
a = a[1:]




print("""
<form action=http://192.168.43.207/cgi-bin/lvmpartition.py>
<table>
<tr>
<td>Select device name </td>
<td><select name=device>
""")

for token in a:
	b = token.split()
	for part in b:
		if part.startswith("/dev/s"):
			part = part.split(":")
			print("<option>{}</option>".format(part[0]))
print("</td></tr></select>")

print("""


<tr>
<td>Enter format (Initial Directory '/')  </td>
<td> <input type=text name=fs /></td>
</tr>

<tr>
<td>Enter Mounted Point   </td>
<td> <input type=text name=path /></td>
</tr>

<tr>
<td>Enter Name Of Vg   </td>
<td> <input type=text name=vg_name /></td>
</tr>


<tr>
<td>Enter PE extent size of VG (default in MiB)  </td>
<td> <input type=text name=vg_size /></td>
</tr>



<tr>
<td>Enter name of LVM   </td>
<td> <input type=text name=lv_name /></td>
</tr>




<tr>
<td>Enter size of lvm   </td>
<td> <input type=text name=lv_size /></td>
</tr>

</table>
<input type=submit />
""")

