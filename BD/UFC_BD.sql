-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema ufc2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ufc2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ufc2` DEFAULT CHARACTER SET utf8mb3 ;
USE `ufc2` ;

-- -----------------------------------------------------
-- Table `ufc2`.`localizacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ufc2`.`localizacion` (
  `localizacion` VARCHAR(80) NOT NULL,
  `coordenadas` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`localizacion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ufc2`.`evento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ufc2`.`evento` (
  `evento` VARCHAR(80) NOT NULL,
  `fecha` DATE NOT NULL,
  `mes` VARCHAR(15) NOT NULL,
  `localizacion` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`evento`),
  INDEX `fk_evento_localizacion1_idx` (`localizacion` ASC) VISIBLE,
  CONSTRAINT `fk_evento_localizacion1`
    FOREIGN KEY (`localizacion`)
    REFERENCES `ufc2`.`localizacion` (`localizacion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ufc2`.`combate`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ufc2`.`combate` (
  `evento` VARCHAR(80) NOT NULL,
  `combate` INT NOT NULL,
  `round` SMALLINT NOT NULL,
  `minuto` SMALLINT NOT NULL,
  `segundo` SMALLINT NOT NULL,
  `forma` VARCHAR(30) NOT NULL,
  `metodo` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`evento`, `combate`),
  INDEX `fk_combate_evento1_idx` (`evento` ASC) VISIBLE,
  CONSTRAINT `fk_combate_evento1`
    FOREIGN KEY (`evento`)
    REFERENCES `ufc2`.`evento` (`evento`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ufc2`.`division`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ufc2`.`division` (
  `division` VARCHAR(30) NOT NULL,
  `peso` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`division`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ufc2`.`peleador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ufc2`.`peleador` (
  `peleador` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`peleador`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ufc2`.`pertenece`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ufc2`.`pertenece` (
  `division` VARCHAR(30) NOT NULL,
  `peleador` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`division`, `peleador`),
  INDEX `fk_division_has_peleador_peleador1_idx` (`peleador` ASC) VISIBLE,
  INDEX `fk_division_has_peleador_division_idx` (`division` ASC) VISIBLE,
  CONSTRAINT `fk_division_has_peleador_division`
    FOREIGN KEY (`division`)
    REFERENCES `ufc2`.`division` (`division`),
  CONSTRAINT `fk_division_has_peleador_peleador1`
    FOREIGN KEY (`peleador`)
    REFERENCES `ufc2`.`peleador` (`peleador`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ufc2`.`se_pelean`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ufc2`.`se_pelean` (
  `peleador` VARCHAR(80) NOT NULL,
  `evento` VARCHAR(80) NOT NULL,
  `combate` INT NOT NULL,
  `i_sig_str` SMALLINT NOT NULL,
  `i_total_str` SMALLINT NOT NULL,
  `i_td` SMALLINT NOT NULL,
  `i_cabeza` SMALLINT NOT NULL,
  `i_cuerpo` SMALLINT NOT NULL,
  `i_piernas` SMALLINT NOT NULL,
  `i_clinch` SMALLINT NOT NULL,
  `i_ground` SMALLINT NOT NULL,
  `c_sig_str` SMALLINT NOT NULL,
  `c_total_str` SMALLINT NOT NULL,
  `c_td` SMALLINT NOT NULL,
  `c_cabeza` SMALLINT NOT NULL,
  `c_cuerpo` SMALLINT NOT NULL,
  `c_piernas` SMALLINT NOT NULL,
  `c_clinch` SMALLINT NOT NULL,
  `c_ground` SMALLINT NOT NULL,
  `i_sub` SMALLINT NOT NULL,
  `kd` SMALLINT NOT NULL,
  `w_l` VARCHAR(10) NOT NULL,
  `t_control` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`peleador`, `evento`, `combate`),
  INDEX `fk_se_pelean_combate1_idx` (`evento` ASC, `combate` ASC) VISIBLE,
  CONSTRAINT `fk_se_pelean_combate1`
    FOREIGN KEY (`evento` , `combate`)
    REFERENCES `ufc2`.`combate` (`evento` , `combate`),
  CONSTRAINT `fk_se_pelean_peleador1`
    FOREIGN KEY (`peleador`)
    REFERENCES `ufc2`.`peleador` (`peleador`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
