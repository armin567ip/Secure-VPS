#importing modules

import os
import crypt


password ="armin567id" 
encPass = crypt.crypt(password,"22")
print (str(encPass))
#os.system("useradd -p "+encPass+" johnsmith")
