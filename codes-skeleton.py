
import arduino_connect


# Codes for the 5 signals sent to this level from the Arduino




# Morse Code Class
class mocoder():
    dot = 1
    dash = 2
    symbol_pause = 3
    word_pause = 4
    reset = 5
    current_message = ""
    current_word = ""
    current_symbol = ""

# O = dot, 1 = dash
    morse_codes = {'01':'a','1000':'b','1010':'c','100':'d','0':'e','0010':'f','110':'g','0000':'h','00':'i','0111':'j',
               '101':'k','0100':'l','11':'m','10':'n','111':'o','0110':'p','1101':'q','010':'r','000':'s','1':'t',
               '001':'u','0001':'v','011':'w','1001':'x','1011':'y','1100':'z','01111':'1','00111':'2','00011':'3',
               '00001':'4','00000':'5','10000':'6','11000':'7','11100':'8','11110':'9','11111':'0'}

#Test: 00003111301030003030004
    def __init__(self,sport=True):
        if sport:
            self.serial_port = arduino_connect.basic_connect()
        self.reset()

    def reset(self):
        self.current_message = ''
        self.current_word = ''
        self.current_symbol = ''

    # This should receive an integer in range 1-4 from the Arduino via a serial port
    def read_one_signal(self,port=None):
        connection = port if port else self.serial_port
        while True:
            # Reads the input from the arduino serial connection
            data = connection.readline()
            if data:
                return data

    # The signal returned by the serial port is one (sometimes 2) bytes, that represent characters of a string.  So,
    # a 2 looks like this: b'2', which is one byte whose integer value is the ascii code 50 (ord('2') = 50).  The use
    # of function int on the string converts it automatically.   But, due to latencies, the signal sometimes
    # consists of 2 ascii codes.  In that case, we need to pull out each of the codes and convert them separately using
    # chr (and then int).

    def decoding_loop(self):
        while True:
            s = self.read_one_signal(self.serial_port)

            if len(s) == 2:
                self.process_signal(int(chr(s[0])))
                self.process_signal(int(chr(s[1])))
            else:
                self.process_signal(int(s))

    def process_signal(self, number):
        print(number)
        if(number==self.word_pause):
            self.current_message += self.current_word
            self.current_word = ""
        elif(number==self.symbol_pause):
            try:
                print(self.current_symbol)
                self.current_word += self.morse_codes[self.current_symbol]
                self.current_symbol = ""
            except Exception:
                print("No morse code symbol found")
        elif(number==self.dash):
            self.current_symbol += "1"
        elif(number==self.dot):
            self.current_symbol += "0"

        print(self.current_word + self.current_message)


code = mocoder()
code.decoding_loop()