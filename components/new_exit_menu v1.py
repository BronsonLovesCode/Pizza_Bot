print ("*** Do you wish to start another order or exit? ***")
print ("*** To start another order, enter 1. ***")
print ("*** To exit the BOT, enter 2. ***")

while True:
      try:
            confirm = int(input("*** Please enter a number. *** "))
            if confirm >= 1 and confirm <= 2:
                  if confirm == 1:
                        print ("*** New Order ***")
                        break

                  elif confirm == 2:
                        print ("*** Exiting BOT ***")
                        break
            else:
                  print ("*** The number must be 1 or 2. *** ")
      except ValueError:
            print ("*** That was not a valid input... *** ")
            print ("*** Please enter 1 or 2. *** ")