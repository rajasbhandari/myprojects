import scapy.all as scapy
import optparse

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option('-t','--target',dest='target_ip',help='specify the ip or the network to scan')
    getargs,_= parser.parse_args()
    return getargs.target_ip

def scanner(ip):
    arp_request= scapy.ARP(pdst=ip)
    arp_boradcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_combine= arp_boradcast/arp_request
    answer= scapy.srp(arp_combine,timeout=1,verbose=False)[0]

    myList=[]
    for elements in answer:
        # print(elements[1].psrc+'\t\t'+elements[1].hwsrc)
        myList.append({"ip":elements[1].psrc,"mac":elements[1].hwsrc})
    return myList
    # print(myList)


def printer(result_list):
    print("IP\t\t\t\tMAC Address\n---------------------------------------------------------")
    for i in result_list:
        print(i['ip'] + '\t\t\t'+ i['mac'])

requ_range=get_arguments()
result=scanner(requ_range)
printer(result)



# printer(result)

# arp= scapy.arping("192.168.1.1/24")
# print(arp)


