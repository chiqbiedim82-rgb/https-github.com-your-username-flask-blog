from flask import Flask, render_template, request, redirect, url_for, flash
from data import posts, get_next_id
from datetime import datetime

app = Flask(__name__)
app.secret_key = "change-this-in-production"

@app.route('/')
def dashboard():
    total_posts = len(posts)
    latest_post = posts[0] if posts else None
    return render_template('dashboard.html', total_posts=total_posts, latest_post=latest_post)

@app.route('/feed')
def feed():
    return render_template('feed.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author', 'Anonymous')

        if not title or not content:
            flash('Title and content are required!', 'danger')
            return redirect(url_for('create'))

        new_post = {
            "id": get_next_id(),
            "title": title,
            "content": content,
            "author": author,
            "date": datetime.now().strftime("%B %d, %Y")
        }
        posts.insert(0, new_post)  # Newest first
        flash('Blog post published successfully!', 'success')
        return redirect(url_for('feed'))

    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)

  git remote add origin https://github.com/chiqbiedim82-rgb/https-github.com-your-username-flask-blog.git
git branch -M main
git push -u origin main


import os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = "supersecretkey"  # change this to something secure

# Load environment variables from .env
load_dotenv()
PASSWORD_HASH = os.getenv("PASSWORD_HASH")

@app.route("/")
def home():
    # If logged in, go to dashboard, else show login page
    if "logged_in" in session and session["logged_in"]:
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    password = request.form.get("password")
    if check_password_hash(PASSWORD_HASH, password):
        session["logged_in"] = True
        return redirect(url_for("dashboard"))
    else:
        return "Invalid password, try again."

@app.route("/dashboard")
def dashboard():
    if "logged_in" in session and session["logged_in"]:
        return render_template("dashboard.html")
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)


