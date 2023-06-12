from mac import MAC_changer

if __name__ == "__main__":
    mc = MAC_changer()
    mac = mc.get_MAC("eth0")
    print(mac)

    curr_mac = mc.change_mac("eth0", "00:11:99:33:44:55")
    print(curr_mac)
