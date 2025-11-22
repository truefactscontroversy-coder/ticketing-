# start 
 station_board = ("board + your location")
 start_now = input ("start voucher ")

 while start_now == "":
  print("please select: start voucher")
  start_now = input ("start voucher ")
  if start_now == "start voucher":
   break 
 voucher = []
 
print("new page loading") 
# need to have a way to send code back to start
# add departure 
def printed_zones ():
  zones = ["Down town zone", "Mid town zone", "Central zone"]
  print(zones) 
printed_zones()
print("Please select a starting zone: ")

your_location = input()

select_zone = your_location

 while select_zone == "":
   printed_zones()
   print("Please select a zone") 
   select_zone = input()
   if select_zone != "":
    your_location = select_zone
    voucher.append (F"Departure zone: {your_location}")
    print("New page loading")
    break
   else: 
    voucher.append (F"Departure zone: {your_location}")
    print("New page loading")

# add destination  
# problems not sure if the calculations are correct
print("station board with all zones and stations")
printed_zones()
print("Please select a destinationn zone: ")
destination_zone = input()

 

 while destination_zone == "":
   printed_zones()
   print("Please select a zone") 
   destination_zone = input()
   if destination_zone != "" :
    break
   
 

if your_location == select_zone:
    zone_num = 1
    voucher.append (f"Destination zone: {destination_zone}")
    print("New page loading")
elif your_location == "Down town zone" and destination_zone == "Central zone":
    zone_num = 3
    voucher.append (f"Destination zone: {destination_zone}")
    print("New page loading")
elif your_location == "Central zone" and destination_zone == "Down town zone":
    zone_num = 3
    voucher.append (f"Destination zone: {destination_zone}")
    print("New page loading")
elif your_location == "Mid town zone" :
     zone_num = 2 
     voucher.append (f"Destination zone: {destination_zone}")
     print("New page loading")

     
# add destination station

down_town = ("Adohad, Brunad, Edert, Elyot, Erean, Holmer, Kelvia, Mareng, Perinad, Pryn, Ruril, Ryall, Zord")

mid_town = ("Agraile, Docia, Garon, Obelyn, Oloadus, Quthiel, Ralith, Riciva, Riladia, Sylas, Wicyt")

central = ("Centrala Frestin Jaund Lomil Ninia Rede Riciva Soth Sylyn Tallan")



if destination_zone == "Down town zone":
  print(f"List of stations for down town: {down_town}")
 elif destination_zone == "Mid town zone":
  print(f"List of stations for midtown: {mid_town}")
 elif destination_zone == "Central zone":
  print(f"List of stations for {central}")


print("Please select a station: ")
destination_station = input()

 while destination_station == "":
  print("please select a station")
  destination_station = input()
  if destination_station != "":
   print("New page loading")
   break

voucher.append (destination_station)
select_zone = destination_station

# add passenger 
# problems can't add user input to an already defined variable?
print("price page")
print("age selction and add buttons")


 
print("Adult: -1 - +1 or none")
 Adult = input()
 print("Child: -1 - +1 or none")
 Child = input()
 print("Student: -1 - +1 or none ")
 Student = input()
 print("Elderly: -1 - +1 or none")
 Elderly = input()

#passenger calculation
 # for adult there is something in the variable if there is a 0 nned to figure this out!!!
 if adult_num != 0:
  zone_num *= 21.05 
  adult_num *= zone_num
  voucher.append (f"total Adult cost: {adult_num}")
 elif adult_num == 0:
  voucher.append (f"total Adult cost: {0}")
 
 
 # for child
 if child_num != 0:
  zone_num *= 14.10
  child_num *= zone_num
  voucher.append (f"total Child cost: {child_num}")   
  
 elif child_num == 0 :
  voucher.append(f"total Child cost: {0}")


 # for student
 if student_num != 0:
  zone_num *= 17.50
  student_num *= zone_num
  voucher.append (f"total Student cost: {student_num}")
  
 elif student_num == 0:
  voucher.append(f"total Student cost: {0}")



 # For elderly 
 if elderly_num != 0:
  zone_num *= 10.25
  elderly_num *= zone_num
  voucher.append (f"total Elderly cost: {elderly_num}")
  
 elif elderly_num == 0 :
  voucher.append(f"total Elderly cost: {0}")


 print(voucher[3])

 total_cost = Adult + Child + Student + Elderly
 voucher.append (f"Total cost of trip: {total_cost}")

 total_passenger = Adult + Child + Student + Elderly
 voucher.append (f"Total number of passengers: {total_passenger}")

 # if none have been selected
 while total_passenger == 0:
   print("please add passenger") 
   if select_zone != "" :
    print("New page loading")
    break

 # voucher print
 
print(voucher)
 
#passenger calculation
 # for adult there is something in the variable if there is a 0 nned to figure this out!!!
 if adult_num != 0:
  zone_num *= 21.05 
  adult_num *= zone_num
  voucher.append (f"total Adult cost: {adult_num}")
 elif adult_num == 0:
  voucher.append (f"total Adult cost: {0}")
 
 
 # for child
 if child_num != 0:
  zone_num *= 14.10
  child_num *= zone_num
  voucher.append (f"total Child cost: {child_num}")   
  
 elif child_num == 0 :
  voucher.append(f"total Child cost: {0}")


 # for student
 if student_num != 0:
  zone_num *= 17.50
  student_num *= zone_num
  voucher.append (f"total Student cost: {student_num}")
  
 elif student_num == 0:
  voucher.append(f"total Student cost: {0}")



 # For elderly 
 if elderly_num != 0:
  zone_num *= 10.25
  elderly_num *= zone_num
  voucher.append (f"total Elderly cost: {elderly_num}")
  
 elif elderly_num == 0 :
  voucher.append(f"total Elderly cost: {0}")


 print(voucher[3])

 total_cost = Adult + Child + Student + Elderly
 voucher.append (f"Total cost of trip: {total_cost}")

 total_passenger = Adult + Child + Student + Elderly
 voucher.append (f"Total number of passengers: {total_passenger}")

 # if none have been selected
 while total_passenger == 0:
   print("please add passenger") 
   if select_zone != "" :
    print("New page loading")
    break

 # voucher print
 

 print(voucher)
 
# restart or end 
 restart_end = input("Please select start a new voucher by selecting restart or end processs by selecting end process")
 while restart_end == "":
   restart_end = input("Please select start a new voucher or end processs")
 if restart_end == "end process":
  print("new page loading")
 elif restart_end == "restart": 
  ticketing_system()
 
