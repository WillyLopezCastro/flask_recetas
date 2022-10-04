-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema receta
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema receta
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `receta` DEFAULT CHARACTER SET utf8 ;
USE `receta` ;

-- -----------------------------------------------------
-- Table `receta`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `receta`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuario` VARCHAR(255) NOT NULL,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `receta`.`recetas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `receta`.`recetas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `descripcion` VARCHAR(255) NOT NULL,
  `instruccion` TEXT NOT NULL,
  `date_made` DATETIME NOT NULL,
  `under_30` TINYINT NOT NULL,
  `usuario_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recetas_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_recetas_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `receta`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
