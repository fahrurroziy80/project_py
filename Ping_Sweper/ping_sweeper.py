import subprocess
import platform
import ipaddress
import socket
from concurrent.futures import ThreadPoolExecutor

# Cek host hidup atau tidak
def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", str(ip)]
    result = subprocess.run(command, stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        try:
            hostname = socket.gethostbyaddr(str(ip))[0]
        except socket.herror:
            hostname = "Tidak diketahui"
        return (str(ip), hostname)
    return None

# Fungsi utama Ping Sweeper
def ping_sweeper(network):
    print(f"🔍 Memindai jaringan {network} ...")
    net = ipaddress.ip_network(network, strict=False)
    alive_hosts = []

    # Multi-threading
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(ping_host, net.hosts())

    for result in results:
        if result:
            ip, hostname = result
            print(f"✅ Host aktif: {ip} ({hostname})")
            alive_hosts.append(f"{ip} ({hostname})")

    # Simpan ke file
    if alive_hosts:
        with open("alive_hosts.txt", "w") as f:
            for host in alive_hosts:
                f.write(host + "\n")
        print(f"\n📁 Hasil disimpan ke 'alive_hosts.txt'")

    print(f"\n📊 Total host aktif: {len(alive_hosts)}")
    return alive_hosts

# Main program
subnet = input("Masukkan subnet (contoh: 192.168.1.0/24): ")
ping_sweeper(subnet)
