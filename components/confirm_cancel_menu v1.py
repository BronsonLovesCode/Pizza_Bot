print ("*** Please confirm your order. ***")
print ("*** To confirm order, enter 1. ***")
print ("*** To cancel order, enter 2. ***")

while True:
      try:
            confirm = int(input("*** Please enter a number. *** "))
            if confirm >= 1 and confirm <= 2:
                  if confirm == 1:
                        print ("Order confirmed")
                        break

                  elif confirm == 2:
                        print ("Order cancelled")
                        break
            else:
                  print ("*** The number must be 1 or 2. *** ")
      except ValueError:
            print ("*** That was not a valid input... *** ")
            print ("*** Please enter 1 or 2. *** ")