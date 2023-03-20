# Automated-Port-Scanner

This program automates the process of scanning a network for open ports on a specified range of IP addresses. The program uses socket programming to establish a connection with each IP address and port in the range to determine whether it is open or closed.

The program starts by prompting the user to enter a range of IP addresses and a range of ports to scan. The program then uses threading to establish connections with each IP address and port in the range simultaneously, rather than sequentially, which can significantly reduce the time required to complete the scan.

## TODO:
- [ ] Add support for scanning multiple ports simultaneously for each IP address to improve the efficiency of the program.

- [x] Implement an option to save the results of the port scan to a file for later analysis.

- [ ] **Ongoing** Improve error handling and provide more informative error messages to the user.

- [x] Add support for scanning UDP ports in addition to TCP ports.

- [ ] Implement a user-friendly command-line interface with options for specifying the range of IP addresses and ports to scan, and other scan parameters.

- [ ] Implement a graphical user interface (GUI) to make the program more accessible to non-technical users.

- [x] Add support for scanning IPv6 addresses in addition to IPv4 addresses.

- [x] Implement support for detecting the service running on each open port.

- [ ] Add support for scanning for vulnerabilities associated with open ports using known vulnerability databases.

- [ ] Implement support for scanning for web application vulnerabilities on open ports that host web applications.
