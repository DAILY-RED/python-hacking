import subprocess
import re
# ifconfig eth0 down 
# ifconfig eth0 hw ether 00:11:22
# ifconfig eth0 up


class MAC_changer: 
    def __init__(self):
        self.MAC = ""
    
    def get_MAC(self, iface):
        # Get the ifconfig output 
        output = subprocess.run(["ifconfig", iface], shell=False, capture_output=True)

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
