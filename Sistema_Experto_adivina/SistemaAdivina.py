import pymysql
    
print('Cristian Ramirez')


def sistema_experto(NombreUsuario):
  usuario = []
  usuario.append(NombreUsuario)
  a = input("No se nada dime en que piensas ")
  usuario.append(a)
  b = input('Que lo caracteriza: ')
  usuario.append(b)
  #print(usuario)
  Insertar(conexion,usuario)
  Start = int(input("¿Jugamos de nuevo? SI = 0 NO = 1:  "))
  

  
  while(Start == 0):
    print("¿estas pensando en ?  ",usuario[1])
    Pregunta_1 = int(input( "SI = 0 NO = 1:  "))
    while(Pregunta_1 == 0):
        print("¿Su caracteristica es?  ",usuario[2])
        Pregunta_2 = int(input( "SI = 0 NO = 1:  "))
        print('te gane ajaajajajajaj :)  ')
        break
    print('Gracias Por jugar  ')
    break

def SistemaExperto(NombreUsuario):
    Informacion = mostrar(conexion)
    lista=[]
    for usuario in Informacion:
        if (usuario[0] == NombreUsuario ):
            lista.append([usuario[1],usuario[2]])
            print ("¿estas pensando en ?",lista[0][0])
            Pregunta_1 = int(input( "SI = 0 NO = 1:  "))
            while(Pregunta_1 == 0):
                print("¿estas pensando en ?",lista[0][1])
                Pregunta_2 = int(input( "SI = 0 NO = 1:  "))
                if (Pregunta_2 == 0):
                    print('te gane ajaajajajajaj :)  ')
                    break
                if (Pregunta_2 == 1):
                    print('lastima  ')
                    break
                else:
                    print ("Opcion equivocada... ")
                    break
                break
            print('Gracias Por jugar  ')
            
    
    
            
    
    

        


def InicioConexion():
    conexion = pymysql.connect(host = 'localhost',user = 'root',password= '',db = 'sistemadifusoadivina')
    return conexion

def FinConexion(conexion):
    conexion.close()
    
def mostrar(conexion):
    try : 
        with conexion.cursor() as cursor :
            cursor.execute('SELECT * FROM usuarios;')
            usuarios = list(cursor.fetchall())
            return usuarios
    except(pymysql.err.IntegrityError):
        print(' connection false ')
        return False
    

def Insertar(conexion,datos):
    try : 
        with conexion.cursor() as cursor :
            consulta = "INSERT INTO usuarios(Nombre_Usuario, Objeto, Caracteristica) VALUES (%s,%s,%s); "
            cursor.execute(consulta,(datos))
            conexion.commit()
            return True
        
    except(pymysql.err.IntegrityError):
        print(' User not save ')
        return False


                
            

        
conexion = InicioConexion()
usuarios=mostrar(conexion)
UsuariosRegistrados = []


def ObtenerUsuarios():
    for usuario in usuarios:
        UsuariosRegistrados.append(usuario[0])
    return UsuariosRegistrados


def comprobar(usuario):

    existe = 'no'
    for i in UsuariosRegistrados:
        if (usuario == i):
            existe = 'si'
    return existe

UsuariosRegistrados = ObtenerUsuarios()




def RegistroControl():
    NombreUsuario = input('Ingresa tu nombre: ')
    Comprobacion = comprobar(NombreUsuario)
    if (Comprobacion == 'no'):
        sistema_experto(NombreUsuario)
    if (Comprobacion == 'si'):
        SistemaExperto(NombreUsuario)
        

RegistroControl()




