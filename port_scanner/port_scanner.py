import socket
import time
from idlelib.debugger_r import restart_subprocess_debugger
from ssl import socket_error

from project.BurteForce import target


def port_scanner(target, start_port, end_port):
    print(f"Memindai {target} dari port {start_port} hingga {end_port}.....")
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) #timeout setengah detik
        result = s.connect_ex(target, port)
        if result == 0:
            print(f"✅ port {port} terbuka")
        s.close()


    end_time = time.time()
    print(f"\n Selesai dalam {end_time- start_time:.2f} detik.")


#main program
target_host = input("Masukan hostname atau IP target :")
start_port = int(input("Masukan port awal: "))
end_port = int(input("Masukan port akhir : "))

try:
    target_ip = socket.gethostbyname(target_host)
    port_scanner(target_ip, start_port, end_port)
except socket.gaierror:
    print("Host tidak ditemukan!")








