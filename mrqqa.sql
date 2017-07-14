SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

CREATE SCHEMA IF NOT EXISTS `mrqqa_database` DEFAULT CHARACTER SET latin1 ;
USE `mrqqa_database` ;


-- -----------------------------------------------------
-- Table `mrqqa_database`.`scanner_details`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mrqqa_database`.`scanner_details` ;

CREATE  TABLE IF NOT EXISTS `mrqqa_database`.`scanner_details` (
  `scanner_id` INT(11) NOT NULL AUTO_INCREMENT ,
  `scanner_name` VARCHAR(100) NULL DEFAULT NULL ,
  `scanner_notes` VARCHAR(8000) NULL DEFAULT NULL ,
  PRIMARY KEY (`scanner_id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `mrqqa_database`.`coil_details`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mrqqa_database`.`coil_details` ;

CREATE  TABLE IF NOT EXISTS `mrqqa_database`.`coil_details` (
  `coil_id` INT(11) NOT NULL AUTO_INCREMENT ,
  `coil_name` VARCHAR(100) NOT NULL ,
  `coil_notes` VARCHAR(8000) NOT NULL ,
  PRIMARY KEY (`coil_id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `mrqqa_database`.`version_details`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mrqqa_database`.`version_details` ;

CREATE  TABLE IF NOT EXISTS `mrqqa_database`.`version_details` (
  `version_id` INT(11) NOT NULL  AUTO_INCREMENT,
  `version_name` VARCHAR(100) NOT NULL ,
  `version_notes` VARCHAR(8000) NOT NULL ,
  PRIMARY KEY (`version_id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `mrqqa_database`.`gradsys_details`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mrqqa_database`.`gradsys_details` ;

CREATE  TABLE IF NOT EXISTS `mrqqa_database`.`gradsys_details` (
  `gradsys_id` INT(11) NOT NULL AUTO_INCREMENT,
  `gradsys_name` VARCHAR(100) NOT NULL ,
  `gradsys_notes` VARCHAR(8000) NOT NULL ,
  PRIMARY KEY (`gradsys_id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `mrqqa_database`.`phantom_details`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mrqqa_database`.`phantom_details` ;

CREATE  TABLE IF NOT EXISTS `mrqqa_database`.`phantom_details` (
  `phantom_id` INT(11) NOT NULL  AUTO_INCREMENT,
  `phantom_name` VARCHAR(100) NOT NULL ,
  `phantom_notes` VARCHAR(8000) NOT NULL ,
  PRIMARY KEY (`phantom_id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `mrqqa_database`.`date_details`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mrqqa_database`.`date_details` ;

CREATE  TABLE IF NOT EXISTS `mrqqa_database`.`date_details` (
  `date_id` INT(11) NOT NULL  AUTO_INCREMENT,
  `full_date` DATE NOT NULL ,  
  `scanner_id` INT(11) NOT NULL ,
  `version_id` VARCHAR(11) NOT NULL ,
  `gradsys_id` INT(11) NOT NULL ,
  `coil_id` INT(11) NOT NULL ,
  `phantom_id` INT(11) NOT NULL ,  
  PRIMARY KEY (`date_id`) ,
  INDEX `fk_scanner_id_1` (`scanner_id` ASC) ,
  CONSTRAINT `fk_scanner_id_1`
    FOREIGN KEY (`scanner_id` )
    REFERENCES `mrqqa_database`.`scanner_id` (`scanner_id` ) ,
  INDEX `fk_coil_id_1` (`coil_id` ASC) ,
  CONSTRAINT `fk_coil_id_1`
    FOREIGN KEY (`coil_id`)
    REFERENCES `mrqqa_database`.`coil_id` (`coil_id`) ,
  INDEX `fk_phantom_id_1` (`phantom_id` ASC) ,
  CONSTRAINT `fk_phantom_id_1`
    FOREIGN KEY (`phantom_id`)
    REFERENCES `mrqqa_database`.`phantom_id` (`phantom_id`) ,
  INDEX `fk_version_id_1` (`version_id` ASC) ,
  CONSTRAINT `fk_version_id_1`
    FOREIGN KEY (`version_id`)
    REFERENCES `mrqqa_database`.`version_id` (`version_id`) ,
  INDEX `fk_gradsys_id_1` (`gradsys_id` ASC) ,
  CONSTRAINT `fk_gradsys_id_1`
    FOREIGN KEY (`gradsys_id`)
    REFERENCES `mrqqa_database`.`gradsys_id` (`gradsys_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)

ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `mrqqa_database`.`seriesid_details`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mrqqa_database`.`series_details` ;

CREATE  TABLE IF NOT EXISTS `mrqqa_database`.`series_details` (
  `series_id` INT(11) NOT NULL AUTO_INCREMENT,
  `series` VARCHAR(100) NOT NULL ,
  `series_notes` VARCHAR(8000) NOT NULL ,  
  PRIMARY KEY (`series_id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;






-- -----------------------------------------------------
-- Table `mrqqa_database`.`results`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mrqqa_database`.`results` ;

CREATE  TABLE IF NOT EXISTS `mrqqa_database`.`results` (
  `result_id` INT(11) NOT NULL  AUTO_INCREMENT,
  `result` VARCHAR(6000) NOT NULL ,
  `date_id` INT(11) NOT NULL ,
  `series_id` INT(11) NOT NULL ,

  PRIMARY KEY (`result_id`) ,
  INDEX `fk_date_id_1` (`date_id` ASC) ,
  CONSTRAINT `fk_date_id_1`
    FOREIGN KEY (`date_id` )
    REFERENCES `mrqqa_database`.`date_id` (`date_id` ) ,
  INDEX `fk_series_id_1` (`series_id` ASC) ,
  CONSTRAINT `fk_series_id_1`
    FOREIGN KEY (`series_id` )
    REFERENCES `mrqqa_database`.`series_id` (`series_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;






