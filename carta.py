#"🃏🛸🤬🤡🤖🤩🃏🃏🃏🃏"
guia = input ()
jugador1 = input()
jugador2 = input()
i=0
while(i<10):
  if(guia[i] == "🃏"):
    print("🛸", end="")
  else:
    if(jugador1[i] == "🃏" and jugador2[i] == "🃏"):
      print("🤩", end="")
    elif(jugador1[i] == "🃁" and jugador2[i] == "🃁" and guia[i] != "🃁"):
      print("🤬", end="")
    elif(jugador1[i]<=guia[i] and jugador2[i]<=guia[i]):
      print("🛸", end="")
    elif(jugador1[i] == jugador2[i]):
      print("🛸", end="")
    elif(jugador1[i]<jugador2[i]):
      print("🤡", end="")
    elif(jugador1[i]>jugador2[i]):
      print("🤖", end="")  
  i+=1