##Using NoxPlayer emulator
##!!Run under 1280*720 emulator resolution!!
import actions as ac
import datetime, time

##Constans
dashs = "-------------------------------------------------"

##The simply GUI
print("+++++Wellcome to Clash-Of-Clans-Auto-Player!+++++")
print("--------------", datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"), "--------------")
while True:
    print(dashs,"\n"
          "1:Collect Resource\n"
          "0:Exit")
    option = int(input("Chose an opction by input an number:"))
    print(dashs)
    if option == 0:
        print("Exiting...")
        time.sleep(1)
        break
    elif option == 1:
        print("Collecting resouces...")
        status = ac.collectResources()
        if(status[0]):
            print("Elixirs collect")
        elif(not status[0]):
            print("Can't found elixirs!")
        if (status[1]):
            print("Golds collect!")
        elif (not status[1]):
            print("Can't found golds!")
    else:
        print("Please re-enter your option.")




