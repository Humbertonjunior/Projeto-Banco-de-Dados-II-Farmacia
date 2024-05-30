import mysql.connector


class CriarBanco:
    def __init__(self, usuario, senha):
        self.cnx = mysql.connector.connect(user=usuario, password=senha, host='localhost')
        print("Conectado= ", self.cnx.is_connected())
        self.cursor = self.cnx.cursor()
        self.cursor.execute("CREATE SCHEMA IF NOT EXISTS `Farmácia` DEFAULT CHARACTER SET utf8;")
        self.cursor.execute("USE `Farmácia`;")
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
        print("---Banco Criado com sucesso!---")

    def cliente(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Cliente` (
                `id_cliente` INT NOT NULL AUTO_INCREMENT,
                `nome_cliente` VARCHAR(50) NOT NULL,
                `cpf_cliente` VARCHAR(20) NOT NULL,
                `endereço_cliente` VARCHAR(50) NULL,
                `telefone_cliente` VARCHAR(20) NOT NULL,
                `e-mail_cliente` VARCHAR(50) NULL,
                `Antecedente médico` LONGTEXT NULL,
                PRIMARY KEY (`id_cliente`, `cpf_cliente`))
                ENGINE = InnoDB;'''
        self.cursor.execute(sql)
        print("------Tabela cliente criada com sucesso!------")

    def prescricao(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Prescrição` (
                 `id_prescrição` INT NOT NULL AUTO_INCREMENT,
                 `produto` VARCHAR(30) NOT NULL,
                 `descrição` LONGTEXT NULL,
                 `orientação` LONGTEXT NOT NULL,
                  PRIMARY KEY (`id_prescrição`))
                 ENGINE = InnoDB;'''
        self.cursor.execute(sql)
        print("------Tabela prescricao criada com sucesso!------")

    def pedido(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Pedido` (
        `id_Pedido` INT NOT NULL AUTO_INCREMENT,
        `valor_total_item` DECIMAL(10,2) NOT NULL,
        `Data_pedido` DATE NOT NULL,
        `Status_pedido` VARCHAR(50) NOT NULL,
        `Cliente_id_cliente` INT NOT NULL,
        `Cliente_cpf` VARCHAR(20) NOT NULL,
        `Prescrição_id_prescrição` INT NOT NULL,
        PRIMARY KEY (`id_Pedido`),
        CONSTRAINT `fk_Pedido_Cliente1`
        FOREIGN KEY (`Cliente_id_cliente` , `Cliente_cpf`)
        REFERENCES `Farmácia`.`Cliente` (`id_cliente` , `cpf_cliente`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
        CONSTRAINT `fk_Pedido_Prescrição1`
        FOREIGN KEY (`Prescrição_id_prescrição`)
        REFERENCES `Farmácia`.`Prescrição` (`id_prescrição`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
        ENGINE = InnoDB;'''
        self.cursor.execute(sql)
        print("------Tabela pedido criada com sucesso!------")

    def Funcionario(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Funcionário` (
                `id_Funcionário` INT NOT NULL AUTO_INCREMENT,
                `nome_funcionario` VARCHAR(50) NOT NULL,
                `cpf_funcionario` VARCHAR(20) NOT NULL,
                `cargo_funcionario` VARCHAR(40) NOT NULL,
                `Data_de_admissão_funcionario` DATE NOT NULL,
                `Pedido_id_Pedido` INT NOT NULL,
                PRIMARY KEY (`id_Funcionário`),
                CONSTRAINT `fk_Funcionário_Pedido1`
                FOREIGN KEY (`Pedido_id_Pedido`)
                REFERENCES `Farmácia`.`Pedido` (`id_Pedido`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)
                ENGINE = InnoDB;'''
        self.cursor.execute(sql)
        print("------Tabela Funcionario criada com sucesso!------")

    def Produto(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Produto` (
                `id_Produto` INT NOT NULL AUTO_INCREMENT,
                `nome_produto` VARCHAR(45) NOT NULL,
                `Código_produto` VARCHAR(30) NOT NULL,
                `descrição_produto` LONGTEXT NOT NULL,
                `forma_de_preparo` LONGTEXT NOT NULL,
                PRIMARY KEY (`id_Produto`))
                ENGINE = InnoDB;'''
        self.cursor.execute(sql)
        print("------Tabela Produto criada com sucesso!------")

    def Categoria(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Categoria` (
                `código_categoria` VARCHAR(30) NOT NULL,
                `descrição_categoria` LONGTEXT NOT NULL,
                `nome_categoria` VARCHAR(45) NOT NULL,
                `tipo_categoria` VARCHAR(50) NOT NULL,
                PRIMARY KEY (`código_categoria`))
                ENGINE = InnoDB;'''
        self.cursor.execute(sql)
        print("------Tabela Categoria criada com sucesso!------")

    def Insumo(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Insumo` (
                `nome_insumo` VARCHAR(45) NOT NULL,
                `validade_insumo` DATE NOT NULL,
                `estoque_insumo` VARCHAR(50) NOT NULL,
                 PRIMARY KEY (`nome_insumo`))
                ENGINE = InnoDB;'''
        self.cursor.execute(sql)
        print("------Tabela Insumo criada com sucesso!------")

    def Fornecedor(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Fornecedor` (
                `id_Fornecedor` INT NOT NULL AUTO_INCREMENT,
                `nome_fornecedor` VARCHAR(45) NOT NULL,
                `preço_insumo` DECIMAL(10,2) NOT NULL,
                `endereço_fornecedor` LONGTEXT NOT NULL,
                `telefone_fornecedor` VARCHAR(20) NOT NULL,
                `Cnpj_fornecedor` VARCHAR(30) NOT NULL,
                PRIMARY KEY (`id_Fornecedor`))
                ENGINE = InnoDB;'''
        self.cursor.execute(sql)
        print("------Tabela Fornecedor criada com sucesso!------")



    def Pagamento(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Pagamento` (
                `Valor_a_ser_pago` DECIMAL(10,2) NOT NULL,
                `metodo_de_pagamento` VARCHAR(45) NOT NULL,
                `Pedido_id_Pedido` INT NOT NULL,
                `status_pagamento` VARCHAR(45) NOT NULL,
                PRIMARY KEY (`Pedido_id_Pedido`),
                CONSTRAINT `fk_Pagamento_Pedido1`
                FOREIGN KEY (`Pedido_id_Pedido`)
                REFERENCES `Farmácia`.`Pedido` (`id_Pedido`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)
                ENGINE = InnoDB;'''
        self.cursor.execute(sql)
        print("------Tabela Tem Pagamento com sucesso!------")

    def Item(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Item` (
                `idt_item` INT NOT NULL AUTO_INCREMENT,
                `quantidade_item` VARCHAR(20) NOT NULL,
                `preco_unitario_item` DECIMAL(10,2) NOT NULL,
                `Pedido_id_Pedido` INT NOT NULL,
                `Produto_id_Produto` INT NOT NULL,
                PRIMARY KEY (`idt_item`),
                CONSTRAINT `fk_Item_Pedido1`
                FOREIGN KEY (`Pedido_id_Pedido`)
                REFERENCES `Farmácia`.`Pedido` (`id_Pedido`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
                CONSTRAINT `fk_Item_Produto1`
                FOREIGN KEY (`Produto_id_Produto`)
                REFERENCES `Farmácia`.`Produto` (`id_Produto`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)
                ENGINE = InnoDB;'''
        self.cursor.execute(sql)
        print("------Tabela Item criada com sucesso!------")

    def Pedido_has_Cliente(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Pedido_has_Cliente` (
                `Pedido_id_Pedido` INT NOT NULL,
                `Cliente_id_cliente` INT NOT NULL,
                `Cliente_cpf` VARCHAR(20) NOT NULL,
                PRIMARY KEY (`Pedido_id_Pedido`, `Cliente_id_cliente`, `Cliente_cpf`),
                CONSTRAINT `fk_Pedido_has_Cliente_Pedido1`
                FOREIGN KEY (`Pedido_id_Pedido`)
                REFERENCES `Farmácia`.`Pedido` (`id_Pedido`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
                CONSTRAINT `fk_Pedido_has_Cliente_Cliente1`
                FOREIGN KEY (`Cliente_id_cliente` , `Cliente_cpf`)
                REFERENCES `Farmácia`.`Cliente` (`id_cliente` , `cpf_cliente`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)
                ENGINE = InnoDB;'''
        self.cursor.execute(sql)
        print("------Tabela Pedido_has_Cliente criada com sucesso!------")

    def Insumo_has_Produto(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Insumo_has_Produto` (
                `Insumo_nome_insumo` VARCHAR(45) NOT NULL,
                `Produto_id_Produto` INT NOT NULL,
                CONSTRAINT `fk_Insumo_has_Produto_Insumo1`
                FOREIGN KEY (`Insumo_nome_insumo`)
                REFERENCES `Farmácia`.`Insumo` (`nome_insumo`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
                CONSTRAINT `fk_Insumo_has_Produto_Produto1`
                FOREIGN KEY (`Produto_id_Produto`)
                REFERENCES `Farmácia`.`Produto` (`id_Produto`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)
                ENGINE = InnoDB;'''
        self.cursor.execute(sql)
        print("------Tabela Insumo_has_Produto criada com sucesso!------")

    def Categoria_has_Produto(self):
            sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Categoria_has_Produto` (
                    `Categoria_código_categoria` VARCHAR(30) NOT NULL,
                    `Produto_id_Produto` INT NOT NULL,
                    PRIMARY KEY (`Categoria_código_categoria`, `Produto_id_Produto`),
                   CONSTRAINT `fk_Categoria_has_Produto_Categoria1`
                    FOREIGN KEY (`Categoria_código_categoria`)
                    REFERENCES `Farmácia`.`Categoria` (`código_categoria`)
                    ON DELETE NO ACTION
                    ON UPDATE NO ACTION,
                    CONSTRAINT `fk_Categoria_has_Produto_Produto1`
                    FOREIGN KEY (`Produto_id_Produto`)
                    REFERENCES `Farmácia`.`Produto` (`id_Produto`)
                    ON DELETE NO ACTION
                    ON UPDATE NO ACTION)
                    ENGINE = InnoDB;'''
            self.cursor.execute(sql)
            print("------Tabela Categoria_has_Produto criada com sucesso!------")

    def Fornecedor_has_Insumo(self):
            sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Fornecedor_has_Insumo` (
                    `Fornecedor_id_Fornecedor` INT NOT NULL,
                    `Insumo_nome_insumo` VARCHAR(45) NOT NULL,
                    PRIMARY KEY (`Insumo_nome_insumo`),
                    INDEX `fk_Fornecedor_has_Insumo_Insumo1_idx` (`Insumo_nome_insumo` ASC),
                    INDEX `fk_Fornecedor_has_Insumo_Fornecedor1_idx` (`Fornecedor_id_Fornecedor` ASC),
                    CONSTRAINT `fk_Fornecedor_has_Insumo_Fornecedor1`
                    FOREIGN KEY (`Fornecedor_id_Fornecedor`)
                    REFERENCES `Farmácia`.`Fornecedor` (`id_Fornecedor`)
                    ON DELETE NO ACTION
                    ON UPDATE NO ACTION,
                    CONSTRAINT `fk_Fornecedor_has_Insumo_Insumo1`
                    FOREIGN KEY (`Insumo_nome_insumo`)
                    REFERENCES `Farmácia`.`Insumo` (`nome_insumo`)
                    ON DELETE NO ACTION
                    ON UPDATE NO ACTION)
                    ENGINE = InnoDB;'''
            self.cursor.execute(sql)
            print("------Tabela Fornecedor_has_Insumo criada com sucesso!------")

    def Análise_e_controle_de_qualidade(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Farmácia`.`Análise e controle de qualidade` (
  `tipo_analise` VARCHAR(30) NOT NULL,
  `Data_analise` DATE NOT NULL,
  `resultado_analise` LONGTEXT NOT NULL,
  `Observações` LONGTEXT NULL,
  `Insumo_nome_insumo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`tipo_analise`),
  CONSTRAINT `fk_Análise e controle de qualidade_Insumo1`
    FOREIGN KEY (`Insumo_nome_insumo`)
    REFERENCES `Farmácia`.`Insumo` (`nome_insumo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;'''
        self.cursor.execute(sql)
        print("------Tabela Análise e controle de qualidade criada com sucesso!------")

    def main(self):
        self.cliente()
        self.Funcionario()
        self.prescricao()
        self.Fornecedor()
        self.pedido()
        self.Produto()
        self.Categoria()
        self.Pagamento()
        self.Item()
        self.Pedido_has_Cliente()
        self.Categoria_has_Produto()
        self.Insumo_has_Produto()
        self.Insumo()
        self.Fornecedor_has_Insumo()
        self.Análise_e_controle_de_qualidade()
        self.cnx.commit()
        print("------Tabelas Construidas e alteradas com sucesso!------")
        self.cursor.close()
        self.cnx.close()