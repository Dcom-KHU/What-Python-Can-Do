from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    dict_var = {
        'message': 'Hello! D.Com!',
        'context': 'D.Com에 온걸 환영해요 ><'
    }
    return render_template('index.html', **dict_var)

if __name__ == '__main__':
    app.run(debug=True)
