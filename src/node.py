import hashlib
from struct import unpack

class Node:
    def __init__(self, ip_addr:str, port:int, de_bruijn_node=True, de_bruijn_flag = False):
        self.ip_addr = ip_addr
        self.port = port
        self.de_bruijn = (de_bruijn_node, de_bruijn_flag)
        self.hash_position = float(unpack("Q", hashlib.sha3_256((ip_addr + str(port)).encode()).digest()[:8])[0]) / 2**64
        if not de_bruijn_node:
            if de_bruijn_flag:
                self.hash_position = (self.hash_position + 1) / 2
            else:
                self.hash_position /= 2
        self.right = None
        self.left = None
        self.right_position = 2.0
        self.left_position = -1.0