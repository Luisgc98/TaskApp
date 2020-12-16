from app import create_app
from flask import render_template, make_response, redirect, url_for

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
    
    response = make_response(redirect(url_for('auth.login')))
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)