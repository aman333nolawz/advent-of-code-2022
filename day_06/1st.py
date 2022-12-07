def start_of_packet(packet):
    for i in range(len(packet)):
        try:
            chars_recvd = packet[i] + packet[i+1] + packet[i+2] + packet[i+3]
            if len(set(chars_recvd)) == len(chars_recvd):
                return i + 4
        except IndexError:
            return

with open("input", "r") as fp:
    packet = fp.read().strip()

print(start_of_packet(packet))
