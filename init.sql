SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `OrderApp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `OrderApp`;

DROP TABLE IF EXISTS `drinks`;
CREATE TABLE `drinks` (
  `drink_id` int NOT NULL AUTO_INCREMENT,
  `drink_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`drink_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `drinks` (`drink_id`, `drink_name`) VALUES
(1,	'Gin');