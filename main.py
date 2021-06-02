from flask import Flask, render_template, redirect, url_for
import data

app = Flask(__name__)
app.secret_key = 'mYAoTSUidztoGQpVrYDWK7punVjKk7Xw'


@app.route('/')
def home():
    return render_template('home.html', title='Covid Response', active_page='home')


@app.route('/data')
def view_data():
    return render_template('data.html', title='Covid Response | Data', active_page='data')


@app.route('/news')
def news():
    return redirect(url_for('home'))


@app.route('/update')
def update_data():
    data.update()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
