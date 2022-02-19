from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
all_post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    all_post_objects.append(post_obj)

@app.route('/')
def home():

    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def render_post(index):
    requested_post = None
    for blog_post in all_post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", blog_post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
