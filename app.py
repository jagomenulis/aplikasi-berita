from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('SECRET_KEY', 'devkey')

db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

def create_tables():
    db.create_all()

@app.route('/')
def index():
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def detail(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('detail.html', article=article)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        body = request.form.get('body', '').strip()
        if not title or not body:
            flash('Title and body are required.', 'danger')
            return redirect(url_for('create'))
        a = Article(title=title, body=body)
        db.session.add(a)
        db.session.commit()
        flash('Article created.', 'success')
        return redirect(url_for('index'))
    return render_template('form.html', action='create')

@app.route('/edit/<int:article_id>', methods=['GET', 'POST'])
def edit(article_id):
    article = Article.query.get_or_404(article_id)
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        body = request.form.get('body', '').strip()
        if not title or not body:
            flash('Title and body are required.', 'danger')
            return redirect(url_for('edit', article_id=article_id))
        article.title = title
        article.body = body
        db.session.commit()
        flash('Article updated.', 'success')
        return redirect(url_for('detail', article_id=article.id))
    return render_template('form.html', action='edit', article=article)

@app.route('/delete/<int:article_id>', methods=['POST'])
def delete(article_id):
    article = Article.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    flash('Article deleted.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        create_tables()
    app.run(debug=True)
