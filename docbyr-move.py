import pyperclip
import subprocess
import sys

if len(sys.argv) < 2:
	print('ERROR: Open this script with a file!')
else:
	input_file = sys.argv[1]
	pyperclip.copy(f'scp -r "{input_file}" root@10.0.0.118:/docbyr/ && exit')
	subprocess.Popen(['C:/Program Files/Git/git-cmd.exe'])