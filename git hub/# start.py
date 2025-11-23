def ticketing_system():
 # start of start unit
 # message to user
 print("Welcome to the ticketing " 
      "system please select: start voucher")
 start_now = input ()
 #error loop if user does not input correct code
 while start_now != "start voucher":
  print("please select: start voucher")
  start_now = input ()
  if start_now == "start voucher":
   break 
 # voucher list for travel details
 voucher = []
 voucher.append ("date / time")
 zone_counter = []
 print("new page loading") 
 # need to have a way to send code back to start: fixed
 # end of start unit

 # start of add departure unit 
 # function to repeatedly print zones
 def printed_zones ():
  zones = ["Down town zone", "Mid town zone", "Central zone"]
  print(zones) 

 printed_zones()
 #initial user input for departure zone
 print("Please select a starting zone: ") 
 your_location = input()
 
 #error handling function for departure zone
 def zone_check():
  location = input()
  while (location != "Down town zone" or 
         location != "Mid town zone" or 
         location != "Central zone"):
      if (location == "Down town zone" or 
          location == "Mid town zone" or 
          location == "Central zone"):
       voucher.append (F"Departure zone: {location}")
       print("new page loading") 
       zone_counter.append(location)
       break
      else:
       printed_zones()
       print("Please select a vaild zone") 
       location = input()
       
  

 # error handling statment for initial departure zone input
 
 if (your_location == "Down town zone" or 
     your_location == "Mid town zone" or 
     your_location == "Central zone"):
  voucher.append (F"Departure zone: {your_location}")
  zone_counter.append (your_location)
  print("new page loading") 
 else: 
    printed_zones()
    print("Please select a vaild zone") 
    zone_check()
 # end of add departure unit


 # start of add destination unit
 # problems not sure if the calculations are correct: fixed 

 # initial user input for destination zone
 print("station board with all zones and stations")
 printed_zones()
 print("Please select a destinationn zone: ")


 destination_zone = input()
 # error handling function for destination zone
 def destination_zone_check():
    current_or_desired_location = input()
    while (current_or_desired_location != "Down town zone" or 
           current_or_desired_location != "Mid town zone" or 
           current_or_desired_location != "Central zone"):
      if (current_or_desired_location == "Down town zone" or 
          current_or_desired_location == "Mid town zone" or 
          current_or_desired_location == "Central zone"):
        voucher.append (F"Destination zone: {current_or_desired_location}")
        zone_counter.append(current_or_desired_location)
        break
      else:
       printed_zones()
       print("Please select a vaild zone") 
       current_or_desired_location = input()
      
 # error handling statment for initial destination zone input
 
 if (destination_zone == "Down town zone" or 
     destination_zone == "Mid town zone" or 
     destination_zone == "Central zone"):
     voucher.append (F"Destination zone: {destination_zone}")
     print("new page loading") 
     zone_counter.append(destination_zone)
 else:
     printed_zones()
     print("Please select a vaild zone") 
     destination_zone_check()
 
  # calculation of zones traveled through    
 
 your_location = zone_counter[0]
 destination_zone = zone_counter[1]

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


 # station lists for each zone
 DOWN_TOWN = (
   "Adohad, Brunad, Edert, Elyot, Erean," 
   "Holmer, Kelvia, Mareng, Perinad, Pryn, Ruril, Ryall, Zord"
   )

 MID_TOWN = (
   "Agraile, Docia, Garon, Obelyn, Oloadus,"
   "Quthiel, Ralith, Riciva, Riladia, Sylas, Wicyt"
   )

 CENTRAL = (
   "Centrala, Frestin, Jaund, Lomil,"
   "Ninia, Rede, Riciva, Soth, Sylyn, Tallan"
   )

 # display station list based on destination zone

 if destination_zone == "Down town zone":
  print(f"List of stations for down town: {DOWN_TOWN}")
 elif destination_zone == "Mid town zone":
  print(f"List of stations for midtown: {MID_TOWN}")
 elif destination_zone == "Central zone":
  print(f"List of stations for {CENTRAL}")

 # user input for destination station
 print("Please select a station: ")
 destination_station = input()

 while destination_station == "":
  print("please select a station")
  destination_station = input()
  if destination_station != "":
   voucher.append (f"destination station: {destination_station}")
   print("New page loading")
   break


 

 # start of add passenger unit
 # problems can't add user input to an already defined variable?: fixed 
 # initial message to user
 print("price page")
 print("catagory selction and add buttons")


 # user input for passenger catagory
 print("Adult: -1 - +1 or none")
 Adult = input()
 print("Child: -1 - +1 or none")
 Child = input()
 print("Student: -1 - +1 or none ")
 Student = input()
 print("Elderly: -1 - +1 or none")
 Elderly = input()
 # conversion of user input to integers
 adult_num = Adult = int(Adult)
 child_num = Child = int(Child)
 student_num = Student = int(Student)
 elderly_num = Elderly = int(Elderly)

 # end of add passenger unit
 
 # start of passenger calculation unit 
 # for adult (there is something in the variable if there is a 
 # 0 need to figure this out!!!: fixed) 

 # for adult
 if adult_num != 0:
  adult_num *= 21.05 
  adult_num *= zone_num
  voucher.append (f"total Adult cost: {adult_num}")
 elif adult_num == 0:
  voucher.append (f"total Adult cost: {0}")
 
 
 # for child
 if child_num != 0:
  child_num *= 14.10
  child_num *= zone_num
  voucher.append (f"total Child cost: {child_num}")   
 elif child_num == 0 :
  voucher.append(f"total Child cost: {0}")


 # for student
 if student_num != 0:
  student_num *= 17.50
  student_num *= zone_num
  voucher.append (f"total Student cost: {student_num}")
 elif student_num == 0:
  voucher.append(f"total Student cost: {0}")



 # For elderly 
 if elderly_num != 0:
  elderly_num *= 10.25
  elderly_num *= zone_num
  voucher.append (f"total Elderly cost: {elderly_num}")
 elif elderly_num == 0 :
  voucher.append(f"total Elderly cost: {0}")


 

 total_cost = adult_num + child_num + student_num + elderly_num
 voucher.append (f"Total cost of trip: {total_cost}")

 total_passenger = Adult + Child + Student + Elderly
 voucher.append (f"Total number of passengers: {total_passenger}")
 # end of passenger calculation unit
 
 
 # error handling for passenger calculation unit: added 
 while total_passenger == 0:
   print("please add passenger") 
   if total_passenger != 0 :
    print("New page loading")
    break

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
 print(
   "Type 'start a new voucher' to start a new voucher "
   "or 'end process' to end voucher process")
 restart_end = input()
 
 
 # function for error handling of restart or end input
 def restart_or_end():
   restart_end = input()
   while (restart_end != "start a new voucher" or 
          restart_end != "end process"):
      if (restart_end == "start a new voucher" or 
          restart_end == "end process"):
       print("Please select: 'start a new voucher' or 'end process'")
       restart_end = input()
       break
      
 restart_or_end()
 # restart or end statment
 if restart_end == "end process":
       print("new page loading")
 elif restart_end == "start a new voucher": 
   ticketing_system()
 

ticketing_system()
# end of project