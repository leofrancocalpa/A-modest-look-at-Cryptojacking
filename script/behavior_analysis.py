#Camilo Sepulveda
#Luis Munoz
#Leonardo Franco

import os
import psutil
import time
import subprocess

urls = []  #URL a analizar


def loadURL(path):
    """
        Metodo que carga los URL que se van a analizar
        path: ruta del archivo que contiene los URL
        """
    f = open(path, 'r')
    x = f.read() + ''
    urls.extend(x.split())
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


def get_process(process_name):
    """
    Busca y retorna un proceso. \n
    process_name: nombre del proceso a buscar
    """
    for process in psutil.process_iter():
        if process.name() == process_name:
            return process


def calculate_cpu_usage(url_name, case):
    """
    Calcula el uso de los recursos fisicos del sistema que se consumen despues de iniciar un 
    proceso que abre un sitio web desde chromium
    """

    usage = []
    curren_process = get_process("chromium")
    print('Calculando uso de cpu para proceso ')
    for i in range(100):
        net = psutil.net_io_counters(pernic=True)
        sent = net['wlan0'].bytes_sent
        sent = sent / 1024 #kilobytes
        received = net['wlan0'].bytes_recv
        received = received / 1024 #kilobytes
        salida = repr(curren_process.cpu_percent()) + ";" + repr(psutil.cpu_percent()) + ';' + repr(psutil.virtual_memory().percent)+ ';'+repr(sent)+';'+repr(received)
        print(salida)
        usage.append(salida)
        time.sleep(0.5)
    export_results(usage, url_name, case)


def analyze(case):
    """
    Metodo encargado de iniciar el analisis a una lista de URL que son el insumo para determinar el comportamiento 
    de los sitios web que presentan un comportamiento malisioso que esta asociado al Cryptojacking \n
    case: 0 si el analisis es a sitios limpios de scripts mineros. \n
        1 si el analisis es a sitios con scripts mineros.
    """

    print('process started')
    print('----------------------------------------------------')
    print('----------------------------------------------------')
    for url in urls:
        print('Ejecutando para ' + url)
        sub_process = subprocess.Popen(["chromium", url])
        time.sleep(3)
        web_site_name = url.replace("http://", "")
        calculate_cpu_usage(web_site_name, case)
        time.sleep(2)
        sub_process.kill()
        time.sleep(2)
        print('-------------------------------')
        print('-------------------------------')


if __name__ == '__main__':
    #Comente o quite los comentarios de acuerdo con el caso que se desea analizar. Solo corra un caso a la vez.

    #Analisis para sitios limpios de scripts mineros. Case 0
    """path_limpios = os.path.join('data', 'urls-limpios.txt')
    loadURL(path_limpios)
    analyze(0)"""

    #Analisis para sitios con scripts mineros. Case 1

    path_mineros = os.path.join('data', 'urls-mineros.txt')
    loadURL(path_mineros)
    analyze(1)
