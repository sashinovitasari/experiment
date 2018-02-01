'''
Text normalizer (Indonesia)
Author	: Sashi Novitasari
Date	: January 2018
'''

from file_handler import loadtxt,loadlist,savetxt,savelist,loaddict
import re

#-----WORD/TOKEN LEVEL-------

#Normalize word repetition that symbolized by certain symbol. E.g: 
# dua2: dua dua
# tiga"nya: tiga tiga nya
#Input	: word		- target word
#		  symbol	- repetition symbol
#Output	: Normalized word if word contain symbol, otherwise the original word 
def norm_word_repetition(word,symbol):
	new_tok = word
	if symbol in word:
		words = word.split(symbol)
		new_tok = words[0]+" "+words[0]
		if len(words)>1:
			new_tok+=" "+words[1]
	return new_tok

#Remove non-alphabet/numeric char in word, with exception for char in exception_list,
#and replace one-char emoji with '.'. Removed char replaced with ' '
#Input	: word		- target word
#		  except_list- list of non-aplabet/numric char that don't want to be removed
#Output	: Normalized word 
def norm_remove_nonchar(word,except_list):
	txt=""
	for i in word:
		if ((ord(i)>=48 and ord(i)<=57) or (ord(i)>=97 and ord(i)<=122)) or i in except_list:
			txt+=i
		elif (ord(i)>100000):
			txt+='.'
		else:
			txt+=" "
	return txt

#Normalize repeated substring. E.g:
# wkwkwkwk: wk
# hahahaha: ha
#Input	: word	- target word (lower cased)
#Output	: normalized word
def norm_substring_corner(word):
	substring = loadlist("dict/dict_repeat_substring")
	for s in substring:
		word = re.sub('^('+s+')+',s,word)#front anchor
	return word

#Remove repeated char in word (beginning/end). E.g:
# ohhh	: oh
# yyeah	: yeah
#Input	: word 	- target word (lower cased)
#Output	: normalized word
def norm_remove_repeat_char(word):
	#beginning of word
	if len(word)>2 and word[0]==word[1]:
		i=word[0]
		if ((ord(i)>=48 and ord(i)<=57) or (ord(i)>=97 and ord(i)<=122)):
			word = re.sub('^('+i+')+',i,word)
		else:
			word = re.sub('^(\\'+i+')+',i,word)
	#end of word
	if len(word)>2 and word[-1]==word[-2]:
		i=word[-1]
		if ((ord(i)>=48 and ord(i)<=57) or (ord(i)>=97 and ord(i)<=122)):
			word = re.sub('('+i+')+$',i,word)
		else:
			word = re.sub('(\\'+i+')+$',i,word)
	return word

def norm_formalize(word):
	substitute = loaddict('dict\dict_word_substitution')
	replacement = loadlist('dict\dict_word_replace')
	suffix = ""
	if word[-2:]=="ny":
		word = word[:-2]
		suffix = "nya"
	if word[-3:]=="nye" or word[-3:]=="nya":
		word = word[:-3]
		suffix = "nya"

	if ',' in word:
		word = word.replace(',','')
		suffix+=','

	if word in substitute:
		word = substitute[word]

	for r in replacement:
		if r in word:
			word = word.replace(r[0],r[1])
	return word+suffix

#-------SENTENCE LEVEL--------

#Normalize repeated punct. E.g:
# ... : .
# ?? : ?
#Input	: text	- target text (lower cased)
#Output	: normalized text
def norm_repeated_punct(text):
	substring = loadlist("dict/dict_punct")
	for s in substring:
		if s in text:
			if s==',':
				text = re.sub('\\,+','. ',text)#front anchor
			else:
				text = re.sub('\\'+s+'+',s+' ',text)#front anchor
	return text

#Remove multiple-char emoji in sentence/text, replaced with ' '
#Input	: text	- target text
#Output	: normalized text
def norm_remove_emoji(text):
	emoji = loadlist("dict/dict_emoji")
	for e in emoji:
		text = text.replace(e," ")
	return text

def clean_norm_sentence(text,sentence_break=['!','?','.'],except_list=['.',',','?','!','=','+']):
	#text = norm_substring_corner(text)
	text = norm_repeated_punct(text)
	text = norm_remove_emoji(text)
	text = text.replace(',',', ')
	text = text.replace(' ,',', ')
	words = text.split(" ")
	new_text = ""

	for w in words:
		break_point=" "
		w = norm_substring_corner(w)
		#if token are not number
		if len([i for i in w if (ord(i)>=48 and ord(i)<=57)])!=len(w):

			if w.count('"')==1:
				w = w.replace("\"",'2')
			if 'yonglex'in text:
				print(w)
			w = norm_remove_nonchar(w,except_list)

			#if word contain sentence-break symbol
			if len([i for i in sentence_break if i in w])>0: 
				break_point = "\n"
				w = norm_remove_nonchar(w,[','])

			w = norm_word_repetition(w,"2")
			if ' ' in w:
				ws = w.split(' ')
				ws[0] = norm_remove_repeat_char(ws[0])
				ws[1] = norm_remove_repeat_char(ws[1])
				new_text+= norm_formalize(ws[0])+' '+norm_formalize(ws[1])+break_point
			else:
				w = norm_remove_repeat_char(w)
				new_text+= norm_formalize(w)+break_point
		else:
			new_text+= w+break_point

	return new_text

#---------TEXT-LEVEL-------------
def clean_list_sentence(text,sentence_break=['!','?','.'],except_list=['.',',','?','!','=','+']):
	list_sent = text.split("\n")
	new_text = ""
	for s in list_sent:
		if ' ' in s and len(s.split(" "))>1 and 'http' not in s:
			new_text += clean_norm_sentence(s.lower(),sentence_break,except_list)+"\n"
	while '  ' in new_text:
		new_text = new_text.replace("  "," ")
	while '\n\n' in new_text:
		new_text = new_text.replace("\n\n","\n")

	return new_text

def clean_unrelevant_sent(text):
	list_sent = text.split("\n")
	new_text = ""
	for sent in list_sent:
		sent = re.sub('^( )+','',sent)
		sent = re.sub('( )+$','',sent)
		if ' ' in sent:
			new_text+= sent+'\n'
	return new_text

text = loadtxt("youtube_raw13.csv")
text = clean_list_sentence(text)
text = clean_unrelevant_sent(text)
savetxt(text,"y13try.csv")
