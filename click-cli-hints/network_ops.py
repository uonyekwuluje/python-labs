import ipaddress

cidr_suffix = "/32"

# Validate IP Address
def is_valid_ipv4_address(address: str) -> bool:
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        pass

    try:
        ipaddress.ip_network(address, strict=False)
        if '/' in address:
            return True
    except ValueError:
        pass

    return False

# Add and Test IP Address
def _add_ip(ip_addresses_list):
    file_name = "ipaddress-list.txt"
    values = set()

    # Validate IP Addresses
    for ip_address in ip_addresses_list:
        if not is_valid_ipv4_address(ip_address):
            print(f"{ip_address} is not a valid address")
            return

    # Create Local File
    with open(file_name, "w") as f:
        for ip_address in ip_addresses_list:
            if '/' in ip_address:
                f.write(f"{ip_address}" + "\n")
            else:    
                f.write(f"{ip_address}{cidr_suffix}" + "\n")

    # Update set
    with open(file_name, "r") as f2:
        for line in f2:
            values.add(line.strip())

#    with open(s3_file_object_name, "w") as out:
#        for v in sorted(values):
#            out.write(v + "\n")
