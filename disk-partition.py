#!/usr/bin/python36

print("content-type: text/html")
print()

import subprocess as sp

a = (sp.getoutput("sudo fdisk -l"))
a = a.split("\n")
a = a[1:]




print("""
<form action=http://192.168.43.207/cgi-bin/partition.py>
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
<td>Enter size of partition (with size GiB/MiB/KiB) </td>
<td> <input type=text name=size /></td>
</tr>


<tr>
<td>Enter format (Initial Directory '/')  </td>
<td> <input type=text name=fs /></td>
</tr>

<tr>
<td>Enter Mounted Point   </td>
<td> <input type=text name=path /></td>
</tr>

</table>
<input type=submit />
""")

