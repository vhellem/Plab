import PythonLabs.BitLab as btl
import kdprims.py
import math

class Coder:
    bina = 1
    def gen_message_from_file(self, filepath):
        f = open(filepath)
        s = ""
        for line in f.readlines():
            s += line
            s += " "

        return s

    def encode(self, m):
        pass
    def decode(self, m):
        pass

    def encode_decode_test(self, message, ):
        encoded = self.encode(message)
        decoded = self.decode(encoded)
        print("Message is " + message)
        print("encoded message is " + encoded)
        print("decodede message is " + decoded)
        print("original message length is: " + str(len(message)))
        print("encoded length is: " + str(len(encoded)))
        print("decoded length is: " + str(len(decoded)))
        if(message==decoded):
            print("They are equal)")
        else:
            print("You fucked up")
        comp = (1-(len(encoded)/(len(message)*self.bina)))
        print("Compression fraction is" + str(comp))


class AsciiCoder(Coder):
    bina = 8
    def encode(self, string):
        bins = ""
        for symbol in string:
            print(format(ord(symbol), "#010b")[2:])

            bins += (format(ord(symbol), "#010b")[2:])

        return bins


    def decode(self, bits):
        mess = ""

        for i in range(0, len(bits)-7, 8):

            mess += chr(int(bits[i:i+8], 2))

        return mess






class HuffCoder(Coder):
    tree = ""



    def encode(self, message):

        tree = self.build_tree(dict)
        self.encoded =  btl.huffman_encode(message, self.tree)
        return self.encoded.__repr__()

    def build_tree(self, filepath):
        freqs = kdprims.calc_char_freqs(filepath)
        pq = btl.init_queue(freqs)
        while len(pq) > 1:
            n1 = pq.pop()
            n2 = pq.pop()
            pq.insert(btl.Node(n1,n2))
        self.tree = pq[0]
    def decode(self, m):
        return btl.huffman_decode(self.encoded, self.tree)


#ascii = AsciiCoder()
#ascii.encode_decode_test("hello")


class LZCoder(Coder):
    def encode(self, m):
        compressed_data = []
        code_count = 257
        current_string = ""
        for c in string:
            current_string = current_string + c
            if not (codes.has_key(current_string)):
                codes[current_string] = code_count
                compressed_data.append(codes[current_string[:-1]])
                code_count += 1
                current_string = c
        compressed_data.append(codes[current_string])
#
#
#
#     def lz_encode(self, message):
#         target = ""
#         seen = len(message)
#         target[0] = source[0]
#         LT = {source[0]: 1}
#         size = 2
#         currloc = 1
#         while(currloc < size):
#             oldseq, newbit = self.find_next_segment(message, currloc, LT)
#             bitlen = math.log(size, 2)
#             index = LT[oldseg]
#             index_bits = self.integer_to_bits(index, bitlen)
#             index_bits += newbit
#             target += index_bits
#             LT[oldseq] = newbit
#             currloc += length(oldseq)
#             size += 1
#
#         return target
# def find_next_segment(m, log, lt):
#     seq = oldseq = ""
#     newbit = ""
#
#
# def integer_to_bits(i, len):
#
#     bits = bin(i)[2:]
#
#     for i in range(len(bit), len):
#         bits = "0" + bits
#
#     return bits