import sqlite3 

def get_all_aeticles():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()
    conn.close()

    return articles