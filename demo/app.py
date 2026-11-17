from flask import Flask, jsonify, render_template, request, redirect, session
from flask_session import Session
from sql import SQL

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

db = SQL("sqlite:///todo.db")

@app.route("/tasks")
def tasks():
    tasks_db = db.execute("SELECT * FROM todo_list")
    
    # return render_template('tasks.html', tasks=tasks_db) # Version HTML
    
    return jsonify(tasks_db) # Version JSON

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/task/create", methods=["POST"])
def create_task():
    task_name_var = request.form.get("task_name"),
    status_var = 'done' if request.form.get("status_check") else 'todo'
    db.execute("INSERT INTO todo_list (task_name, status) VALUES(?, ?)", task_name_var, status_var)
    return redirect('/')

# @app.route('/toggle/<int:id>')
# def toggle_task(id):
#     tasks = db.execute('SELECT * FROM todo_list WHERE id = ?', id)
#     if not tasks:
#         return 'Task not found', 404
    
#     if tasks[0]['status'] == 'todo':
#         db.execute("UPDATE todo_list SET status = 'done' WHERE id = ?", id)
#     else:
#         db.execute("UPDATE todo_list SET status = 'todo' WHERE id = ?", id)
    
#     return redirect('/')

@app.route('/toggle/<int:id>', methods=["POST"])
def toggle_task(id):
    tasks = db.execute('SELECT * FROM todo_list WHERE id = ?', id)
    if not tasks:
        return 'Task not found', 404
    
    if tasks[0]['status'] == 'todo':
        db.execute("UPDATE todo_list SET status = 'done' WHERE id = ?", id)
    else:
        db.execute("UPDATE todo_list SET status = 'todo' WHERE id = ?", id)
    
    return '', 204 # No content

if __name__ == '__main__':
    app.run(port=5000)