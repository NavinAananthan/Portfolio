from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/work.html')
def work():
    return render_template('work.html')

@app.route('/work2.html')
def work2():
    return render_template('work2.html')

@app.route('/work3.html')
def work3():
    return render_template('work3.html')

@app.route('/work4.html')
def work4():
    return render_template('work4.html')



if __name__ == "__main__":
    app.run(debug=True)