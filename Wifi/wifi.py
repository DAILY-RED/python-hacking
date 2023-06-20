# import subprocess

# completed_process = subprocess.run(["netsh", "wlan", "show", "profiles"], shell=True, capture_output=True)

# output = completed_process.stdout.decode()
# print(output)
# output = output.split("\n")


# access_points = []
# for line in output:
#     if "ALL User Profile" in line:
#         split_line = line.split(":")
#         ap = split_line[1][1:-1]
#         access_points.append(ap)

# for access_point in access_points:
#     ap_result = subprocess.run(["netsh", "wlan", "show", "profile", access_point, "key=clear"], shell=True, capture_output=True)
#     ap_result = ap_result.stdout.decode( )
#     ap_result_list = ap_result.split("\n")
#     for line_result in ap_result_list:
#         if "SSID name" in line_result:
#             print(line_result)
        
#         if "Key Content" in line_result:
#             print(line_result)
        




import subprocess

def get_wireless_profiles():
    completed_process = subprocess.run(["netsh", "wlan", "show", "profiles"], shell=True, capture_output=True)
    output = completed_process.stdout.decode()
    output = output.split("\n")

    access_points = []
    for line in output:
        if "All User Profile" in line:
            split_line = line.split(":")
            ap = split_line[1][1:-1]
            access_points.append(ap)

    return access_points

def get_key_content(profile):
    ap_result = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], shell=True, capture_output=True)
    ap_result = ap_result.stdout.decode()
    ap_result_list = ap_result.split("\n")
    key_content = ""
    for line_result in ap_result_list:
        if "Key Content" in line_result:
            key_content = line_result.split(":")[1].strip()
            break

    return key_content

def main():
    profiles = get_wireless_profiles()

    print("Wireless Profiles:")
    for i, profile in enumerate(profiles):
        print(f"{i + 1}. {profile}")

    choice = input("Enter the number of the profile to view the key content (or 'q' to quit): ")
    if choice == "q":
        return

    try:
        profile_index = int(choice) - 1
        selected_profile = profiles[profile_index]
        key_content = get_key_content(selected_profile)

        print(f"\nProfile: {selected_profile}")
        print(f"Key Content: {key_content}")
    except (ValueError, IndexError):
        print("Invalid choice.")

if __name__ == "__main__":
    main()

