import mysql.connector

SHOW_TABLES = "SHOW TABLES"
SHOW_DATABASE = "SHOW DATABASE"
ALTER_TABLE = "alter table keywords_analysis ADD UNIQUE INDEX(fk_raw_article_id, fk_keyword_id, count);"
DELETE_ENTRIES = "DELETE FROM keywords_analysis WHERE id>0"

def create_db_object():
	mydb = mysql.connector.connect(
		host = "192.168.205.5",
		user = "admin",
		password = "c00Lm@rJ3to",
		database = "global_threat_thermometer"
	)
	return mydb


def upload_to_server(finalized_list, db_object):
	insert_cursor = db_object.cursor()
	for element in finalized_list:
		if element[2] != 0:
			insert_cursor.execute("INSERT IGNORE INTO keywords_analysis (fk_raw_article_id, fk_keyword_id, "
								  "count, weighted_count) VALUES (%s, %s, %s, %s)", element)
	db_object.commit()


def reset_table(db_obj):
	cursor = db_obj.cursor()
	cursor.execute(DELETE_ENTRIES)
	db_obj.commit()
	auto_reset = db_obj.cursor()
	auto_reset.execute("ALTER TABLE keywords_analysis AUTO_INCREMENT = 1")
	db_obj.commit()


def create_keyword_list(db_object):
	keyword_cursor = db_object.cursor()
	keyword_list = []
	keyword_cursor.execute("SELECT * FROM keywords")
	for entry in keyword_cursor:
		temp_lst = []
		for item in entry:
			temp_lst.append(item)
		keyword_list.append(temp_lst)
	return keyword_list


def analyze_data(db_object, keyword_list):
	raw_cursor = db_object.cursor()
	raw_cursor.execute("SELECT * FROM raw_articles")
	final_list = []
	for entry in raw_cursor:
		for keyword in keyword_list:
			count = 0
			key_id = keyword[0]
			word = keyword[1]
			weight = keyword[3]
			article_id = entry[0]
			word_list = entry[4].split()
			for piece in word_list:
				if piece.lower() == word.lower():
					count += 1
				else:
					continue
			final_list.append(analyzed_list(article_id,key_id,count, calculate_weighted_keyword(weight,count)))
	return final_list


def analyzed_list(article_id, keyword_id, count, weighted_count):
	return (article_id, keyword_id, count, weighted_count)


def get_database(db_object):
	cursor = db_object.cursor()
	cursor.execute("SELECT * FROM keywords_analysis")
	for element in cursor:
		print(element)


def get_keywords(db_obj):
	cursor = db_obj.cursor()
	cursor.execute("SELECT * FROM keywords")
	for element in cursor:
		print(element)


def get_recent_article_id(db_obj):
	cursor = db_obj.cursor()
	cursor.execute("SELECT * FROM keywords_analysis")
	recent = 0
	for element in cursor:
		recent = element[1]
	return recent


def get_num_documents(db_obj):
	cursor = db_obj.cursor()
	cursor.execute("SELECT * FROM raw_articles")
	last_id = 0
	for element in cursor:
		last_id = element[0]
	return last_id


def calculate_weighted_keyword(weight, count):
	return weight * count


def main():
	db_obj = create_db_object()
	#reset_table(db_obj)
	keyword_list = create_keyword_list(db_obj)
	analyze_list = analyze_data(db_obj, keyword_list)
	upload_to_server(analyze_list, db_obj)
	get_database(db_obj)
main()