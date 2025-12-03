# Microblog — Flask (Simple + Reply Targeting)

This is a tiny Flask microblog application featuring:

- Create posts with username + timestamp  
- Reply to posts OR reply to a specific user  
- Replies show “↪ @username”  
- Clean HTML + CSS  
- No database required (in‑memory storage)  
- Super simple to run and extend  

---

## 🚀 Install & Run

### 1. Install dependencies

You only need Flask:

```bash
pip install flask
```

(Optional but recommended: create a venv)

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate    # Windows
```

### 2. Start the server

Inside the project folder:

```bash
python app.py
```

### 3. Open in browser

Visit:

```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
microblog/
│── app.py
│── README.md
│── templates/
│     └── index.html
│── static/
      └── style.css
```

---

## 🧠 How It Works

### Posts look like this:

```python
{
  "id": 1,
  "user": "Alice",
  "content": "Hello world!",
  "time": "2025‑12‑03 12:45:23",
  "replies": []
}
```

### Replies look like:

```python
{
  "user": "Bob",
  "content": "Nice message!",
  "time": "2025‑12‑03 12:48:10",
  "reply_to": "Alice"
}
```

### Reply targeting

Clicking “Reply to <name>” automatically:

- Fills a hidden input `reply_to="<name>"`
- Shows “Replying to: <name>”
- Displays `↪ @<name>` in the UI

---

## ⚠️ Important Notes

- Data is **not saved permanently** (in-memory only).
- Restarting the server clears all posts & replies.
- Perfect for learning or rapid prototyping.

If you want persistence, you can upgrade to SQLite or PostgreSQL—I can generate that version for you.

---