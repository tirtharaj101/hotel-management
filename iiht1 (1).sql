-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jun 03, 2021 at 02:28 PM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `iiht1`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE IF NOT EXISTS `customer` (
  `ref` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `father` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `pincode` varchar(50) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `nationality` varchar(50) NOT NULL,
  `idproof` varchar(50) NOT NULL,
  `idnumber` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  PRIMARY KEY (`ref`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8895 ;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`ref`, `name`, `father`, `gender`, `pincode`, `mobile`, `email`, `nationality`, `idproof`, `idnumber`, `address`) VALUES
(7601, 'Debayan Basu', 'Tarak Basu', 'Male', '700129', '8478697865', 'basu23@gmail.com', 'Bangladeshi', 'Passport', '234567890987', 'Dhaka'),
(7702, 'tanmoy sarkar', 'pc sarkar', 'Male', '700120', '1234567890', 'tanmoy@brazzers.com', 'Indian', 'Adhaar Card', '123456789012', 'barrackpore kundu bari'),
(8117, 'tirtha', 'tapas', 'Male', '700120', '9875302855', 'dastirtharaj10@gmail.com', 'Indian', 'Adhaar Card', '38834382204', 'monirampore,barrackpore.'),
(8894, 'sunny das', 'arun das', 'Male', '700126', '7003444797', 'sunnydas@gmail.com', 'Others', 'Passport', '1234567890', 'barasat mochpole');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE IF NOT EXISTS `room` (
  `RoomNo` int(11) NOT NULL AUTO_INCREMENT,
  `BedNo` varchar(50) NOT NULL,
  `Bedtype` varchar(50) NOT NULL,
  `RoomType` varchar(50) NOT NULL,
  `Bathroom` varchar(50) NOT NULL,
  `RoomService` varchar(50) NOT NULL,
  PRIMARY KEY (`RoomNo`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`RoomNo`, `BedNo`, `Bedtype`, `RoomType`, `Bathroom`, `RoomService`) VALUES
(1, '2', 'Double', 'Ac', 'Attach', 'yes'),
(2, '3', 'Double', 'Air Conditioned', 'Attached', 'No'),
(3, '2', 'Double', 'Air Conditioned', 'Attached', 'Yes');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE IF NOT EXISTS `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `f_name` varchar(200) NOT NULL,
  `l_name` varchar(200) NOT NULL,
  `contact` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `question` varchar(200) NOT NULL,
  `answer` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `f_name`, `l_name`, `contact`, `email`, `question`, `answer`, `password`) VALUES
(1, 'tirtha', 'das', '1234567890', 'tirtha@gmail.com', 'Your Pet Name', 'lanka pakhi', '12345'),
(2, 'sunny ', 'Das', '8697084337', 'sunny@gmail.com', 'Your Birth Place', 'barasat', '12345');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
