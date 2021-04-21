import pickle
import os
import secrets
from random import randint
from time import sleep

loaded={}
passwords={}
global remembero
global ask_token

def save(data,file_name,wm):
  pickle.dump(data,open(file_name,wm))


def load(file_name, rm):
  pickle.load(open(file_name, rm))

def newacc():
  global a
  a=secrets.token_hex(16)
  
  print("From now on you have to register with this token: " + a)


def register_psw(media,psw):
  global loaded
  loaded=pickle.load(open("passwords.dat", "rb"))
  loaded[media]=psw


def store_psw():
  mediaa=input("I need this psw for... ")
  ask_psw=input("Ingresa contraseña: ")
  print("Ok, saving data...")
  sleep(1.5)
  register_psw(mediaa,ask_psw)
  save(loaded, "passwords.dat", "wb")
  
  print("Data saved")
  print("Returning to menu...")
  sleep(2)
  main()

def generate_psw(length):
  choice=randint(0,10)

  if choice <= 5:
    new_psw=secrets.token_urlsafe(length)
    ask_media=input("I need this psw for... (Ex. Fcebook): ")
    ask=input("Is " + new_psw + " ok for your media(Y/N)? ")

    if ask=="Y" or ask=="y":
      print("Ok, saving data...")
      sleep(1.5)
      register_psw(ask_media,new_psw)
      save(loaded,"passwords.dat", "wb")
      
      print("Data saved")
      print("Returning to menu...")
      sleep(2)
      main()

    if ask=="N" or ask=="n":
      
      print("Wait while we return to the psw generator...")
      sleep(1)
      
      ask_length=int(input("Type password length: "))
      generate_psw(ask_length)


  elif choice <= 10:
    new_psw=secrets.token_hex(length)
    ask_media=input("I need this psw for... (Ex. Fcebook): ")
    ask=input("Is " + new_psw + " ok for your media(Y/N)? ")

    if ask=="Y" or ask=="y":
      print("Ok, saving data...")
      sleep(1.5)
      register_psw(ask_media,new_psw)
      save(loaded,"passwords.dat", "wb")
      
      print("Data saved")
      print("Returning to menu...")
      sleep(2)
      main()


    if ask=="N" or ask=="n":
      
      print("Wait while we return to the psw generator...")
      sleep(1)
      
      ask_length=int(input("Type password length: "))
      generate_psw(ask_length)


def login(what,token):
  secure_log=pickle.load(open("log.dat", "rb"))
  if what==secure_log:

    
    print("Welcome back...\n")
    l=input("\n\n1._Generate and store passwords\n2._Store passwords\n3._Show all passwords\n4._Search password\n5._Delete Passwords\n6._Log out\n7._Remember me[BETA]\n\nType option: ")
    if l=="1":
      po=input("Type the password length: ")
      generate_psw(int(po))

    if l=="2":
      store_psw()

    if l=="3":
      print("Loading data...")
      sleep(1.5)
      
      loaded=pickle.load(open("passwords.dat", "rb"))
      print(loaded)
      c=input("Press enter to return to the Menu...")
      main()

    if l=="4":
      
      search=input("Type EXACTLY the social media: ")
      passwords_loaded=pickle.load(open("passwords.dat", "rb"))
      print(passwords_loaded[search])
      c=input("Press enter to return to the Menu...")
      main()

    if l=="5":
      ask_delete=input("Write the social media you want to delete: ")
      loaded=pickle.load(open("passwords.dat", "rb"))
      loaded.pop(ask_delete, None)
      save(loaded, "passwords.dat", "wb")
      print("Sucesfully deleted")
      sleep(1.5)
      main()

    if l=="6":
      try:
        os.remove("Remember.dat")
      except:
        pass
      print("Login out, DON'T LOSS YOUR TOKEN")
      sleep(1.5)
      main()

    if l=="7":
      pickle.dump(ask_token,open("Remember.dat", "wb"))
      print("Succesful!")
      sleep(1)
      print("Returning to menu")
      sleep(1)
      main()

    else:
      print("Returning to menu...")
      sleep(2)
      main()
      

  else:
    print("Wrong token")
    sleep(1)
    main()

def main():

  try:
    remembero=pickle.load(open("Remember.dat", "rb"))
    realpsw=pickle.load(open("log.dat", "rb"))
    if remembero==realpsw:
      login(remembero,remembero)

  except:
    pass

  try:
    global ask_token
    login(ask_token, ask_token)
  except:
    pass

  
  print("Welcome to the password storer and generator")
  d=input("Login or register? (L/R) ")
  if d=="R" or d=="r":
    s=input("Are you sure, registering again will loss all the data of your back sessions (Y/N) ")
    if s=="Y" or s=="y":
      pickle.dump(passwords,open("passwords.dat", "wb"))
      newacc()
      print("\n\nSaving data...")
      save(a,"log.dat","wb")
      print("\nData saved")
      c=input("Press enter to return to the menu...")
      if c=="":
        main()
  if d=="L" or d=="l":
    ask_token=input("Write your token: ")
    login(ask_token,ask_token)

        





main()