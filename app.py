from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import subprocess
import base64
import os
import datetime
import cv2


app = Flask(__name__)
video_writer=None
app.secret_key = 'ma_clé_secrète'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login'

mysql = MySQL(app)
app.secret_key = 'ma_clé_secrète'


@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        password = request.form['password']
        photo = request.files['photo']
        
        # Crypter le mot de passe
        hashed_password = generate_password_hash(password)

        # Encoder la photo en base64
        photo_bytes = photo.read()
        photo_base64 = base64.b64encode(photo_bytes).decode('utf-8')

        # Vérifier si l'adresse e-mail existe déjà dans la base de données
        cur = mysql.connection.cursor()
        cur.execute("SELECT COUNT(*) FROM utilisateurs WHERE email = %s", (email,))
        result = cur.fetchone()

        if result[0] != 0:
            # Adresse e-mail déjà utilisée, afficher un message d'erreur
            return 'Adresse e-mail déjà utilisée.'

        # Insérer les données dans la base de données
        cur.execute("INSERT INTO utilisateurs (Nom, Prénom, email, password, photo) VALUES (%s, %s, %s, %s, %s)", (nom, prenom, email,
                                                                                                                    hashed_password, photo_base64))
        mysql.connection.commit()

        # Rediriger l'utilisateur vers la page de connexion
        return redirect(url_for('page_connexion'))

    # Si la méthode est GET, afficher la page d'inscription
    return render_template('inscription.html')



# Page de connexion
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, Nom, Prénom, email, password, photo FROM utilisateurs WHERE email=%s", (email,))
    user = cur.fetchone()

    if user is None:
        return "Email non valide"
    elif not check_password_hash(user[4], password):
        return "Mot de passe incorrecte"
    
    elif user[3] == 'admin@cobotique.com':
        return render_template('inscription.html')
    else:
         # Extraire les données binaires de l'image à partir de la base de données
        photo_data = user[5]
        # Convertir les données binaires en une chaîne Base64
        photo_base64 = base64.b64encode(photo_data).decode('utf-8')
        
        # Stocker les informations de l'utilisateur dans la session Flask
        session['user_id'] = user[0]
        session['user_Nom'] = user[1]
        session['user_Prénom'] = user[2]
        session['user_email'] = user[3]
        
        # Afficher l'image dans le template HTML
        return render_template('index.html',  photo_base64=photo_base64)





@app.route('/')
def home():
    return render_template('connexionhome.html')

@app.route('/page_connexion')
def page_connexion():
    return render_template('connexion.html')
@app.route('/page_compte', methods=['GET', 'POST'])
def page_compte():
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, Nom, Prénom, email, photo FROM utilisateurs WHERE email=%s", (session['user_email'],))
    utilisateur = cur.fetchone()

    return render_template('compte.html', utilisateur=utilisateur)


# Route pour aller au menu
@app.route('/page_index')
def page_index():
    return render_template('index.html')

# Route pour les deux autres page
@app.route('/page_direct')
def page_direct():
    return render_template('direct.html')

@app.route('/page_pre')
def page_preenregistrer():
    return render_template('pre.html')

# Route pour lancer le programme
@app.route('/start_preenregistrer', methods=['POST'])
def start_program():
    subprocess.Popen(['python', 'Connectionrobot.py'])
    subprocess.Popen(['python', 'xyz.py'])
    return render_template('pre.html')
@app.route('/pose1', methods=['POST'])
def pose1():
    subprocess.Popen(['python', 'pose1.py'])
    return render_template('pre.html')

@app.route('/pose2', methods=['POST'])
def pose2():
    subprocess.Popen(['python', 'pose2.py'])
    return render_template('pre.html')

@app.route('/pose3', methods=['POST'])
def pose3():
    subprocess.Popen(['python', 'pose3.py'])
    return render_template('pre.html')

@app.route('/start_direct', methods=['POST'])
def start_direct():
    subprocess.Popen(['python', 'xyz.py'])
    subprocess.Popen(['python', 'Connectionrobot.py'])
    return render_template('direct.html')

# Route pour arrêter le programme
@app.route('/stop_direct', methods=['POST'])
def stop_direct():
    subprocess.kill()
    return render_template('direct.html')
    
if __name__ == '__main__':
    app.run(debug=True)