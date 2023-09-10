from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/restaurant/chick-fil-a')
def chickfila():
    return render_template('chickfila.html')

@app.route('/restaurant/panda-express')
def pandaexpress():
    return render_template('pandaexpress.html')
@app.route('/restaurant/slutty-vegan')
def sluttyvegan():
    return render_template('sluttyvegan.html')

if __name__ == '__main__':
    app.run(debug=True)
