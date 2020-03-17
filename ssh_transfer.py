import os
import sys
import time
import paramiko

# input_file = 'C:\\Users\\Lomzem\\Desktop\\Literature.pdf'
input_file = sys.argv[1]
input_file = os.path.basename(input_file)
output_dir = '/var/mobile/Documents/docbyr/'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('10.0.0.118', username='root',password='Elephant13')

ftp_client=ssh_client.open_sftp()

if os.path.isfile(input_file):
	ftp_client.put(input_file, os.path.join(output_dir, os.path.basename(input_file)))

elif os.path.isdir(input_file):
	path_len = (len(input_file))-(len(os.path.basename(input_file)))
	print('Starting...')
	for dirpath, dirs, files in os.walk(input_file):
		needed_dir = os.path.join(output_dir, dirpath).replace('\\', '/')
		try:
			ftp_client.mkdir(needed_dir)
		except IOError:
			pass
		for file in files:
			filepath = os.path.join(dirpath, file)
			fileoutpath = filepath[path_len:].replace('\\', '/')
			ftp_client.put(filepath, os.path.join(output_dir, fileoutpath))