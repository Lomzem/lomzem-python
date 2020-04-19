echo off
set input_file=%~dpnx1
set output_dir=/var/mobile/Documents/docbyr/
scp -r "%input_file%" mobile@10.0.0.118:"'%output_dir%'"
pause