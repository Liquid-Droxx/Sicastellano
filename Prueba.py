import csv
def validar_rut(rut):
    rut = rut.replace(".","").replace("-","")
    if not re.match(r"^\d{7,8}[0-9kK]$",rut):
        return False
    cuerpo= rut[:-1]
    verificador=rut[-1].upper()
    suma=0
    factor=2
    for c in reversed(cuerpo):
        suma += int(c)* factor
        factor= factor + 1 if factor < 7 else 2
    dv = 11-(suma % 11)
    if dv == 10:
        dv='K'


def calcular_nota_presentacion(n1,n2,n3,n4):
    return (n1 * 0.30)+(n2 * 0.30)+(n3 * 0.30)+(n4 * 0.10)

def registro_estudiantes():
    estudiantes = []


print(""" 
    Menu Estudiantes
   1. Registrar Estudiante
   2. Ver estudiantes registrados
   3. Buscar estudiante por RUT
        """)

op=int(input("Seleccione Una Opcion "))

if op==1:
    while True:
        try:
            rut=int(input("Ingrese el Rut, sin puntos"))
            while rut.len() not in (1, 10):
                break
        except ValueError:
            print("Ingrese el rut correctamente")
        try:
            n1=float(input("Ingrese la primera nota"))
            n2=float(input("Ingrese la segunda nota"))
            n3=float(input("Ingrese la tercera nota"))
            n4=float(input("Ingrese la cuarta nota"))
            nota_presentacion = calcular_nota_presentacion(n1,n2,n3,n4) 
            if nota_presentacion >= 4:
                resultado = "Aprobado"
            else:
                "Reprobado"        
            estudiante = [rut, nombre, n1,n2.n3,n4,nota_presentacion,resultado]
            estudiantes.append(estudiante)
            print("Estudiante registrado de manera correcta")
            break
        except ValueError:
            print("Porfavor Vuelva a Intentar")


elif op == 2:
    if estudiantes:
        print(f"{'RUT':<12}{'Nombre':<15}")

    
        

