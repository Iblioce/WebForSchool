CREATE TABLE todo_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT CHECK(status IN ('todo', 'done')) NOT NULL,
    task_name TEXT NOT NULL
);
