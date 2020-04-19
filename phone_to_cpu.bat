echo off
set output_dir=C:/Users/Lomzem/Desktop/
set /P input_path=Enter phone path: 
scp -r mobile@10.0.0.118:"'%input_path%'" "%output_dir%"
pause