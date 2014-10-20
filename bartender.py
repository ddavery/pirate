import random
questions = {
	"strong": "Do ye like yer drinks strong?",
	"salty": "Do ye like it with a salty tang?",
	"bitter": "Are ye a lubber who likes it bitter?",
	"sweet": "Would ye like a bit of sweetness with yer poison?",
	"fruity": "Are ye one for a fruity finish?"
}
ingredients = {
	"strong": ["glug of rum", "slug of whisky", "splash of gin"],
	"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
	"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
	"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
	"fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}
def answer_questions():
	answer_quest = {}
	for key in questions:
		print key,questions[key]
		answers = raw_input("Please enter in a yes or y or no n if you like the drink: ")
		if answers == 'yes' or answers == 'y':
			answer_quest[key] = questions[key]
			answer_quest[key] = True
		elif answers == 'no' or answers == 'n':
		    answer_quest[key] = questions[key]
		    answer_quest[key] = False
		else:
			print 'Please enter yes or no in lower case'
	#rr
	return answer_quest
drinks1 = answer_questions()
def drinks(drinks1):
	shot = []
	for k in drinks1:
		if drinks1[k]:
		  shot.append(random.choice(ingredients[k]))
	print shot
drinks(drinks1)