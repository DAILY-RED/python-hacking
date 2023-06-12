from mac import MAC_Changer

if __name__ == "__main__":
    mc = MAC_Changer()
    mac = mc.get_MAC("eth0")
    print(mac)

    # The new MAC address that it will get. 
    curr_mac = mc.change_mac("eth0", "00:11:22:33:44:55")
    print(curr_mac)


# if __name__ == "__main__":
#     mc = MAC_Changer()
#     mac = mc.get_current_mac("eth0")
#     if mac:
#         print(f"[+] Current MAC address: {mac}")

#         # The new MAC address to set
#         new_mac = "00:11:99:33:44:55"
#         updated_mac = mc.change_mac("eth0", new_mac)
#         if updated_mac:
#             print(f"[+] Updated MAC address: {updated_mac}")
#         else:
#             print("[-] Failed to change MAC address.")
#     else:
#         print("[-] Unable to get the current MAC address.")