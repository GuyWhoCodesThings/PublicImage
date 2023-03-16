
from flask import Flask, jsonify, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile', methods=['GET','POST'])
def profile():
    if request.method == "POST":
        attribute = request.form['newAttribute']
        if attribute:
            return jsonify({'output':'entered token is: ' + attribute})
        return jsonify({'error' : 'Missing data!'})
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)