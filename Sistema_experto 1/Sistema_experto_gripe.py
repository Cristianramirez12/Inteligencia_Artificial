#Cristian Ramirez
def sistema_experto_1():
  Start = int(input("Desea utilizar el sistema experto? SI = 0 NO = 1:  "))
  sintomas_gripa = ["friebre","tos","malestar"]
  sintomas_covid_19 = ["dolor_garganta","malestar","falta_de_gusto","fiebre","dolor_de_espalda"]
  covid_19=0
  gripa=0
  while(Start == 0):
    a = input("¿Usted que sintomatologia tiene?: ")
    if(a in sintomas_gripa and a in sintomas_covid_19):
      gripa +=1
      covid_19 +=1 
    elif(a in sintomas_covid_19):
      covid_19 +=1
    elif(a in sintomas_gripa):
      gripa +=1
    else:
      print("no escribio ninguno de los sintomas permitidos: ")
    Start = int(input("Desea utilizar de nuevo el sistema experto? SI = 0 NO = 1: ")) 

  if(gripa > covid_19):
    print("Usted tiene gripa por favor aislese...  ")
  elif(covid_19 > gripa):
    print("Usted tiene covid_19 por favor aislese lo mas pronto posible...")  
  else:
    print("no se ha podido identificar el sintoma...")

sistema_experto_1()
