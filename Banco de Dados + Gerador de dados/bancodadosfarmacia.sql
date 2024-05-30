CREATE DATABASE  IF NOT EXISTS `farmácia` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci */;
USE `farmácia`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: farmácia
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.27-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `análise e controle de qualidade`
--

DROP TABLE IF EXISTS `análise e controle de qualidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `análise e controle de qualidade` (
  `tipo_analise` varchar(30) NOT NULL,
  `Data_analise` date NOT NULL,
  `resultado_analise` longtext NOT NULL,
  `Observações` longtext DEFAULT NULL,
  `Insumo_nome_insumo` varchar(45) NOT NULL,
  PRIMARY KEY (`tipo_analise`),
  KEY `fk_Análise e controle de qualidade_Insumo1` (`Insumo_nome_insumo`),
  CONSTRAINT `fk_Análise e controle de qualidade_Insumo1` FOREIGN KEY (`Insumo_nome_insumo`) REFERENCES `insumo` (`nome_insumo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categoria` (
  `código_categoria` varchar(30) NOT NULL,
  `descrição_categoria` longtext NOT NULL,
  `nome_categoria` varchar(45) NOT NULL,
  `tipo_categoria` varchar(50) NOT NULL,
  PRIMARY KEY (`código_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `categoria_has_produto`
--

DROP TABLE IF EXISTS `categoria_has_produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categoria_has_produto` (
  `Categoria_código_categoria` varchar(30) NOT NULL,
  `Produto_id_Produto` int(11) NOT NULL,
  PRIMARY KEY (`Categoria_código_categoria`,`Produto_id_Produto`),
  KEY `fk_Categoria_has_Produto_Produto1` (`Produto_id_Produto`),
  CONSTRAINT `fk_Categoria_has_Produto_Categoria1` FOREIGN KEY (`Categoria_código_categoria`) REFERENCES `categoria` (`código_categoria`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Categoria_has_Produto_Produto1` FOREIGN KEY (`Produto_id_Produto`) REFERENCES `produto` (`id_Produto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `nome_cliente` varchar(50) NOT NULL,
  `cpf_cliente` varchar(20) NOT NULL,
  `endereço_cliente` varchar(50) DEFAULT NULL,
  `telefone_cliente` varchar(20) NOT NULL,
  `e-mail_cliente` varchar(50) DEFAULT NULL,
  `Antecedente médico` longtext DEFAULT NULL,
  PRIMARY KEY (`id_cliente`,`cpf_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fornecedor`
--

DROP TABLE IF EXISTS `fornecedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fornecedor` (
  `id_Fornecedor` int(11) NOT NULL AUTO_INCREMENT,
  `nome_fornecedor` varchar(45) NOT NULL,
  `preço_insumo` decimal(10,2) NOT NULL,
  `endereço_fornecedor` longtext NOT NULL,
  `telefone_fornecedor` varchar(20) NOT NULL,
  `Cnpj_fornecedor` varchar(30) NOT NULL,
  PRIMARY KEY (`id_Fornecedor`)
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fornecedor_has_insumo`
--

DROP TABLE IF EXISTS `fornecedor_has_insumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fornecedor_has_insumo` (
  `Fornecedor_id_Fornecedor` int(11) NOT NULL,
  `Insumo_nome_insumo` varchar(45) NOT NULL,
  PRIMARY KEY (`Insumo_nome_insumo`),
  KEY `fk_Fornecedor_has_Insumo_Insumo1_idx` (`Insumo_nome_insumo`),
  KEY `fk_Fornecedor_has_Insumo_Fornecedor1_idx` (`Fornecedor_id_Fornecedor`),
  CONSTRAINT `fk_Fornecedor_has_Insumo_Fornecedor1` FOREIGN KEY (`Fornecedor_id_Fornecedor`) REFERENCES `fornecedor` (`id_Fornecedor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Fornecedor_has_Insumo_Insumo1` FOREIGN KEY (`Insumo_nome_insumo`) REFERENCES `insumo` (`nome_insumo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `funcionário`
--

DROP TABLE IF EXISTS `funcionário`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funcionário` (
  `id_Funcionário` int(11) NOT NULL AUTO_INCREMENT,
  `nome_funcionario` varchar(50) NOT NULL,
  `cpf_funcionario` varchar(20) NOT NULL,
  `cargo_funcionario` varchar(40) NOT NULL,
  `Data_de_admissão_funcionario` date NOT NULL,
  `Pedido_id_Pedido` int(11) NOT NULL,
  PRIMARY KEY (`id_Funcionário`),
  KEY `fk_Funcionário_Pedido1` (`Pedido_id_Pedido`),
  CONSTRAINT `fk_Funcionário_Pedido1` FOREIGN KEY (`Pedido_id_Pedido`) REFERENCES `pedido` (`id_Pedido`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `insumo`
--

DROP TABLE IF EXISTS `insumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `insumo` (
  `nome_insumo` varchar(45) NOT NULL,
  `validade_insumo` date NOT NULL,
  `estoque_insumo` varchar(50) NOT NULL,
  PRIMARY KEY (`nome_insumo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `insumo_has_produto`
--

DROP TABLE IF EXISTS `insumo_has_produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `insumo_has_produto` (
  `Insumo_nome_insumo` varchar(45) NOT NULL,
  `Produto_id_Produto` int(11) NOT NULL,
  KEY `fk_Insumo_has_Produto_Insumo1` (`Insumo_nome_insumo`),
  KEY `fk_Insumo_has_Produto_Produto1` (`Produto_id_Produto`),
  CONSTRAINT `fk_Insumo_has_Produto_Insumo1` FOREIGN KEY (`Insumo_nome_insumo`) REFERENCES `insumo` (`nome_insumo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Insumo_has_Produto_Produto1` FOREIGN KEY (`Produto_id_Produto`) REFERENCES `produto` (`id_Produto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `item` (
  `idt_item` int(11) NOT NULL AUTO_INCREMENT,
  `quantidade_item` varchar(20) NOT NULL,
  `preco_unitario_item` decimal(10,2) NOT NULL,
  `Pedido_id_Pedido` int(11) NOT NULL,
  `Produto_id_Produto` int(11) NOT NULL,
  PRIMARY KEY (`idt_item`),
  KEY `fk_Item_Pedido1` (`Pedido_id_Pedido`),
  KEY `fk_Item_Produto1` (`Produto_id_Produto`),
  CONSTRAINT `fk_Item_Pedido1` FOREIGN KEY (`Pedido_id_Pedido`) REFERENCES `pedido` (`id_Pedido`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Item_Produto1` FOREIGN KEY (`Produto_id_Produto`) REFERENCES `produto` (`id_Produto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pagamento`
--

DROP TABLE IF EXISTS `pagamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pagamento` (
  `Valor_a_ser_pago` decimal(10,2) NOT NULL,
  `metodo_de_pagamento` varchar(45) NOT NULL,
  `Pedido_id_Pedido` int(11) NOT NULL,
  `status_pagamento` varchar(45) NOT NULL,
  PRIMARY KEY (`Pedido_id_Pedido`),
  CONSTRAINT `fk_Pagamento_Pedido1` FOREIGN KEY (`Pedido_id_Pedido`) REFERENCES `pedido` (`id_Pedido`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pedido`
--

DROP TABLE IF EXISTS `pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pedido` (
  `id_Pedido` int(11) NOT NULL AUTO_INCREMENT,
  `valor_total_item` decimal(10,2) NOT NULL,
  `Data_pedido` date NOT NULL,
  `Status_pedido` varchar(50) NOT NULL,
  `Cliente_id_cliente` int(11) NOT NULL,
  `Cliente_cpf` varchar(20) NOT NULL,
  `Prescrição_id_prescrição` int(11) NOT NULL,
  PRIMARY KEY (`id_Pedido`),
  KEY `fk_Pedido_Cliente1` (`Cliente_id_cliente`,`Cliente_cpf`),
  KEY `fk_Pedido_Prescrição1` (`Prescrição_id_prescrição`),
  CONSTRAINT `fk_Pedido_Cliente1` FOREIGN KEY (`Cliente_id_cliente`, `Cliente_cpf`) REFERENCES `cliente` (`id_cliente`, `cpf_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Pedido_Prescrição1` FOREIGN KEY (`Prescrição_id_prescrição`) REFERENCES `prescrição` (`id_prescrição`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pedido_has_cliente`
--

DROP TABLE IF EXISTS `pedido_has_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pedido_has_cliente` (
  `Pedido_id_Pedido` int(11) NOT NULL,
  `Cliente_id_cliente` int(11) NOT NULL,
  `Cliente_cpf` varchar(20) NOT NULL,
  PRIMARY KEY (`Pedido_id_Pedido`,`Cliente_id_cliente`,`Cliente_cpf`),
  KEY `fk_Pedido_has_Cliente_Cliente1` (`Cliente_id_cliente`,`Cliente_cpf`),
  CONSTRAINT `fk_Pedido_has_Cliente_Cliente1` FOREIGN KEY (`Cliente_id_cliente`, `Cliente_cpf`) REFERENCES `cliente` (`id_cliente`, `cpf_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Pedido_has_Cliente_Pedido1` FOREIGN KEY (`Pedido_id_Pedido`) REFERENCES `pedido` (`id_Pedido`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `prescrição`
--

DROP TABLE IF EXISTS `prescrição`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prescrição` (
  `id_prescrição` int(11) NOT NULL AUTO_INCREMENT,
  `produto` varchar(30) NOT NULL,
  `descrição` longtext DEFAULT NULL,
  `orientação` longtext NOT NULL,
  PRIMARY KEY (`id_prescrição`)
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `produto`
--

DROP TABLE IF EXISTS `produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produto` (
  `id_Produto` int(11) NOT NULL AUTO_INCREMENT,
  `nome_produto` varchar(45) NOT NULL,
  `Código_produto` varchar(30) NOT NULL,
  `descrição_produto` longtext NOT NULL,
  `forma_de_preparo` longtext NOT NULL,
  PRIMARY KEY (`id_Produto`)
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping routines for database 'farmácia'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-18 23:35:48
