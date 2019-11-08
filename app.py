from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, template_folder="view")
from controller import register as Register
from controller import auth as Auth

@app.route('/')
def main():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        auth = Auth.Auth()
        if not auth.user_exists(request.form['email'],request.form['password']):
            error = 'Invalid username or password'
        else:
            return redirect(url_for('home'))
    return render_template('auth/login.html', error=error)

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        auth = Auth.Auth()
        if auth.user_exists(request.form['email'], request.form['password']):
            error = 'Choose different username'
        else:
            #capture and send credentials to DB
            register = Register.Register()
            register.create_account(username=request.form['email'], password=request.form['password'])
            return redirect(url_for('home'))
    return render_template("/auth/register.html",error=error)
@app.route('/forgot_password')
def forgot_password():
    return render_template("/auth/forgot_password.html")
if __name__ == '__main__':
    app.run()
