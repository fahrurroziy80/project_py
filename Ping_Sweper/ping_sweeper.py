import subprocess
import platform
import ipaddress

def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", str(ip)]
    result = subprocess.run(command, stdout=subprocess.DEVNULL)
    return result.returncode == 0

def ping_sweeper(network):
    print(f"🔍 Memindai jaringan {network} ...")
    net = ipaddress.ip_network(network, strict=False)
    alive_hosts = []

    for host in net.hosts():
        if ping_host(host):
            print(f"✅ Host aktif: {host}")
            alive_hosts.append(str(host))

    print(f"\n📊 Total host aktif: {len(alive_hosts)}")
    return alive_hosts

# Main program
subnet = input("Masukkan subnet (contoh: 192.168.1.0/24): ")
ping_sweeper(subnet)
