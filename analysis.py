import sys

from create_Image import create_Image


class analysis:
    def __init__(self, image, chunk):
        self.create = create_Image(image)
        self.image = image
        self.chunks = {}
        self.format()
        self.write_chunks()

        if chunk == "all":
            for key in self.chunks.keys():
                self.data(key)
        else:
            self.data(chunk)

    def data(self, chunk):
        if chunk == "IHDR":
            self.IHDR()
        elif chunk == "PLTE":
            self.PLTE()
        elif chunk == "tRNS":
            self.tRNS()
        elif chunk == "iCCP":
            self.iCCP()
        elif chunk == "cHRM":
            self.cHRM()
        elif chunk == "gAMA":
            self.gAMA()
        elif chunk == "sBIT":
            self.sBIT()
        elif chunk == "sRGB":
            self.sRGB()
        elif chunk == "tEXt":
            self.tEXt()
        elif chunk == "zTXt":
            self.zTXt()
        elif chunk == "iTXt":
            self.iTXt()
        elif chunk == "bKGD":
            self.bKGD()
        elif chunk == "hIST":
            self.hIST()
        elif chunk == "pHYs":
            self.pHYs()
        elif chunk == "sPLT":
            self.sPLT()

    def format(self):
        str_format = ""
        for i in range(8):
            str_format += " " + self.create.new_hex_list[0][i]
        if str_format == " 89 50 4E 47 D0 A0 1A A0":
            print("PNG")

    def write_chunks(self):
        image = open(self.image, 'rb')
        image_1 = image.readline()
        image_2 = image.readline()
        bytes = image.read()
        count = 0
        while count < len(bytes):
            block = bytes[count:count + 4]
            length = int(block.hex(), 16)
            name_block = str(bytes[count + 4: count + 8])
            name = name_block[2:len(name_block)-1]
            data = bytes[count + 8: count + 8 + length]
            self.chunks[name] = data
            crs = bytes[count + 8 + length: count + 12 + length]
            # print("length {0} name {1} data {2} crs {3}".format(length, name, data, crs))
            print(name)
            count += length + 12
        image.close()

    def IHDR(self):
        str_width = self.chunks.get('IHDR')[:4].hex()
        self.width = int(str_width, 16)
        print('Ширина: {0}'.format(self.width))

        str_height = self.chunks.get('IHDR')[4:8].hex()
        self.height = int(str_height, 16)
        print('Высота: {0}'.format(self.height))

        str_bit_depth = self.chunks.get('IHDR')[8:9].hex()
        bit_depth = int(str_bit_depth, 16)
        print('Битовая глубина: {0}'.format(bit_depth))

        str_colour_type = self.chunks.get('IHDR')[9:10].hex()
        colour_type = int(str_colour_type, 16)
        print('Тип цвета: {0}'.format(colour_type))

        str_compression_method = self.chunks.get('IHDR')[10:11].hex()
        compression_method = int(str_compression_method, 16)
        print('Метод сжатия: {0}'.format(compression_method))

        str_filter_method = self.chunks.get('IHDR')[11:12].hex()
        filter_method = int(str_filter_method, 16)
        print('Метод фильтрации: {0}'.format(filter_method))

        str_interlace_method = self.chunks.get('IHDR')[12:13].hex()
        interlace_method = int(str_interlace_method, 16)
        print('Interlace метод: {0}'.format(interlace_method))

    def PLTE(self):
        str_red = self.chunks.get('PLTE')[:1].hex()
        red = int(str_red, 16)
        print('Красный: {0}'.format(red))

        str_green = self.chunks.get('PLTE')[1:2].hex()
        green = int(str_green, 16)
        print('Красный: {0}'.format(green))

        str_blue = self.chunks.get('PLTE')[2:3].hex()
        blue = int(str_blue, 16)
        print('Красный: {0}'.format(blue))

    def tRNS(self):
        str_grey_sample_value = self.chunks.get('tRNS')[:2].hex()
        grey_sample_value = int(str_grey_sample_value, 16)
        print('Значение серого: {0}'.format(grey_sample_value))

        str_red_sample_value = self.chunks.get('tRNS')[2:4].hex()
        red_sample_value = int(str_red_sample_value, 16)
        print('Значение красного: {0}'.format(red_sample_value))

        str_blue_sample_value = self.chunks.get('tRNS')[4:6].hex()
        blue_sample_value = int(str_blue_sample_value, 16)
        print('Значение синего: {0}'.format(blue_sample_value))

        str_green_sample_value = self.chunks.get('tRNS')[6:8].hex()
        green_sample_value = int(str_green_sample_value, 16)
        print('Значение зеленого: {0}'.format(green_sample_value))

        str_alpha_for_palette_index_0 = self.chunks.get('tRNS')[8:9].hex()
        alpha_for_palette_index_0 = int(str_alpha_for_palette_index_0, 16)
        print('Альфа для индекса палитры 0: {0}'.format(alpha_for_palette_index_0))

        str_alpha_for_palette_index_1 = self.chunks.get('tRNS')[9:10].hex()
        alpha_for_palette_index_1 = int(str_alpha_for_palette_index_1, 16)
        print('Альфа для индекса палитры 1: {0}'.format(alpha_for_palette_index_1))

        str_etc = self.chunks.get('tRNS')[10:11].hex()
        etc = int(str_etc, 16)
        print('и т.д.: {0}'.format(etc))

    def iCCP(self):
        index = self.chunks.get('ICCP').find(b'\x00')

        str_profile_name = self.chunks.get('ICCP')[:index].hex()
        profile_name = int(str_profile_name, 16)
        print('Имя профиля: {0}'.format(profile_name))

        str_compression_method = self.chunks.get('ICCP')[index+1:index+2].hex()
        compression_method = int(str_compression_method, 16)
        print('Метод сжатия: {0}'.format(compression_method))

        str_compressed_profile = self.chunks.get('ICCP')[index + 2:].hex()
        compressed_profile = int(str_compressed_profile, 16)
        print('Сжатый профиль: {0}'.format(compressed_profile))

    def cHRM(self):
        str_white_x = self.chunks.get('cHRM')[:4].hex()
        white_x = int(str_white_x, 16)
        print('Белый по x: {0}'.format(white_x))

        str_white_y = self.chunks.get('cHRM')[4:8].hex()
        white_y = int(str_white_y, 16)
        print('Белый по y: {0}'.format(white_y))

        str_red_x = self.chunks.get('cHRM')[8:12].hex()
        red_x = int(str_red_x, 16)
        print('Красный по x: {0}'.format(red_x))

        str_red_y = self.chunks.get('cHRM')[12:16].hex()
        red_y = int(str_red_y, 16)
        print('Красный по y: {0}'.format(red_y))

        str_green_x = self.chunks.get('cHRM')[16:20].hex()
        green_x = int(str_green_x, 16)
        print('Зелёный по x: {0}'.format(green_x))

        str_green_y = self.chunks.get('cHRM')[20:24].hex()
        green_y = int(str_green_y, 16)
        print('Зелёный по y: {0}'.format(green_y))

        str_blue_x = self.chunks.get('cHRM')[24:28].hex()
        blue_x = int(str_blue_x, 16)
        print('Синий по x: {0}'.format(blue_x))

        str_blue_y = self.chunks.get('cHRM')[28:32].hex()
        blue_y = int(str_blue_y, 16)
        print('Синий по y: {0}'.format(blue_y))

    def gAMA(self):
        str_gamma = self.chunks.get('gAMA')[:4].hex()
        gamma = int(str_gamma, 16)
        print('Гамма: {0}'.format(gamma))

    def sBIT(self):
        str_significant_greyscale_bits_0 = self.chunks.get('sBIT')[:1].hex()
        significant_greyscale_bits_0 = int(str_significant_greyscale_bits_0, 16)
        print('Значащие биты серого 0: {0}'.format(significant_greyscale_bits_0))

        str_significant_red_bits_2_3 = self.chunks.get('sBIT')[1:2].hex()
        significant_red_bits_2_3 = int(str_significant_red_bits_2_3, 16)
        print('Значащие биты красного 2 и 3: {0}'.format(significant_red_bits_2_3))

        str_significant_green_bits_2_3 = self.chunks.get('sBIT')[2:3].hex()
        significant_green_bits_2_3 = int(str_significant_green_bits_2_3, 16)
        print('Значащие биты зелёного 2 и 3: {0}'.format(significant_green_bits_2_3))

        str_significant_blue_bits_2_3 = self.chunks.get('sBIT')[3:4].hex()
        significant_blue_bits_2_3 = int(str_significant_blue_bits_2_3, 16)
        print('Значащие биты синего 2 и 3: {0}'.format(significant_blue_bits_2_3))

        str_significant_greyscale_bits_4 = self.chunks.get('sBIT')[4:5].hex()
        significant_greyscale_bits_4 = int(str_significant_greyscale_bits_4, 16)
        print('Значащие биты серого 4: {0}'.format(significant_greyscale_bits_4))

        str_significant_alpha_bits_4 = self.chunks.get('sBIT')[5:6].hex()
        significant_alpha_bits_4 = int(str_significant_alpha_bits_4, 16)
        print('Значительные альфа-биты 4: {0}'.format(significant_alpha_bits_4))

        str_significant_red_bits_6 = self.chunks.get('sBIT')[6:7].hex()
        significant_red_bits_6 = int(str_significant_red_bits_6, 16)
        print('Значащие биты красного 6: {0}'.format(significant_red_bits_6))

        str_significant_green_bits_6 = self.chunks.get('sBIT')[7:8].hex()
        significant_green_bits_6 = int(str_significant_green_bits_6, 16)
        print('Значащие биты зелёного 6: {0}'.format(significant_green_bits_6))

        str_significant_blue_bits_6 = self.chunks.get('sBIT')[8:9].hex()
        significant_blue_bits_6 = int(str_significant_blue_bits_6, 16)
        print('Значащие биты синего 6: {0}'.format(significant_blue_bits_6))

        str_significant_alpha_bits_6 = self.chunks.get('sBIT')[9:10].hex()
        significant_alpha_bits_6 = int(str_significant_alpha_bits_6, 16)
        print('Значительные альфа-биты 6: {0}'.format(significant_alpha_bits_6))

    def sRGB(self):
        str_rendering_intent = self.chunks.get('sRGB')[:4].hex()
        rendering_intent = int(str_rendering_intent, 16)
        print('Рендеринг: {0}'.format(rendering_intent))

    def tEXt(self):
        index = self.chunks.get('tEXt').find(b'\x00')

        str_keyword = self.chunks.get('tEXt')[:index].hex()
        keyword = int(str_keyword, 16)
        print('Ключевое слово: {0}'.format(keyword))

        str_text_string = self.chunks.get('tEXt')[index+1:].hex()
        text_string = int(str_text_string, 16)
        print('Текстовая строка: {0}'.format(text_string))

    def zTXt(self):
        index = self.chunks.get('zTXt').find(b'\x00')

        str_keyword = self.chunks.get('zTXt')[:index].hex()
        keyword = int(str_keyword, 16)
        print('Ключевое слово: {0}'.format(keyword))

        str_compression_method = self.chunks.get('zTXt')[index + 1:index+2].hex()
        compression_method = int(str_compression_method, 16)
        print('Метод сжатия: {0}'.format(compression_method))

        str_compressed_text_datastream = self.chunks.get('zTXt')[index + 2:].hex()
        compressed_text_datastream = int(str_compressed_text_datastream, 16)
        print('Сжатый текстовый поток данных: {0}'.format(compressed_text_datastream))

    def iTXt(self):
        index_1 = self.chunks.get('iTXt').find(b'\x00')
        index_2 = self.chunks.get('iTXt')[index_1:].find(b'\x00')
        index_3 = self.chunks.get('iTXt')[index_2:].find(b'\x00')

        str_keyword = self.chunks.get('iTXt')[:index_1].hex()
        keyword = int(str_keyword, 16)
        print('Ключевое слово: {0}'.format(keyword))

        str_compression_flag = self.chunks.get('iTXt')[index_1 + 1:index_1 + 2].hex()
        compression_flag = int(str_compression_flag, 16)
        print('Флаг сжатия: {0}'.format(compression_flag))

        str_compression_method = self.chunks.get('iTXt')[index_1 + 2:index_1 + 3].hex()
        compression_method = int(str_compression_method, 16)
        print('Метод сжатия: {0}'.format(compression_method))

        str_language_tag = self.chunks.get('iTXt')[index_1 + 3:index_2].hex()
        language_tag = int(str_language_tag, 16)
        print('Языковой тег: {0}'.format(language_tag))

        str_translated_keyword = self.chunks.get('iTXt')[index_2+1:index_3].hex()
        translated_keyword = int(str_translated_keyword, 16)
        print('Транслированное ключевое слово: {0}'.format(translated_keyword))

        str_text = self.chunks.get('iTXt')[index_3 + 1:].hex()
        text = int(str_text, 16)
        print('Текст: {0}'.format(text))

    def bKGD(self):
        str_greyscale = self.chunks.get('bKGD')[:2].hex()
        greyscale = int(str_greyscale, 16)
        print('Серый: {0}'.format(greyscale))

        str_red = self.chunks.get('bKGD')[2:4].hex()
        red = int(str_red, 16)
        print('Красный: {0}'.format(red))

        str_green = self.chunks.get('bKGD')[4:6].hex()
        green = int(str_green, 16)
        print('Зелёный: {0}'.format(green))

        str_blue = self.chunks.get('bKGD')[6:8].hex()
        blue = int(str_blue, 16)
        print('Синий: {0}'.format(blue))

        str_palette_index = self.chunks.get('bKGD')[8:9].hex()
        palette_index = int(str_palette_index, 16)
        print('Индекс палитры: {0}'.format(palette_index))

    def hIST(self):
        str_frequency = self.chunks.get('hIST')[:2].hex()
        frequency = int(str_frequency, 16)
        print('Частота: {0}'.format(frequency))

        str_etc = self.chunks.get('hIST')[2:].hex()
        etc = int(str_etc, 16)
        print('и т.д.: {0}'.format(etc))

    def pHYs(self):
        str_pixels_per_unit_X_axis = self.chunks.get('pHYs')[:4].hex()
        pixels_per_unit_X_axis = int(str_pixels_per_unit_X_axis, 16)
        print('Пиксели на единицу, ось X: {0}'.format(pixels_per_unit_X_axis))

        str_pixels_per_unit_Y_axis = self.chunks.get('pHYs')[4:8].hex()
        pixels_per_unit_Y_axis = int(str_pixels_per_unit_Y_axis, 16)
        print('Пиксели на единицу, ось Y: {0}'.format(pixels_per_unit_Y_axis))

        str_unit_specifier = self.chunks.get('pHYs')[8:12].hex()
        unit_specifier = int(str_unit_specifier, 16)
        print('Спецификатор блока: {0}'.format(unit_specifier))

    def sPLT(self):
        index = self.chunks.get('sPLT').find(b'\x00')
        str_palette_name = self.chunks.get('sPLT')[:index].hex()
        palette_name = int(str_palette_name, 16)
        print('Название палитры: {0}'.format(palette_name))

        str_sample_depth = self.chunks.get('sPLT')[index+1:index+2].hex()
        sample_depth = int(str_sample_depth, 16)
        print('Глубина образца: {0}'.format(sample_depth))

        str_red = self.chunks.get('sPLT')[index + 2:index + 3].hex()
        red = int(str_red, 16)
        print('Красный: {0}'.format(red))

        str_green = self.chunks.get('sPLT')[index + 3:index + 4].hex()
        green = int(str_green, 16)
        print('Зелёный: {0}'.format(green))

        str_blue = self.chunks.get('sPLT')[index + 4:index + 5].hex()
        blue = int(str_blue, 16)
        print('Синий: {0}'.format(blue))

        str_alpha = self.chunks.get('sPLT')[index + 5:index + 6].hex()
        alpha = int(str_alpha, 16)
        print('Альфа: {0}'.format(alpha))

        str_frequency = self.chunks.get('sPLT')[index + 6:index + 8].hex()
        frequency = int(str_frequency, 16)
        print('Частота: {0}'.format(frequency))

if __name__ == '__main__':
    analysis("images/facebook.png", "all")
    #analysis(sys.argv[1], sys.argv[2])
    sys.exit()
