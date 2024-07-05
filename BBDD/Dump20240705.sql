-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: restaurante
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comentarios`
--

DROP TABLE IF EXISTS `comentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comentarios` (
  `id_comentario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `correo_electronico` varchar(100) DEFAULT NULL,
  `comentario` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_comentario`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comentarios`
--

LOCK TABLES `comentarios` WRITE;
/*!40000 ALTER TABLE `comentarios` DISABLE KEYS */;
INSERT INTO `comentarios` VALUES (1,'Yonathan','Diaz','yd@123gmail.com','El sitio es genial'),(2,'Lucas','Perez','lp@123hotmail.com','Comida sobrevalorada'),(3,'Emily','Watson','EmilyW@gmail.com','dolor de estomago'),(4,'Homer','Simpson','Hsimpsom@gmail.com','MMMMMMM Rosquillas ahhhhhg');
/*!40000 ALTER TABLE `comentarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imagen`
--

DROP TABLE IF EXISTS `imagen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `imagen` (
  `id_imagen` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(60) DEFAULT NULL,
  `texto_alternativo` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id_imagen`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imagen`
--

LOCK TABLES `imagen` WRITE;
/*!40000 ALTER TABLE `imagen` DISABLE KEYS */;
INSERT INTO `imagen` VALUES (1,'https://github.com/NoeliaMV/sitioresto.github.io/blob/master','imagen coctail sin alcohol'),(2,'https://github.com/NoeliaMV/sitioresto.github.io/blob/master','Mousee'),(3,'https://github.com/NoeliaMV/sitioresto.github.io/blob/master','Pappardell'),(4,'https://github.com/NoeliaMV/sitioresto.github.io/blob/master','Roast-Beef'),(5,'https://github.com/NoeliaMV/sitioresto.github.io/blob/master','Smootie'),(6,'https://github.com/NoeliaMV/sitioresto.github.io/blob/master','Soufflet'),(7,'https://github.com/NoeliaMV/sitioresto.github.io/blob/master','batatas'),(8,'https://github.com/NoeliaMV/sitioresto.github.io/blob/master','Biscocho de limon'),(9,'https://github.com/NoeliaMV/sitioresto.github.io/blob/master','Ceviche');
/*!40000 ALTER TABLE `imagen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `platillo`
--

DROP TABLE IF EXISTS `platillo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `platillo` (
  `platillo_id` int(11) NOT NULL AUTO_INCREMENT,
  `imagen_id` int(2) DEFAULT NULL,
  `plato` varchar(50) DEFAULT NULL,
  `descripcion` varchar(2500) DEFAULT NULL,
  `precio` int(50) DEFAULT NULL,
  PRIMARY KEY (`platillo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `platillo`
--

LOCK TABLES `platillo` WRITE;
/*!40000 ALTER TABLE `platillo` DISABLE KEYS */;
INSERT INTO `platillo` VALUES (1,1,'Cocktail sin alcohol','Nuestros Mocktails Creativos son la prueba de que la diversión no necesita ron ni vodka. Desde el Virgin Mojito con su frescura a base de menta y lima',35),(2,2,'Mousse de Frutas del Bosque','En un elegante vasito, servimos una mousse suave y aireada, coronada con frutos rojos frescos. Cada cucharada es un viaje a los bosques silvestres, do',40),(3,3,'Pappardelle','El Pappardelle es más que un simple plato; es una obra maestra de la gastronomía italiana. Nuestra pasta Pappardelle es perfecta para absorber salsas ',25),(4,4,'Roast-Beef','En nuestro restaurante, servimos el Roast Beef con Puré de Papas en un plato de porcelana blanca. El roast beef se corta en rodajas generosas y se col',45);
/*!40000 ALTER TABLE `platillo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `valoracion`
--

DROP TABLE IF EXISTS `valoracion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `valoracion` (
  `id_valoracion` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_number` int(11) DEFAULT NULL,
  `platillo_number` int(11) DEFAULT NULL,
  `puntos` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_valoracion`),
  KEY `platillo_number` (`platillo_number`),
  KEY `usuario_number` (`usuario_number`),
  CONSTRAINT `valoracion_ibfk_1` FOREIGN KEY (`platillo_number`) REFERENCES `platillo` (`platillo_ID`),
  CONSTRAINT `valoracion_ibfk_2` FOREIGN KEY (`usuario_number`) REFERENCES `comentarios` (`id_comentario`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `valoracion`
--

LOCK TABLES `valoracion` WRITE;
/*!40000 ALTER TABLE `valoracion` DISABLE KEYS */;
INSERT INTO `valoracion` VALUES (2,1,1,'2'),(3,1,1,'2'),(4,2,2,'44');
/*!40000 ALTER TABLE `valoracion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-05 19:45:24
