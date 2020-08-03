import shortener


sess = shortener.get_session(username="root", password="Villa#25", host="0.0.0.0", db_name="shortener")
print(len(shortener.shorten_from_file(sess, "shortener/data/input.txt")))
print(shortener.shorten(sess, "https://hello-world.com"))
print(shortener.get_original_url(sess, "005qBDMT"))
