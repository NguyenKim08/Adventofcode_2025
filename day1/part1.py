nb_0 = 0 #counter de 0
x = 50 #position initial
with open("file.txt","r") as file : #please enter the file where you stock your input
  for line in file:
    line = line.strip()#clear the unwanted spaces or etc
    if not line:
      continue
      
      lettre = line[0] #index 0 est l'apparition de lettre car le format est de R/L avec nombre
      nombre = line([1:]) #le reste
      
      if lettre == "R":
        x = (x + nombre) % 100 
      elif lettre == "L":
        x = (x - nombre) % 100
      else:
        continue
        
        if x == 0:
          nb_0 += 1
        print(nb_0)
      
