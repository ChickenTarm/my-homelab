import os

sshd_config_path = "/etc/ssh/sshd_config"

with open(sshd_config_path, "r") as f:
    sshd_config_contents = [line.split() for line in f.readlines()]

for line_number in range(0, len(sshd_config_contents)):
    if len(sshd_config_contents[line_number]) > 0:
        # Allows VSCode to ssh into TrueNAS
        if sshd_config_contents[line_number][0] == "AllowTcpForwarding":
            sshd_config_contents[line_number][1] = "yes"
        sshd_config_contents[line_number] = " ".join(sshd_config_contents[line_number])
    else:
        sshd_config_contents[line_number] = ""

with open(sshd_config_path, "w") as f:
    f.write("\n".join(sshd_config_contents))

# os.system("chmod +x /usr/bin/apt*")
# os.system("apt update")
# os.system("systemctl enable ntp")
# os.system("systemctl start ntp")
# os.system("systemctl enable ssh")
# os.system("systemctl start ssh")