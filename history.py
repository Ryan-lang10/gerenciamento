import random

# Função que gera o início da história 
def gerar_inicio():
    inicio = ["Hoje estamos aprendendo a linguagem Python,"]
    return random.choice(inicio)

# Função que gera o meio da história 
def gerar_meio():
    meio = [
        "Python é uma linguagem de programação orientada a objetos,",
        "Python é interpretada e de uso geral."
    ]
    return random.choice(meio)

# Função que gera o final da história
def gerar_final():
    finais = [
        "e amplamente usada em aplicações web.",
        "usada no desenvolvimento de software.",
        "usada na ciência de dados."
    ]
    return random.choice(finais)

# Função que gera a história
def gerar_historia():
    introducao = gerar_inicio()
    desenvolvimentos = gerar_meio()
    final = gerar_final()

    historia = f"{introducao} {desenvolvimentos} {final}"
    return historia 

# Exibe a história gerada 
if __name__ == "__main__":
    print(gerar_historia())









