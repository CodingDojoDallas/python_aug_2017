SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';
-- Schema user_reg
-- Schema user_reg
CREATE SCHEMA IF NOT EXISTS user_reg DEFAULT CHARACTER SET utf8 ;
USE user_reg ;
-- Table user_reg.users
CREATE TABLE IF NOT EXISTS user_reg.users (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NULL,
  email VARCHAR(45) NULL,
  password VARCHAR(45) NULL,
  salt VARCHAR(255) NULL,
  created_at DATETIME NULL,
  updated_at DATETIME NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB;
-- Table user_reg.messages
CREATE TABLE IF NOT EXISTS user_reg.messages (
  id INT NOT NULL AUTO_INCREMENT,
  message_text TEXT NULL,
  created_at DATETIME NULL,
  updated_at DATETIME NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (id),
  INDEX fk_messages_users_idx (user_id ASC),
  CONSTRAINT fk_messages_users
    FOREIGN KEY (user_id)
    REFERENCES user_reg.users (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
-- Table user_reg.comments
CREATE TABLE IF NOT EXISTS user_reg.comments (
  message_id INT NOT NULL,
  user_id INT NOT NULL,
  comment TEXT NULL,
  created_at DATETIME NULL,
  updated_at DATETIME NULL,
  INDEX fk_comments_messages1_idx (message_id ASC),
  INDEX fk_comments_users1_idx (user_id ASC),
  CONSTRAINT fk_comments_messages1
    FOREIGN KEY (message_id)
    REFERENCES user_reg.messages (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_comments_users1
    FOREIGN KEY (user_id)
    REFERENCES user_reg.users (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;