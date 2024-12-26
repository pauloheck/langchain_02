from agents import agente_projeto
def main():
    print("Iniciando o processo...")
    # Exemplo 1: Criar a descição completa do projeto
    input = """
    Você deve criar uma descrição completa de um projeto de desenvolvimento de software.
    O projeto é um sistema de consolidação dos pagamentos realizados por PIX
    Precisa ser descrito claramente contendo Titulo, Descricao, Tecnologias e Diferenciais
    Lista com os riscos do projeto.
    Lista de historias de usuário.
    Lista com os requisitos do projeto.
    Lista com os escopos do projeto.

    """
    output = agente_projeto.run(input)
    print("Projeto:", output)




if __name__ == "__main__":
    main()
