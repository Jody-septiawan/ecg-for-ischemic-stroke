-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: May 17, 2021 at 07:00 AM
-- Server version: 5.7.26
-- PHP Version: 7.2.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sinyal`
--

-- --------------------------------------------------------

--
-- Table structure for table `akurasi_subject`
--

CREATE TABLE `akurasi_subject` (
  `id` int(11) NOT NULL,
  `subject` varchar(10) DEFAULT NULL,
  `target` int(11) DEFAULT NULL,
  `prediksi` int(11) DEFAULT NULL,
  `nilai_k` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `akurasi_subject`
--

INSERT INTO `akurasi_subject` (`id`, `subject`, `target`, `prediksi`, `nilai_k`) VALUES
(1, 's0242', 0, 1, 33),
(2, 's0243', 0, 0, 33),
(3, 's0246', 0, 1, 33),
(4, 's0305', 0, 1, 33),
(5, 's0371', 1, 1, 33),
(6, 's0374', 1, 1, 33),
(7, 's0378', 1, 1, 33),
(8, 's0379', 1, 1, 33),
(9, 's0380', 1, 1, 33),
(10, 's0388', 1, 1, 33),
(11, 's0389', 1, 1, 33),
(12, 's0397', 1, 1, 33),
(13, 's0402', 1, 1, 33);

-- --------------------------------------------------------

--
-- Table structure for table `hasil`
--

CREATE TABLE `hasil` (
  `id` int(11) NOT NULL,
  `subject` varchar(10) DEFAULT NULL,
  `jml_puncak` int(11) DEFAULT NULL,
  `jml_data` int(11) DEFAULT NULL,
  `meanrr` float DEFAULT NULL,
  `sdrr` float DEFAULT NULL,
  `cvrr` float DEFAULT NULL,
  `rmssd` float DEFAULT NULL,
  `label` int(11) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `proses` int(11) DEFAULT NULL,
  `is_active` int(11) NOT NULL,
  `over` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `hasil`
--

INSERT INTO `hasil` (`id`, `subject`, `jml_puncak`, `jml_data`, `meanrr`, `sdrr`, `cvrr`, `rmssd`, `label`, `status`, `proses`, `is_active`, `over`) VALUES
(8, 's0064', 0, 0, 618, 65.3835, 10.5799, 19.7026, 0, 'latih', 1, 1, 0),
(9, 's0164', 0, 0, 455, 19.7484, 4.34031, 7.85461, 0, 'latih', 1, 1, 0),
(10, 's0165', 0, 0, 454, 47.6025, 10.4851, 33.7333, 0, 'latih', 1, 1, 0),
(11, 's0172', 0, 0, 467, 37.3229, 7.99206, 42.3581, 0, 'latih', 1, 1, 0),
(12, 's0184', 0, 0, 484, 84.2912, 17.4155, 21.8663, 0, 'latih', 1, 1, 0),
(13, 's0194', 0, 0, 455, 53.5724, 11.7741, 25.8148, 0, 'latih', 1, 1, 0),
(14, 's0200', 0, 0, 431, 70.6187, 16.3848, 19.0774, 0, 'latih', 1, 1, 0),
(15, 's0203', 0, 0, 499, 43.3705, 8.69148, 26.5714, 0, 'latih', 1, 1, 0),
(16, 's0204', 0, 0, 584, 55.9643, 9.58292, 52.6222, 0, 'latih', 1, 1, 0),
(17, 's0207', 0, 0, 427, 23.2594, 5.44717, 21.1643, 0, 'latih', 1, 1, 0),
(18, 's0208', 0, 0, 431, 62.2575, 14.4449, 68.6748, 0, 'latih', 1, 1, 0),
(21, 's0210', 0, 0, 613, 119.662, 19.5207, 192.87, 0, 'latih', 1, 1, 0),
(33, 's0212', 0, 0, 384, 22.9347, 5.97258, 15.581, 0, 'latih', 1, 1, 0),
(34, 's0213', 0, 0, 489, 48.6518, 9.94925, 8.26872, 0, 'latih', 1, 1, 0),
(35, 's0215', 0, 0, 445, 26.4008, 5.93275, 20.3582, 0, 'latih', 1, 1, 0),
(36, 's0218', 0, 0, 476, 45.3211, 9.52123, 21.6702, 0, 'latih', 1, 1, 0),
(37, 's0221', 0, 0, 414, 41.4126, 10.003, 30.507, 0, 'latih', 1, 1, 0),
(38, 's0225', 0, 0, 429, 26.6083, 6.20239, 13.3417, 0, 'latih', 1, 1, 0),
(39, 's0227', 0, 0, 390, 37.4566, 9.60427, 12.8857, 0, 'latih', 1, 1, 0),
(40, 's0228', 0, 0, 538, 44.6654, 8.30212, 18.5409, 0, 'latih', 1, 1, 0),
(41, 's0242', 0, 0, 448, 39.7115, 8.86417, 24.8411, 0, 'uji', 1, 1, 0),
(42, 's0243', 0, 0, 450, 38.7943, 8.62096, 46.9799, 0, 'uji', 1, 1, 0),
(43, 's0246', 0, 0, 317, 26.9815, 8.51151, 2.61302, 0, 'uji', 1, 1, 0),
(44, 's0305', 0, 0, 361, 33.8378, 9.37337, 8.22607, 0, 'uji', 1, 1, 0),
(45, 's0205', 0, 0, 551, 13.6015, 2.46851, 10.4872, 1, 'latih', 1, 1, 0),
(46, 's0214', 0, 0, 383, 47.6445, 12.4398, 19.9321, 1, 'latih', 1, 1, 0),
(47, 's0230', 0, 0, 353, 102.64, 29.0765, 147.821, 1, 'latih', 1, 1, 0),
(48, 's0231', 0, 0, 481, 59.127, 12.2925, 18.5032, 1, 'latih', 1, 1, 0),
(49, 's0232', 0, 0, 362, 34.9714, 9.66061, 17.4584, 1, 'latih', 1, 1, 0),
(50, 's0239', 0, 0, 402, 30.5287, 7.5942, 29.6014, 1, 'latih', 1, 1, 0),
(51, 's0240', 0, 0, 423, 27.4044, 6.47858, 7.05185, 1, 'latih', 1, 1, 0),
(52, 's0244', 0, 0, 348, 25.7488, 7.39908, 5.94048, 1, 'latih', 1, 1, 0),
(53, 's0247', 0, 0, 460, 32.3419, 7.03085, 19.617, 1, 'latih', 1, 1, 0),
(54, 's0248', 0, 0, 416, 35, 8.41346, 46.0334, 1, 'latih', 1, 1, 0),
(55, 's0261', 0, 0, 376, 23.388, 6.22022, 5.86618, 1, 'latih', 1, 1, 0),
(56, 's0277', 0, 0, 302, 28.0179, 9.27743, 5.47593, 1, 'latih', 1, 1, 0),
(57, 's0295', 0, 0, 442, 38.7814, 8.77408, 9.41215, 1, 'latih', 1, 1, 0),
(58, 's0321', 0, 0, 390, 45.2659, 11.6066, 31.8686, 1, 'latih', 1, 1, 0),
(59, 's0322', 0, 0, 408, 26.1725, 6.41483, 29.076, 1, 'latih', 1, 1, 0),
(60, 's0324', 0, 0, 420, 36.7423, 8.74818, 20.4161, 1, 'latih', 1, 1, 0),
(61, 's0331', 0, 0, 440, 43.6807, 9.92742, 20.6106, 1, 'latih', 1, 1, 0),
(62, 's0332', 0, 0, 422, 36.9053, 8.74533, 10.4754, 1, 'latih', 1, 1, 0),
(63, 's0334', 0, 0, 357, 27.2947, 7.64557, 11.0887, 1, 'latih', 1, 1, 0),
(64, 's0336', 0, 0, 409, 25.7682, 6.30029, 7.769, 1, 'latih', 1, 1, 0),
(65, 's0337', 0, 0, 438, 29.7993, 6.8035, 22.8683, 1, 'latih', 1, 1, 0),
(66, 's0340', 0, 0, 398, 85.668, 21.5246, 81.35, 1, 'latih', 1, 1, 0),
(67, 's0348', 0, 0, 403, 27.2764, 6.76833, 27.6, 1, 'latih', 1, 1, 0),
(68, 's0351', 0, 0, 350, 28.2666, 8.07617, 8.36812, 1, 'latih', 1, 1, 0),
(69, 's0352', 0, 0, 428, 45.9347, 10.7324, 33.0162, 1, 'latih', 1, 1, 0),
(70, 's0353', 0, 0, 446, 15.6844, 3.51668, 12.3185, 1, 'latih', 1, 1, 0),
(71, 's0354', 0, 0, 479, 49.3052, 10.2934, 11.5906, 1, 'latih', 1, 1, 0),
(72, 's0355', 0, 0, 465, 55.7853, 11.9968, 21.8265, 1, 'latih', 1, 1, 0),
(73, 's0361', 0, 0, 481, 45.8694, 9.53625, 69.6632, 1, 'latih', 1, 1, 0),
(74, 's0363', 0, 0, 362, 31.7648, 8.7748, 22.9912, 1, 'latih', 1, 1, 0),
(75, 's0371', 0, 0, 432, 53.963, 12.4914, 67.4602, 1, 'uji', 1, 1, 0),
(76, 's0374', 0, 0, 406, 35.0428, 8.63124, 6.88692, 1, 'uji', 1, 1, 0),
(77, 's0378', 0, 0, 438, 63.8905, 14.5869, 17.0868, 1, 'uji', 1, 1, 0),
(78, 's0379', 0, 0, 479, 47.4868, 9.91374, 14.757, 1, 'uji', 1, 1, 0),
(79, 's0380', 0, 0, 565, 46.4866, 8.22771, 22.3195, 1, 'uji', 1, 1, 0),
(80, 's0388', 0, 0, 418, 41.9762, 10.0421, 31.8564, 1, 'uji', 1, 1, 0),
(81, 's0389', 0, 0, 442, 34.1028, 7.71556, 15.0174, 1, 'uji', 1, 1, 0),
(82, 's0397', 0, 0, 394, 76.8245, 19.4986, 109.962, 1, 'uji', 1, 1, 0),
(83, 's0402', 0, 0, 484, 41.5331, 8.58122, 10.5295, 1, 'uji', 1, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `takurasi`
--

CREATE TABLE `takurasi` (
  `id` int(11) NOT NULL,
  `nilai_k` int(11) DEFAULT NULL,
  `akurasi` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `takurasi`
--

INSERT INTO `takurasi` (`id`, `nilai_k`, `akurasi`) VALUES
(1, 1, 53.85),
(2, 2, 46.15),
(3, 3, 61.54),
(4, 4, 46.15),
(5, 5, 69.23),
(6, 6, 61.54),
(7, 7, 53.85),
(8, 8, 46.15),
(9, 9, 69.23),
(10, 10, 38.46),
(11, 11, 69.23),
(12, 12, 61.54),
(13, 13, 76.92),
(14, 14, 69.23),
(15, 15, 69.23),
(16, 16, 69.23),
(17, 17, 69.23),
(18, 18, 69.23),
(19, 19, 69.23),
(20, 20, 69.23),
(21, 21, 69.23),
(22, 22, 69.23),
(23, 23, 69.23),
(24, 24, 61.54),
(25, 25, 61.54),
(26, 26, 61.54),
(27, 27, 69.23),
(28, 28, 76.92),
(29, 29, 69.23),
(30, 30, 61.54),
(31, 31, 69.23),
(32, 32, 76.92),
(33, 33, 76.92),
(34, 34, 69.23),
(35, 35, 69.23),
(36, 36, 61.54),
(37, 37, 69.23),
(38, 38, 69.23),
(39, 39, 69.23),
(40, 40, 69.23),
(41, 41, 69.23),
(42, 42, 69.23),
(43, 43, 69.23),
(44, 44, 69.23),
(45, 45, 69.23),
(46, 46, 69.23),
(47, 47, 69.23),
(48, 48, 69.23),
(49, 49, 69.23),
(50, 50, 69.23);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `akurasi_subject`
--
ALTER TABLE `akurasi_subject`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hasil`
--
ALTER TABLE `hasil`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `takurasi`
--
ALTER TABLE `takurasi`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `akurasi_subject`
--
ALTER TABLE `akurasi_subject`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `hasil`
--
ALTER TABLE `hasil`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- AUTO_INCREMENT for table `takurasi`
--
ALTER TABLE `takurasi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
