import psycopg2
from psycopg2 import sql

def conectar():
    try:
        conn = psycopg2.connect(
            dbname="projeto_mandala",
            user="postgres",
            password="1221",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def cadastrar_cliente():
    conn = conectar()
    if conn is None:
        return
    try:
        nome = input("Digite o nome do cliente: ")
        end_rua = input("Digite a rua: ")
        end_logradouro = input("Digite o logradouro: ")
        end_numero = input("Digite o número: ")
        end_bairro = input("Digite o bairro: ")
        end_cidade = input("Digite a cidade: ")
        end_estado = input("Digite o estado: ")
        end_cep = input("Digite o CEP: ")

        with conn.cursor() as cursor:
            query = sql.SQL("""
                INSERT INTO cliente (nome, end_rua, end_logradouro, end_numero, end_bairro, end_cidade, end_estado, end_cep)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """)
            cursor.execute(query, (nome, end_rua, end_logradouro, end_numero, end_bairro, end_cidade, end_estado, end_cep))
            conn.commit()
        print("Cliente cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar cliente: {e}")
        conn.rollback()
    finally:
        conn.close()

def buscar_clientes_por_nome(nome):
    conn = conectar()
    if conn is None:
        return []
    try:
        with conn.cursor() as cursor:
            query = sql.SQL("""
                SELECT id, nome FROM cliente WHERE nome ILIKE %s
            """)
            cursor.execute(query, (f"{nome}%",))
            clientes = cursor.fetchall()
            return clientes
    except Exception as e:
        print(f"Erro ao buscar clientes: {e}")
        return []
    finally:
        conn.close()

def atualizar_cliente():
    conn = conectar()
    if conn is None:
        return
    try:
        nome = input("Digite o primeiro nome do cliente que deseja atualizar: ")
        clientes = buscar_clientes_por_nome(nome)

        if not clientes:
            print("Nenhum cliente encontrado com esse nome.")
            return

        print("\nClientes encontrados:")
        for idx, cliente in enumerate(clientes):
            print(f"{idx + 1}. {cliente[1]} (ID: {cliente[0]})")

        escolha = int(input("Escolha o número do cliente que deseja atualizar: ")) - 1
        cliente_id = clientes[escolha][0]

        data_ultimo_pagamento = input("Digite a data do último pagamento (YYYY-MM-DD): ")
        data_cancelamento = input("Digite a data de cancelamento (YYYY-MM-DD) ou deixe em branco se não houver: ")

        print("\nEscolha o plano do cliente:")
        print("1. Plano Diário")
        print("2. Plano 2x na Semana")
        print("3. Plano 3x na Semana")
        plano_escolha = input("Escolha o número do plano: ")

        planos = {
            '1': 'Plano Diário',
            '2': 'Plano 2x na Semana',
            '3': 'Plano 3x na Semana'
        }
        plano_contratado = planos.get(plano_escolha, None)

        if plano_contratado is None:
            print("Plano inválido.")
            return

        with conn.cursor() as cursor:
            query = sql.SQL("""
                UPDATE matricula
                SET data_ultimo_pagamento = %s, data_cancelamento = %s, plano_contratado = %s
                WHERE cliente_id = %s
            """)
            cursor.execute(query, (data_ultimo_pagamento, data_cancelamento if data_cancelamento else None, plano_contratado, cliente_id))
            conn.commit()
        print("Dados do cliente atualizados com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar cliente: {e}")
        conn.rollback()
    finally:
        conn.close()

def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Cliente")
        print("2. Atualizar Cliente (Data de Cancelamento, Último Pagamento e Plano)")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_cliente()
        elif escolha == '2':
            atualizar_cliente()
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()