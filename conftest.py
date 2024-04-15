import os
import random
import sqlite3


class SetupTest:

    data = None

    def __init__(self):
        self.__generate_data()
        self.__create_database()

    @classmethod
    def __generate_data(cls):

        data = []
        n_row = 1_000_000

        nomes = [
            "Ana", "Beatriz", "Clara", "Gabriela", "Isabella", "Laura",
            "Luiza", "Maria", "Mariana", "Melissa", "Nicole", "Rafaela",
            "Sophia", "Valentina", "Alice", "Amanda", "Bruna", "Carolina",
            "Catarina", "Davi", "Enzo", "Gabriel", "Guilherme", "Henrique",
            "João", "Lucas", "Luís", "Mateus", "Miguel", "Nicolas", "Pedro",
            "Rafael", "Samuel", "Arthur", "Bernardo", "Caio", "Eduardo",
            "Felipe", "Igor", "Leonardo", "Lorenzo", "Marco", "Matheus",
            "Otávio", "Pedro Henrique", "Vinicius", "Yago", "Agatha",
            "Bianca", "Camila", "Débora", "Emily", "Ester", "Giovanna",
            "Júlia", "Letícia", "Lorena", "Manuela", "Marina", "Mirela",
            "Stefany", "Vitória", "Adrielly", "Bárbara", "Beatriz", "Carol",
            "Cecília", "Isabela", "Isadora", "Jennifer", "Larissa", "Lívia",
            "Lorena", "Marcela", "Maria Eduarda", "Melissa", "Nathalia",
            "Rafaela", "Sarah", "Sofia", "Thais", "Vanessa", "Yasmim",
            "Alex", "André", "Bruno", "Carlos", "Daniel", "Diego", "Douglas",
            "Fábio", "Fernando", "Gustavo", "Igor", "João Pedro", "Jonathan",
            "Kevin", "Leonardo", "Lorenzo", "Marcelo", "Marco", "Marcos",
            "Matheus", "Máximo", "Murilo", "Nicolas", "Patrick", "Paulo",
            "Rafael", "Renato", "Ricardo", "Roberto", "Rodrigo", "Thiago",
            "Tomás", "Vicente", "Wagner", "Wesley", "Yan",
        ]

        cidades_brasil = [
            "São Paulo", "Rio de Janeiro", "Salvador", "Brasília", "Fortaleza",
            "Belo Horizonte", "Manaus", "Curitiba", "Recife", "Goiânia", "Belém",
            "Porto Alegre", "São Luís", "Campinas", "São Gonçalo", "Maceió",
            "Duque de Caxias", "Natal", "Teresina", "São Bernardo do Campo",
            "Campo Grande", "Osasco", "Santo André", "João Pessoa",
            "Jaboatão dos Guararapes", "Contagem", "Ribeirão Preto", "Sorocaba",
            "Aracaju", "Cuiabá", "Feira de Santana", "Joinville", "Juiz de Fora",
            "Londrina", "Ananindeua", "Belford Roxo", "Niterói",
            "São João de Meriti", "Aparecida de Goiânia", "Porto Velho",
            "Campos dos Goytacazes", "Caxias do Sul", "Florianópolis",
            "Vila Velha", "São Vicente", "Betim", "Santarém", "Mauá", "Anápolis",
            "Serra"
        ]

        for i in range(n_row):
            data.append({
                'Nome': f'{random.choice(nomes)}',
                'Idade': 20 + i % 10,
                'Cidade': f'{random.choice(cidades_brasil)}'
            })
        cls.data = data

        return cls.data

    @classmethod
    def __create_database(cls):
        conn = sqlite3.connect('mock_data.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS mock_table (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Nome TEXT,
                                Idade INTEGER,
                                Cidade TEXT)''')

        for entry in cls.data:
            cursor.execute('''INSERT INTO mock_table (Nome, Idade, Cidade) VALUES (?, ?, ?)''',
                           (entry['Nome'], entry['Idade'], entry['Cidade']))

        conn.commit()
        conn.close()


class TearDownTest:

    def __init__(self):
        self.__delete_db()

    @staticmethod
    def __delete_db():
        db = 'mock_data.db'
        csv = 'output.csv'

        if os.path.exists(db):
            os.remove(db)
            print(f"Arquivo {db} excluído com sucesso!")
        else:
            print(f"O arquivo {db} não existe.")

        if os.path.exists(csv):
            os.remove(csv)
            print(f"Arquivo {csv} excluído com sucesso!")
        else:
            print(f"O arquivo {csv} não existe.")