from fastapi import FastAPI

app = FastAPI()

cursos = {
    1: {"Titulo": "Programação Para Leigos",
        "aulas": 112,
        "horas": 58},
    2: {"Titulo": "Augoritimo e Lógica de Programação",
        "aulas": 87,
        "horas": 67}
}

@app.get('/cursos')#cria o endpoint
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')#cria o endpoint
async def get_curso(curso_id: int):
    curso = cursos[curso_id]
    curso.update({"id": curso_id})
    
    return curso


# Verifica se o script está sendo executado diretamente (e não importado como módulo)
# Importa o Uvicorn, que é o servidor ASGI usado para rodar a aplicação FastAPI
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level="info",reload=True)
# Inicia o servidor Uvicorn com as configurações definidas
# Nome do arquivo e da instância do FastAPI
# Define o endereço IP do servidor (localhost)
# # Define a porta onde a API será acessível
# Define o nível de log (info, debug, warning, etc.)
# Habilita o recarregamento automático ao modificar o código (útil para desenvolvimento)
                
