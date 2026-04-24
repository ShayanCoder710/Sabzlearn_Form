from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enter')
def enter():
    return render_template('enter.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/singup')
def singup():
    return render_template('singup.html')

@app.route('/submit1', methods=['post'])
def submit1():
    username = request.form.get('username')
    numphone = request.form.get('numphone')
    email = request.form.get('email')
    password = request.form.get('password')

    data = open("data_singup.txt", "a")
    data.write(f"user\nuser name: {username}\number phone: {numphone}\nemail: {email}\npassword: {password}\n\n\n")
    data.close()

    return redirect(url_for('enter'))


@app.route('/submit2', methods=['post'])
def submit2():
    numphone = request.form.get('numphone')

    data = open("data_login.txt", "a")
    data.write(f"number phone: {numphone}\n\n")
    data.close()

    return redirect(url_for('enter'))


app.run(debug=True)
