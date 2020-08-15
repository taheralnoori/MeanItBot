import sqlite3

class DataBase:
	def __init__(self):
		self.conn = sqlite3.connect("usersDB.db", check_same_thread = True)
		self.cursor = self.conn.cursor()
	def __del__(self):
		self.conn.commit()
		self.conn.close()
	def insertUser(self, user_id, cur_language):
		sql = "INSERT INTO users (user_id, cur_language) VALUES (?, ?)"
		self.cursor.execute(sql, (user_id, cur_language))
	def updateLanguage(self, user_id, cur_language):
		sql = "UPDATE users SET cur_language=? WHERE user_id=?"
		self.cursor.execute(sql, (cur_language, user_id))
	def findUser(self, user_id):
		sql = "SELECT * FROM users WHERE user_id=" + user_id
		user = self.cursor.execute(sql)
		return user.fetchone()
