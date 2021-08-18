# Character With High Frequency will have less space and visa versa
# 5Byte -> 2Byte
import heapq as heap
import os

class BinaryTreeNode:
    def __init__(self,value,freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self,other): # Less Than
        return self.freq < other.freq

    def __eq__(self,other): # Equal
        return self.freq == other.freq

class HuffmanCoding:

    def __init__(self,path):
        self.path = path
        self.__heap = []
        self.__codes = {}
        self.__reverseCodes = {}

    def __make_frequency_dict(self,text):
        d = {}
        for c in text:
            d[c] = d.get(c,0) + 1

        return d

    def __buildHeap(self,freq_dict):
        
        for key in freq_dict:
            frequency = freq_dict[key]
            binary_tree_node = BinaryTreeNode(key,frequency)
            heap.heappush(self.__heap, binary_tree_node)

    def __buildTree(self):
        # Get Min freq Nodes and add new Node
        while len(self.__heap) > 1:
            Bt_Node1 = heap.heappop(self.__heap)
            Bt_Node2 = heap.heappop(self.__heap)
            freqSum = Bt_Node1.freq + Bt_Node2.freq
            
            newNode = BinaryTreeNode(None,freqSum)
            newNode.left = Bt_Node1
            newNode.right = Bt_Node2
            
            heap.heappush(self.__heap,newNode)
        
        return

    def __buildCodesHelper(self,root,curr_bits):
        if root is None:
            return
        
        if root.value is not None: # Because in this leaf node is the one with the value and freq
            self.__codes[root.value] = curr_bits
            self.__reverseCodes[curr_bits] = root.value
            return

        self.__buildCodesHelper(root.left,curr_bits + "0")
        self.__buildCodesHelper(root.right,curr_bits + "1")

    def __buildCodes(self):
        root = heap.heappop(self.__heap)
        self.__buildCodesHelper(root,"")
        
    def __getEncodedText(self,text):
        encoded_text = ""
        for char in text:
            encoded_text += self.__codes[char]
        return encoded_text

    def __getPaddedEncodedText(self,encoded_text):
        padded_amount = 8 - (len(encoded_text)%8) 

        for i in range(padded_amount):
            encoded_text += "0"
        
        # 0: in {} specify 0th argument and 08 = number of bits and b = Binary conversion
        padded_info = "{0:08b}".format(padded_amount) 
        
        padded_encoded_text = padded_info + encoded_text
        return padded_encoded_text

    def __getBytesArrary(self,padded_encoded_text):
        array = []

        for i in range(0,len(padded_encoded_text),8):
            byte = padded_encoded_text[i:i+8]
            array.append(int(byte,2)) # Taking base 2 for binary 

        return array

    def compress(self):
        # get file from path

        # Read Text From file
        # text = "fasbsajghbsafjhbashf"
        file_name, file_extension = os.path.splitext(self.path)
        output_Path = file_name + ".bin"

        with open(self.path,"r+") as file, open(output_Path,"wb") as output:
            # To make Frequency dict using the text
            text = file.read()
            text = text.rstrip()
            freq_dict = self.__make_frequency_dict(text)

            # Construct the heap from the frequency_dict
            self.__buildHeap(freq_dict)

            # Construct the Binary Tree from the heap
            self.__buildTree()

            # Contruct the Code Using Binary Tree
            self.__buildCodes()

            # Creating the excoded text using the codes
            encoded_text = self.__getEncodedText(text)

            # Put this encoded text into the binary file

            # Pad this encoded text
            padded_encoded_text = self.__getPaddedEncodedText(encoded_text)

            bytes_array = self.__getBytesArrary(padded_encoded_text)
            # return this binary file as output
            final_byte = bytes(bytes_array)
            output.write(final_byte)
        print("Compressed")
        return output_Path


    def __removePadding(self,text):
        padded_info = text[:8]
        extra_padding = int(padded_info,2)

        text = text[8:]
        text_without_padding = text[:-1*extra_padding]

        return text_without_padding

    def __decodeText(self,text):
        current_bits = ""
        decoded_text = ""

        for bit in text:
            current_bits += bit
            if current_bits in self.__reverseCodes:
                character = self.__reverseCodes[current_bits]
                decoded_text += character
                current_bits = ""

        return decoded_text
            
    def decompress(self,input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"
        with open(input_path,"rb") as file, open(output_path,"w") as output:
            bit_string = ""
            byte = file.read(1)
            while byte:
                # Converts byte format(0xf) -> integer(5)
                byte = ord(byte) 

                # Converts integer-> bits(b'1101) and then we take (1101) part and fill it to 8 char (00001101)
                bits = bin(byte)[2:].rjust(8,'0') 
                bit_string += bits
                byte = file.read(1)

            # Removing Padding
            actual_text = self.__removePadding(bit_string)        

            #Decoding Text
            decompressed_text = self.__decodeText(actual_text)

            output.write(decompressed_text)

        print("Decompressed")


            



path = "D:\Learning\CoursesLearning\Coding Ninjas\Huffman Coding\Sample.txt"
h = HuffmanCoding(path)
output_Path = h.compress()
h.decompress(output_Path)
