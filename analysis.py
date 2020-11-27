import mysql.connector
import math

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


def create_article_list(db_obj):
	cursor = db_obj.cursor()
	cursor.execute("SELECT * FROM raw_articles")
	article_list = list()
	for entry in cursor:
		word_list = entry[4].lower().split(' ')
		article_list.append(word_list)
	return article_list


def create_word_list(table_entry):
	return table_entry[4].split(" ")


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


def create_word_dictionary(article_list):
	word_dictionary = dict()
	for article in article_list:
		comparison_list = list()
		for raw_word in article:
			word = ''.join(rw for rw in raw_word if rw.isalnum())
			if word.lower() in word_dictionary and word.lower() not in comparison_list:
				word_dictionary[word.lower()] += 1
				comparison_list.append(word.lower())
			if word.lower() not in word_dictionary:
				word_dictionary[word.lower()] = 1
	return word_dictionary


def analyze_data(db_object, keyword_list, idf_dictionary):
	raw_cursor = db_object.cursor()
	raw_cursor.execute("SELECT * FROM raw_articles")
	final_list = []
	for entry in raw_cursor:
		w_list = create_word_list(entry)
		tf_table = calculate_tf(w_list)
		for keyword in keyword_list:
			count = 0
			key_id = keyword[0]
			word = keyword[1]
			w = remove_punctuation(word)
			weight = keyword[3]
			article_id = entry[0]
			word_list = entry[4].split()
			for piece in word_list:
				if piece.lower() == word.lower():
					count += 1
				else:
					continue
			if w.lower() in tf_table and w.lower() in idf_dictionary:
				tf_idf_value = calculate_tf_idf(tf_table, idf_dictionary, w.lower())
				final_list.append(analyzed_list(article_id,key_id,count, calculate_weighted_keyword(weight, count),
											tf_table[w.lower()], tf_idf_value))

			if w.lower() not in tf_table:
				final_list.append(analyzed_list(article_id, key_id, count, calculate_weighted_keyword(weight, count),
												0, 0))
	return final_list


def analyzed_list(article_id, keyword_id, count, weighted_count, tf_value, tf_idf_value):
	return (article_id, keyword_id, count, weighted_count, tf_value, tf_idf_value)


def describe_table(db_obj):
	cursor = db_obj.cursor()
	cursor.execute("DESCRIBE raw_articles")
	for element in cursor:
		print(element)


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


def get_articles(db_obj):
	cursor = db_obj.cursor()
	cursor.execute("SELECT * FROM raw_articles")
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


def calculate_tf(raw_article_word_list):
	tf_dictionary = dict()
	word_dictionary = dict()
	article_length = len(raw_article_word_list)
	for element in raw_article_word_list:
		word = ''.join(e for e in element if e.isalnum())
		if word in word_dictionary:
			word_dictionary[word.lower()] += 1
		else:
			word_dictionary[word.lower()] = 1
	for element in raw_article_word_list:
		word = ''.join(e for e in element if e.isalnum())
		tf_dictionary[word.lower()] = word_dictionary[word.lower()]/float(article_length)
	return tf_dictionary


def calculate_idf(articles_list, word_dictionary):
	num_articles = len(articles_list)
	idf_dictionary = dict()
	for word in word_dictionary:
		count = word_dictionary[word.lower()]
		if count == 0:
			idf_value = math.log(num_articles / (1 + count) )
			idf_dictionary[word.lower()] = idf_value
		else:
			idf_value = math.log(num_articles / (count))
			idf_dictionary[word.lower()] =  idf_value
	return idf_dictionary


def calculate_tf_idf(tf_dictionary, idf_dict, keyword):
	#if keyword in tf_dictionary and keyword in idf_dict:
	return (tf_dictionary[keyword] * idf_dict[keyword])
	#if keyword not in tf_dictionary:
	#	return 0
	#if keyword not in idf_dict:
	#	return 0


def reset_table(db_obj):
	cursor = db_obj.cursor()
	cursor.execute(DELETE_ENTRIES)
	db_obj.commit()
	auto_reset = db_obj.cursor()
	auto_reset.execute("ALTER TABLE keywords_analysis AUTO_INCREMENT = 1")
	db_obj.commit()


def upload_to_server(finalized_list, db_object):
	insert_cursor = db_object.cursor()
	for element in finalized_list:
		if element[2] != 0:
			insert_cursor.execute("INSERT IGNORE INTO keywords_analysis (fk_raw_article_id, fk_keyword_id, "
								  "count, weighted_count, tf_value, tf_idf_value) VALUES (%s, %s, %s, %s, %s, %s)",
								  element)
	db_object.commit()


def remove_punctuation(word):
	return ''.join(rw for rw in word if rw.isalnum())


def run_program(db_object):
	article_list = create_article_list(db_object)
	word_dictionary = create_word_dictionary(article_list)
	keyword_list = create_keyword_list(db_object)
	idf_dictionary = calculate_idf(article_list, word_dictionary)
	update_keyword_idf(db_object, idf_dictionary)
	update_keywords_word_count(db_object, word_dictionary, keyword_list)
	finalized_lst = analyze_data(db_object, keyword_list, idf_dictionary)
	upload_to_server(finalized_lst, db_object)


def update_keyword_idf(db_object, idf_dictionary):
	keywords_list = create_keyword_list(db_object)
	for keyword in keywords_list:
		cursor = db_object.cursor()
		id = keyword[0]
		word = keyword[1]
		w = ''.join(e for e in word if e.isalnum())
		if w.lower() in idf_dictionary:
			cursor.execute("UPDATE keywords SET idf_value=" + str(idf_dictionary[w.lower()]) + " WHERE id=" + str(id))
			db_object.commit()
		else:
			cursor.execute("UPDATE keywords SET idf_value=0 WHERE id=" + str(id))
			db_object.commit()


def update_keywords_word_count(db_object, word_dictionary, keyword_list):
	for element in keyword_list:
		cursor = db_object.cursor()
		word = element[1]
		word_id = element[0]
		w = ''.join(e for e in word if e.isalnum())
		if w.lower() in word_dictionary:
			cursor.execute("UPDATE keywords SET word_count=" + str(word_dictionary[w.lower()]) + " WHERE id=" + str(word_id))
			db_object.commit()
		else:
			cursor.execute("UPDATE keywords SET word_count=0 WHERE id=" + str(word_id))
			db_object.commit()


def main():
	db_obj = create_db_object()
	reset_table(db_obj)
	run_program(db_obj)
	get_database(db_obj)
main()