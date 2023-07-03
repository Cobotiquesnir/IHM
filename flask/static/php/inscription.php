<?php
// Connexion à la base de données
$servername = "192.168.196.5";
$username = "root";
$password = "";
$dbname = "login";

$conn = mysqli_connect($servername, $username, $password, $dbname);

// Vérification de la connexion
if (!$conn) {
	die("La connexion a échoué : " . mysqli_connect_error());
}

// Récupération des données du formulaire
$prenom = $_POST["prenom"];
$nom = $_POST["nom"];
$email = $_POST["email"];
$password = $_POST['password'];
$hash = password_hash($password, PASSWORD_DEFAULT);


// Insertion des données dans la base de données
$sql = "INSERT INTO utilisateurs (prenom, nom, email, password) VALUES ('$prenom', '$nom', '$email', '$hash')";
//$sql = "INSERT INTO utilisateurs (prenom, nom, email, password) VALUES ('$prenom', '$nom', '$email', '$password')";

if (mysqli_query($conn, $sql)) {
	echo "Inscription réussie !";
} else {
	echo "Erreur : " . $sql . "<br>" . mysqli_error($conn);
}

// Fermeture de la connexion à la base de données
mysqli_close($conn);
?>
