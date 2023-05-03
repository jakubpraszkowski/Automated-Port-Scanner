from IpRange import IpRange
from PortScanner import PortScanner
from Save import Save


def ports(ip_range):
    user_input_ports = input_ports()
    port_scanner = PortScanner(ip_range.range_ip, user_input_ports[0], user_input_ports[1])
    port_scanner.scan_ports()


def input_ips():
    user_ips = []
    start_ip = input("Provide first ip address: ")
    user_ips.append(start_ip)
    end_ip = input("Provide last ip address: ")
    user_ips.append(end_ip)
    return user_ips


def input_ip():
    ip = input("Provide ip: ")
    return ip


def input_ports():
    user_port_range = []
    start_port = input("Provide starting port for scanning: ")
    user_port_range.append(start_port)
    end_port = input("Provide ending port for scanning: ")
    user_port_range.append(end_port)

    return user_port_range


def user_menu():
    user_decision = input("You can scan for ports using these options:\n"
                          "1. Loopback (127.0.0.1)\n"
                          "2. Default gate (192.168.0.1)\n"
                          "3. Only 1 IP\n"
                          "4. IP range\n")
    if user_decision == "1":

        ip_range = IpRange("127.0.0.1", "127.0.0.1")
        ports(ip_range)

    elif user_decision == "2":
        ip_range = IpRange("192.168.0.1", "192.168.0.1")
        ports(ip_range)

    elif user_decision == "3":
        user_input_ip = input_ip()
        ip_one = IpRange(user_input_ip, user_input_ip)
        ports(ip_one)

    elif user_decision == "4":
        user_input_ips = input_ips()
        ip_range = IpRange(user_input_ips[0], user_input_ips[1])
        ports(ip_range)
    else:
        print("No option")


def main():
    user_menu()


if __name__ == "__main__":
    main()
