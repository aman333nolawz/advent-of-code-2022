def start_of_packet(packet):
    for i in range(len(packet)):
        try:
            chars_recvd = ''.join([packet[c] for c in range(i, i+14)])
            if len(set(chars_recvd)) == len(chars_recvd):
                return i + 14
        except IndexError:
            return

with open("input", "r") as fp:
    packet = fp.read().strip()

print(start_of_packet(packet))
