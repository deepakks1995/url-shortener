Create database shortener;
use shortener;


# Dump of table url
# ------------------------------------------------------------

CREATE TABLE `url` (
  `custom` varchar(32) NOT NULL DEFAULT '',
  `original` varchar(512) NOT NULL DEFAULT '',
  PRIMARY KEY (`custom`)
) ENGINE=InnoDB;

