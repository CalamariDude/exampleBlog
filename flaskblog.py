from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '8789a834b01df30ca6727d09962bd54f'
posts = [
    {
        'author': 'Jad Boi',
        'title': 'My first Post',
        'content': 'Hello guys this is my first blog post whats going on.'
    }
        ]
    
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Posts')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Acount created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
