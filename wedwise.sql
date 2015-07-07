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
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add customer',7,'add_customer'),(20,'Can change customer',7,'change_customer'),(21,'Can delete customer',7,'delete_customer'),(22,'Can add category',8,'add_category'),(23,'Can change category',8,'change_category'),(24,'Can delete category',8,'delete_category'),(25,'Can add vendor',9,'add_vendor'),(26,'Can change vendor',9,'change_vendor'),(27,'Can delete vendor',9,'delete_vendor'),(28,'Can add vendor lead',10,'add_vendorlead'),(29,'Can change vendor lead',10,'change_vendorlead'),(30,'Can delete vendor lead',10,'delete_vendorlead'),(31,'Can add messages',11,'add_messages'),(32,'Can change messages',11,'change_messages'),(33,'Can delete messages',11,'delete_messages'),(34,'Can add book',12,'add_book'),(35,'Can change book',12,'change_book'),(36,'Can delete book',12,'delete_book'),(37,'Can add bid',13,'add_bid'),(38,'Can change bid',13,'change_bid'),(39,'Can delete bid',13,'delete_bid');
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
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$cuaKF9yaj59W$PjlRnLv7o3YJMQcDRprsBw6I5x95l9KcBLvRC4JotxI=','2015-07-07 12:19:53',1,'root','','','root@gm.com',1,1,'2015-06-28 17:32:56');
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
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-07-07 12:20:14','3','vendor@test.com belong to vendor Banquets (as )',3,'',9,1),(2,'2015-07-07 12:20:14','2','root belong to vendor Banquets (as Admin)',3,'',9,1),(3,'2015-07-07 12:20:14','1','nishusaxena@gmail.com belong to vendor Banquets (as )',3,'',9,1),(4,'2015-07-07 12:21:05','38','ccc',3,'',4,1),(5,'2015-07-07 12:21:05','53','customer@test.com',3,'',4,1),(6,'2015-07-07 12:21:05','44','nishu.saxena@gmail.com',3,'',4,1),(7,'2015-07-07 12:21:05','34','nishu.ssddccsaxenadd@gmail.com',3,'',4,1),(8,'2015-07-07 12:21:05','37','nishu.ssddsaasccsaxenadd@gmail.com',3,'',4,1),(9,'2015-07-07 12:21:05','33','nishu.ssddsaxenadd@gmail.com',3,'',4,1),(10,'2015-07-07 12:21:05','36','nishu.ssddssccsaxenadd@gmail.com',3,'',4,1),(11,'2015-07-07 12:21:05','51','nishusaxena@gmail.com',3,'',4,1),(12,'2015-07-07 12:21:05','41','ss@gm.com',3,'',4,1),(13,'2015-07-07 12:21:05','42','ssdd@gm.com',3,'',4,1),(14,'2015-07-07 12:21:05','43','ssdsssd@gm.com',3,'',4,1),(15,'2015-07-07 12:21:05','39','sss@gm.com',3,'',4,1),(16,'2015-07-07 12:21:05','40','ssss@gm.com',3,'',4,1),(17,'2015-07-07 12:21:05','52','vendor@test.com',3,'',4,1),(18,'2015-07-07 12:27:05','54','jafferbhai@wedwise.in',1,'',4,1),(19,'2015-07-07 12:29:34','54','jafferbhai@wedwise.in',3,'',4,1),(20,'2015-07-07 14:48:47','8','nishu.sacxaenaa@gmailq.com belong to vendor Banquets (as )',3,'',9,1),(21,'2015-07-07 14:48:47','7','nishu.sacxaena@gmailq.com belong to vendor Banquets (as )',3,'',9,1),(22,'2015-07-07 14:48:47','6','nishu.saxaena@gmailq.com belong to vendor Banquets (as )',3,'',9,1),(23,'2015-07-07 14:48:47','5','nishu.saxena@gmailq.com belong to vendor Banquets (as )',3,'',9,1),(24,'2015-07-07 14:48:47','4','nishu.saxena@gmail.com belong to vendor Banquets (as )',3,'',9,1),(25,'2015-07-07 15:48:13','11','nish@gm.com belong to vendor Catereres (as )',3,'',9,1),(26,'2015-07-07 15:48:13','10','nisshu.saxena@gmail.com belong to vendor Catereres (as )',3,'',9,1),(27,'2015-07-07 15:48:13','9','nishu.saxena@gmail.com belong to vendor Catereres (as )',3,'',9,1),(28,'2015-07-07 15:48:35','65','nish@gm.com',3,'',4,1),(29,'2015-07-07 15:48:35','62','nishu.sacxaena@gmailq.com',3,'',4,1),(30,'2015-07-07 15:48:35','63','nishu.sacxaenaa@gmailq.com',3,'',4,1),(31,'2015-07-07 15:48:35','61','nishu.saxaena@gmailq.com',3,'',4,1),(32,'2015-07-07 15:48:35','59','nishu.saxena@gmail.com',3,'',4,1),(33,'2015-07-07 15:48:35','60','nishu.saxena@gmailq.com',3,'',4,1),(34,'2015-07-07 15:48:35','64','nisshu.saxena@gmail.com',3,'',4,1);
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
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'customer','customer','customer'),(8,'category','vendor','category'),(9,'vendor','vendor','vendor'),(10,'vendor lead','vendor','vendorlead'),(11,'messages','wedwise_messages','messages'),(12,'book','wedwise_messages','book'),(13,'bid','wedwise_messages','bid');
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-06-28 17:31:36'),(2,'auth','0001_initial','2015-06-28 17:31:50'),(3,'admin','0001_initial','2015-06-28 17:31:52'),(4,'customer','0001_initial','2015-06-28 17:31:53'),(5,'sessions','0001_initial','2015-06-28 17:31:54'),(6,'vendor','0001_initial','2015-06-28 17:31:59'),(7,'customer','0002_auto_20150629_1300','2015-06-29 07:32:28'),(8,'customer','0003_auto_20150629_1301','2015-06-29 07:32:28'),(9,'customer','0004_auto_20150629_1301','2015-06-29 07:32:29'),(10,'vendor','0002_auto_20150702_1849','2015-07-02 13:19:48'),(11,'vendor','0003_vendorlead_name','2015-07-02 13:19:49'),(12,'vendor','0004_auto_20150702_1850','2015-07-02 13:20:46'),(13,'vendor','0005_auto_20150702_1920','2015-07-02 13:50:15'),(14,'vendor','0006_vendor_identifier','2015-07-02 14:36:28'),(15,'vendor','0007_vendor_dynamic_info','2015-07-02 17:58:44'),(16,'vendor','0008_auto_20150704_0910','2015-07-04 09:10:55'),(17,'wedwise_messages','0001_initial','2015-07-04 19:53:45'),(18,'wedwise_messages','0002_auto_20150704_2010','2015-07-04 20:10:14'),(19,'vendor','0009_remove_vendor_email','2015-07-07 14:31:11'),(20,'wedwise_messages','0003_auto_20150707_1431','2015-07-07 14:31:11');
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
INSERT INTO `django_session` VALUES ('q4ui5k158ykuh1fx0mqfd1e16r6cqsye','NzQyYWZhNzhlNmFiZmM5ZDZlOWRhMmNiZjczNDQ3NGFmNGMzZjJlMDp7Il9hdXRoX3VzZXJfaGFzaCI6IjhjZDlhNjRjNzQzODE0YTBkYjVlYmUyNDllMDIzYzU4OWQzNWUxODMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-07-16 02:52:28'),('vghlrzs5jzcdmloeze7k4ekhkiprt8gj','NzQyYWZhNzhlNmFiZmM5ZDZlOWRhMmNiZjczNDQ3NGFmNGMzZjJlMDp7Il9hdXRoX3VzZXJfaGFzaCI6IjhjZDlhNjRjNzQzODE0YTBkYjVlYmUyNDllMDIzYzU4OWQzNWUxODMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-07-21 12:19:53');
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendor_vendor`
--

LOCK TABLES `vendor_vendor` WRITE;
/*!40000 ALTER TABLE `vendor_vendor` DISABLE KEYS */;
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
-- Table structure for table `wedwise_messages_bid`
--

DROP TABLE IF EXISTS `wedwise_messages_bid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wedwise_messages_bid` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_to` varchar(2) NOT NULL,
  `message` longtext NOT NULL,
  `msg_time` datetime NOT NULL,
  `event_date` date NOT NULL,
  `quoted_price` varchar(512) NOT NULL,
  `bid_price` double NOT NULL,
  `quoted_price_label` varchar(512) NOT NULL,
  `bid_price_entity` double NOT NULL,
  `bid_price_entity_label` varchar(512) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `vendor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wedwise_messages_bid_cb24373b` (`customer_id`),
  KEY `wedwise_messages_bid_96b1f972` (`vendor_id`),
  CONSTRAINT `wedwise_messages__vendor_id_74b2f30336eee45b_fk_vendor_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `vendor_vendor` (`id`),
  CONSTRAINT `wedwis_customer_id_3cca49f03ccf540b_fk_customer_customer_user_id` FOREIGN KEY (`customer_id`) REFERENCES `customer_customer` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wedwise_messages_bid`
--

LOCK TABLES `wedwise_messages_bid` WRITE;
/*!40000 ALTER TABLE `wedwise_messages_bid` DISABLE KEYS */;
/*!40000 ALTER TABLE `wedwise_messages_bid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wedwise_messages_book`
--

DROP TABLE IF EXISTS `wedwise_messages_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wedwise_messages_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_to` varchar(3),
  `msg_time` datetime NOT NULL,
  `quoted_price_label` varchar(512) NOT NULL,
  `message` longtext NOT NULL,
  `customer_id` int(11) NOT NULL,
  `vendor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wedwise_messages_book_cb24373b` (`customer_id`),
  KEY `wedwise_messages_book_96b1f972` (`vendor_id`),
  CONSTRAINT `wedwise_messages__vendor_id_509964d5266538c6_fk_vendor_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `vendor_vendor` (`id`),
  CONSTRAINT `wedwis_customer_id_18c3b9080d988a96_fk_customer_customer_user_id` FOREIGN KEY (`customer_id`) REFERENCES `customer_customer` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wedwise_messages_book`
--

LOCK TABLES `wedwise_messages_book` WRITE;
/*!40000 ALTER TABLE `wedwise_messages_book` DISABLE KEYS */;
/*!40000 ALTER TABLE `wedwise_messages_book` ENABLE KEYS */;
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
  PRIMARY KEY (`id`),
  KEY `wedwise_messages_messages_cb24373b` (`customer_id`),
  KEY `wedwise_messages_messages_96b1f972` (`vendor_id`),
  CONSTRAINT `wedwise_messages__vendor_id_5a214c5fcbedd4d3_fk_vendor_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `vendor_vendor` (`id`),
  CONSTRAINT `wedwis_customer_id_4d15317179ef6bc3_fk_customer_customer_user_id` FOREIGN KEY (`customer_id`) REFERENCES `customer_customer` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
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

-- Dump completed on 2015-07-07 21:19:07
