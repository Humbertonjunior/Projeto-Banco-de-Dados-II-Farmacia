import mysql.connector
import random
from faker import Faker
from banco_gerador import CriarBanco

nomes_masculinos = ["Alexandre", "Bruno", "Carlos", "Diego", "Eduardo", "Fábio", "Gustavo", "Henrique", "Igor",
                    "João", "Kleber", "Lucas", "Marcelo", "Nelson", "Otávio", "Pedro", "Rafael", "Sérgio",
                    "Thiago", "Vitor", "Wagner", "Xavier", "Yuri", "Zé"]

sobrenomes_masculinos = ["Silva", "Santos", "Oliveira", "Souza", "Costa", "Pereira", "Rodrigues", "Almeida",
                         "Nascimento", "Fernandes", "Gonçalves", "Carvalho", "Gomes", "Mendes", "Lima", "Araújo",
                         "Ribeiro", "Barbosa", "Martins", "Moreira", "Cardoso", "Teixeira", "Correia", "Cavalcanti",
                         "Ferreira"]

sobrenomes_diferentes = ["Moura", "Menezes", "Castro", "Mello", "Furtado", "Vasconcelos", "Calixto", "Bastos",
                         "Goulart",
                         "Fagundes", "Coutinho", "Lacerda", "Albuquerque", "Prado", "Guimarães", "Pimentel", "Rocha",
                         "Leal", "Fonseca", "Alcântara", "Miranda", "Xavier", "Coelho", "Camargo", "Aragão"]

nomes_femininos = ["Ana", "Bianca", "Camila", "Daniela", "Eduarda", "Fernanda", "Gabriela", "Helena", "Isabela",
                   "Julia",
                   "Kamila", "Larissa", "Mariana", "Nathalia", "Olivia", "Priscila", "Rafaela", "Sophia", "Tatiana",
                   "Valentina",
                   "Agatha", "Beatriz", "Clarissa", "Dandara", "Elisa", "Fabiana", "Gabriella", "Heloísa", "Isadora",
                   "Júlia", "Karina"]
def criar_nome(counter):
    if counter >= 300:
        nomes = random.choice(nomes_masculinos)
    else:
        nomes = random.choice(nomes_femininos)
    sobrenome = random.choice(sobrenomes_masculinos)
    nome_final = random.choice(sobrenomes_diferentes)
    return str((nomes + " " + sobrenome + " " + nome_final))
def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    soma = sum([cpf[_] * (10 - i) for _ in range(9)])
    resto = 11 - (soma % 11)
    cpf.append(resto if resto <= 9 else 0)
    soma = sum([cpf[_] * (11 - i) for _ in range(10)])
    resto = 11 - (soma % 11)
    cpf.append(resto if resto <= 9 else 0)
    return f"{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}"
def gerar_data_nascimento():
    fake = Faker()
    data_str = fake.date()
    return data_str
def endereco():
    fake = Faker()
    address = fake.address()
    return address
def cnpj():
    fake = Faker("pt_BR")
    cnpj = fake.cnpj()
    return cnpj
def telefone():
    fake = Faker("pt_BR")
    telefone = fake.phone_number()
    return telefone
def pagamento():
    pagamento = ['Boleto', 'Crédito', 'Débito', 'Pix', 'Dinheiro', 'Cheque']
    return random.choice(pagamento)
def nome_produto():
    nome_produto = ['Aciclovir', 'HUMIRA', 'ACETADOTE', 'NEXTERONE', 'RYBREVANT', 'BROVANA', 'ELSPAR', 'ZITHROMAX']
    return random.choice(nome_produto)
def status():
    planos_aluguel = ['Econômico', 'Intermediário', 'Executivo', 'Fim de semana', 'Mensal', 'Fim de ano']
    return random.choice(planos_aluguel)
def Ant_medico():
    antecedentes = ['alergia ao remedio A', 'alergia ao remedio B', 'alergia ao remedio C', 'alergia ao remedio D',  'alergia ao remedio F']
    return random.choice(antecedentes)
def carg_func():
    cargos = ['Gerente', 'farmaceutico(a)', 'atendente', 'enfermeiro',  'secretaria', 'quimico']
    return random.choice(cargos)
def email():
    fake = Faker()
    return fake.email()
def descrição():
    descrições = ['produto com ingredienes selecionados', 'produto feito com materias radioativos', 'te cura da diabetes', 'melhor remedio pra garganta',  'melhor remedio para dor de cabeça']
    return random.choice(descrições)
def form_preparo():
    forma_preparo = ['coloque 50 gramas de iluio', 'coloque 100 gramas de rtyu e 200 ml de yiakut', 'coloque 100ml de agua e coloque 100 gramas de viou', 'coloque 100 gramas de viou e 200 ml de yiakut']
    return random.choice(forma_preparo )
def descrição_categoria():
    desc_categoria = ['referencia', 'generico', 'similar']
    return random.choice(desc_categoria)
def tipo_analise():
    fake = Faker()
    return fake.ascii_company_email()

def resultado_analise():
    result_anal = ['correta', 'incorreta', 'impropria', 'propria', 'errada']
    return random.choice(result_anal)
def observação_analise():
    obs_anal = ['esse produto está perto do vencimento', 'este produto está perfeito', 'produto vencido', 'produto dentro da validade']
    return random.choice(obs_anal)
def nome_insumo():
    nme_ins = ['agua', 'pedra', 'alcool', 'adubo', 'folhas', 'cloridrato', 'cloro', 'sal', 'açucar', 'ferro']
    return random.choice(nme_ins)
def orientacao():
    nme_ins = ['3 vezes por semana', '1 vez por dia', '2 vezes por mês', 'não tomar banho após uso', 'tomar antes de dormir', 'não tomar alcool', 'não comer por 40 minutos', 'não saia do quarto ꒰ϱ﹏-๑꒱', 'não praticar exercício']
    return random.choice(nme_ins)
def preço():
    preço1 = random.randint(200, 500)
    return preço1
def contato():
    fake = Faker()
    return fake.email()
def data():
    year = random.randint(2017, 2022)
    month = random.randint(1, 12)
    day = random.randint(1, 29)
    data = f"{year}-{month}-{day}"
    return data
def codigo():
    codigo = ""
    for _ in range(10):
        codigo += str(random.randint(0, 9))
    return codigo


usuario = "root"
senha = ""
cnx = mysql.connector.connect(user=usuario, password=senha, host='localhost')
cursor = cnx.cursor()
create_BG = CriarBanco(usuario, senha)
if int(input("Você ja criou a tabela?(digite 1 se sim e 0 não): ")) == 0:
    create_BG.main()
cursor.execute("USE `Farmácia`;")
cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
i = 0
for z in range(10):
    data_nascimento = gerar_data_nascimento()
    cpf = gerar_cpf()

    cursor.execute("INSERT INTO Cliente VALUES(%s,%s,%s,%s,%s,%s,%s);",
                       [i, criar_nome(i), cpf, endereco(),
                        telefone(), email(), Ant_medico()])
    cursor.execute("INSERT INTO Funcionário(nome_funcionario,cpf_funcionario,cargo_funcionario,Data_de_admissão_funcionario,Pedido_id_Pedido) VALUES(%s,%s,%s,%s,%s);",
        [criar_nome(i), gerar_cpf(), carg_func(),data_nascimento,i])
    CNPJ_juridico = cnpj()
    while True:
        try:
            cursor.execute("SELECT 1 FROM Fornecedor WHERE Cnpj_fornecedor = %s;", [CNPJ_juridico])
            result = cursor.fetchone()
            if result:
                CNPJ_juridico = cnpj()
            else:
                break
        except Exception as e:
            print("Erro ao verificar duplicidade de CNPJ:", e)
            break
    cursor.execute("INSERT INTO Fornecedor(nome_fornecedor,endereço_fornecedor,preço_insumo,telefone_fornecedor,Cnpj_fornecedor) VALUES(%s,%s,%s,%s,%s);",
                   [criar_nome(i),endereco(),preço() ,telefone(), cnpj()])
    cursor.execute(
        "INSERT INTO Produto(nome_produto,Código_produto,descrição_produto,forma_de_preparo) VALUES(%s,%s,%s,%s);",
        [nome_produto(), codigo(), descrição(),form_preparo()])
    cursor.execute("INSERT INTO Categoria VALUES(%s,%s,%s,%s);", [codigo(), descrição_categoria(), descrição_categoria(), descrição_categoria()])
    cursor.execute("INSERT INTO `Análise e controle de qualidade`(tipo_analise,Data_analise,resultado_analise,Observações) VALUES(%s,%s,%s,%s);",
                   [tipo_analise(), data_nascimento, resultado_analise(), observação_analise()])
    cursor.execute("INSERT INTO `Insumo`(nome_insumo,validade_insumo,estoque_insumo) VALUES(%s,%s,%s);",
                   [tipo_analise(), gerar_data_nascimento(), random.randint(0, 1700)])

    cursor.execute("INSERT INTO `Pagamento` VALUES(%s,%s,%s,%s);", [preço(),pagamento(),i,status()])

    cursor.execute("INSERT INTO `Item`(quantidade_item,preco_unitario_item,Pedido_id_Pedido,Produto_id_Produto) VALUES(%s,%s,%s,%s);",
                   [random.randint(0, 1700), preço(),i,i])
    cursor.execute("INSERT INTO `Pedido`(Data_pedido,valor_total_item,Status_pedido,Cliente_id_cliente,Cliente_cpf,Prescrição_id_prescrição) VALUES(%s,%s,%s,%s,%s,%s);",
                   [gerar_data_nascimento(),preço(), status(), i, cpf, i])
    cursor.execute("INSERT INTO Prescrição(produto,descrição,orientação)VALUES(%s,%s,%s);",
                   [nome_produto(), descrição(), orientacao()])
    cursor.execute("INSERT INTO `Insumo_has_Produto` VALUES(%s,%s);", [nome_insumo(), i])
    cursor.execute("INSERT INTO `Pedido_has_Cliente` VALUES(%s,%s,%s);", [i, i, cpf])
    cursor.execute("INSERT INTO `Categoria_has_Produto` VALUES(%s,%s);", [codigo(), i])
    cursor.execute(f"INSERT INTO `Fornecedor_has_Insumo` VALUES(%s,%s);", [i, tipo_analise()])
    i += 1
cnx.commit()
cursor.close()
cnx.close()
print("Dados falsos inserido com sucesso!")