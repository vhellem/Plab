import PythonLabs.BitLab as btl
import kdprims
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
        target = ""
        seen = len(m)
        currloc = 1
        size = 2
        target += m[0:1]
        LT = {"": 0 , m[0]: 1}

        while currloc < seen:
            oldseq, newbit = self.find_next_segment(m, currloc, LT)
            bitlen = int(math.ceil(math.log(size, 2)))
            index = LT[oldseq]
            index_bits = self.integer_to_bits(index, bitlen)
            index_bits += newbit
            target += index_bits
            oldseq += newbit
            LT[oldseq] = size
            size += 1
            currloc += len(oldseq)
        return target

    def find_next_segment(self, m, loc, lt):
        seq = oldseq = ""
        newbit = ""
        while seq in lt.keys():
            if(loc>= len(m)):
                return seq, ""
            newbit = m[loc]
            loc += 1
            oldseq = seq
            seq += newbit

        return oldseq, newbit

    def integer_to_bits(self, i, l):

        bits = str(bin(i)[2:])


        for k in range(len(bits), l):
            bits = "0" + bits

        return bits

    def decode(self, target):
        tlen = len(target)
        source = target[0]
        LT = ["", target[0]]
        loc = 1
        size = 2
        while(loc<tlen):
            bitlen = int(math.ceil(math.log(size, 2)))

            index = self.bits_to_integer(target[loc:loc+bitlen])

            seq = LT[index]
            if((loc+bitlen)<tlen):
                seq += target[loc+bitlen]
                LT.append(seq)
                size += 1
                loc +=1

            source += seq

            loc += bitlen
        return source


    def bits_to_integer(self, bit):
        return int(bit, 2)




def Ascii_test(msg="Hello World", filepath=False,lz_flag=False):
    coder = AsciiCoder()
    if(filepath):
            msg = coder.gen_message_from_file(filepath)
    test(coder, msg, lz_flag)


def Huff_test(msg="Hello World",filepath=False,lz_flag=False):
    coder = HuffCoder()
    if(filepath):
        msg = coder.gen_message_from_file(filepath)
    test(coder, msg, lz_flag)



def LZ_test(msg="0"*20, filepath=False):
    coder = LZCoder()
    if(filepath):
        msg = coder.gen_message_from_file(filepath)
    test(coder, msg ,False)



def test(coder, message, lz):
    coder.encode_decode_test(message)
    if lz:
        lz =LZCoder()
        lz.encode_decode_test(coder.encode(message))

Huff_test(=s)

