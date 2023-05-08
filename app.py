from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    # Connect to the database
    conn = sqlite3.connect('D:/PycharmProjects/final_project_dbm110/data.db')
    c = conn.cursor()

    # Retrieve the questions from the database
    c.execute('SELECT question, option_1, option_2, option_3, option_4, answer FROM quotes')
    questions = c.fetchall()

    # Close the database connection
    conn.close()

    return render_template('index.html', questions=questions)


if __name__ == '__main__':
    app.run(debug=True)
