    # ListaIngredientes = ["1/2 xícara de farinha", "1/2 xícara de açúcar", "1/2 xícara de água ou leite",
    #     "Manteiga com sal em temperatura ambiente para cobertura"]

    # ListaPassos = ["Despeje a farinha em uma tigela média", 
    #     "Coloque o açúcar na tigela junto com a farinha",
    #     "Despeje água ou leite na tigela"," Misture tudo e bata até que tudo esteja bem homogêneo", 
    #     "Coloque a frigideira no fogão.", "Deixe o fogo médio e espere a frigideira aquecer.", 
    #     "Despeje um pouco da massa na frigideira. Tente deixar um formato circular ou oval.",
    #     "Espere um ou dois minutos até a massa cozinhar completamente.",
    #     "Use uma espátula para virar e tirar a panqueca da frigideira.",
    #     "Empilhe-as em um prato conforme for cozinhando-as. Continue até usar toda a massa.",
    #     "Coloque todas as panquecas em um prato e espere até que elas esfriem.",
    #     "Pronto! Agora é só aproveitar!"
# ]

class ReceitaPanqueca():

    def __init__(self, panqueca, farinha, acucar, leite, manteiga):
        self.panqueca = panqueca
        self.farinha = farinha
        self.acucar = acucar
        self.leite = leite
        self.manteiga = manteiga

    def get_all (self):
        print("Essa receita é de {} e leva 1/2 de {}, 1/2 de {}, 1/2 de {} e {} com sal em temperatura ambiente".format(self.panqueca, self.farinha, self.acucar, self.leite, self.manteiga))

abobrinha = ReceitaPanqueca( 'panqueca', 1/2, 1/2, 1/2, 1/2 )
abobrinha.get_all()

class ReceitaBolo(ReceitaPanqueca):

    def __init__(self, bolo, farinha, acucar, leite, manteiga):
        self.bolo = bolo
        self.farinha = farinha
        self.acucar = acucar
        self.leite = leite
        self.manteiga = manteiga
    def get_all (self):
        print("Essa receita é de {} e leva 1/2 de {}, 1/2 de {}, 1/2 de {} e {} com sal em temperatura ambiente".format(self.bolo, self.farinha, self.acucar, self.leite, self.manteiga))
bolo_de_cenoura = ReceitaBolo("bolo", "farinha", "2 xicaras", "1 xicara", "1 colher")

bolo_de_cenoura.get_all()
