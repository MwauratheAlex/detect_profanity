from profanity_filter import ProfanityFilter
import config

#Enter the path to your textfile here. Eg. path = "C:\xxx\yyy\zzz\movie_quotes.txt"
path = config.path

def read_text():
	quotes = open(path)
	contents_of_file = quotes.read()

	print("***ORIGINAL CONTENT***\n")
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	pf = ProfanityFilter()

	if(pf.is_clean(text_to_check)):
		print("\nHurray! Your text is clean!\n")

	else:
		print("\n\nOops! Your text is profane!\n")
		print("\n***CENSORED CONTENT***\n")
		print(pf.censor(text_to_check))
		

read_text()


