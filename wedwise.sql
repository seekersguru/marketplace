-- MySQL dump 10.13  Distrib 5.5.43, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: wedwise
-- ------------------------------------------------------
-- Server version	5.5.43-0ubuntu0.14.04.1

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
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add customer',7,'add_customer'),(20,'Can change customer',7,'change_customer'),(21,'Can delete customer',7,'delete_customer'),(22,'Can add category',8,'add_category'),(23,'Can change category',8,'change_category'),(24,'Can delete category',8,'delete_category'),(25,'Can add vendor',9,'add_vendor'),(26,'Can change vendor',9,'change_vendor'),(27,'Can delete vendor',9,'delete_vendor'),(28,'Can add vendor lead',10,'add_vendorlead'),(29,'Can change vendor lead',10,'change_vendorlead'),(30,'Can delete vendor lead',10,'delete_vendorlead');
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
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$cuaKF9yaj59W$PjlRnLv7o3YJMQcDRprsBw6I5x95l9KcBLvRC4JotxI=','2015-07-02 02:52:28',1,'root','','','root@gm.com',1,1,'2015-06-28 17:32:56'),(33,'pbkdf2_sha256$12000$oDloHP51dspv$9EfQuvam72w6YUuiJx1vRuF2UknGM9PYjAkU9DZ89/4=','2015-06-29 12:23:08',0,'nishu.ssddsaxenadd@gmail.com','','','nishu.ssddsaxenadd@gmail.com',0,1,'2015-06-29 12:23:08'),(34,'pbkdf2_sha256$12000$4so8CYr1ZjoZ$AfAKDYEssJV4AriRvYKTxtpLVET6TvxsLQKeWdAVUmI=','2015-06-29 12:23:15',0,'nishu.ssddccsaxenadd@gmail.com','','','nishu.ssddccsaxenadd@gmail.com',0,1,'2015-06-29 12:23:15'),(36,'pbkdf2_sha256$12000$vYLn0RovmxZ2$C413Fadg3roT61m6hrSyB0tKRt6BMuqDwumOb0vVRIE=','2015-06-29 12:27:29',0,'nishu.ssddssccsaxenadd@gmail.com','','','nishu.ssddssccsaxenadd@gmail.com',0,1,'2015-06-29 12:27:29'),(37,'pbkdf2_sha256$12000$8and7zrmxA5F$3CJ1MT9Q/iBtG748KlksEKL+yr0t3rcJUDPFAa0vrlo=','2015-06-29 12:27:55',0,'nishu.ssddsaasccsaxenadd@gmail.com','','','nishu.ssddsaasccsaxenadd@gmail.com',0,1,'2015-06-29 12:27:55'),(38,'pbkdf2_sha256$12000$q5otyl6THn9M$HGGZ51TMZz2nUHaWbWKVpkICjgTHjhDQKVRxdLUC5rg=','2015-06-29 19:27:35',0,'ccc','','','ccc',0,1,'2015-06-29 19:27:35'),(39,'pbkdf2_sha256$12000$sslW5NPT3Tj6$DmEow6xvpNKgn5jQ6jBQMW2nOp4omXyrcbCNgMaVsRM=','2015-06-29 19:33:14',0,'sss@gm.com','','','sss@gm.com',0,1,'2015-06-29 19:33:14'),(40,'pbkdf2_sha256$12000$3TwAwKy1jn4j$NuxepPZyRtNj423TLWBt6vMhkkGwCEvQf0haHJq6WgE=','2015-06-29 19:33:42',0,'ssss@gm.com','','','ssss@gm.com',0,1,'2015-06-29 19:33:42'),(41,'pbkdf2_sha256$12000$Zg9ysvG1pPpi$ETrbzb24eJN9KJZ+fN0r28MEwy6e+FGIVXDxdm4CaeU=','2015-07-02 00:37:30',0,'ss@gm.com','','','ss@gm.com',0,1,'2015-07-02 00:37:30'),(42,'pbkdf2_sha256$12000$4IEcdRrYQ5dJ$ILxs0ogNsF28Tv1upo3CZQ1GtLuZ2I6aJv5751pycA8=','2015-07-02 00:38:07',0,'ssdd@gm.com','','','ssdd@gm.com',0,1,'2015-07-02 00:38:07'),(43,'pbkdf2_sha256$12000$uq3NySYsPx0X$lO3FOnH0leoDG0uwBlkMjfgshPedIUvBCp4a8bIK4go=','2015-07-02 00:41:32',0,'ssdsssd@gm.com','','','ssdsssd@gm.com',0,1,'2015-07-02 00:41:32'),(44,'pbkdf2_sha256$12000$MJ7UfTL70mxz$b/waH1CcompA3KIG6nD63+nUCyTrogRo0sa/w3q4Hjg=','2015-07-02 01:53:52',0,'nishu.saxena@gmail.com','','','nishu.saxena@gmail.com',0,1,'2015-07-02 01:53:52'),(51,'pbkdf2_sha256$12000$lSZPyS6AQ74C$QWiBmj8unoST+7rJuGsEpAhWnFibaqwH0+uWOj5gi94=','2015-07-02 14:36:43',0,'nishusaxena@gmail.com','','','nishusaxena@gmail.com',0,1,'2015-07-02 14:36:43');
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
INSERT INTO `customer_customer` VALUES (33,'NNN','NNNN','NNN','','','nishu.ssddsaxenadd@gmail.com:xHGJ4LD08HTnP3WhxmVbMvoWoOU'),(34,'NNN','NNNN','NNN','','','nishu.ssddccsaxenadd@gmail.com:Y2_s_jOreXqApMsUkNonFAFMfFg'),(36,'NNN','NNNN','NNN','','','nishu.ssddssccsaxenadd@gmail.com:9g4VS6bAJPrVuc3STRhHN9wgxGQ'),(37,'NNN','NNNN','NNN','','','nishu.ssddsaasccsaxenadd@gmail.com:3exXQeUXm62CcKsHpj4f2gY_fDg'),(38,'ccc','ccc','ccccc','','','ccc:edgWvDKUo5izxVWTjZHvl0U9pXA'),(39,'`msmsm','mmm','mmmm','','','sss@gm.com:Bjp_Ul4oDb0iA0JeNc87F25vyZg'),(40,'`msmsm','mmm','mmmm','','','ssss@gm.com:ru3h8HnRLJFqE9F8Mj03WkDYdHY'),(41,'ss','ss','01010101010','','','ss@gm.com:WBivtuTuZ5JaF-fl-eghfzgG_nk'),(42,'ss','ss','01010101010','','','ssdd@gm.com:be5saLWEkx5-hZoTN9lIdb0nL7w'),(43,'ss','ss','9010101010','','','ssdsssd@gm.com:HUVFpvfSfvlT6ph7w_ybJ5utPv8'),(44,'Nishant','HP','9032092000','','','nishu.saxena@gmail.com:-aXxfMHFNWGP9SY6d6DStZ0qDnY');
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'customer','customer','customer'),(8,'category','vendor','category'),(9,'vendor','vendor','vendor'),(10,'vendor lead','vendor','vendorlead');
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-06-28 17:31:36'),(2,'auth','0001_initial','2015-06-28 17:31:50'),(3,'admin','0001_initial','2015-06-28 17:31:52'),(4,'customer','0001_initial','2015-06-28 17:31:53'),(5,'sessions','0001_initial','2015-06-28 17:31:54'),(6,'vendor','0001_initial','2015-06-28 17:31:59'),(7,'customer','0002_auto_20150629_1300','2015-06-29 07:32:28'),(8,'customer','0003_auto_20150629_1301','2015-06-29 07:32:28'),(9,'customer','0004_auto_20150629_1301','2015-06-29 07:32:29'),(10,'vendor','0002_auto_20150702_1849','2015-07-02 13:19:48'),(11,'vendor','0003_vendorlead_name','2015-07-02 13:19:49'),(12,'vendor','0004_auto_20150702_1850','2015-07-02 13:20:46'),(13,'vendor','0005_auto_20150702_1920','2015-07-02 13:50:15'),(14,'vendor','0006_vendor_identifier','2015-07-02 14:36:28'),(15,'vendor','0007_vendor_dynamic_info','2015-07-02 17:58:44'),(16,'vendor','0008_auto_20150704_0910','2015-07-04 09:10:55');
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
INSERT INTO `django_session` VALUES ('q4ui5k158ykuh1fx0mqfd1e16r6cqsye','NzQyYWZhNzhlNmFiZmM5ZDZlOWRhMmNiZjczNDQ3NGFmNGMzZjJlMDp7Il9hdXRoX3VzZXJfaGFzaCI6IjhjZDlhNjRjNzQzODE0YTBkYjVlYmUyNDllMDIzYzU4OWQzNWUxODMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-07-16 02:52:28');
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
  `email` varchar(75) NOT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendor_vendor`
--

LOCK TABLES `vendor_vendor` WRITE;
/*!40000 ALTER TABLE `vendor_vendor` DISABLE KEYS */;
INSERT INTO `vendor_vendor` VALUES (1,'Nishant .Saxena','9032092000','Dharam Kran Road','','',51,1,'nishusaxena@gmail.com:qfTWg0bJkKk1E_WMxN7uH_PbYOw','2015-07-02','',''),(2,'sss','ss','sss','ssds@gmail.com','Admin',1,1,'sss','ssss','','');
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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-07-04 14:45:57
