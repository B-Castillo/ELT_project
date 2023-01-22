
#import numpy as np
#import pandas as pd
from geopy.geocoders import Nominatim


def sep_col(df,rang1, rang2, arg1 = " ", arg2 = ""):

    res = int(input(print("¿Que metodo quiere hacer?\n 1. split\n 2. strip\n 3. remplace\n 4. salir")))

    while res != 4:

        if res == 1:
            
            for columna in df.columns[rang1:rang2]:

                # Iteramos por las columnas que tiene mas de un elemnto.
                df[columna] = df[columna].str.split(arg1)
                # Spliteamos por las comas

            return df.head(1)

        elif res == 2:
            
            for columna in df.columns[rang1:rang2]:
                    
                for x in range(df.shape[0]):
                    # Iteramos sobre las columnas que queremos limpiar y a su vez sobre las filas de nuestro DataFrame
                        
                    df[columna][x] = df[columna][x].strip(arg1)
                    # Eliminamos los elementos indeseados al principio y al final de nuestro String y lo guardamos en su ubicación

            return df.head(1)

        elif res == 3:
            
            for columna in df.columns[rang1:rang2]:
            
                for x in range(df.shape[0]):
                    # Iteramos sobre las columnas que queremos cambiar y a su vez sobre las filas de nuestro DataFrame
                        
                    df[columna][x] = df[columna][x].replace(arg1, str(arg2))
                    # Cambiaremos el elemento "\n" y lo cambiaremos por ","
            
            return df.head(1)
            
        else:

            print("Opción no valida")
    
        res = int(input(print("¿Que metodo quiere hacer? \n1. split\n 2. strip\n 3. remplace\n 4. salir")))




def drop_uneven_len(df, inicio, fin):

    filas_mal = []

    for indice, fila in df.iterrows():
    
        for columna in df.columns[inicio:fin]:
            if len(fila[df.columns[inicio]]) != len(fila[columna]):
                filas_mal.append(indice)
                break

    print(f"Hay {len(filas_mal)} filas en las que no coincide las longitud de las listas")
    res =input(print("¿Quiere eliminarlas? [si/no]"))

    if res == "si":

        for fila_mal in filas_mal:
        #Eliminamos las filas discordantes de la iteración anterior
            df.drop(fila_mal, axis=0, inplace=True)

        return print(f"Han sido eliminadas {len(filas_mal)} filas en las que no coincide las longitud de las listas") 
    elif res == "no":
        print("No se han eliminado las filas.")
    else:
        print("Opción no valida")
    


def nueva_col(df, old_col1, new_col, posicion):

    n_col = []
    #Creamos una lista para guardar los valores selecionados

    for elemento in df[old_col1]:
        # Iteramos por la columna mientras guardmos cada uno de los elementos deseados 
        n_col.append(elemento[posicion])

    #Creamos una nueva columna con el nombre anteriormente introducido y con lista creada con los elemntos deseados.
    df[new_col] = n_col


def col_reasig(df, inicio, fin, posicion):

    #Iteramos por las columnas indicadas
    for columna in df.columns[inicio:fin]:

        n_col = []
        #Creamos una lista para guardar los valores selecionados
        for elemento in df[columna]:
            # Iteramos por la columna mientras guardmos cada uno de los elementos deseados 
            n_col.append(elemento[posicion])
        
        #Guardamos los valores deseados en la columna correspondiente.
        df[columna] = n_col

    return df.head(2)


def fecha_mes(fecha):
    return fecha.split()[0]

def geo_cord(local):

    geoloca = Nominatim(user_agent= "brand")
    localizacion = geoloca.geocode(local)
    
    return localizacion.latitude, localizacion.longitude


    



