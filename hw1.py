from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import NewUserForm, UpdateUserForm

app = Flask(__name__)

# Secret key is REQUIRED to use flask forms
# Code pulled from flask tutorial (see readMe), key is custom
app.config['SECRET_KEY'] = '83d685d340c51b8eb295b579a96ab2ac'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    firstName = db.Column(db.String(15), nullable=False)
    lastName = db.Column(db.String(15), nullable=False)
    idNum = db.Column(db.Integer, primary_key = True)
    points = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{ self.firstName }', '{ self.lastName}', '{self.idNum}')"

@app.route('/')
@app.route('/home')
def home():
    users = User.query.all()
    return render_template('home.html', users=users)

# to accept a post request, need to add a list of allowed methods in a route
@app.route('/newUser', methods=['GET', 'POST'])
def newUser():
    form = NewUserForm()
    if form.validate_on_submit():
        user = User(firstName=form.firstName.data,
         lastName=form.lastName.data, idNum=form.idNum.data, points=form.points.data)
        db.session.add(user)
        db.session.commit()
        flash(f'New User Created for {form.firstName.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('newUser.html', title='New User', form=form)

# reopens the new user form, without the option to update ID
# uses user ID to find user
@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    currUser = User.query.get(id)
    form = UpdateUserForm()
    if form.validate_on_submit():
        currUser.firstName=form.firstName.data
        currUser.lastName=form.lastName.data
        currUser.points=form.points.data
        db.session.commit()

        flash(f'User {form.firstName.data} successfully updated!', 'success')
        return redirect(url_for('home'))
    return render_template('update.html', title='Update User', form=form, user=currUser)

@app.route('/delete/<id>')
def delete(id):
    currUser = User.query.get(id)
    db.session.delete(currUser)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()

