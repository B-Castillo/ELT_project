

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def rec_fight(urls):

    #dormir = np.random.randint(0.5,1)

    driver = webdriver.Chrome(ChromeDriverManager().install())

    #Chuleta de estadisticas
    lista_clases = ["W/L", "FIGHTER", "KD", "C. STR", "C. TD", "SUB", "WEIGHT CLASS", "METHOD", "ROUND", "TIME", "SIG. STR",
                    "TOTAL STR.", "TD", "T. CONTROL", "CABEZA", "CUERPO", "PIERNA", "CLINCH", "GROUND"]

    #Diccionario de estadisticas
    list_stats = {"FIGHTER":[], "KD":[],"C. STR":[], "C. TD":[], "SUB":[], "WEIGHT CLASS":[], "METHOD":[], "ROUND":[],
                "TIME":[], "SIG. STR":[], "TOTAL STR." :[], "TD":[], "T. CONTROL":[], "CABEZA":[], 
                "CUERPO":[], "PIERNA":[], "CLINCH":[], "GROUND":[]}

    # Sepodria utilizar "tqdm(urls)" para medir el tiempo.
    for url in urls:
        #Iteramos por las urls de los combates.
        driver.get(url)
        
        try:
            
            #sleep(dormir)
            for columna in range(2,11):
                
                # Declaramos las listas de cada una de las estadisticas de las peleas de la cartelera
                res_noche = []
                Sig_str = []
                Total_str =[]
                Td = []
                T_piso = []
                Cabeza = []
                Cuerpo = []
                Piernas = []
                Clinch = []
                Ground = []
                try:
                    
                    #Provamos con un "try" una alta cantidad de filas para poder abarcar la mas alta cantidad de convates posibles en una cartelera,
                    # sino llega al rango el "except" cuardara los datos recopilado y pasra a la siguiente columna.
                    for fila in range(1,20):
                        #sleep(dormir)
                        res1 = driver.find_element("css selector",f"body > section > div > div > table > tbody > tr:nth-child({fila}) > td:nth-child({columna})").text
                        res_noche.append(res1)
                        #Probamos a extarer los datos de todo la tabal.
                        if columna == 10:
                            #sleep(dormir)
                            # Solo se activara la recopilacion de las estadisticas ampliadas al llegar a la utima columna 
                            #sleep(dormir)
                            #Se tiene que clicar en alguno de los datos del conbate, en este caso el tiempo de duración
                            driver.find_element("css selector",f"body > section > div > div > table > tbody > tr:nth-child({fila}) > td:nth-child({columna})").click()
                            
                            sig_str = driver.find_element("css selector", "body > section > div > div > section:nth-child(4) > table > tbody > tr > td:nth-child(3)").text
                            Sig_str.append(sig_str)
                            
                            total_str = driver.find_element("css selector", "body > section > div > div > section:nth-child(4) > table > tbody > tr > td:nth-child(5)").text
                            Total_str.append(total_str)
                            
                            td = driver.find_element("css selector", "body > section > div > div > section:nth-child(4) > table > tbody > tr > td:nth-child(6)").text
                            Td.append(td)
                            
                            t_piso = driver.find_element("css selector", "body > section > div > div > section:nth-child(4) > table > tbody > tr > td:nth-child(10)").text
                            T_piso.append(t_piso)
                            
                            cabeza = driver.find_element("css selector", "body > section > div > div > table > tbody > tr > td:nth-child(4)").text
                            Cabeza.append(cabeza)
                            
                            cuerpo = driver.find_element("css selector", "body > section > div > div > table > tbody > tr > td:nth-child(5)").text
                            Cuerpo.append(cuerpo)
                            
                            piernas = driver.find_element("css selector", "body > section > div > div > table > tbody > tr > td:nth-child(6)").text
                            Piernas.append(piernas)
                            
                            clinch = driver.find_element("css selector", "body > section > div > div > table > tbody > tr > td:nth-child(8)").text
                            Clinch.append(clinch)
                            
                            ground = driver.find_element("css selector", "body > section > div > div > table > tbody > tr > td:nth-child(9)").text
                            Ground.append(ground)
                            
                            #Tenemos que svolver para seguir recolectando los datos de la duracion de los combates
                            driver.back()
                            
                except:
                    
                    #Guardamos los datos cada vez que llege a la ultima fila
                    list_stats[lista_clases[columna-1]].append(res_noche)
                    
                    if columna == 10:
                        #Se guardaran los datos de estadisticas ampliadas cuando cundo se haya recolectado la ultima columna.
                        list_stats[lista_clases[10]].append(Sig_str)
                        list_stats[lista_clases[11]].append(Total_str)
                        list_stats[lista_clases[12]].append(Td)
                        list_stats[lista_clases[13]].append(T_piso)
                        list_stats[lista_clases[14]].append(Cabeza)
                        list_stats[lista_clases[15]].append(Cuerpo)
                        list_stats[lista_clases[16]].append(Piernas)
                        list_stats[lista_clases[17]].append(Clinch)
                        list_stats[lista_clases[18]].append(Ground)
                    
        except: 
            
            print("Error")
            #Si no funciona insertaremos la url para posterior mente inspecionear cual ha sido el problema que ha surgido en dicha url.

    driver.quit()

    return list_stats