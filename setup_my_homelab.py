import os

os.system("chmod +x /usr/bin/apt*")
os.system("apt update")
os.system("systemctl enable ntp")
os.system("systemctl start ntp")
os.system("systemctl enable ssh")
os.system("systemctl start ssh")