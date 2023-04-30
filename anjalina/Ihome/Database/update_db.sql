/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - ihome
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ihome` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `ihome`;

/*Table structure for table `area` */

DROP TABLE IF EXISTS `area`;

CREATE TABLE `area` (
  `area_id` int(11) NOT NULL AUTO_INCREMENT,
  `area_name` varchar(50) DEFAULT NULL,
  `area_description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`area_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `area` */

insert  into `area`(`area_id`,`area_name`,`area_description`) values (3,'Alappuzha','				Good Place to work.is\r\n			'),(4,'kottayam','			nice city'),(5,'ernakulam','	abcd		'),(6,'malappuram','			asd'),(7,'kozhikode','			asdf'),(8,'pathanamthitta','			qwe'),(9,'idukki','	asd		'),(10,'palakkad','			asde'),(11,'kannur','		qwer	'),(12,'wayanad','	qwert		'),(13,'trivandrum','			asdfg'),(15,'Kochi','	ghhh		');

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `provider_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  `booking_date` date DEFAULT NULL,
  `booking_status` varchar(50) DEFAULT NULL,
  `booking_description` varchar(200) DEFAULT NULL,
  `work_image1` varchar(500) DEFAULT NULL,
  `work_image2` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`user_id`,`provider_id`,`service_id`,`booking_date`,`booking_status`,`booking_description`,`work_image1`,`work_image2`) values (1,1,1,1,'2021-04-16','booked','hhj','static/uploads/de390cd6-f3c3-433d-8f67-0d1190aeef4dBZONE.png','static/uploads/33906584-a72e-4ec1-a443-729b81e70d41Circle.png'),(2,2,1,1,'2022-02-07','booked','nppp','static/uploads/8f5688eb-189f-4859-aab7-87055a920313IMG-20200530-WA0012.jpg','static/uploads/1f8ec7d4-e2f4-45f0-a95d-b447e019bb5dIMG-20200530-WA0012.jpg');

/*Table structure for table `cart` */

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cart_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `cart` */

insert  into `cart`(`cart_id`,`user_id`,`product_id`,`quantity`) values (1,2,1,'1'),(2,2,1,'1');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `complaint_description` varchar(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  `complaint_date` date DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`user_id`,`complaint_description`,`reply`,`complaint_date`) values (1,1,'Bad Quality','Ok.','2021-02-11'),(2,2,'sddd','pending','2022-02-07');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'bency','bency','provider'),(3,'bless','bless','provider'),(5,'anu','anuelsa123A','user'),(6,'ajin','ajin','user'),(7,'libi','libi','provider');

/*Table structure for table `order_details` */

DROP TABLE IF EXISTS `order_details`;

CREATE TABLE `order_details` (
  `od_id` int(11) NOT NULL AUTO_INCREMENT,
  `om_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `qunatity` varchar(50) DEFAULT NULL,
  `total_amount` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`od_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `order_details` */

insert  into `order_details`(`od_id`,`om_id`,`product_id`,`qunatity`,`total_amount`,`status`) values (1,1,1,'1','10000','ordered'),(2,1,1,'1','10000','ordered'),(3,2,1,'1','10000','ordered'),(4,2,1,'1','10000','ordered'),(5,3,1,'1','10000','ordered'),(6,3,1,'1','10000','ordered');

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `om_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `delivery_status` varchar(50) DEFAULT NULL,
  `total_amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`om_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `order_master` */

insert  into `order_master`(`om_id`,`user_id`,`date`,`delivery_status`,`total_amount`) values (1,2,'2022-02-07','0','10000'),(2,2,'2022-02-07','0','10000'),(3,2,'2022-02-07','pending','10000');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `proposal_id` int(11) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  `amount_paid` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`booking_id`,`proposal_id`,`payment_date`,`amount_paid`) values (1,1,1,'2021-02-11','5000'),(2,1,1,'2021-02-11','5000'),(3,1,1,'2021-02-11','5000'),(4,1,1,'2021-04-16','5000'),(5,1,1,'2021-04-16','5000'),(6,1,1,'2021-04-16','5000');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `shop_id` int(11) DEFAULT NULL,
  `product_name` varchar(50) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `stock` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`shop_id`,`product_name`,`image`,`amount`,`stock`) values (1,1,'pr1','static/uploads/9ee87075-3711-4d8e-b7cd-546f5c0c8549IMG-20200530-WA0013.jpg','10000','116'),(2,1,'df','static/uploads/288b7d79-48fd-48d3-bfb6-baecbd14be82IMG-20200530-WA0012.jpg','10000','122');

/*Table structure for table `proposal` */

DROP TABLE IF EXISTS `proposal`;

CREATE TABLE `proposal` (
  `proposal_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `proposal_description` varchar(200) DEFAULT NULL,
  `estimated_amount` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`proposal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `proposal` */

insert  into `proposal`(`proposal_id`,`booking_id`,`proposal_description`,`estimated_amount`,`date`,`status`) values (1,1,'Interior','5000','2021-02-10','confirmed');

/*Table structure for table `ratings` */

DROP TABLE IF EXISTS `ratings`;

CREATE TABLE `ratings` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `provider_id` int(11) DEFAULT NULL,
  `review` varchar(100) DEFAULT NULL,
  `ratings` varchar(50) DEFAULT NULL,
  `review_date` date DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `ratings` */

insert  into `ratings`(`rating_id`,`user_id`,`provider_id`,`review`,`ratings`,`review_date`) values (1,1,1,'Good Work','1','2021-02-11'),(2,2,2,'sddd','5','2022-02-07');

/*Table structure for table `service_provider` */

DROP TABLE IF EXISTS `service_provider`;

CREATE TABLE `service_provider` (
  `provider_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `area_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`provider_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `service_provider` */

insert  into `service_provider`(`provider_id`,`login_id`,`area_id`,`first_name`,`last_name`,`place`,`pincode`,`phone_number`,`email`) values (1,3,3,'Blesson','Baby','Alappy','690890','8978654533','bless@gmail.com'),(2,7,5,'Libin','Mathew','Alappuzha','690890','9196564323','libi@gmail.com');

/*Table structure for table `service_type` */

DROP TABLE IF EXISTS `service_type`;

CREATE TABLE `service_type` (
  `service_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `service_type_name` varchar(50) DEFAULT NULL,
  `service_type_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`service_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `service_type` */

insert  into `service_type`(`service_type_id`,`service_type_name`,`service_type_description`) values (1,'Interior','Good');

/*Table structure for table `services` */

DROP TABLE IF EXISTS `services`;

CREATE TABLE `services` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `provider_id` int(11) DEFAULT NULL,
  `service_type_id` int(11) DEFAULT NULL,
  `service_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `services` */

insert  into `services`(`service_id`,`provider_id`,`service_type_id`,`service_name`) values (1,1,1,'Design');

/*Table structure for table `shop` */

DROP TABLE IF EXISTS `shop`;

CREATE TABLE `shop` (
  `shop_id` int(11) NOT NULL AUTO_INCREMENT,
  `provider_id` int(11) DEFAULT NULL,
  `shop_name` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`shop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `shop` */

insert  into `shop`(`shop_id`,`provider_id`,`shop_name`,`phone`,`email`,`place`) values (1,2,'Shop1','9656323078','shop1@gamil.com','Alappuzha'),(2,2,'Shop2','9189786756','bless@gmail.com','Alappuzha');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `area_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `house_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `contact` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`user_id`,`login_id`,`area_id`,`first_name`,`last_name`,`house_name`,`place`,`pincode`,`district`,`contact`,`email`) values (1,5,3,'Anu','Elsa','Modiyil','Kuttanad','690890','Alappuzha','9656323078','anu@gmail.com'),(2,6,3,'ajin','abraham','Parappattu (h),','chenngannor','686539','alapuzha','9696969696','ajinabraham1111@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
