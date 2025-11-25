def ticketing_system():
 # start of start unit
 # message to user
 print("Welcome to the ticketing " 
      "system please select: start voucher")
 start_now = input ()

 #error loop if user does not input correct code
 def start_voucher_check():
  print("please select: start voucher")
  start_now = input ()
  if start_now == "start voucher":
   return 0
  else:
    start_voucher_check()
 
 if start_now != "start voucher":
  start_voucher_check()

 # voucher list for travel details
 voucher = []
 voucher.append ("date / time")
 print("New page loading") 
 # need to have a way to send code back to start: fixed
 # end of start unit

 # start of add departure unit 
 # function to repeatedly print zones
 def printed_zones ():
  zones = ["Down town zone", "Mid town zone", "Central zone"]
  print(zones) 


 #initial user input for departure zone

 printed_zones()
 print("Please select a starting zone: ") 
 your_location = input()
 
 #error handling function for departure zone
 def zone_check():
   printed_zones()
   print("Please select a vaild zone") 
   location = input()
   if (location == "Down town zone" or 
       location == "Mid town zone" or 
       location == "Central zone"): 
       return location
   else:
      zone_check()
 
       
       
 

 # error handling statment for initial departure zone input
 
 if (your_location == "Down town zone" or 
     your_location == "Mid town zone" or 
     your_location == "Central zone"):
  voucher.append (F"Departure zone: {your_location}")
  print("new page loading") 
 else: 
    your_location = zone_check()
    voucher.append (F"Departure zone: {your_location}")
    print("New page loading")

 # end of add departure unit


 # start of add destination unit
 # problems not sure if the calculations are correct: fixed 

 # station lists for each zone
 DOWN_TOWN = (
   "Adohad, Brunad, Edert, Elyot, Erean, " 
   "Holmer, Kelvia, Mareng, Perinad, Pryn, Ruril, Ryall, Zord"
   )

 MID_TOWN = (
   "Agraile, Docia, Garon, Obelyn, Oloadus, "
   "Quthiel, Ralith, Riciva, Riladia, Sylas, Wicyt"
   )

 CENTRAL = (
   "Centrala, Frestin, Jaund, Lomil, "
   "Ninia, Rede, Riciva, Soth, Sylyn, Tallan"
   )

 # initial user input for destination zone
 print("station board with all zones and stations")
 print(f"Down town zone stations: {DOWN_TOWN}")
 print(f"Mid town zone stations: {MID_TOWN}")
 print(f"Central zone stations: {CENTRAL}")
 printed_zones()
 print("Please select a destinationn zone: ")


 destination_zone = input()
 # error handling function for destination zone
 
      
 # error handling statment for initial destination zone input
 
 if (destination_zone == "Down town zone" or 
     destination_zone == "Mid town zone" or 
     destination_zone == "Central zone"):
     voucher.append (F"Destination zone: {destination_zone}") 
 else:
     destination_zone = zone_check()
     voucher.append (F"Destination zone: {destination_zone}")
 
  # calculation of zones traveled through    
 
 

 if your_location == destination_zone:
       zone_num = 1
       print("New page loading")
 elif (your_location == "Down town zone" and 
       destination_zone == "Central zone"):
       zone_num = 3
       print("New page loading")
 elif (your_location == "Central zone" and 
       destination_zone == "Down town zone"):
       zone_num = 3
       print("New page loading")
 elif your_location == "Mid town zone" :
       zone_num = 2 
       print("New page loading")
 
 #end of add destination unit
     
 # start of add destination station unit



 # display station list based on destination zone 


 #error handling system for if downtown is selected
 if destination_zone == "Down town zone":
  print(f"List of stations for down town: {DOWN_TOWN}")
  print("Please select a station: ")
  destination_station = input()
  if destination_station in DOWN_TOWN:
    voucher.append (f"destination station: {destination_station}")
    print("New page loading")
  else:
    print("please select a station")
    destination_station = input()
    while (destination_station != DOWN_TOWN for destination_station in DOWN_TOWN):  
      if destination_station in DOWN_TOWN:
        voucher.append (f"destination station: {destination_station}")
        print("New page loading")
        break
      else:
         print("Please select a station: ")
         destination_station = input()
  

 # error handling system for if mid town is selected
 if destination_zone == "Mid town zone":
  print(f"List of stations for midtown: {MID_TOWN}")
  print("Please select a station: ")
  destination_station = input()
  if destination_station in MID_TOWN:
    voucher.append (f"destination station: {destination_station}")
    print("New page loading")
  else:
    print("please select a station")
    destination_station = input()
    while (destination_station != MID_TOWN for destination_station in MID_TOWN):  
      if destination_station in MID_TOWN:
        voucher.append (f"destination station: {destination_station}")
        print("New page loading")
        break
      else:
         print("Please select a station: ")
         destination_station = input()

 # error handling for if central is selected
 if destination_zone == "Central zone":
  print(f"List of stations for {CENTRAL}")
  print("Please select a station: ")
  destination_station = input()
  if destination_station in CENTRAL:
    voucher.append (f"destination station: {destination_station}")
    print("New page loading")
  else:
    print("please select a station")
    destination_station = input()
    while (destination_station != CENTRAL for destination_station in CENTRAL):  
      if destination_station in CENTRAL:
        voucher.append (f"destination station: {destination_station}")
        print("New page loading")
        break
      else:
         print("Please select a station: ")
         destination_station = input()

 


 

 # start of add passenger unit
 # problems can't add user input to an already defined variable?: fixed 
 # initial message to user
 print("cost of one zone is automatically added to total cost")
 print ("cost will double for two zones and triple for three zones")
 print("catagory selction and add buttons")
 
 print("price page")
 print("Adult: $21.05 per zone")
 print("Child: $14.10 per zone")
 print("Student: $17.50 per zone")
 print("Elderly: $10.25 per zone")


 # user input for passenger catagory
 def passenger_catagory_adult():
  print("Adult : -1 - +1 ")
  Adult = int(input())
  return Adult
 def passenger_catagory_child():
  print("Child: -1 - +1 ")
  Child = int(input())
  return Child
 def passenger_catagory_student():
   print("Student: -1 - +1 ")
   Student = int(input())
   return Student
 def passenger_catagory_elderly():
   print("Elderly: -1 - +1 ")
   Elderly = int(input())
   return Elderly
  
 Adult = passenger_catagory_adult()
 Child = passenger_catagory_child()
 Student = passenger_catagory_student()
 Elderly = passenger_catagory_elderly()
 total_passenger = Adult + Child + Student + Elderly

 if (total_passenger != 0): 
  print("New page loading")
  voucher.append (f"Total number of passengers: {total_passenger}")
 while total_passenger == 0:
  print("please add at least one passenger")
  Adult = passenger_catagory_adult()
  Child = passenger_catagory_child()
  Student = passenger_catagory_student()
  Elderly = passenger_catagory_elderly()
  total_passenger = Adult + Child + Student + Elderly
 if (total_passenger != 0): 
  print("New page loading")
  voucher.append (f"Total number of passengers: {total_passenger}")
 

 # end of add passenger unit
 
 # start of passenger calculation unit 
 # for adult (there is something in the variable if there is a 
 # 0 need to figure this out!!!: fixed) 

 # for adult
 if Adult != 0:
  Adult *= 21.05 
  Adult *= zone_num
  voucher.append (f"Total Adult cost: {Adult}")
 elif Adult == 0:
  voucher.append (f"Total Adult cost: {0}")
 
 
 # for child
 if Child != 0:
  Child *= 14.10
  Child *= zone_num
  voucher.append (f"Total Child cost: {Child}")   
 elif Child == 0 :
  voucher.append(f"Total Child cost: {0}")


 # for student
 if Student != 0:
  Student *= 17.50
  Student *= zone_num
  voucher.append (f"Total Student cost: {Student}")
 elif Student == 0:
  voucher.append(f"Total Student cost: {0}")



 # For elderly 
 if Elderly != 0:
  Elderly *= 10.25
  Elderly *= zone_num
  voucher.append (f"Total Elderly cost: {Elderly}")
 elif Elderly == 0 :
  voucher.append(f"Total Elderly cost: {0}")


 total_cost = Adult + Child + Student + Elderly
 voucher.append (f"Total cost of trip: {total_cost}")

 
 # end of passenger calculation unit
 # error handling for passenger calculation unit: added 
 

 # start of voucher print unit
 # subtraction of zone to comply with required output
 if zone_num == 1:
   voucher.append ("Zones traveled through: None")
 elif zone_num != 1: 
    zone_num -= 1 
    voucher.append (f"Zones traveled through: {zone_num}")

 print(voucher)
 
 # end of voucher print unit
 
 # start of restart or end unit
 
 # function for error handling of restart or end input
 def restart_or_end():
   print("Please select: 'start a new voucher' or 'end process'")
   restart_end = input()
   if (restart_end == "start a new voucher" or 
          restart_end == "end process"):
       return restart_end
   else:
        restart_or_end()
       

 print(
   "Type 'start a new voucher' to start a new voucher "
   "or 'end process' to end voucher process")
 restart_end = restart_or_end()
 print(restart_end)
 if restart_end == "end process":
       print("new page loading")
 elif restart_end == "start a new voucher": 
   ticketing_system()

   
 

ticketing_system()
# end of project