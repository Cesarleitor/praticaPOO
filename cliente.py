# PRATICA DE CLASS E POO

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"] # VARIÁVEL FIXA
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano Inválido")

    # MUDAR DE PLANO
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano Inválido")
    # ESCOLHER FILME CONFORME O PLANO
    def ver_filme(self, filme, plano_filme):

        # SE O PLANO DO CLIENTE FOR O MESMO DO FILME, LIBERAR O FILME
        if self.plano == plano_filme:
            print(f"Ver Filme {filme}")

        # SE O PLANO DO CLIENTE FOR PREMIUM, LIBERA QUALQUER FILME
        elif self.plano == "premium":
            print(f"Ver Filme {filme}")

        # SE O PLANO DO CLIENTE FOR BASIC E O FILME FOR DO PLANO PREMIUM, FAÇA UPGRADE PARA PLANO PREMIUM
        elif self.plano == "basic" and plano_filme == "premium":
            print("Faça Upgrade para premium para ver esse filme!")

        # SE NENHUMA DAS ALTERNATIVAS FOREM VALIDADAS. "PLANO INVÁLIDO"
        else:
            print("Plano Inválido!")
