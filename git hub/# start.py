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

  
 
