from langchain.agents import initialize_agent
from tools import TecnologiaSugerida, EstimarPrazo
from config import init_llm

# Inicializando o LLM
modelo = init_llm()

# Lista de ferramentas
ferramentas = [
    TecnologiaSugerida(),
    EstimarPrazo(),
]

# Inicializando o agente
agente_projeto = initialize_agent(
    ferramentas,
    modelo,
    agent="zero-shot-react-description",
    verbose=True
)
