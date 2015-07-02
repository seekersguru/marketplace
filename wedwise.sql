-- phpMyAdmin SQL Dump
-- version 4.3.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jul 02, 2015 at 04:37 PM
-- Server version: 5.6.24
-- PHP Version: 5.6.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `wedwise`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add customer', 7, 'add_customer'),
(20, 'Can change customer', 7, 'change_customer'),
(21, 'Can delete customer', 7, 'delete_customer'),
(22, 'Can add category', 8, 'add_category'),
(23, 'Can change category', 8, 'change_category'),
(24, 'Can delete category', 8, 'delete_category'),
(25, 'Can add vendor', 9, 'add_vendor'),
(26, 'Can change vendor', 9, 'change_vendor'),
(27, 'Can delete vendor', 9, 'delete_vendor'),
(28, 'Can add vendor lead', 10, 'add_vendorlead'),
(29, 'Can change vendor lead', 10, 'change_vendorlead'),
(30, 'Can delete vendor lead', 10, 'delete_vendorlead');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(256) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$12000$cuaKF9yaj59W$PjlRnLv7o3YJMQcDRprsBw6I5x95l9KcBLvRC4JotxI=', '2015-07-02 02:52:28', 1, 'root', '', '', 'root@gm.com', 1, 1, '2015-06-28 17:32:56'),
(33, 'pbkdf2_sha256$12000$oDloHP51dspv$9EfQuvam72w6YUuiJx1vRuF2UknGM9PYjAkU9DZ89/4=', '2015-06-29 12:23:08', 0, 'nishu.ssddsaxenadd@gmail.com', '', '', 'nishu.ssddsaxenadd@gmail.com', 0, 1, '2015-06-29 12:23:08'),
(34, 'pbkdf2_sha256$12000$4so8CYr1ZjoZ$AfAKDYEssJV4AriRvYKTxtpLVET6TvxsLQKeWdAVUmI=', '2015-06-29 12:23:15', 0, 'nishu.ssddccsaxenadd@gmail.com', '', '', 'nishu.ssddccsaxenadd@gmail.com', 0, 1, '2015-06-29 12:23:15'),
(36, 'pbkdf2_sha256$12000$vYLn0RovmxZ2$C413Fadg3roT61m6hrSyB0tKRt6BMuqDwumOb0vVRIE=', '2015-06-29 12:27:29', 0, 'nishu.ssddssccsaxenadd@gmail.com', '', '', 'nishu.ssddssccsaxenadd@gmail.com', 0, 1, '2015-06-29 12:27:29'),
(37, 'pbkdf2_sha256$12000$8and7zrmxA5F$3CJ1MT9Q/iBtG748KlksEKL+yr0t3rcJUDPFAa0vrlo=', '2015-06-29 12:27:55', 0, 'nishu.ssddsaasccsaxenadd@gmail.com', '', '', 'nishu.ssddsaasccsaxenadd@gmail.com', 0, 1, '2015-06-29 12:27:55'),
(38, 'pbkdf2_sha256$12000$q5otyl6THn9M$HGGZ51TMZz2nUHaWbWKVpkICjgTHjhDQKVRxdLUC5rg=', '2015-06-29 19:27:35', 0, 'ccc', '', '', 'ccc', 0, 1, '2015-06-29 19:27:35'),
(39, 'pbkdf2_sha256$12000$sslW5NPT3Tj6$DmEow6xvpNKgn5jQ6jBQMW2nOp4omXyrcbCNgMaVsRM=', '2015-06-29 19:33:14', 0, 'sss@gm.com', '', '', 'sss@gm.com', 0, 1, '2015-06-29 19:33:14'),
(40, 'pbkdf2_sha256$12000$3TwAwKy1jn4j$NuxepPZyRtNj423TLWBt6vMhkkGwCEvQf0haHJq6WgE=', '2015-06-29 19:33:42', 0, 'ssss@gm.com', '', '', 'ssss@gm.com', 0, 1, '2015-06-29 19:33:42'),
(41, 'pbkdf2_sha256$12000$Zg9ysvG1pPpi$ETrbzb24eJN9KJZ+fN0r28MEwy6e+FGIVXDxdm4CaeU=', '2015-07-02 00:37:30', 0, 'ss@gm.com', '', '', 'ss@gm.com', 0, 1, '2015-07-02 00:37:30'),
(42, 'pbkdf2_sha256$12000$4IEcdRrYQ5dJ$ILxs0ogNsF28Tv1upo3CZQ1GtLuZ2I6aJv5751pycA8=', '2015-07-02 00:38:07', 0, 'ssdd@gm.com', '', '', 'ssdd@gm.com', 0, 1, '2015-07-02 00:38:07'),
(43, 'pbkdf2_sha256$12000$uq3NySYsPx0X$lO3FOnH0leoDG0uwBlkMjfgshPedIUvBCp4a8bIK4go=', '2015-07-02 00:41:32', 0, 'ssdsssd@gm.com', '', '', 'ssdsssd@gm.com', 0, 1, '2015-07-02 00:41:32'),
(44, 'pbkdf2_sha256$12000$MJ7UfTL70mxz$b/waH1CcompA3KIG6nD63+nUCyTrogRo0sa/w3q4Hjg=', '2015-07-02 01:53:52', 0, 'nishu.saxena@gmail.com', '', '', 'nishu.saxena@gmail.com', 0, 1, '2015-07-02 01:53:52'),
(51, 'pbkdf2_sha256$12000$lSZPyS6AQ74C$QWiBmj8unoST+7rJuGsEpAhWnFibaqwH0+uWOj5gi94=', '2015-07-02 14:36:43', 0, 'nishusaxena@gmail.com', '', '', 'nishusaxena@gmail.com', 0, 1, '2015-07-02 14:36:43');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `customer_customer`
--

CREATE TABLE IF NOT EXISTS `customer_customer` (
  `user_id` int(11) NOT NULL,
  `groom_name` varchar(100) NOT NULL,
  `bride_name` varchar(100) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `fbid` varchar(1024) NOT NULL,
  `gid` varchar(1024) NOT NULL,
  `identifier` varchar(512) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer_customer`
--

INSERT INTO `customer_customer` (`user_id`, `groom_name`, `bride_name`, `contact_number`, `fbid`, `gid`, `identifier`) VALUES
(33, 'NNN', 'NNNN', 'NNN', '', '', 'nishu.ssddsaxenadd@gmail.com:xHGJ4LD08HTnP3WhxmVbMvoWoOU'),
(34, 'NNN', 'NNNN', 'NNN', '', '', 'nishu.ssddccsaxenadd@gmail.com:Y2_s_jOreXqApMsUkNonFAFMfFg'),
(36, 'NNN', 'NNNN', 'NNN', '', '', 'nishu.ssddssccsaxenadd@gmail.com:9g4VS6bAJPrVuc3STRhHN9wgxGQ'),
(37, 'NNN', 'NNNN', 'NNN', '', '', 'nishu.ssddsaasccsaxenadd@gmail.com:3exXQeUXm62CcKsHpj4f2gY_fDg'),
(38, 'ccc', 'ccc', 'ccccc', '', '', 'ccc:edgWvDKUo5izxVWTjZHvl0U9pXA'),
(39, '`msmsm', 'mmm', 'mmmm', '', '', 'sss@gm.com:Bjp_Ul4oDb0iA0JeNc87F25vyZg'),
(40, '`msmsm', 'mmm', 'mmmm', '', '', 'ssss@gm.com:ru3h8HnRLJFqE9F8Mj03WkDYdHY'),
(41, 'ss', 'ss', '01010101010', '', '', 'ss@gm.com:WBivtuTuZ5JaF-fl-eghfzgG_nk'),
(42, 'ss', 'ss', '01010101010', '', '', 'ssdd@gm.com:be5saLWEkx5-hZoTN9lIdb0nL7w'),
(43, 'ss', 'ss', '9010101010', '', '', 'ssdsssd@gm.com:HUVFpvfSfvlT6ph7w_ybJ5utPv8'),
(44, 'Nishant', 'HP', '9032092000', '', '', 'nishu.saxena@gmail.com:-aXxfMHFNWGP9SY6d6DStZ0qDnY');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'log entry', 'admin', 'logentry'),
(2, 'permission', 'auth', 'permission'),
(3, 'group', 'auth', 'group'),
(4, 'user', 'auth', 'user'),
(5, 'content type', 'contenttypes', 'contenttype'),
(6, 'session', 'sessions', 'session'),
(7, 'customer', 'customer', 'customer'),
(8, 'category', 'vendor', 'category'),
(9, 'vendor', 'vendor', 'vendor'),
(10, 'vendor lead', 'vendor', 'vendorlead');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2015-06-28 17:31:36'),
(2, 'auth', '0001_initial', '2015-06-28 17:31:50'),
(3, 'admin', '0001_initial', '2015-06-28 17:31:52'),
(4, 'customer', '0001_initial', '2015-06-28 17:31:53'),
(5, 'sessions', '0001_initial', '2015-06-28 17:31:54'),
(6, 'vendor', '0001_initial', '2015-06-28 17:31:59'),
(7, 'customer', '0002_auto_20150629_1300', '2015-06-29 07:32:28'),
(8, 'customer', '0003_auto_20150629_1301', '2015-06-29 07:32:28'),
(9, 'customer', '0004_auto_20150629_1301', '2015-06-29 07:32:29'),
(10, 'vendor', '0002_auto_20150702_1849', '2015-07-02 13:19:48'),
(11, 'vendor', '0003_vendorlead_name', '2015-07-02 13:19:49'),
(12, 'vendor', '0004_auto_20150702_1850', '2015-07-02 13:20:46'),
(13, 'vendor', '0005_auto_20150702_1920', '2015-07-02 13:50:15'),
(14, 'vendor', '0006_vendor_identifier', '2015-07-02 14:36:28');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('q4ui5k158ykuh1fx0mqfd1e16r6cqsye', 'NzQyYWZhNzhlNmFiZmM5ZDZlOWRhMmNiZjczNDQ3NGFmNGMzZjJlMDp7Il9hdXRoX3VzZXJfaGFzaCI6IjhjZDlhNjRjNzQzODE0YTBkYjVlYmUyNDllMDIzYzU4OWQzNWUxODMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2015-07-16 02:52:28');

-- --------------------------------------------------------

--
-- Table structure for table `vendor_category`
--

CREATE TABLE IF NOT EXISTS `vendor_category` (
  `id` int(11) NOT NULL,
  `name` varchar(250) NOT NULL,
  `key` varchar(250) NOT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vendor_category`
--

INSERT INTO `vendor_category` (`id`, `name`, `key`, `image`) VALUES
(1, 'Banquets', 'banquets', ''),
(2, 'Catereres', 'caterers', ''),
(3, 'Decorators', 'decorators', ''),
(4, 'Photographers', 'photographers', ''),
(5, 'Others', 'others', '');

-- --------------------------------------------------------

--
-- Table structure for table `vendor_vendor`
--

CREATE TABLE IF NOT EXISTS `vendor_vendor` (
  `id` int(11) NOT NULL,
  `name` varchar(250) NOT NULL,
  `contact_number` varchar(50) NOT NULL,
  `address` longtext NOT NULL,
  `email` varchar(75) NOT NULL,
  `role` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  `vendor_type_id` int(11),
  `identifier` varchar(512) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vendor_vendor`
--

INSERT INTO `vendor_vendor` (`id`, `name`, `contact_number`, `address`, `email`, `role`, `user_id`, `vendor_type_id`, `identifier`) VALUES
(1, 'Nishant .Saxena', '9032092000', 'Dharam Kran Road', '', '', 51, 1, 'nishusaxena@gmail.com:qfTWg0bJkKk1E_WMxN7uH_PbYOw');

-- --------------------------------------------------------

--
-- Table structure for table `vendor_vendorlead`
--

CREATE TABLE IF NOT EXISTS `vendor_vendorlead` (
  `id` int(11) NOT NULL,
  `email` varchar(75) NOT NULL,
  `address` varchar(512) NOT NULL,
  `mobile` varchar(11) NOT NULL,
  `services` varchar(512) NOT NULL,
  `name` varchar(100)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vendor_vendorlead`
--

INSERT INTO `vendor_vendorlead` (`id`, `email`, `address`, `mobile`, `services`, `name`) VALUES
(1, 'cc@gm.com', 'cc', '9090909090', 'cc', 'cc'),
(2, 'ccaa@gm.com', 'cc', '9090909090', 'cc', 'cc');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `group_id` (`group_id`,`permission_id`), ADD KEY `auth_group_permissions_0e939a4f` (`group_id`), ADD KEY `auth_group_permissions_8373b171` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `content_type_id` (`content_type_id`,`codename`), ADD KEY `auth_permission_417f1b1c` (`content_type_id`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `user_id` (`user_id`,`group_id`), ADD KEY `auth_user_groups_e8701ad4` (`user_id`), ADD KEY `auth_user_groups_0e939a4f` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `user_id` (`user_id`,`permission_id`), ADD KEY `auth_user_user_permissions_e8701ad4` (`user_id`), ADD KEY `auth_user_user_permissions_8373b171` (`permission_id`);

--
-- Indexes for table `customer_customer`
--
ALTER TABLE `customer_customer`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`), ADD KEY `django_admin_log_417f1b1c` (`content_type_id`), ADD KEY `django_admin_log_e8701ad4` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`), ADD KEY `django_session_de54fa62` (`expire_date`);

--
-- Indexes for table `vendor_category`
--
ALTER TABLE `vendor_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vendor_vendor`
--
ALTER TABLE `vendor_vendor`
  ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `user_id` (`user_id`), ADD KEY `vendor_vendor_96b1f972` (`vendor_type_id`);

--
-- Indexes for table `vendor_vendorlead`
--
ALTER TABLE `vendor_vendorlead`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=52;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `vendor_category`
--
ALTER TABLE `vendor_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `vendor_vendor`
--
ALTER TABLE `vendor_vendor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `vendor_vendorlead`
--
ALTER TABLE `vendor_vendorlead`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
ADD CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
ADD CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
ADD CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
ADD CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
ADD CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
ADD CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
ADD CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `customer_customer`
--
ALTER TABLE `customer_customer`
ADD CONSTRAINT `customer_customer_user_id_57101913_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
ADD CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
ADD CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `vendor_vendor`
--
ALTER TABLE `vendor_vendor`
ADD CONSTRAINT `vendor_vendor_user_id_73675de7_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
ADD CONSTRAINT `vendor_vendor_vendor_type_id_6f6c99e_fk_vendor_category_id` FOREIGN KEY (`vendor_type_id`) REFERENCES `vendor_category` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
