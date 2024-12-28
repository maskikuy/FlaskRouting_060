from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return f'Welcome, {name}!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm', '').strip()
        if not user:
            return "Error: Name cannot be empty", 400
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm', '').strip()
        if not user:
            return "Error: Name cannot be empty", 400
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(debug=True)