#"ππΈπ€¬π€‘π€π€©ππππ"
guia = input ()
jugador1 = input()
jugador2 = input()
i=0
while(i<10):
  if(guia[i] == "π"):
    print("πΈ", end="")
  else:
    if(jugador1[i] == "π" and jugador2[i] == "π"):
      print("π€©", end="")
    elif(jugador1[i] == "π" and jugador2[i] == "π" and guia[i] != "π"):
      print("π€¬", end="")
    elif(jugador1[i]<=guia[i] and jugador2[i]<=guia[i]):
      print("πΈ", end="")
    elif(jugador1[i] == jugador2[i]):
      print("πΈ", end="")
    elif(jugador1[i]<jugador2[i]):
      print("π€‘", end="")
    elif(jugador1[i]>jugador2[i]):
      print("π€", end="")  
  i+=1