import socket
import threading
import ipaddress
import queue

user_ip_range = []
range_ip = []
user_port_range = []
range_port_formatting = []
ip_addresses_to_str = []


def input_ips():
    start_ip = input("Provide first ip address: ")
    user_ip_range.append(start_ip)
    end_ip = input("Provide last ip address: ")
    user_ip_range.append(end_ip)


def ip_range():
    start_ip = ipaddress.IPv4Address(user_ip_range[0])
    end_ip = ipaddress.IPv4Address(user_ip_range[1])

    for ip in range(int(start_ip), int(end_ip) + 1):
        range_ip.append(ipaddress.IPv4Address(ip))


def socket_range():
    start_port = input("Provide starting port for scanning: ")
    user_port_range.append(start_port)
    end_port = input("Provide ending port for scanning: ")
    user_port_range.append(end_port)


def ip_range_formatting():
    for ipv4_address in range_ip:
        ipv4_address_str = str(ipv4_address)
        ip_addresses_to_str.append(ipv4_address_str)

    for i, ip_addr in enumerate(ip_addresses_to_str):
        if (i + 1) % 3 == 0:
            print(ip_addr)
        else:
            print(f"{ip_addr} | ", end='')


def check_port(ip, port, results):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    if result == 0:
        results.put(port)
    sock.close()


def looking_for_open_ports():
    ip_range_formatting()
    question = input("\nWhich ip do you wish to look for open ports? ")
    ipv4 = ipaddress.IPv4Address(question)
    if ipv4:
        start_port = int(input("Provide first port: "))
        end_port = int(input("Provide last port: "))

        results = queue.Queue()

        threads = []
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=check_port, args=(question, port, results))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        while not results.empty():
            port = results.get()
            print("Port {} is open".format(port))


def main():
    input_ips()
    ip_range()
    looking_for_open_ports()


if __name__ == "__main__":
    main()
