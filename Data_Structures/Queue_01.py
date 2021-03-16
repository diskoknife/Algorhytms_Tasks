#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)

"""

Simulation of network packet tracer. Every packet have arrival time and
duration time. Program should have next view:
Input:
First string (size num_of_packets)
Every next string: (arrival duration)
Output:
Print for every packet time when processor starts packet tracing
or (-1) if packet been thrown out

"""


def set_header():
    size, num_of_packets = map(int, input().split())
    return size, num_of_packets


def fill_packets(num_of_packets, packets = []):
    for i in range(num_of_packets):
        packets[i] = map(int, input().split())
        return packets

def packet_tracer(arrival, duration):
    pass
