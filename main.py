#importing modules
import os
import crypt
import secrets
import getpass

# First step codes
first_codes = ("""
username = input ("Enter a username: ")

# Choose a random password length between 14 and 20
password_length = secrets.choice(range(14, 21))
password = (secrets.token_urlsafe(password_length))

# Adding a linux user
encPass = crypt.crypt(password,"22")
os.system("useradd -p "+encPass+ f" {username}")

# Disabling QEMU
os.system("sudo apt-get remove --auto-remove qemu-guest-agent -y")

# Disabling the root account
os.system("sudo passwd -l root")

# Disabling the getty service (Read docs.txt for further information)
os.system("sudo systemctl disable getty@.service")

# Saving the data
with open('privatevm.txt', 'w') as f:
    f.write('1')

# printing username and password
os.system("clear")
print (f"Username: {username}")
print (f"Password: {password}")

# Performing a system reboot
os.system("Reboot")
""")

try:
    with open('privatevm.txt') as f:
        data = f.read()
    if data == ("0"):
        exec(first_codes)
    else:
        current_user = getpass.getuser()
        os.system(f"sudo passwd {current_user}")
except:
    exec (first_codes)