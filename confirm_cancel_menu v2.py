print ("*** Please confirm your order. ***")
print ("*** To confirm order, enter 1. ***")
print ("*** To cancel order, enter 2. ***")

while True:
      try:
            confirm = int(input("*** Please enter a number. *** "))
            if confirm >= 1 and confirm <= 2:
                  if confirm == 1:
                        print ()
                        print ("*** Order confirmed ***")
                        print ()
                        print ("Your order has been sent to our kitchen to be prepared,")
                        print ("your pizza will be with you shortly!")
                        print ()
                        break

                  elif confirm == 2:
                        print ()
                        print ("*** Order cancelled ***")
                        print ()
                        print ("You can restart your order or exit the BOT.")
                        print ()
                        break
            else:
                  print ("*** The number must be 1 or 2. *** ")
      except ValueError:
            print ("*** That was not a valid input... *** ")
            print ("*** Please enter 1 or 2. *** ")