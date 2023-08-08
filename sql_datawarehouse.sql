-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema edu_superior
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema edu_superior
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `edu_superior` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `edu_superior` ;

-- -----------------------------------------------------
-- Table `edu_superior`.`localoferta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `edu_superior`.`localoferta` (
  `REGION_ID` INT NOT NULL AUTO_INCREMENT,
  `NO_REGIAO` VARCHAR(255) NOT NULL,
  `CO_REGIAO` INT NOT NULL,
  `NO_UF` VARCHAR(255) NULL DEFAULT NULL,
  `SG_UF` VARCHAR(2) NULL DEFAULT NULL,
  `CO_UF` INT NULL DEFAULT NULL,
  `NO_MUNICIPIO` VARCHAR(255) NULL DEFAULT NULL,
  `CO_MUNICIPIO` INT NULL DEFAULT NULL,
  PRIMARY KEY (`REGION_ID`, `CO_REGIAO`, `NO_REGIAO`),
  INDEX `fk_co_regiao_int` (`CO_REGIAO` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 591404
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

ALTER TABLE `edu_superior`.`localoferta` ADD INDEX `idx_NO_REGIAO` (`NO_REGIAO`);

-- -----------------------------------------------------
-- Table `edu_superior`.`instituicao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `edu_superior`.`instituicao` (
  `INSTITUICAO_ID` INT NOT NULL AUTO_INCREMENT,
  `CO_IES` INT NOT NULL,
  `TP_ORGANIZACAO_ACADEMICA` VARCHAR(255) NOT NULL,
  `TP_CATEGORIA_ADMINISTRATIVA` VARCHAR(255) NULL DEFAULT NULL,
  `TP_REDE` VARCHAR(255) NOT NULL,
  `localoferta_CO_REGIAO` INT NOT NULL,
  PRIMARY KEY (`INSTITUICAO_ID`, `CO_IES`, `TP_ORGANIZACAO_ACADEMICA`, `TP_REDE`),
  INDEX `fk_instituicao_localoferta1_idx` (`localoferta_CO_REGIAO` ASC) VISIBLE,
  INDEX `fk_CO_IES` (`CO_IES` ASC) VISIBLE,
  CONSTRAINT `fk_instituicao_localoferta1`
    FOREIGN KEY (`localoferta_CO_REGIAO`)
    REFERENCES `edu_superior`.`localoferta` (`CO_REGIAO`))
ENGINE = InnoDB
AUTO_INCREMENT = 591404
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

ALTER TABLE `edu_superior`.`instituicao` ADD INDEX `idx_TP_ORGANIZACAO_ACADEMICA` (`TP_ORGANIZACAO_ACADEMICA`);
ALTER TABLE `edu_superior`.`instituicao` ADD INDEX `idx_TP_REDE` (`TP_REDE`);

-- -----------------------------------------------------
-- Table `edu_superior`.`curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `edu_superior`.`curso` (
  `CURSO_ID` INT NOT NULL AUTO_INCREMENT,
  `CO_CURSO` INT NOT NULL,
  `NO_CURSO` VARCHAR(255) NULL DEFAULT NULL,
  `TP_MODALIDADE_ENSINO` INT NOT NULL,
  `TP_GRAU_ACADEMICO` INT NOT NULL,
  `TP_NIVEL_ACADEMICO` INT NULL DEFAULT NULL,
  `instituicao_CO_IES` INT NOT NULL,
  `localoferta_CO_REGIAO` INT NOT NULL,
  PRIMARY KEY (`CURSO_ID`, `CO_CURSO`, `TP_MODALIDADE_ENSINO`, `TP_GRAU_ACADEMICO`),
  INDEX `fk_curso_instituicao1_idx` (`instituicao_CO_IES` ASC) INVISIBLE,
  INDEX `fk_curso_localoferta_idx` (`CO_CURSO` ASC) VISIBLE,
  INDEX `fk_curso_localoferta1_idx` (`localoferta_CO_REGIAO` ASC) INVISIBLE,
  CONSTRAINT `fk_curso_instituicao1`
    FOREIGN KEY (`instituicao_CO_IES`)
    REFERENCES `edu_superior`.`instituicao` (`CO_IES`),
  CONSTRAINT `fk_curso_localoferta1`
    FOREIGN KEY (`localoferta_CO_REGIAO`)
    REFERENCES `edu_superior`.`localoferta` (`CO_REGIAO`))
ENGINE = InnoDB
AUTO_INCREMENT = 591404
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

ALTER TABLE `edu_superior`.`curso` ADD INDEX `idx_TP_MODALIDADE_ENSINO` (`TP_MODALIDADE_ENSINO`);
ALTER TABLE `edu_superior`.`curso` ADD INDEX `idx_TP_GRAU_ACADEMICO` (`TP_GRAU_ACADEMICO`);
-- -----------------------------------------------------
-- Table `edu_superior`.`concluintes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `edu_superior`.`concluintes` (
  `CONCLUINTES_ID` INT NOT NULL AUTO_INCREMENT,
  `QT_CONC` INT NOT NULL,
  `QT_CONC_FEM` INT NULL DEFAULT NULL,
  `QT_CONC_MASC` INT NULL DEFAULT NULL,
  `QT_CONC_0_17` INT NULL DEFAULT NULL,
  `QT_CONC_18_24` INT NULL DEFAULT NULL,
  `QT_CONC_25_29` INT NULL DEFAULT NULL,
  `QT_CONC_30_34` INT NULL DEFAULT NULL,
  `QT_CONC_35_39` INT NULL DEFAULT NULL,
  `QT_CONC_40_49` INT NULL DEFAULT NULL,
  `QT_CONC_50_59` INT NULL DEFAULT NULL,
  `QT_CONC_60_MAIS` INT NULL DEFAULT NULL,
  `QT_CONC_DIURNO` INT NULL DEFAULT NULL,
  `QT_CONC_NOTURNO` INT NULL DEFAULT NULL,
  `curso_CO_CURSO` INT NOT NULL,
  INDEX `fk_concluintes_curso1_idx` (`curso_CO_CURSO` ASC) INVISIBLE,
  PRIMARY KEY (`CONCLUINTES_ID`, `QT_CONC`),
  CONSTRAINT `fk_concluintes_curso1`
    FOREIGN KEY (`curso_CO_CURSO`)
    REFERENCES `edu_superior`.`curso` (`CO_CURSO`))
ENGINE = InnoDB
AUTO_INCREMENT = 601404
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

ALTER TABLE `edu_superior`.`concluintes` ADD INDEX `idx_QT_CONC` (`QT_CONC`);

-- -----------------------------------------------------
-- Table `edu_superior`.`ingressantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `edu_superior`.`ingressantes` (
  `INGRESSANTES_ID` INT NOT NULL AUTO_INCREMENT,
  `QT_ING_FEM` INT NOT NULL,
  `QT_ING_MASC` INT NOT NULL,
  `QT_ING_NOTURNO` INT NULL DEFAULT NULL,
  `QT_ING_DIURNO` INT NULL DEFAULT NULL,
  `QT_ING` INT NULL DEFAULT NULL,
  `QT_ING_0_17` INT NOT NULL,
  `QT_ING_18_24` INT NOT NULL,
  `QT_ING_25_29` INT NOT NULL,
  `QT_ING_30_34` INT NOT NULL,
  `QT_ING_35_39` INT NOT NULL,
  `QT_ING_40_49` INT NOT NULL,
  `QT_ING_50_59` INT NOT NULL,
  `QT_ING_60_MAIS` INT NOT NULL,
  `curso_CO_CURSO` INT NOT NULL,
  PRIMARY KEY (`INGRESSANTES_ID`, `QT_ING_FEM`, `QT_ING_MASC`, `QT_ING_0_17`, `QT_ING_18_24`, `QT_ING_25_29`, `QT_ING_30_34`, `QT_ING_35_39`, `QT_ING_40_49`, `QT_ING_50_59`, `QT_ING_60_MAIS`),
  INDEX `fk_ingressantes_curso1_idx` (`curso_CO_CURSO` ASC) VISIBLE,
  CONSTRAINT `fk_ingressantes_curso1`
    FOREIGN KEY (`curso_CO_CURSO`)
    REFERENCES `edu_superior`.`curso` (`CO_CURSO`))
ENGINE = InnoDB
AUTO_INCREMENT = 591404
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

ALTER TABLE `edu_superior`.`ingressantes` ADD INDEX `idx_ING_FEM` (`QT_ING_FEM`);
ALTER TABLE `edu_superior`.`ingressantes` ADD INDEX `idx_ING_MASC` (`QT_ING_MASC`);
ALTER TABLE `edu_superior`.`ingressantes` ADD INDEX `idx_ING_MAT_0_17` (`QT_ING_0_17`);
ALTER TABLE `edu_superior`.`ingressantes` ADD INDEX `idx_ING_MAT_18_24` (`QT_ING_18_24`);
ALTER TABLE `edu_superior`.`ingressantes` ADD INDEX `idx_ING_MAT_25_29` (`QT_ING_25_29`);
ALTER TABLE `edu_superior`.`ingressantes` ADD INDEX `idx_ING_MAT_30_34` (`QT_ING_30_34`);
ALTER TABLE `edu_superior`.`ingressantes` ADD INDEX `idx_ING_MAT_35_39` (`QT_ING_35_39`);
ALTER TABLE `edu_superior`.`ingressantes` ADD INDEX `idx_ING_MAT_40_49` (`QT_ING_40_49`);
ALTER TABLE `edu_superior`.`ingressantes` ADD INDEX `idx_ING_MAT_50_59` (`QT_ING_50_59`);
ALTER TABLE `edu_superior`.`ingressantes` ADD INDEX `idx_ING_MAT_60_MAIS` (`QT_ING_60_MAIS`);

-- -----------------------------------------------------
-- Table `edu_superior`.`matriculas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `edu_superior`.`matriculas` (
  `MATRICULAS_ID` INT NOT NULL AUTO_INCREMENT,
  `QT_MAT` INT NULL DEFAULT NULL,
  `QT_MAT_FEM` INT NOT NULL,
  `QT_MAT_MASC` INT NOT NULL,
  `QT_MAT_DIURNO` INT NOT NULL,
  `QT_MAT_NOTURNO` INT NOT NULL,
  `QT_MAT_0_17` INT NOT NULL,
  `QT_MAT_18_24` INT NOT NULL,
  `QT_MAT_25_29` INT NOT NULL,
  `QT_MAT_30_34` INT NOT NULL,
  `QT_MAT_35_39` INT NOT NULL,
  `QT_MAT_40_49` INT NOT NULL,
  `QT_MAT_50_59` INT NOT NULL,
  `QT_MAT_60_MAIS` INT NOT NULL,
  `curso_CO_CURSO` INT NOT NULL,
  PRIMARY KEY (`MATRICULAS_ID`, `QT_MAT_FEM`, `QT_MAT_MASC`, `QT_MAT_0_17`, `QT_MAT_18_24`, `QT_MAT_25_29`, `QT_MAT_30_34`, `QT_MAT_35_39`, `QT_MAT_40_49`, `QT_MAT_50_59`, `QT_MAT_60_MAIS`, `QT_MAT_DIURNO`, `QT_MAT_NOTURNO`),
  INDEX `fk_matriculas_curso1_idx` (`curso_CO_CURSO` ASC) VISIBLE,
  CONSTRAINT `fk_matriculas_curso1`
    FOREIGN KEY (`curso_CO_CURSO`)
    REFERENCES `edu_superior`.`curso` (`CO_CURSO`))
ENGINE = InnoDB
AUTO_INCREMENT = 591404
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

ALTER TABLE `edu_superior`.`matriculas` ADD INDEX `idx_QT_MAT_FEM` (`QT_MAT_FEM`);
ALTER TABLE `edu_superior`.`matriculas` ADD INDEX `idx_QT_MAT_MASC` (`QT_MAT_MASC`);
ALTER TABLE `edu_superior`.`matriculas` ADD INDEX `idx_QT_MAT_0_17` (`QT_MAT_0_17`);
ALTER TABLE `edu_superior`.`matriculas` ADD INDEX `idx_QT_MAT_18_24` (`QT_MAT_18_24`);
ALTER TABLE `edu_superior`.`matriculas` ADD INDEX `idx_QT_MAT_25_29` (`QT_MAT_25_29`);
ALTER TABLE `edu_superior`.`matriculas` ADD INDEX `idx_QT_MAT_30_34` (`QT_MAT_30_34`);
ALTER TABLE `edu_superior`.`matriculas` ADD INDEX `idx_QT_MAT_35_39` (`QT_MAT_35_39`);
ALTER TABLE `edu_superior`.`matriculas` ADD INDEX `idx_QT_MAT_40_49` (`QT_MAT_40_49`);
ALTER TABLE `edu_superior`.`matriculas` ADD INDEX `idx_QT_MAT_50_59` (`QT_MAT_50_59`);
ALTER TABLE `edu_superior`.`matriculas` ADD INDEX `idx_QT_MAT_60_MAIS` (`QT_MAT_60_MAIS`);
ALTER TABLE `edu_superior`.`matriculas` ADD INDEX `idx_QT_MAT_DIURNO` (`QT_MAT_DIURNO`);
ALTER TABLE `edu_superior`.`matriculas` ADD INDEX `idx_QT_MAT_NOTURNO` (`QT_MAT_NOTURNO`);


-- -----------------------------------------------------
-- Table `edu_superior`.`fato_taxa_evasao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `edu_superior`.`fato_taxa_evasao` (
  `concluintes_QT_CONC` INT NOT NULL,
  `instituicao_TP_ORGANIZACAO_ACADEMICA` VARCHAR(255) NOT NULL,
  `instituicao_TP_REDE` VARCHAR(255) NOT NULL,
  `curso_TP_MODALIDADE_ENSINO` INT NOT NULL,
  `matricula_QT_MAT_FEM` INT NOT NULL,
  `matricula_QT_MAT_MASC` INT NOT NULL,
  `matricula_QT_MAT_0_17` INT NOT NULL,
  `matricula_QT_MAT_18_24` INT NOT NULL,
  `matricula_QT_MAT_25_29` INT NOT NULL,
  `matricula_QT_MAT_30_34` INT NOT NULL,
  `matricula_QT_MAT_35_39` INT NOT NULL,
  `matricula_QT_MAT_40_49` INT NOT NULL,
  `matricula_QT_MAT_50_59` INT NOT NULL,
  `matricula_QT_MAT_60_MAIS` INT NOT NULL,
  `localoferta_NO_REGIAO` VARCHAR(255) NOT NULL,
  `matricula_QT_MAT_DIURNO` INT NOT NULL,
  `matricula_QT_MAT_NOTURNO` INT NOT NULL,
  `curso_TP_GRAU_ACADEMICO` INT NOT NULL,
  INDEX `fk_instituicao_TP_ORGANIZACAO_ACADEMICA_idx` (`instituicao_TP_ORGANIZACAO_ACADEMICA` ASC) VISIBLE,
  INDEX `fk_instituicao_TP_REDE_idx` (`instituicao_TP_REDE` ASC) VISIBLE,
  INDEX `fk_curso_TP_MODALIDADE_ENSINO_idx` (`curso_TP_MODALIDADE_ENSINO` ASC) VISIBLE,
  INDEX `fk_matricula_QT_MAT_FEM_idx` (`matricula_QT_MAT_FEM` ASC) VISIBLE,
  INDEX `fk_matricula_QT_MAT_MASC_idx` (`matricula_QT_MAT_MASC` ASC) VISIBLE,
  INDEX `fk_matricula_QT_MAT_0_17_idx` (`matricula_QT_MAT_0_17` ASC) VISIBLE,
  INDEX `fk_matricula_QT_MAT_18_24_idx` (`matricula_QT_MAT_18_24` ASC) VISIBLE,
  INDEX `fk_matricula_QT_MAT_25_29_idx` (`matricula_QT_MAT_25_29` ASC) VISIBLE,
  INDEX `fk_matricula_QT_MAT_30_34_idx` (`matricula_QT_MAT_30_34` ASC) VISIBLE,
  INDEX `fk_matricula_QT_MAT_35_39_idx` (`matricula_QT_MAT_35_39` ASC) VISIBLE,
  INDEX `fk_matricula_QT_MAT_40_49_idx` (`matricula_QT_MAT_40_49` ASC) VISIBLE,
  INDEX `fk_matricula_QT_MAT_50_59_idx` (`matricula_QT_MAT_50_59` ASC) VISIBLE,
  INDEX `fk_matricula_QT_MAT_60_MAIS_idx` (`matricula_QT_MAT_60_MAIS` ASC) VISIBLE,
  INDEX `fk_localoferta_NO_REGIAO_idx` (`localoferta_NO_REGIAO` ASC) VISIBLE,
  INDEX `fk_matricula_QT_MAT_DIURNO_idx` (`matricula_QT_MAT_DIURNO` ASC) VISIBLE,
  INDEX `fk_matricula_QT_MAT_DIURNO_NOTURNO_idx` (`matricula_QT_MAT_NOTURNO` ASC) VISIBLE,
  INDEX `fk_curso_TP_GRAU_ACADEMICO_idx` (`curso_TP_GRAU_ACADEMICO` ASC) VISIBLE,
  INDEX `fk_concluintes_QT_CONC_idx` (`concluintes_QT_CONC` ASC) INVISIBLE,
  CONSTRAINT `fk_concluintes_QT_CONC`
    FOREIGN KEY (`concluintes_QT_CONC`)
    REFERENCES `edu_superior`.`concluintes` (`QT_CONC`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_instituicao_TP_ORGANIZACAO_ACADEMICA`
    FOREIGN KEY (`instituicao_TP_ORGANIZACAO_ACADEMICA`)
    REFERENCES `edu_superior`.`instituicao` (`TP_ORGANIZACAO_ACADEMICA`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_instituicao_TP_REDE`
    FOREIGN KEY (`instituicao_TP_REDE`)
    REFERENCES `edu_superior`.`instituicao` (`TP_REDE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_curso_TP_MODALIDADE_ENSINO`
    FOREIGN KEY (`curso_TP_MODALIDADE_ENSINO`)
    REFERENCES `edu_superior`.`curso` (`TP_MODALIDADE_ENSINO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_QT_MAT_FEM`
    FOREIGN KEY (`matricula_QT_MAT_FEM`)
    REFERENCES `edu_superior`.`matriculas` (`QT_MAT_FEM`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_QT_MAT_MASC`
    FOREIGN KEY (`matricula_QT_MAT_MASC`)
    REFERENCES `edu_superior`.`matriculas` (`QT_MAT_MASC`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_QT_MAT_0_17`
    FOREIGN KEY (`matricula_QT_MAT_0_17`)
    REFERENCES `edu_superior`.`matriculas` (`QT_MAT_0_17`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_QT_MAT_18_24`
    FOREIGN KEY (`matricula_QT_MAT_18_24`)
    REFERENCES `edu_superior`.`matriculas` (`QT_MAT_18_24`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_QT_MAT_25_29`
    FOREIGN KEY (`matricula_QT_MAT_25_29`)
    REFERENCES `edu_superior`.`matriculas` (`QT_MAT_25_29`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_QT_MAT_30_34`
    FOREIGN KEY (`matricula_QT_MAT_30_34`)
    REFERENCES `edu_superior`.`matriculas` (`QT_MAT_30_34`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_QT_MAT_35_39`
    FOREIGN KEY (`matricula_QT_MAT_35_39`)
    REFERENCES `edu_superior`.`matriculas` (`QT_MAT_35_39`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_QT_MAT_40_49`
    FOREIGN KEY (`matricula_QT_MAT_40_49`)
    REFERENCES `edu_superior`.`matriculas` (`QT_MAT_40_49`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_QT_MAT_50_59`
    FOREIGN KEY (`matricula_QT_MAT_50_59`)
    REFERENCES `edu_superior`.`matriculas` (`QT_MAT_50_59`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_QT_MAT_60_MAIS`
    FOREIGN KEY (`matricula_QT_MAT_60_MAIS`)
    REFERENCES `edu_superior`.`matriculas` (`QT_MAT_60_MAIS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_localoferta_NO_REGIAO`
    FOREIGN KEY (`localoferta_NO_REGIAO`)
    REFERENCES `edu_superior`.`localoferta` (`NO_REGIAO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_QT_MAT_DIURNO`
    FOREIGN KEY (`matricula_QT_MAT_DIURNO`)
    REFERENCES `edu_superior`.`matriculas` (`QT_MAT_DIURNO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_QT_MAT_DIURNO_NOTURNO`
    FOREIGN KEY (`matricula_QT_MAT_NOTURNO`)
    REFERENCES `edu_superior`.`matriculas` (`QT_MAT_NOTURNO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_curso_TP_GRAU_ACADEMICO`
    FOREIGN KEY (`curso_TP_GRAU_ACADEMICO`)
    REFERENCES `edu_superior`.`curso` (`TP_GRAU_ACADEMICO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `edu_superior`.`fato_distribuicao_ingressantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `edu_superior`.`fato_distribuicao_ingressantes` (
  `instituicao_TP_ORGANIZACAO_ACADEMICA` VARCHAR(255) NOT NULL,
  `instituicao_TP_REDE` VARCHAR(255) NOT NULL,
  `curso_TP_MODALIDADE_ENSINO` INT NOT NULL,
  `localoferta_NO_REGIAO` VARCHAR(255) NOT NULL,
  `curso_TP_GRAU_ACADEMICO` INT NOT NULL,
  `ingressantes_QT_ING_FEM` INT NOT NULL,
  `ingressantes_QT_ING_MASC` INT NOT NULL,
  `ingressantes_QT_ING_0_17` INT NOT NULL,
  `ingressantes_QT_ING_18_24` INT NOT NULL,
  `ingressantes_QT_ING_25_29` INT NOT NULL,
  `ingressantes_QT_ING_30_34` INT NOT NULL,
  `ingressantes_QT_ING_35_39` INT NOT NULL,
  `ingressantes_QT_ING_40_49` INT NOT NULL,
  `ingressantes_QT_ING_50_59` INT NOT NULL,
  `ingressantes_QT_ING_60_MAIS` INT NOT NULL,
  INDEX `fk_instituicao_TP_ORGANIZACAO_ACADEMICA_idx` (`instituicao_TP_ORGANIZACAO_ACADEMICA` ASC) VISIBLE,
  INDEX `fk_instituicao_TP_REDE_idx` (`instituicao_TP_REDE` ASC) VISIBLE,
  INDEX `fk_curso_TP_MODALIDADE_ENSINO_idx` (`curso_TP_MODALIDADE_ENSINO` ASC) VISIBLE,
  INDEX `fk_localoferta_NO_REGIAO_idx` (`localoferta_NO_REGIAO` ASC) VISIBLE,
  INDEX `fk_curso_TP_GRAU_ACADEMICO_idx` (`curso_TP_GRAU_ACADEMICO` ASC) VISIBLE,
  INDEX `fk_ingressantes_QT_ING_FEM_idx` (`ingressantes_QT_ING_FEM` ASC) VISIBLE,
  INDEX `fk_ingressantes_QT_ING_MASC_idx` (`ingressantes_QT_ING_MASC` ASC) VISIBLE,
  INDEX `fk_ingressantes_QT_ING_0_17_idx` (`ingressantes_QT_ING_0_17` ASC) VISIBLE,
  INDEX `fk_ingressantes_QT_ING_18_24_idx` (`ingressantes_QT_ING_18_24` ASC) VISIBLE,
  INDEX `fk_ingressantes_QT_ING_25_29_idx` (`ingressantes_QT_ING_25_29` ASC) VISIBLE,
  INDEX `fk_ingressantes_QT_ING_30_34_idx` (`ingressantes_QT_ING_30_34` ASC) VISIBLE,
  INDEX `fk_ingressantes_QT_ING_35_39_idx` (`ingressantes_QT_ING_35_39` ASC) VISIBLE,
  INDEX `fk_ingressantes_QT_ING_40_49_idx` (`ingressantes_QT_ING_40_49` ASC) VISIBLE,
  INDEX `fk_ingressantes_QT_ING_50_59_idx` (`ingressantes_QT_ING_50_59` ASC) VISIBLE,
  INDEX `fk_ingressantes_QT_ING_60_MAIS_idx` (`ingressantes_QT_ING_60_MAIS` ASC) VISIBLE,
  CONSTRAINT `fk_instituicao_TP_ORGANIZACAO_ACADEMICA0`
    FOREIGN KEY (`instituicao_TP_ORGANIZACAO_ACADEMICA`)
    REFERENCES `edu_superior`.`instituicao` (`TP_ORGANIZACAO_ACADEMICA`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_instituicao_TP_REDE0`
    FOREIGN KEY (`instituicao_TP_REDE`)
    REFERENCES `edu_superior`.`instituicao` (`TP_REDE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_curso_TP_MODALIDADE_ENSINO0`
    FOREIGN KEY (`curso_TP_MODALIDADE_ENSINO`)
    REFERENCES `edu_superior`.`curso` (`TP_MODALIDADE_ENSINO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_localoferta_NO_REGIAO0`
    FOREIGN KEY (`localoferta_NO_REGIAO`)
    REFERENCES `edu_superior`.`localoferta` (`NO_REGIAO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_curso_TP_GRAU_ACADEMICO0`
    FOREIGN KEY (`curso_TP_GRAU_ACADEMICO`)
    REFERENCES `edu_superior`.`curso` (`TP_GRAU_ACADEMICO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingressantes_QT_ING_FEM`
    FOREIGN KEY (`ingressantes_QT_ING_FEM`)
    REFERENCES `edu_superior`.`ingressantes` (`QT_ING_FEM`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingressantes_QT_ING_MASC`
    FOREIGN KEY (`ingressantes_QT_ING_MASC`)
    REFERENCES `edu_superior`.`ingressantes` (`QT_ING_MASC`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingressantes_QT_ING_0_17`
    FOREIGN KEY (`ingressantes_QT_ING_0_17`)
    REFERENCES `edu_superior`.`ingressantes` (`QT_ING_0_17`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingressantes_QT_ING_18_24`
    FOREIGN KEY (`ingressantes_QT_ING_18_24`)
    REFERENCES `edu_superior`.`ingressantes` (`QT_ING_18_24`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingressantes_QT_ING_25_29`
    FOREIGN KEY (`ingressantes_QT_ING_25_29`)
    REFERENCES `edu_superior`.`ingressantes` (`QT_ING_25_29`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingressantes_QT_ING_30_34`
    FOREIGN KEY (`ingressantes_QT_ING_30_34`)
    REFERENCES `edu_superior`.`ingressantes` (`QT_ING_30_34`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingressantes_QT_ING_35_39`
    FOREIGN KEY (`ingressantes_QT_ING_35_39`)
    REFERENCES `edu_superior`.`ingressantes` (`QT_ING_35_39`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingressantes_QT_ING_40_49`
    FOREIGN KEY (`ingressantes_QT_ING_40_49`)
    REFERENCES `edu_superior`.`ingressantes` (`QT_ING_40_49`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingressantes_QT_ING_50_59`
    FOREIGN KEY (`ingressantes_QT_ING_50_59`)
    REFERENCES `edu_superior`.`ingressantes` (`QT_ING_50_59`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingressantes_QT_ING_60_MAIS`
    FOREIGN KEY (`ingressantes_QT_ING_60_MAIS`)
    REFERENCES `edu_superior`.`ingressantes` (`QT_ING_60_MAIS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
