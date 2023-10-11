-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 11, 2023 at 06:30 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `portfolio`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) UNSIGNED NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `mes` text NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `mes`, `date`, `email`) VALUES
(1, 'Adarsh Tiwari', '7012219336', 'Nothing', '2023-10-02 04:54:22', 'tiwariadarsh125@gmail.com'),
(2, 'Adarsh Tiwari', '7012219336', 'Nothing', '2023-10-02 04:55:40', 'tiwariadarsh125@gmail.com'),
(3, 'Adarsh Tiwari', '7012219336', 'Nothing much this is new message', '2023-10-02 04:58:56', 'tiwariadarsh125@gmail.com'),
(4, 'zoops', '7012219336', 'hoops', '2023-10-03 16:02:07', 'tiwariadarsh125@gmail.com'),
(5, 'Adarsh Tiwari', '6282404947', 'Hi there Nice connecting with you hope to work together in future', '2023-10-07 18:39:28', 'adarshtiwari25122001@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(50) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`sno`, `title`, `content`, `img_file`, `date`) VALUES
(1, 'Tic Tac Toe Project Using Python', 'This is a very cool project Where I used Minimax algorithm where the only possible outcomes of the game are DRAW or WIN of the computer. It uses recursion and the fact that both players will be playing optimally. \r\nSo Basically computer makes all possible moves moves in our case 8! as one move is already made by User So computationally not very expensive for the computer else we would have to opt for alpha beta pruning.', 'miniMax.gif', '2023-10-07 18:58:55'),
(2, 'Sudoku Solver using Backtracking', 'Here using javascript and html/css we make a sudoku solver also  enabled for humans to solve.', 'Sudoku_Solver.gif', '2023-10-03 20:24:03'),
(3, 'Banking System Using Python', 'Here we employ the oops concepts of python to play and design a Banking system', 'Bank.gif', '2023-10-03 20:25:11');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
