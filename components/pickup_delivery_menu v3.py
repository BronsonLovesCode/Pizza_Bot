# Menu so that users can choose either pickup or delivery

# Bug - Need to make it so that it only accepts 1 or 2

print ("*** Is your order for pickup or delivery? ***")

print ("*** For delivery, enter 1. ***")
print ("*** For pickup, enter 2. ***")

while True:
      try:
            delivery = int(input("*** Please enter a number. *** "))
            if delivery >= 1 and delivery <= 2:
                  if delivery == 1:
                        print ("Delivery")
                        break

                  elif delivery == 2:
                        print ("Pickup")
                        break
            else:
                  print ("*** The number must be 1 or 2. *** ")
      except ValueError:
            print ("*** That was not a valid input... *** ")
            print ("*** Please enter 1 or 2. *** ")
          