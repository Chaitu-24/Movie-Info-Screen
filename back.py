import sqlite3
#backend
def studentData():
    con=sqlite3.connect("movies.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS movie(id INTEGER PRIMARY KEY,MOVIE_ID text, MOVIE_NAME text, RELEASE_DATE text, DIRECTOR text,CAST text, BUDGET text,DURATION text,RATING text)")
    con.commit()
    con.close()

def addStdRec(MOVIE_ID, MOVIE_NAME, RELEASE_DATE , DIRECTOR ,CAST, BUDGET, DURATION, RATING):
    con = sqlite3.connect("MOVIES.db")
    cur = con.cursor()
    cur.execute("INSERT INTO movie VALUES (NULL,?,?,?,?,?,?,?,?) ", (MOVIE_ID, MOVIE_NAME,RELEASE_DATE,DIRECTOR,CAST, BUDGET,DURATION,RATING))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("movies.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM movie")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("movies.db")
    cur = con.cursor()
    cur.execute("DELETE FROM movie WHERE MOVIE_ID=?",(id,))
    con.commit()
    con.close()

def searchData(MOVIE_ID="", MOVIE_NAME="", RELEASE_DATE="" , DIRECTOR="",CAST="", BUDGET="", DURATION="", RATING=""):
    con = sqlite3.connect("movies.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM movie WHERE MOVIE_NAME=?",(MOVIE_NAME,))
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,StdID="",MOVIE_ID="", MOVIE_NAME="", RELEASE_DATE="",DIRECTOR="", CAST="", BUDGET="", DURATION="", RATING=""):
    con = sqlite3.connect("movies.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET MOVIE_ID=?, MOVIE_NAME=?,RELEASE_DATE=?, DIRECTOR=?,CAST=?,BUDGET=?,DURATION=?,RATING=?,WHERE id=?", (MOVIE_ID, MOVIE_NAME,RELEASE_DATE,DIRECTOR,CAST, BUDGET,DURATION,RATING,id))
    con.commit()
    con.close()

studentData()
