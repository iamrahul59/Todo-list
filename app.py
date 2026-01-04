from flask import Flask, request

app = Flask(__name__)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
    return '<h2>To-Do List</h2>' + '<br>'.join(tasks) + '<br><form method="post"><input name="task"><button>Add</button></form>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
