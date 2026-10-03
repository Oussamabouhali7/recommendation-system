-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 28 mai 2021 à 19:46
-- Version du serveur :  10.4.19-MariaDB
-- Version de PHP : 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `cbrs`
--

-- --------------------------------------------------------

--
-- Structure de la table `produit`
--

CREATE TABLE `produit` (
  `IdPdt` text NOT NULL,
  `NomPdt` text CHARACTER SET latin1 DEFAULT NULL,
  `Couleur` text CHARACTER SET latin1 DEFAULT NULL,
  `Description` text CHARACTER SET latin1 DEFAULT NULL,
  `Top1` text CHARACTER SET latin1 DEFAULT NULL,
  `Top2` text CHARACTER SET latin1 DEFAULT NULL,
  `Top3` text CHARACTER SET latin1 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `produit`
--

INSERT INTO `produit` (`IdPdt`, `NomPdt`, `Couleur`, `Description`, `Top1`, `Top2`, `Top3`) VALUES
('1', 'Pc Portable LENOVO S145-15API AMD 3020e, Ecran 15.6\" HD-Gray', 'Gris', 'Processeur AMD 3020E Dual-core(1.20 GHz Up To 2.60 GHz, 5 MB cache) Mémoire RAM 4 Go DDR4, Disque Dur 1To, Carte graphique AMD Radeon™ Graphics, USB 3.0, HDMI, Wifi, Bluetooth, et Lecteur de Carte Mémoire 4 En 1, Ecran 15.6\" LED HD.', '5', '4', '9'),
('2', 'GF63 10SCSR-1202XFR', 'Noir', 'Processeur Intel Core i5-10300H Quad-Core( 2.5 GHz up to 4.5 GHz Turbo, 8 Mo de mémoire cache), Mémoire RAM 16 Go DDR4, Disque Dur 512 Go SSD M.2 PCIe NVMe, Carte Graphique NVIDIA GeForce GTX1650TI 4 Go GDDR6 , Wifi, Bluetooth, HDMI, Ecran 15.6\" 144Hz FULL HD', '7', '4', '12'),
('3', 'Pc portable Gamer Asus TUF506IU-HN457T R5-4600H, écran 15.6\" IPS 144Hz', 'Noir', 'Processeur AMD® R5-4600H Hexa-Core(3.00 GHz up to 4.00 GHz, 11 MB Cache), Mémoire RAM 8 Go DDR4, Disque dur  512GO  M.2 NVMe™ PCIe® 3.0 SSD, Carte graphique NVIDIA® GeForce®  GTX 1660TI avec 6 Go GDDR6 de mémoire dédiée, Clavier RGB , Ecran 15.6\" FULL-HD IPS 144Hz.', '16', '11', '12'),
('4', 'Pc Portable Lenovo IP3, i3 10é Gén, MX330 2G, Ecran 15\" HD Black', 'Noir', 'Processeur Intel® Core™ i3 -1005G1 Dual-Core(1.2 GHz up to 3.4GHz, 4 MB Intel® Smart Cache), Mémoire RAM 8 Go DDR4, Disque Dur 512 SSD, Carte Graphique Nvidia Geforce MX330 2G, Wifi, Bluetooth, HDMI, Ecran 15\" LED HD.', '5', '2', '1'),
('5', 'Pc potable HP250 G8 i3-10é , écran15,6 HD Top Load', 'Noir', 'Processeur Intel® i3-1005G1 Dual-Core(1.20 GHz, Up To 3.40 GHz, 4 MB Intel® Smart Cache), Mémoire RAM 4 Go DDR4, Disque dur HDD 1TO, Carte graphique Intel® UHD, Ecran 15.6\" HD.', '8', '1', '6'),
('6', 'Pc Portables Dell INSPIRON 5491 I3', 'Gris', 'Processeur Intel Core i3-10110U Duel-core (2.10 GHz up to 4.10 GHz, 4 MB Intel® Smart Cache), Mémoire RAM: 4Go DDR4, Disque dur SSD 256 Go, Ecran 14\" Full HD tactile, Carte graphique Intel® UHD Graphics.', '14', '5', '8'),
('7', 'Pc portable HP Envy 13-ba0000nk i5 10è Gé ,écran 13\" Full HD', 'Silver', 'Processeur Intel I5-1035G1 Quad-Core (1.0 GHz Up To 3.60 GHz, 6 Mo de mémoire cache), Mémoire RAM 8 Go DDR 4, Disque SSD 256gb ,  Carte  Intel UHD, Wifi, Bluetooth, HDMI, Ecran 13.3\" IPS Full HD.', '2', '8', '14'),
('8', 'Pc potable HP250 G8 i5-10é , écran15,6 HD', 'Noir', 'Processeur Intel® i5-1035G1 Quad-Core(1.00 GHz, Up To 3.60 GHz, 6 MB Intel® Smart Cache), RAM 4 Go DDR4, Disque dur HDD 1TO, Carte graphique Intel® UHD, Ecran 15.6\" HD.', '5', '14', '6'),
('9', 'Pc portable Asus Vivo Book S14 R5-4500U, écran 14\"', 'Noir', 'Processeur AMD Ryzen™ 5 4500U Hexa-Core(de 2.30 GHz à 4.00 GHz, 11Mo de mémoire cache), RAM 16 Go DDR4, Disque Dur 512GO SSD,  Carte Graphique AMD Radeon™ Graphics, Wifi, Bluetooth, HDMI, Ecran 14\" Full-HD.', '1', '11', '2'),
('10', 'Pc de bureau DELL Optiplex 3080 i5-10é', 'Bleu', 'Processeur Intel Core i5-10500 Hexa-Core (3.10 GHz up to 4.50GHz, 12 MB Intel® Smart Cache) RAM 4 Go, Disque HDD 1 To, Carte graphique Intel® UHD Graphics 630  équipé d un Graveur DVD plus Clavier et Souris USB.', '6', '5', '14'),
('11', 'Pc de bureau DELL Optiplex 3080 i5-10é', 'Bleu', 'Processeur AMD Ryzen R5-4600H Hexa-Core(3.00GHz up to 4.00 GHz, 11 MB Cache), Mémoire RAM 8 Go DDR4, Disque dur HDD 1TO + 256 Go SSD, Carte graphique NVIDIA® GeForce®  GTX 1650TI 4 Go, Clavier Rétroéclairé , Ecran 15.6\" Full-HD IPS.', '3', '5', '8'),
('12', 'Pc de bureau DELL Optiplex 3080 i5-10é', 'ECLIPSE GRAY', 'Processeur intel® i7-11370H Quad-core(3.00 GHz up to 4.80 GHz, 12 MB Intel® Smart Cache), RAM 16 Go DDR4, Disque Dur 512G PCIE G3 SSD, Carte Graphique NVIDIA® GeForce RTX™ 3060 6G GDDR6, WiFi 6, Bluetooth, Clavier RGB ILLUMINATED CHICLET, Ecran 15.6\" Full HD IPS 144Hz.', '16', '2', '8'),
('13', 'Pc de bureau DELL Optiplex 3080 i5-10é', 'ECLIPSE GRAY', 'Intel Core i7-8565U 1.8 GHz / 4.6 GHz Turbo - 8 Mo cache 16 Go DDR4 Disque dur 256 Go SSD LED FULL HD 15.6 pouces Intel UHD Graphics 620', '2', '6', '14'),
('14', 'Pc de bureau DELL Optiplex 3080 i5-10é', 'ECLIPSE GRAY', 'Processeur Intel® I5-1035G4 Quad-Core (1.10 GHz up to 3.70 GHz, 6 MB Intel® Smart Cache), Mémoire RAM 8 Go DDR4, Disque dur 256 Go SSD, Carte graphique Intel® Iris® Plus, Ecran 14\" FULL HD.', '6', '8', '5'),
('15', 'Pc de bureau DELL Optiplex 3080 i5-10é', 'Gris', 'Processeur Intel Core i3-10110U Duel-core (2.10 GHz up to 4.10 GHz, 4 MB Intel® Smart Cache), Mémoire RAM: 4Go DDR4, Disque dur SSD 256 Go, Ecran 14\" Full HD tactile, Carte graphique Intel® UHD Graphics.', '14', '5', '8'),
('16', 'Pc de bureau DELL Optiplex 3080 i5-10é', 'Gris', 'Processeur Intel® I7-10870H Octa-Core (2.20 GHz up to 5.00 GHz, 16 MB Intel® Smart Cache), Mémoire RAM 24 Go DDR4, Disque dur  512GO  M.2 NVMe™ PCIe® 3.0 SSD, Carte graphique NVIDIA® GeForce®  GTX 1660TI avec 6 Go GDDR6 de mémoire dédiée, Clavier RGB , Ecran 15.6\" FULL HD IPS 144hz.', '3', '12', '14');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
