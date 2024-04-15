    
# stream de dados

Um pequeno pedaço de código para realizaçar stream de dados entre um banco e um arquivo .csv

o código levanta um banco de dados SQLite chamado **mock_data.db**, sendo que a quantidade de linhas você poderá customizar no arquivo conftest.py na variável **n_row**. Todos os dados são dados mockados aleatoriamente.


## Instalação

Para configurar o ambiente, crie um venv

```bash
  python -m venv venv
```
inicie a venv (exemplo windows)

```bash
  ./venv/Scripts/activate
```
instale as dependências

```bash
  pip install -r requirements.txt
```

## Rodando os testes

Para rodar os testes, você poderá rodar da pasta raiz.

```bash
  pytest -v
```

Ou você poderá optar por rodar a própria aplicação em sí

```bash
  python .\main.py
```

Caso queira rodar com os dados de consumo de memória, será criado um arquivo chamado **memory_profiler.log**

```bash
  python -m memory_profiler .\main.py
```