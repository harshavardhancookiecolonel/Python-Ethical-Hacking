import scapy.all as scapy

def scan(ip):
  arp_request = scapy.ARP(pdst=ip)
  broadcast = scapy.Ether(dst="MAC_ADDRESS")
  arp_packet = broadcast/arp_request
  answered_list = scapy.srp(arp_packet, timeout=1, verbose=False)[0]
  clients_list = []
  for element in answered_list:
    clients_dict = {"ip": element[1].psrc, "mac": element[1].hwdst}
    clients_list.append(clients_dict)
  return(clients_list)

def print_result(result_list):
  print("IP\t\t\tMAC_ADDRESS\n----------------------------------------------------------")
  for client in result_list:
    print(client["ip"] + "\t\t" + client["mac"])


scan_result = scan("gateway")
print_result(scan_result)
