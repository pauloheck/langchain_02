from langchain.tools import BaseTool

# Ferramenta: Sugestão de tecnologias
class TecnologiaSugerida(BaseTool):
    name = "SugerirTecnologias"
    description = "Sugere tecnologias e frameworks baseados no tipo de projeto."

    def _run(self, query: str):
        if "frontend" in query.lower():
            return "Sugestão: React"
        elif "backend" in query.lower():
            return "Sugestão: Spring Boot ou Node.js"
        elif "banco de dados" in query.lower():
            return "Sugestão: PostgreSQL, MongoDB"
        else:
            return "Especifique o tipo de tecnologia desejada."

    def _arun(self, query: str):
        raise NotImplementedError("Execução assíncrona não implementada!")

# Ferramenta: Calcular prazos
class EstimarPrazo(BaseTool):
    name = "CalcularPrazo"
    description = "Calcula o prazo estimado com base no número de tarefas e equipe."

    def _run(self, query: str):
        try:
            partes = query.split()
            tarefas = int(partes[0])
            equipe = int(partes[1])
            prazo = (tarefas * 2) / equipe  # Exemplo simples de cálculo
            return f"Prazo estimado: {prazo:.1f} dias."
        except:
            return "Forneça o número de tarefas e o tamanho da equipe, separados por espaço."

    def _arun(self, query: str):
        raise NotImplementedError("Execução assíncrona não implementada!")
