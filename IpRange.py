import ipaddress


class IpRange:
    def __init__(self, start_ip, end_ip):
        self.start_ip = ipaddress.IPv4Address(start_ip)
        self.end_ip = ipaddress.IPv4Address(end_ip)
        self.range_ip = self.generate_ip_range()

    def generate_ip_range(self):
        range_ip = []

        for ip in range(int(self.start_ip), int(self.end_ip) + 1):
            range_ip.append(ipaddress.IPv4Address(ip))

        return range_ip
