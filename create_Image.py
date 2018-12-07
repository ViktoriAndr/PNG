import sys


class create_Image:
    def __init__(self, image):
        self.image = image
        self.new_hex_list = []
        self.convert_hex_code()

    def file_byte(self):
        bytelist = bytearray()
        characters_list = []
        with open(self.image, 'rb') as bytes:
            for byte in bytes:
                bytelist.extend(byte)
        # print(bytelist)
        for i in range(len(bytelist)):
            characters_list.extend(hex(int(bytelist[i])))
        return characters_list

    def convert_hex_code(self):
        characters_list = self.file_byte()
        hex_list = []
        for j in range(len(characters_list)-3):
            if characters_list[j] == '0' and characters_list[j+1] == 'x':
                temp_list = []
                temp_list.extend(characters_list[j+2] + characters_list[j+3])
                str_hex = ''.join(temp_list)
                hex_list.append(str_hex.upper())

        count = 0
        for i in range(len(hex_list)):
            if i % 16 == 0:
                count += 1

        for j in range(count):
            self.new_hex_list.append([])
            for e in range(j*16, len(hex_list)):
                if e <= (j*16 + 15):
                    self.new_hex_list[j].append(hex_list[e])
        for line in self.new_hex_list:
            print(line)


if __name__ == '__main__':
    create_Image(sys.argv[1])
    sys.exit()
