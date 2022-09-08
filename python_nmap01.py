import nmap
port_scan=nmap.PortScanner()
port_result=port_scan.scan('192.168.214.132','80','-sV')
print(port_result)
print('**************************************************')
print(port_scan.command_line())

for host in port_scan.all_hosts():
    print('*Host Info: ', host, port_scan[host].hostname())
    print('*Host Stat: ',port_scan[host].state())
