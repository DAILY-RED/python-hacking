import subprocess
import re
# ifconfig eth0 down 
# ifconfig eth0 hw ether 00:11:22
# ifconfig eth0 up


class MAC_Changer: 
    def __init__(self):
        self.MAC = ""
    
    def get_MAC(self, iface):
        # Get the ifconfig output 
        output = subprocess.run(["ipconfig", iface], shell=False, capture_output=True)

        # Print the output
        cmd_result = output.stdout.decode('utf-8')
        #print(cmd_result)

        # This will grab the line "ether 00:11:22:33:44:55" in the ifconfig
        pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'

        # to compile the pattern
        regex = re.compile(pattern)

        # to search for string 
        ans = regex.search(cmd_result)

        # To extract "ether 00:11:22:33:44:55"
        current_mac = ans.group().split(" ")[1]
        self.MAC = current_mac
        return current_mac
    
    def change_mac(self, iface, new_mac):
        print ("[+] Current MAC address is ", self.get_MAC(iface))
 
        # Shut down eth0 network interface
        output = subprocess.run(["ipconfig", iface, "down"], shell= False, capture_output=True)
        print(output.stderr.decode('utf-8'))

        # Change the MAC address 
        output = subprocess.run(["ipconfig", iface, "hw", "ether", new_mac], shell= False, capture_output=True)
        print(output.stderr.decode('utf-8'))

        # Set start eth0 again
        output = subprocess.run(["ipconfig", iface, "up", "ether", new_mac], shell= False, capture_output=True)
        print(output.stderr.decode('utf-8'))

        print("[+] Updated MAC address is ", self.get_MAC(iface))
        return self.get_MAC(iface)




# class MAC_Changer:
#     def __init__(self):
#         self.current_mac = ""

#     def get_current_mac(self, iface):
#         output = subprocess.run(["ifconfig", iface], capture_output=True, text=True)
#         cmd_result = output.stdout

#         pattern = r'ether\s([\da-f]{2}(?::[\da-f]{2}){5})'
#         regex = re.compile(pattern)
#         match = regex.search(cmd_result)

#         if match:
#             self.current_mac = match.group(1)
#         else:
#             self.current_mac = None

#         return self.current_mac

#     def change_mac(self, iface, new_mac):
#         if not self.current_mac:
#             self.get_current_mac(iface)

#         if self.current_mac:
#             print(f"[+] Current MAC address: {self.current_mac}")

#             subprocess.run(["ifconfig", iface, "down"])
#             subprocess.run(["ifconfig", iface, "hw", "ether", new_mac])
#             subprocess.run(["ifconfig", iface, "up"])

#             new_mac = self.get_current_mac(iface)
#             if new_mac == new_mac:
#                 print(f"[+] Successfully changed MAC address to: {new_mac}")
#                 return new_mac
#             else:
#                 print("[-] Failed to change MAC address.")
#         else:
#             print("[-] Unable to get the current MAC address.")

#         return None