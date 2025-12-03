from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

# Each post:
# {
#   "id": int,
#   "user": str,
#   "content": str,
#   "time": str,
#   "replies": [
#       {
#           "user": str,
#           "content": str,
#           "time": str,
#           "reply_to": Optional[str]
#       }
#   ]
# }
posts = []
post_id_counter = 1

@app.route("/", methods=["GET", "POST"])
def index():
    global post_id_counter

    if request.method == "POST":
        user = request.form.get("user")
        content = request.form.get("content")

        if user and content:
            posts.append({
                "id": post_id_counter,
                "user": user,
                "content": content,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "replies": []
            })
            post_id_counter += 1

        return redirect("/")

    return render_template("index.html", posts=reversed(posts))


@app.route("/reply/<int:post_id>", methods=["POST"])
def reply(post_id):
    user = request.form.get("reply_user")
    content = request.form.get("reply_content")
    reply_to = request.form.get("reply_to")  # who you're replying to

    if not (user and content):
        return redirect("/")

    for post in posts:
        if post["id"] == post_id:
            post["replies"].append({
                "user": user,
                "content": content,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "reply_to": reply_to or None,
            })
            break

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
