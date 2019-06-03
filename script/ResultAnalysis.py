#Camilo Sepulveda
#Luis Munoz
#Leonardo Franco

import os
import psutil
import time
import subprocess
from os import listdir
from os.path import isfile, join

dataPage = []  #datos recopilados de la pagina a analizar
dataTotal = []

def loadURL(path):
    """
        Metodo que carga la informacion de la pagina a analizar
        path: ruta del archivo
        """
    f = open(path, 'r')
    x = f.read() + ''
    dataPage.extend(x.split("\n"))
    f.close()


def export_results(data, web_site, case):
    """
        Exporta en un archivo .txt los resultados del monitoreo del sistema \n
        data: list que contiene los datos correspondientes al uso de cpu_por proceso, cpu_total, consumo de RAM \n
        web_site: Dominio del sitio al que se realizo el analisis. \n
        case: 0 si los datos del analisis son de sitios limpios de scripts mineros. \n
             1 si los datos del analisis son de sitios con scripts mineros. \n
        """
    if case == 0:
        print("Exportando resultados")
        cadena = '# cpu usada por el proceso;total cpu usada en el sistema;RAM usada en el sistema;kilobytes enviados; kilobytes recibidos'
        route = 'data/results/limpios/' + repr(web_site) + '.txt'
        if not os.path.isfile(route):
            write_file(route, cadena)
        f = open(route, 'a')
        for result_i in data:
            f.write('\n' + result_i)

        print("Datos exportados: " + route)
        f.close()
    elif case == 1:
        print("Exportando resultados")
        cadena = '# cpu_used;total_cpu_used;RAM_used;'
        route = 'data/results/mineros/' + repr(web_site) + '.txt'
        if not os.path.isfile(route):
            write_file(route, cadena)
        f = open(route, 'a')
        for result_i in data:
            f.write('\n' + result_i)

        print("Datos exportados: " + route)
        f.close()


def write_file(path, data):
    """
        Crea o sobre-escribe un archivo en la ruta dada y escribe el valor que entra por parametro
        path: ruta dek archivo.
        data: cadena que se escribira en el archivo.
        """
    f = open(path, 'w')
    f.write(data)
    f.close()

def average(page):
    """
    Metodo encargado de iniciar el analisis a una lista de URL que son el insumo para determinar el comportamiento 
    de los sitios web que presentan un comportamiento malisioso que esta asociado al Cryptojacking \n
    case: 0 si el analisis es a sitios limpios de scripts mineros. \n
        1 si el analisis es a sitios con scripts mineros.
    """
    cpuProcess= 0.0;
    cpuTotal= 0.0;
    ramUsage= 0.0;
    bytesSended= 0.0;
    bytesReceived= 0.0;
    cant = 0;
    for iteration in dataPage:
        if not(iteration.startswith("#")):
            dataInstant = iteration.split(";")
            cpuProcess += float(dataInstant[0])
            cpuTotal += float(dataInstant[1])
            ramUsage += float(dataInstant[2])
            bytesSended += float(dataInstant[3])
            bytesReceived += float(dataInstant[4])
            cant +=1
    cpuProcess /= cant
    cpuTotal /= cant
    ramUsage /= cant
    dataPage.clear()
    salida = page + "; "+ repr(round(cpuProcess,2)) + "; " + repr(round(cpuTotal,2)) + '; ' + repr(round(ramUsage,2)) + '; '+ repr(round(bytesSended,2)) +'; '+ repr(round(bytesReceived,2))
    print(salida)
    dataTotal.append(salida)

def analyze():
    averCPU = 0.0
    averCPUTotal = 0.0
    averRAM = 0.0
    for page in dataTotal:
        page = page.split(";")
        averCPU += float(page[1])
        averCPUTotal += float(page[2])
        averRAM += float(page[3])
if __name__ == '__main__':
    #Comente o quite los comentarios de acuerdo con el caso que se desea analizar. Solo corra un caso a la vez.
    onlyfiles = [f for f in listdir('data/results/limpios') if isfile(join('data/results/limpios', f))]
    for file in onlyfiles:
        loadURL('data/results/limpios/'+file)
        average(file)
    data = analyze()

    #Analisis para sitios con scripts mineros. Case 1
    onlyfiles = [f for f in listdir('data/results/mineros') if isfile(join('data/results/mineros', f))]
    for file in onlyfiles:
        loadURL('data/results/mineros/'+file)
        average(file)
    data = analyze()
    #export_results(data, web_site, case)
