from flask import render_template, request
from flask_login import login_required, current_user
from models import Post, Comment

@app.route('/news')
def news_feed():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('news.html', posts=posts)