from mac import MAC_changer

if __name__ == "__main__":
    mc = MAC_changer()
    mac = mc.get_MAC("eth0")
    print(mac)
