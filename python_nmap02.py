import nmap
port_scan=nmap.PortScanner()
host_list=input('호스트 정보 입력: ')
port_list="20,21,22,23,25,80,443,3306"
port_scan.scan(hosts=host_list,arguments='-sV -p'+port_list)
print(port_scan.command_line())

host_status=[(i,port_scan[i]['status']['state']) for i in port_scan.all_hosts()]

for host,status in host_status:
    print(host,status)

for protocol in port_scan[host].all_protocols():
    print('프로토콜: ',protocol)
    ports=port_scan[host]['tcp'].keys()
    for port in ports:
        print('포트상태: ',port, port_scan[host][protocol][port]['state'])
