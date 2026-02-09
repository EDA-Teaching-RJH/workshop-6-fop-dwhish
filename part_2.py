# part 2.1

rover_status= {"Battery": 100,"Heater":"off","camera":"standby"}
print(rover_status["Battery"])


# part 2.2
rover_status["Battery"]= 85
rover_status["Heater"]= "on"
rover_status["speed"]= 5
print(rover_status)


# part 2.3

mission_log= [{"site":"crater A","Radiation":"low","Water":False},{"site":"Dune B","Radiation":"High","Water":True}]
print(mission_log[0],["site"])
