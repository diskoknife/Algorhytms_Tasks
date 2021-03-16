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

def main():


def input_queue(message, arrival=None, duration=None):
    size, num_of_packets = map(int, input(message).split())
    for i in range(num_of_packets):
        arrival[i], duration[i] = map(int, input().split())
    return arrival, duration, size


if __name__ == '__main__':
    main()


