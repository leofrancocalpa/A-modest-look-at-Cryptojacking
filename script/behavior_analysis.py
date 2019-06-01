
import csv
import os
import psutil
import time
import subprocess

urls = []
result = []


def loadURL(path):
        f = open(path, 'r')
        x = f.read() + ''
        urls.extend(x.split())
        f.close()

def openwebsites():
    cpu_usage = []
    print('process started' + '\n'+'---------------------------')
    print('----------------------------------------------------')
    for url in urls:
        print('Ejecutando para '+url)
        sub_process = subprocess.Popen(["chromium", url])
        time.sleep(5)
        var = calculate_cpu_usage(url)
        print(var)
        result.append(var)
        time.sleep(2)
        sub_process.kill()
        print('-------------------------------')
        print('-------------------------------')

def export_results():
        print("Exportando resultados")
        print(result)
        num = 0
        for result_i in result:
                cadena = ''
                cadena = result_i.pop(0)
                route = 'data/results/'+repr(num)+'.txt'
                file_name = os.path.join('data', '/'+cadena+'.txt')
                if not os.path.isfile(route):
                        write_file(file_name, result_i)
                else:
                        f = open(file_name, 'a')
                        for data in result_i:
                                f.write('\n'+data)
                                f.close()
        num = num+1  
                
def write_file(path, data):
        f = open(path, 'w')
        f.write(data)
        f.close()
    
def get_process(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            return process

def calculate_cpu_usage(url_name):
        usage = []
        usage.append(url_name)
        curren_process = get_process("chromium")
        print('Calculando uso de cpu para proceso ')
        for i in range(60):
                #print(curren_process.cpu_percent())
                print(psutil.virtual_memory().percent)
                usage.append(curren_process.cpu_percent())
                time.sleep(0.5)
        return usage

def example():
    urls = ["http://forex-trading.hol.es"]
    #urls = ["http://youtube.com"]
    print('process started' + '\n'+'---------------------------')
    print('----------------------------------------------------')
    for url in urls:
        print('Ejecutando para '+url)
        sub_process = subprocess.Popen(["chromium", url])
        time.sleep(3)
        var = calculate_cpu_usage(url)
        #print(var)
        result.append(var)
        time.sleep(2)
        sub_process.kill()
        print('-------------------------------')
        print('-------------------------------')


if __name__ == '__main__':
    path = os.path.join('data', 'urls.txt')
    #loadURL(path)
    #openwebsites()
    #export_results()
    example()
