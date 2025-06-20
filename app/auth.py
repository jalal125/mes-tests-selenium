from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

def validate_credentials(user: str, pwd: str) -> bool:
    return user == 'tomsmith' and pwd == 'SuperSecretPassword!'

@auth_bp.route('/', methods=['GET'])
def home():
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd  = request.form['password']
        if validate_credentials(user, pwd):
            session['user'] = user
            flash('Connexion réussie !', 'success')
            return redirect(url_for('main.index'))
        flash('Identifiants invalides', 'danger')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
