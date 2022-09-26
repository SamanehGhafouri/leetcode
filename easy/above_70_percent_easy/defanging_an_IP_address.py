"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""


def defang_IP_address(address: str) -> str:
    li_address = list(address)

    for i in range(len(li_address)):
        if li_address[i] == ".":
            li_address[i] = "[.]"
    return "".join(li_address)


if __name__ == '__main__':
    ad = "1.1.1.1"
    print(defang_IP_address(ad))
