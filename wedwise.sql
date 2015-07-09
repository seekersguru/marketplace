-- MySQL dump 10.13  Distrib 5.6.16, for osx10.9 (x86_64)
--
-- Host: localhost    Database: wedwise
-- ------------------------------------------------------
-- Server version	5.6.16

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add customer',7,'add_customer'),(20,'Can change customer',7,'change_customer'),(21,'Can delete customer',7,'delete_customer'),(22,'Can add category',8,'add_category'),(23,'Can change category',8,'change_category'),(24,'Can delete category',8,'delete_category'),(25,'Can add vendor',9,'add_vendor'),(26,'Can change vendor',9,'change_vendor'),(27,'Can delete vendor',9,'delete_vendor'),(28,'Can add vendor lead',10,'add_vendorlead'),(29,'Can change vendor lead',10,'change_vendorlead'),(30,'Can delete vendor lead',10,'delete_vendorlead'),(31,'Can add messages',11,'add_messages'),(32,'Can change messages',11,'change_messages'),(33,'Can delete messages',11,'delete_messages');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(256) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$cuaKF9yaj59W$PjlRnLv7o3YJMQcDRprsBw6I5x95l9KcBLvRC4JotxI=','2015-07-02 02:52:28',1,'root','','','root@gm.com',1,1,'2015-06-28 17:32:56'),(33,'pbkdf2_sha256$12000$oDloHP51dspv$9EfQuvam72w6YUuiJx1vRuF2UknGM9PYjAkU9DZ89/4=','2015-06-29 12:23:08',0,'nishu.ssddsaxenadd@gmail.com','','','nishu.ssddsaxenadd@gmail.com',0,1,'2015-06-29 12:23:08'),(34,'pbkdf2_sha256$12000$4so8CYr1ZjoZ$AfAKDYEssJV4AriRvYKTxtpLVET6TvxsLQKeWdAVUmI=','2015-06-29 12:23:15',0,'nishu.ssddccsaxenadd@gmail.com','','','nishu.ssddccsaxenadd@gmail.com',0,1,'2015-06-29 12:23:15'),(36,'pbkdf2_sha256$12000$vYLn0RovmxZ2$C413Fadg3roT61m6hrSyB0tKRt6BMuqDwumOb0vVRIE=','2015-06-29 12:27:29',0,'nishu.ssddssccsaxenadd@gmail.com','','','nishu.ssddssccsaxenadd@gmail.com',0,1,'2015-06-29 12:27:29'),(37,'pbkdf2_sha256$12000$8and7zrmxA5F$3CJ1MT9Q/iBtG748KlksEKL+yr0t3rcJUDPFAa0vrlo=','2015-06-29 12:27:55',0,'nishu.ssddsaasccsaxenadd@gmail.com','','','nishu.ssddsaasccsaxenadd@gmail.com',0,1,'2015-06-29 12:27:55'),(38,'pbkdf2_sha256$12000$q5otyl6THn9M$HGGZ51TMZz2nUHaWbWKVpkICjgTHjhDQKVRxdLUC5rg=','2015-06-29 19:27:35',0,'ccc','','','ccc',0,1,'2015-06-29 19:27:35'),(39,'pbkdf2_sha256$12000$sslW5NPT3Tj6$DmEow6xvpNKgn5jQ6jBQMW2nOp4omXyrcbCNgMaVsRM=','2015-06-29 19:33:14',0,'sss@gm.com','','','sss@gm.com',0,1,'2015-06-29 19:33:14'),(40,'pbkdf2_sha256$12000$3TwAwKy1jn4j$NuxepPZyRtNj423TLWBt6vMhkkGwCEvQf0haHJq6WgE=','2015-06-29 19:33:42',0,'ssss@gm.com','','','ssss@gm.com',0,1,'2015-06-29 19:33:42'),(41,'pbkdf2_sha256$12000$Zg9ysvG1pPpi$ETrbzb24eJN9KJZ+fN0r28MEwy6e+FGIVXDxdm4CaeU=','2015-07-02 00:37:30',0,'ss@gm.com','','','ss@gm.com',0,1,'2015-07-02 00:37:30'),(42,'pbkdf2_sha256$12000$4IEcdRrYQ5dJ$ILxs0ogNsF28Tv1upo3CZQ1GtLuZ2I6aJv5751pycA8=','2015-07-02 00:38:07',0,'ssdd@gm.com','','','ssdd@gm.com',0,1,'2015-07-02 00:38:07'),(43,'pbkdf2_sha256$12000$uq3NySYsPx0X$lO3FOnH0leoDG0uwBlkMjfgshPedIUvBCp4a8bIK4go=','2015-07-02 00:41:32',0,'ssdsssd@gm.com','','','ssdsssd@gm.com',0,1,'2015-07-02 00:41:32'),(44,'pbkdf2_sha256$12000$MJ7UfTL70mxz$b/waH1CcompA3KIG6nD63+nUCyTrogRo0sa/w3q4Hjg=','2015-07-02 01:53:52',0,'nishu.saxena@gmail.com','','','nishu.saxena@gmail.com',0,1,'2015-07-02 01:53:52'),(51,'pbkdf2_sha256$12000$lSZPyS6AQ74C$QWiBmj8unoST+7rJuGsEpAhWnFibaqwH0+uWOj5gi94=','2015-07-02 14:36:43',0,'nishusaxena@gmail.com','','','nishusaxena@gmail.com',0,1,'2015-07-02 14:36:43'),(52,'pbkdf2_sha256$12000$cWSzGFmtdqoV$aa/fZmONr//hzrFufUbmemsKloHpkMBD/2l00Ob8e6w=','2015-07-04 19:16:44',0,'vendor@test.com','','','vendor@test.com',0,1,'2015-07-04 19:16:44'),(53,'pbkdf2_sha256$12000$dJjs78d7opIh$XnRXyZhuZ5TbEvH1Tb9346RmccFQFA6v71KDAeOHuSQ=','2015-07-04 19:18:15',0,'customer@test.com','','','customer@test.com',0,1,'2015-07-04 19:18:15'),(54,'pbkdf2_sha256$12000$NwOfpn7lZSc8$JhxWKifv2kegWAmmBSkf3et9BNtxzRVRHPodwXd39HA=','2015-07-04 20:55:04',0,'test@test.com','','','test@test.com',0,1,'2015-07-04 20:55:04'),(55,'pbkdf2_sha256$12000$ED7ccVkoobMQ$u8wH2DsCB+xKSx+bxGfB1ZCcqcRVcmD//RkaoJAKys0=','2015-07-04 20:58:04',0,'vendor1@test.com','','','vendor1@test.com',0,1,'2015-07-04 20:58:04'),(56,'pbkdf2_sha256$12000$WxCfstilxf5M$sJtCrmEr0kW3qrEIttiqJkByfDh0gF3XLC9S4Fn2x74=','2015-07-04 20:58:09',0,'test1@test1.com','','','test1@test1.com',0,1,'2015-07-04 20:58:09'),(57,'pbkdf2_sha256$12000$ql0Of4jRb52W$KhBPrJ9SftMpx2d8VTvah1uD7ZFrBFortB1RASSzQwc=','2015-07-04 21:08:13',0,'test2@test2.com','','','test2@test2.com',0,1,'2015-07-04 21:08:13'),(58,'pbkdf2_sha256$12000$RricH6CsBvUS$24YcEAjpKJQC/98nOcevDjimU1+9L+BhlaF8r13zmKY=','2015-07-04 21:24:46',0,'test@test1.com','','','test@test1.com',0,1,'2015-07-04 21:24:46'),(59,'pbkdf2_sha256$12000$z9HsSV418GGO$BXjhO9WzrLRc8yleHUR90IUbithmgucQgDXj9Ux6qDA=','2015-07-04 21:36:22',0,'tedt@test.com','','','tedt@test.com',0,1,'2015-07-04 21:36:22'),(60,'pbkdf2_sha256$12000$zLn9Cq8uGwVJ$en+Zcd6TYOTu3xISHixz3zZPqgEk1v5fmOhlK+sk3Po=','2015-07-04 21:46:15',0,'common@test.com','','','common@test.com',0,1,'2015-07-04 21:46:15'),(61,'pbkdf2_sha256$12000$VAce2UhBHZgB$TN2yZuCD8JIBAwugA0BhFZU7E45D8waaIFZDpBqg4lM=','2015-07-04 21:49:35',0,'aa@aa.com','','','aa@aa.com',0,1,'2015-07-04 21:49:35'),(62,'pbkdf2_sha256$12000$YlGNHYP5nStG$MhSnkQoa9+ggCT4ob96FC353u/XPBtTTX6wXSEu3Yco=','2015-07-05 11:02:13',0,'deepak@gmail.in','','','deepak@gmail.in',0,1,'2015-07-05 11:02:13'),(63,'pbkdf2_sha256$12000$qAAzvCJzpwLB$elXhVI+w0FVEhNlvuei4HT8/L2+SVg9MtXRDulLn5vk=','2015-07-06 17:12:55',0,'test11@test.com','','','test11@test.com',0,1,'2015-07-06 17:12:55'),(64,'pbkdf2_sha256$12000$jzIK5rJO10ON$rcvckrDs/YgJJcSMNA3OXnU2tIrcgRO9aoA9SqWV0n4=','2015-07-06 18:42:38',0,'test12@test.com','','','test12@test.com',0,1,'2015-07-06 18:42:38'),(65,'pbkdf2_sha256$12000$9nch7vCkNyYB$kG1nGaUM8RqX0SiWcunP4Hz0pCE2k5jTRtz2QkavAe4=','2015-07-06 18:49:32',0,'aattyy@aa.com','','','aattyy@aa.com',0,1,'2015-07-06 18:49:32'),(66,'pbkdf2_sha256$12000$q4erH69CVlZJ$9UL3hhpgvP9rFWyncmE+mug+tazz/xKT5vZdSBmzoCU=','2015-07-06 18:56:46',0,'atttt@ttt.com','','','atttt@ttt.com',0,1,'2015-07-06 18:56:46'),(67,'pbkdf2_sha256$12000$lUy5MhuHcPiC$3NatMKoPkyf4ZNjeKwt9fomXYnMpRjErZxDwSekJxAA=','2015-07-06 20:25:33',0,'test13@test.com','','','test13@test.com',0,1,'2015-07-06 20:25:33'),(68,'pbkdf2_sha256$12000$r3qpDrP2Z4hM$QFheUYj1qA9B65vYvNRf7SbIssjCct2JgkWvytZ1EBY=','2015-07-07 16:51:18',0,'abc@abc.com','','','abc@abc.com',0,1,'2015-07-07 16:51:18'),(69,'pbkdf2_sha256$12000$qJ6yo3X2d7Xk$PxkEAA6//6/4+n6JW/u5hPRcphvkN65I/qEgy6JR2Po=','2015-07-09 09:55:43',0,'iamcoder7@gmail.com','','','iamcoder7@gmail.com',0,1,'2015-07-09 09:55:43'),(70,'pbkdf2_sha256$12000$HgZsDOu5WXRp$dFz/pzzAH2b/hOfQ2gNX60zrDcEWe8M/ouDusWksy6M=','2015-07-09 10:17:56',0,'sandeeproy.465@gmail.com','','','sandeeproy.465@gmail.com',0,1,'2015-07-09 10:17:56'),(71,'pbkdf2_sha256$12000$yntxYDAY1Ax9$lWVQ0BECN0L07wQsxO8hG9Z9fbik76iE1q0Kip5iXa8=','2015-07-09 10:35:03',0,'sandeepgaddam123@gmail.com','','','sandeepgaddam123@gmail.com',0,1,'2015-07-09 10:35:03'),(72,'pbkdf2_sha256$12000$aA2agnyTl5AC$zltmM6pc1gVJ083vHYs0aShLY1OJEhj4eJSVK1/v7Eo=','2015-07-09 12:14:27',0,'sljlsd@gm.com','','','sljlsd@gm.com',0,1,'2015-07-09 12:14:27'),(73,'pbkdf2_sha256$12000$HFfKkwzRZ35T$Q9S5F5Cpf5kdl+HvwUcyb0Xaip74LZ3y1RyS4WmJFbI=','2015-07-09 12:29:24',0,'vendor2@test.com','','','vendor2@test.com',0,1,'2015-07-09 12:29:24');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_customer`
--

DROP TABLE IF EXISTS `customer_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer_customer` (
  `user_id` int(11) NOT NULL,
  `groom_name` varchar(100) NOT NULL,
  `bride_name` varchar(100) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `fbid` varchar(1024) NOT NULL,
  `gid` varchar(1024) NOT NULL,
  `identifier` varchar(512) NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `customer_customer_user_id_57101913_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_customer`
--

LOCK TABLES `customer_customer` WRITE;
/*!40000 ALTER TABLE `customer_customer` DISABLE KEYS */;
INSERT INTO `customer_customer` VALUES (33,'NNN','NNNN','NNN','','','nishu.ssddsaxenadd@gmail.com:xHGJ4LD08HTnP3WhxmVbMvoWoOU'),(34,'NNN','NNNN','NNN','','','nishu.ssddccsaxenadd@gmail.com:Y2_s_jOreXqApMsUkNonFAFMfFg'),(36,'NNN','NNNN','NNN','','','nishu.ssddssccsaxenadd@gmail.com:9g4VS6bAJPrVuc3STRhHN9wgxGQ'),(37,'NNN','NNNN','NNN','','','nishu.ssddsaasccsaxenadd@gmail.com:3exXQeUXm62CcKsHpj4f2gY_fDg'),(38,'ccc','ccc','ccccc','','','ccc:edgWvDKUo5izxVWTjZHvl0U9pXA'),(39,'`msmsm','mmm','mmmm','','','sss@gm.com:Bjp_Ul4oDb0iA0JeNc87F25vyZg'),(40,'`msmsm','mmm','mmmm','','','ssss@gm.com:ru3h8HnRLJFqE9F8Mj03WkDYdHY'),(41,'ss','ss','01010101010','','','ss@gm.com:WBivtuTuZ5JaF-fl-eghfzgG_nk'),(42,'ss','ss','01010101010','','','ssdd@gm.com:be5saLWEkx5-hZoTN9lIdb0nL7w'),(43,'ss','ss','9010101010','','','ssdsssd@gm.com:HUVFpvfSfvlT6ph7w_ybJ5utPv8'),(44,'Nishant','HP','9032092000','','','nishu.saxena@gmail.com:-aXxfMHFNWGP9SY6d6DStZ0qDnY'),(53,'Rama','Shayama','8198191891','','','customer@test.com:kdr9UCeqzG783-MMiFBw9axN-BY'),(54,'aa','aa','1234567890','','','test@test.com:hOfgcGJRGI2bbQqLGi_fy8NKrw8'),(57,'aa','bb','9314618580','','','test2@test2.com:Xxug54Hq1vWpC0OdK9VhrORu5Wo'),(58,'aa','aa','9314618580','','','test@test1.com:3zCivYpiAfL64FxLxV24J84joYk'),(59,'aa','aa','1234569632','','','tedt@test.com:RgGxpEUQuBbSI0i80yTQMs7NMoE'),(60,'ni','nn','8989898989','','','common@test.com:q8DZMyZ18TIpyom8gArvFbPP1jM'),(61,'aa','aa','9632587412','','','aa@aa.com:G5gijsaCDuUvnjcpO0Tyy8cIlQQ'),(62,'mahi','deepak','1234567890','','','deepak@gmail.in:QPFehKvCQ3WhLN1rUKoDlT46qRQ'),(63,'aa','bb','9314618580','','','test11@test.com:lQIamudUwrrtp37BDUOhRJfEQRQ'),(64,'aa','bb','9314618580','','','test12@test.com:rVTv7xPq_m17kVLbiXAyjrouvdg'),(67,'aa','aa','8523697110','','','test13@test.com:YRm9t37VY8eVWCSwAjvVOP5HnK4'),(68,'bb','bb','9314618580','','','abc@abc.com:joob6VAzAW_GDHjA2JaKZ2Vlm80'),(70,'aaa','aaa','9000080847','','','sandeeproy.465@gmail.com:Va_v1IjtZB4F8Xv4nc07dOpNnpc');
/*!40000 ALTER TABLE `customer_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'customer','customer','customer'),(8,'category','vendor','category'),(9,'vendor','vendor','vendor'),(10,'vendor lead','vendor','vendorlead'),(11,'messages','wedwise_messages','messages');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-06-28 17:31:36'),(2,'auth','0001_initial','2015-06-28 17:31:50'),(3,'admin','0001_initial','2015-06-28 17:31:52'),(4,'customer','0001_initial','2015-06-28 17:31:53'),(5,'sessions','0001_initial','2015-06-28 17:31:54'),(6,'vendor','0001_initial','2015-06-28 17:31:59'),(7,'customer','0002_auto_20150629_1300','2015-06-29 07:32:28'),(8,'customer','0003_auto_20150629_1301','2015-06-29 07:32:28'),(9,'customer','0004_auto_20150629_1301','2015-06-29 07:32:29'),(10,'vendor','0002_auto_20150702_1849','2015-07-02 13:19:48'),(11,'vendor','0003_vendorlead_name','2015-07-02 13:19:49'),(12,'vendor','0004_auto_20150702_1850','2015-07-02 13:20:46'),(13,'vendor','0005_auto_20150702_1920','2015-07-02 13:50:15'),(14,'vendor','0006_vendor_identifier','2015-07-02 14:36:28'),(15,'vendor','0007_vendor_dynamic_info','2015-07-02 17:58:44'),(16,'vendor','0008_auto_20150704_0910','2015-07-04 09:10:55'),(17,'wedwise_messages','0001_initial','2015-07-04 19:53:45'),(18,'wedwise_messages','0002_auto_20150704_2010','2015-07-04 20:10:14'),(19,'vendor','0009_remove_vendor_email','2015-07-07 16:34:47'),(20,'wedwise_messages','0003_auto_20150707_1431','2015-07-07 16:34:47'),(21,'wedwise_messages','0004_auto_20150709_1426','2015-07-09 14:36:28'),(22,'wedwise_messages','0005_auto_20150709_1706','2015-07-09 17:07:08'),(23,'wedwise_messages','0006_auto_20150709_1710','2015-07-09 17:10:13');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('muydet3umch165gqodnrat1rd177b2qy','YTM3MTRhM2Q5YWY1NTQ2YjMxZjdjZWIwZDhjOGZhYzViNzcxY2M2Zjp7fQ==','2015-07-23 12:29:05'),('q4ui5k158ykuh1fx0mqfd1e16r6cqsye','NzQyYWZhNzhlNmFiZmM5ZDZlOWRhMmNiZjczNDQ3NGFmNGMzZjJlMDp7Il9hdXRoX3VzZXJfaGFzaCI6IjhjZDlhNjRjNzQzODE0YTBkYjVlYmUyNDllMDIzYzU4OWQzNWUxODMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-07-16 02:52:28'),('uxkd3jnmogya9x4uu8hd0x5ht0xn62o9','YTM3MTRhM2Q5YWY1NTQ2YjMxZjdjZWIwZDhjOGZhYzViNzcxY2M2Zjp7fQ==','2015-07-18 20:20:21');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendor_category`
--

DROP TABLE IF EXISTS `vendor_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendor_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `key` varchar(250) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendor_category`
--

LOCK TABLES `vendor_category` WRITE;
/*!40000 ALTER TABLE `vendor_category` DISABLE KEYS */;
INSERT INTO `vendor_category` VALUES (1,'Banquets','banquets',''),(2,'Catereres','caterers',''),(3,'Decorators','decorators',''),(4,'Photographers','photographers',''),(5,'Others','others','');
/*!40000 ALTER TABLE `vendor_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendor_vendor`
--

DROP TABLE IF EXISTS `vendor_vendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendor_vendor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `contact_number` varchar(50) NOT NULL,
  `address` longtext NOT NULL,
  `role` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  `vendor_type_id` int(11) DEFAULT NULL,
  `identifier` varchar(512) NOT NULL,
  `dynamic_info` longtext NOT NULL,
  `fbid` varchar(1024) NOT NULL,
  `gid` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `vendor_vendor_96b1f972` (`vendor_type_id`),
  CONSTRAINT `vendor_vendor_user_id_73675de7_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `vendor_vendor_vendor_type_id_6f6c99e_fk_vendor_category_id` FOREIGN KEY (`vendor_type_id`) REFERENCES `vendor_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendor_vendor`
--

LOCK TABLES `vendor_vendor` WRITE;
/*!40000 ALTER TABLE `vendor_vendor` DISABLE KEYS */;
INSERT INTO `vendor_vendor` VALUES (1,'Nishant .Saxena','9032092000','Dharam Kran Road','',51,1,'nishusaxena@gmail.com:qfTWg0bJkKk1E_WMxN7uH_PbYOw','2015-07-02','',''),(2,'sss','ss','sss','Admin',1,1,'sss','ssss','',''),(3,'Banquet wala','9288298292','Santa kruz navi mumbai','',52,1,'vendor@test.com:-1Jwmiucd0MuY9VftiQ_u7XXquw','','',''),(4,'Ankur','9314618580','test@test.com','',54,1,'test@test.com:hOfgcGJRGI2bbQqLGi_fy8NKrw8','','',''),(5,'Vendor 1','9289298392','jsksfjkjslfs','',55,1,'vendor1@test.com:B4leCmOZkTBmex_Ib_822kAcYGA','','',''),(6,'Ankur Paliwal','9571617403','test1@test1.com','',56,1,'test1@test1.com:BihjOvfdNIvyrCYE9LYBFaz48S0','','',''),(7,'Ankur','1234567890','test2@test2.com','',57,1,'test2@test2.com:Xxug54Hq1vWpC0OdK9VhrORu5Wo','','',''),(8,'Vendor 1','9289298392','jsksfjkjslfs','',60,1,'common@test.com:q8DZMyZ18TIpyom8gArvFbPP1jM','','',''),(9,'Ankur Paliwal','9631245783','aa@aa.com','',61,1,'aa@aa.com:G5gijsaCDuUvnjcpO0Tyy8cIlQQ','','',''),(10,'aa','9314618580','jaipur','',63,1,'test11@test.com:lQIamudUwrrtp37BDUOhRJfEQRQ','','',''),(11,'aa','6325417890','aattyy@aa.com','',65,1,'aattyy@aa.com:cKrNpFhEm4DogRm1a8E6Lhc9YBg','','',''),(12,'aa','8523697410','atttt@ttt.com','',66,1,'atttt@ttt.com:FPXE-xSt1kjI5qqr28OQylmE1Dw','','',''),(13,'aaaa','9314618580','abc@abc.com','',68,1,'abc@abc.com:joob6VAzAW_GDHjA2JaKZ2Vlm80','','',''),(14,'iamcoder','1234567890','i am coder','',69,3,'iamcoder7@gmail.com:NBjGCDE9MFDKwS5Jj_YS7JHPBhc','','0','0'),(15,'Sandee','09090990909','shjk dlshkd askldj','',71,1,'sandeepgaddam123@gmail.com:0brBPprz_TBkGOXqQHzbPuzXVGY','','',''),(16,'nn','909090909','kj kj','',72,1,'sljlsd@gm.com:EzwdOkNwcCntPwy4Q44UlT0ELvk','','',''),(17,'vendor_admin','90290290200','kjkl sj','',73,1,'vendor2@test.com:nfExrGRiw-KCBs5IjnOh5nP5w2A','','','');
/*!40000 ALTER TABLE `vendor_vendor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendor_vendorlead`
--

DROP TABLE IF EXISTS `vendor_vendorlead`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendor_vendorlead` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(75) NOT NULL,
  `address` varchar(512) NOT NULL,
  `mobile` varchar(11) NOT NULL,
  `services` varchar(512) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendor_vendorlead`
--

LOCK TABLES `vendor_vendorlead` WRITE;
/*!40000 ALTER TABLE `vendor_vendorlead` DISABLE KEYS */;
INSERT INTO `vendor_vendorlead` VALUES (1,'cc@gm.com','cc','9090909090','cc','cc'),(2,'ccaa@gm.com','cc','9090909090','cc','cc');
/*!40000 ALTER TABLE `vendor_vendorlead` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wedwise_messages_messages`
--

DROP TABLE IF EXISTS `wedwise_messages_messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wedwise_messages_messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_to` varchar(3) DEFAULT NULL,
  `message` longtext NOT NULL,
  `msg_time` datetime NOT NULL,
  `customer_id` int(11) NOT NULL,
  `vendor_id` int(11) NOT NULL,
  `bid_json` varchar(1024) NOT NULL,
  `bid_price` varchar(100) NOT NULL,
  `bid_quantity` int(11) NOT NULL,
  `book_json` varchar(1024) NOT NULL,
  `event_date` date NOT NULL,
  `status` varchar(1) NOT NULL,
  `time_slot` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wedwise_messages_messages_cb24373b` (`customer_id`),
  KEY `wedwise_messages_messages_96b1f972` (`vendor_id`),
  CONSTRAINT `wedwise_messages__vendor_id_5a214c5fcbedd4d3_fk_vendor_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `vendor_vendor` (`id`),
  CONSTRAINT `wedwis_customer_id_4d15317179ef6bc3_fk_customer_customer_user_id` FOREIGN KEY (`customer_id`) REFERENCES `customer_customer` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wedwise_messages_messages`
--

LOCK TABLES `wedwise_messages_messages` WRITE;
/*!40000 ALTER TABLE `wedwise_messages_messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `wedwise_messages_messages` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-07-09 23:02:21
