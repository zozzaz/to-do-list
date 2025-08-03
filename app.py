from flask import Flask, render_template, request

app = Flask(__name__)
todos = []

@app.route("/")
def home():
    return render_template("index.html", tasks = todos)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        todos.append(task)
    return render_template("index.html", tasks=todos)

@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
    return render_template("index.html", tasks=todos)

if __name__ == "__main__":
    app.run(debug=True)