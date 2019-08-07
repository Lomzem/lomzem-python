import pyperclip
import sys

if len(sys.argv) < 2:
	print('ERROR: Open this script with a file!')
else:
	input_file = sys.argv[1]
	pyperclip.copy(f'scp -r "{input_file}" root@10.0.0.200:/var/mobile/Documents/')