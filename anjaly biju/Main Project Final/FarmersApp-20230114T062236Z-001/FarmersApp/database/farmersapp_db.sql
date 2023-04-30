/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - farmesapp
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`farmesapp` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `farmesapp`;

/*Table structure for table `agridepartment` */

DROP TABLE IF EXISTS `agridepartment`;

CREATE TABLE `agridepartment` (
  `dep_id` int(11) NOT NULL AUTO_INCREMENT,
  `dep_name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`dep_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `agridepartment` */

insert  into `agridepartment`(`dep_id`,`dep_name`,`description`) values (1,'Testing','Good\r\n                    '),(2,'Finance','\r\n       Good             ');

/*Table structure for table `agriofficer` */

DROP TABLE IF EXISTS `agriofficer`;

CREATE TABLE `agriofficer` (
  `officer_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `dep_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `mobileno` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`officer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `agriofficer` */

insert  into `agriofficer`(`officer_id`,`log_id`,`dep_id`,`fname`,`lname`,`gender`,`address`,`place`,`mobileno`,`email`) values (1,6,1,'Baby','Daniel','male','                        \r\n    Good                ','Kuttanad','8978675671','baby@gmail.com');

/*Table structure for table `cart` */

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(11) DEFAULT NULL,
  `machine_id` int(11) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cart_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `cart` */

insert  into `cart`(`cart_id`,`farmer_id`,`machine_id`,`quantity`) values (1,3,1,'5'),(2,3,1,'5'),(3,3,1,'6'),(4,3,1,'6'),(5,3,1,'5');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`cat_name`) values (1,'Category1');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(11) DEFAULT NULL,
  `complaint` varchar(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`farmer_id`,`complaint`,`reply`,`date`) values (1,3,'\r\n      bad              ','Let me check','2022-01-11');

/*Table structure for table `crop` */

DROP TABLE IF EXISTS `crop`;

CREATE TABLE `crop` (
  `crop_id` int(11) NOT NULL AUTO_INCREMENT,
  `crop_name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`crop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `crop` */

insert  into `crop`(`crop_id`,`crop_name`,`description`) values (1,'Croptype1','Good\r\n                    ');

/*Table structure for table `enquiry` */

DROP TABLE IF EXISTS `enquiry`;

CREATE TABLE `enquiry` (
  `enquiry_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(11) DEFAULT NULL,
  `officer_id` int(11) DEFAULT NULL,
  `message` varchar(500) DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`enquiry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `enquiry` */

insert  into `enquiry`(`enquiry_id`,`farmer_id`,`officer_id`,`message`,`reply`,`date`) values (1,3,1,'Helo..','Okk','2022-01-11');

/*Table structure for table `farmerregister` */

DROP TABLE IF EXISTS `farmerregister`;

CREATE TABLE `farmerregister` (
  `farmer_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `mobileno` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`farmer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `farmerregister` */

insert  into `farmerregister`(`farmer_id`,`log_id`,`fname`,`lname`,`address`,`gender`,`place`,`district`,`state`,`country`,`pincode`,`mobileno`) values (3,7,'Bency','Baby','Modiyil','female','Kuttanad','Alappuzha','Kerala','India','690890','8978675671');

/*Table structure for table `fertiliser` */

DROP TABLE IF EXISTS `fertiliser`;

CREATE TABLE `fertiliser` (
  `fertiliser_id` int(11) NOT NULL AUTO_INCREMENT,
  `fertiliser_name` varchar(50) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `features` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`fertiliser_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `fertiliser` */

insert  into `fertiliser`(`fertiliser_id`,`fertiliser_name`,`description`,`features`) values (1,'Fertiliser1','Good\r\n                    ','Good');

/*Table structure for table `ideas` */

DROP TABLE IF EXISTS `ideas`;

CREATE TABLE `ideas` (
  `ideas_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(11) DEFAULT NULL,
  `officer_id` int(11) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`ideas_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `ideas` */

insert  into `ideas`(`ideas_id`,`farmer_id`,`officer_id`,`message`,`reply`,`date`) values (1,3,1,'\r\n            Ideas2        ','Okk','2022-01-11');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`log_id`,`username`,`password`,`type`) values (1,'admin','admin','admin'),(6,'baby','baby','Officer'),(7,'bency','bency','farmer'),(8,'libin','libin','dealer');

/*Table structure for table `machine` */

DROP TABLE IF EXISTS `machine`;

CREATE TABLE `machine` (
  `machine_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `machine_name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  `aval_quantity` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`machine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `machine` */

insert  into `machine`(`machine_id`,`category_id`,`machine_name`,`description`,`amount`,`image`,`aval_quantity`) values (1,1,'Machine1','\r\n         Good           ','10000','static/uploads/4910bb9f-96f2-4ec4-9cad-ba1568799772IMG-20200528-WA0004.jpg','73'),(2,1,'Machine2','Good\r\n                    ','5000','static/uploads/2049fd94-9b75-4d36-aa2f-04aa23535cb9IMG-20200530-WA0012.jpg','2');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notify_id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`notify_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notify_id`,`message`,`date`) values (2,'Good\r\n                    ','2022-01-11');

/*Table structure for table `order_details` */

DROP TABLE IF EXISTS `order_details`;

CREATE TABLE `order_details` (
  `od_id` int(11) NOT NULL AUTO_INCREMENT,
  `om_id` int(11) DEFAULT NULL,
  `machine_id` int(11) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `total_amount` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`od_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `order_details` */

insert  into `order_details`(`od_id`,`om_id`,`machine_id`,`quantity`,`total_amount`,`status`) values (1,1,1,'5','50000','ordered');

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `om_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `delivery_status` varchar(50) DEFAULT NULL,
  `total_amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`om_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `order_master` */

insert  into `order_master`(`om_id`,`farmer_id`,`date`,`delivery_status`,`total_amount`) values (1,3,'2022-01-12','Order Accept','50000');

/*Table structure for table `soil_type` */

DROP TABLE IF EXISTS `soil_type`;

CREATE TABLE `soil_type` (
  `soil_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `soil_type_name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`soil_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `soil_type` */

insert  into `soil_type`(`soil_type_id`,`soil_type_name`,`description`) values (1,'SoilType1','\r\nGood'),(2,'SoilType2','\r\nGood');

/*Table structure for table `technicalregisters` */

DROP TABLE IF EXISTS `technicalregisters`;

CREATE TABLE `technicalregisters` (
  `tec_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `mobileno` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`tec_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `technicalregisters` */

insert  into `technicalregisters`(`tec_id`,`log_id`,`fname`,`lname`,`address`,`gender`,`place`,`district`,`state`,`country`,`email`,`mobileno`) values (1,8,'Libin','Mathew','ABCD\r\n                    ','male','Thiruvalla','Alappuzha','Kerala','India','690900','9656432323');

/*Table structure for table `tutorials` */

DROP TABLE IF EXISTS `tutorials`;

CREATE TABLE `tutorials` (
  `tutorial_id` int(11) NOT NULL AUTO_INCREMENT,
  `officer_id` int(11) DEFAULT NULL,
  `path` varchar(500) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`tutorial_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tutorials` */

insert  into `tutorials`(`tutorial_id`,`officer_id`,`path`,`date`) values (1,1,'static/uploads/e28edb00-eb47-489a-8857-9b2657a8b158VID-20210519-WA0050.mp4','2022-01-11');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
