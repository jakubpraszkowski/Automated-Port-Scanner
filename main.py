from IpRange import IpRange
from PortScanner import PortScanner
from Save import Save


def input_ips():
    user_ips = []
    start_ip = input("Provide first ip address: ")
    user_ips.append(start_ip)
    end_ip = input("Provide last ip address: ")
    user_ips.append(end_ip)

    return user_ips


def input_ports():
    user_port_range = []
    start_port = input("Provide starting port for scanning: ")
    user_port_range.append(start_port)
    end_port = input("Provide ending port for scanning: ")
    user_port_range.append(end_port)

    return user_port_range


def main():
    user_input_ips = input_ips()
    ip_range = IpRange(user_input_ips[0], user_input_ips[1])
    user_input_ports = input_ports()
    port_scanner = PortScanner(ip_range.range_ip, user_input_ports[0], user_input_ports[1])
    port_scanner.scan_ports()


if __name__ == "__main__":
    main()
