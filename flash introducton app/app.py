from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Length

app = Flask(__name__)


app.secret_key = "dsjkfgjsdgifbj"

posts = [
    {
        'id': 1,
        'title': 'MUKONGE',
        'content': 'AM_NATURE'
    },
    {
        'id': 2,
        'title': 'ERIC',
        'content': 'AM_RULER'
    },
    {
        'id': 3,
        'title': 'SENJAH',
        'content': 'AM_FOLLOWING'
    },
    {
        'id': 4,
        'title': 'E-CODE',
        'content': 'AM_MACHINE LANGUAGE'
    },
]


class SignUpForm(FlaskForm):
    username = StringField(label="Username", validators=[InputRequired(message="Username should not be blank"),
                                                         Length(min=5, max=25)
                                                         ])

    email = StringField(label="Email", validators=[InputRequired(message="Email should not be blank"),
                                                   Length(
                                                       max=45, message="Email should have less than 45 characters")
                                                   ])

    password = PasswordField(label="Password", validators=[InputRequired(message="Password should not be left blank"),
                                                           Length(
                                                               min=5, max=12, message="Password should be between 5 and 12 caharacters")
                                                           ])

    confirm = PasswordField(label="Confirm Password", validators=[InputRequired(message="Password should not be left blank"),
                                                                  Length(min=5, max=12, message="Password should be between 5 and 12 caharacters"), EqualTo(
                                                                      'password', message="Password do not match")
                                                                  ])

    submit = SubmitField(label="Sign Up")


class LoginForm(FlaskForm):

    email = StringField(label="Email", validators=[InputRequired(message="Email should not be blank"),
                                                   Length(
                                                       max=45, message="Email should have less than 45 characters")
                                                   ])

    password = PasswordField(label="Password", validators=[InputRequired(message="Password should not be left blank"),
                                                           Length(
                                                           min=5, max=12, message="Password should be between 5 and 12 caharacters")
                                                           ])
    submit = SubmitField(label="Login")


@app.route('/')
def index():

    title = "Home page"
    context = {
        'title': title,
        'posts': posts
    }
    return render_template('index.html', **context)


@app.route('/about')
def about():

    title = "About page"
    context = {
        'title': title
    }
    return render_template('about.html', **context)


@app.route('/login')
def login_page():
    title = "Login page"
    form = LoginForm()
    context = {
        'title': title,
        'form': form
    }
    return render_template('login.html', **context)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if request.method == "POST":

        if form.validate_on_submit():
            return "Validation worked"

    context = {
        'form': form
    }
    return render_template('signup.html', **context)


@app.route('/contacts')
def contacts():

    title = "Contact page"

    context = {

        'title': title,

    }
    return render_template('contacts.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
