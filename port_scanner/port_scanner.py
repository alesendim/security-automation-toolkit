import socket

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            return s.connect_ex((host, port)) == 0
    except Exception:
        return False

def main():
    host = input("Digite o host ou IP: ")
    ports = [21, 22, 80, 443]

    print(f"\nEscaneando {host}...\n")
    for port in ports:
        if scan_port(host, port):
            print(f"Porta {port} aberta")
        else:
            print(f"Porta {port} fechada")

if __name__ == "__main__":
    main()
