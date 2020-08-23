import random

class Forca:
    __lista_temas = ['1. INFORMÁTICA','2. FRUTAS','3. CARROS','4. MÓVEIS','5. CORES']
    __lista_informatica = ['MOUSE','TECLADO','MONITOR','IMPRESSORA']
    __lista_frutas = ['BANANA','ABACAXI','INGA','MANGA','MELANCIA','MARACUJA']
    __lista_carros = ['PALIO','GOL','SIENNA','PRISMA','ONIX']
    __lista_moveis = ['SOFA','MESA','CADEIRA','CAMA','ARMARIO','BERCO']
    __lista_cores = ['VERDE','AMARELO','AZUL','BRANCO','VERMELHO','ROSA','ROXO']

    __listas = [__lista_informatica,__lista_frutas,__lista_carros,__lista_moveis,__lista_cores]

    __lista_forca = ["\33[37m ╔══════════╗\033[0;0m",
                     "\33[37m ║\033[0;0m",
                     "\33[37m ║\033[0;0m",
                     "\33[37m ║\033[0;0m",
                     "\33[37m ║\033[0;0m",
                     "\33[37m═╩═\033[0;0m"]
    __lista_corpo = ["\33[37m ║         \033[0;0m"+"\033[33mºoº"+"\033[0;0m",
                     "\33[37m ║          \033[0;0m"+"\033[36m▒\033[0;0m",
                     "\33[37m ║         \033[0;0m"+"\033[33m/"+"\033[36m▒\033[0;0m",
                     "\33[37m ║         \033[0;0m"+"\033[33m/"+"\033[36m▒\033[33m"+chr(92)+"\033[0;0m",
                     "\33[37m ║         \033[0;0m"+"\033[33m/\033[0;0m",
                     "\33[37m ║         \033[0;0m"+"\033[33m/ "+chr(92)+"\033[0;0m"]

    __limite_tentativas = 6
    __palavra = ''
    __masc = ''
    __letras_digitadas = ''

    def __init__(self, tema = 0):
        self.__tema = tema

    @property
    def lista_temas(self):
        return self.__lista_temas

    @property
    def get_tema(self):
        return self.__tema

    def set_tema(self, tema_escolhido):
        self.__tema = tema_escolhido
        self.escolhe_palavra(self.__tema)

    # def __get_tema(self):
    #     return self.__tema
    #
    # def __set_tema(self, tema):
    #     self.__tema = tema
    #
    # tema = property(__get_tema(), __set_tema())

    @property
    def quantidade(self):
        return len(self.__palavra)

    @property
    def tentativas(self):
        return self.__limite_tentativas

    def tentativas_(self):
        self.__limite_tentativas -= 1

    def cls(self):
        for i in range(1,10):
            print("")

    def escolhe_palavra(self, tema):
        lista = self.__listas[tema-1]
        self.__tema = self.__lista_temas[self.__tema-1]
        self.__palavra = random.choice(lista)

    def cabecalho(self):
        self.cls()
        print("JOGO DA FORCA EM PYTHON")
        print("-----------------------")
        print("Dicas:",self.get_tema[3:],"com",self.quantidade,"letras")
        print(f'Você tem {self.__limite_tentativas} tentativas. Teclas digitadas:',self.__letras_digitadas)

    def monta_forca(self):
        self.cabecalho()
        for i in range(0,len(self.__lista_forca)):
            print(self.__lista_forca[i])
        print("")

    def palavra(self):
        return f'Palavra secreta: {self.__masc}'

    def mascara(self):
        for i in range(0,self.quantidade):
            self.__masc += '_ '

    def valida(self, letra_digitada):
        letra_digitada = letra_digitada.upper()
        palavra = ''
        for i in range(0,len(self.__palavra)):
            palavra += self.__palavra[i]
            if i < len(self.__palavra):
                palavra += " "
        if letra_digitada in palavra:
            masc = list(self.__masc)
            indice = 0
            for letra in palavra:
                if letra_digitada == letra:
                    masc[indice] = letra_digitada
                indice += 1
            self.__masc = "".join(masc)
            print("")
            if self.__masc == palavra:
                return True
        else:
            if self.tentativas == 6:
                self.__lista_forca[1] = self.__lista_corpo[0]
            elif self.tentativas == 5:
                self.__lista_forca[2] = self.__lista_corpo[1]
            elif self.tentativas == 4:
                self.__lista_forca[2] = self.__lista_corpo[2]
            elif self.tentativas == 3:
                self.__lista_forca[2] = self.__lista_corpo[3]
            elif self.tentativas == 2:
                self.__lista_forca[3] = self.__lista_corpo[4]
            elif self.tentativas == 1:
                self.__lista_forca[3] = self.__lista_corpo[5]
            self.tentativas_()
            self.__letras_digitadas += letra_digitada + " "
        return False

    @property
    def letras_digitadas(self):
        return self.__letras_digitadas
# 177 ▒
# 186
# 187
# 201
# 205
#  ╔══════════╗
#  ║         ºoº
#  ║         /▒\
#  ║         / \
#  ║
# ═╩═

