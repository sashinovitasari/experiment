'''
Text normalizer (Indonesia)
Author	: Sashi Novitasari
Date	: January 2018
'''

from file_handler import loadtxt,loadlist,savetxt,savelist,loaddict
import re

class normalizer:
	substring = loadlist("dict\dict_repeat_substring")
	substitute = loaddict('dict\dict_word_substitution')
	replacement = loadlist('dict\dict_word_replace','\t')
	subpunct = loadlist("dict\dict_punct")
	emoji = loadlist("dict\dict_emoji")
	prefix_consonant = {'k':'ke','d':'di'}
	vocal = ['a','i','u','e','o','j','h','y']

	#-----DICTIONARY LOADER---------
	def loaddict_substring(self,file):
		self.substring = loadlist(file)

	def loaddict_word_subsitute(self,file):
		self.substitute = loaddict(file)

	def loaddict_word_replacement(self,file,var_separator='\t'):
		self.replacement = loadlist(file,var_separator)

	def loaddict_punct(self,file):
		self.subpunct = loadlist(file)

	def loaddict_emoji(self,file):
		self.emoji = loadlist(file)

	#-----WORD/TOKEN LEVEL-------
	#Normalize word repetition that symbolized by certain symbol. E.g: 
	# dua2: dua dua
	# tiga"nya: tiga tiga nya
	#Input	: word		- target word
	#		  symbol	- repetition symbol
	#Output	: Normalized word if word contain symbol, otherwise the original word 
	def norm_word_repetition(self,word,symbol):
		if symbol in word:
			words = word.split(symbol)
			new_tok = words[0] #+" "+words[0]
			if len(words)>1:
				return new_tok+words[1]
			return new_tok
		return word

	#Remove non-alphabet/numeric char in word, with exception for char in exception_list,
	#and replace one-char emoji with '.'. Removed char replaced with ' '
	#Input	: word		- target word
	#		  except_list- list of non-aplabet/numric char that don't want to be removed
	#Output	: Normalized word 
	def norm_remove_nonchar(self,word,except_list):
		txt=""
		for i in word:
			if (re.match('^[a-zA-Z0-9_]+$',i)) or i in except_list:
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
	def norm_substring_corner(self,word):
		for s in self.substring:
			if sorted(list(set(word)))==sorted(list(set(s))):
				return s
			else:
				word = re.sub('^('+s+')+',s,word)#front anchor
				if sorted(list(set(word)))==sorted(list(set(s))):
					return s
		return word

	#Remove repeated char in word (beginning/end). E.g:
	# ohhh	: oh
	# yyeah	: yeah
	#Input	: word 	- target word (lower cased)
	#Output	: normalized word
	def norm_remove_repeat_char(self,word):
		if len(word)>2:

			#beginning of word
			if word[0]==word[1]:
				i=word[0]
				if (re.match('^[a-zA-Z0-9_]+$',word[0])):
					word = re.sub('^('+word[0]+')+',word[0],word)
				else:
					word = re.sub('^(\\'+word[0]+')+',word[0],word)

			#end of word
			if len(word)>2 and word[-1]==word[-2]:
				if (re.match('^[a-zA-Z0-9_]+$',word[-1])):
					word = re.sub('('+word[-1]+')+$',word[-1],word)
				else:
					word = re.sub('(\\'+word[-1]+')+$',word[-1],word)
		return word
	def norm_prefix(self,word):
		if len(word)>2 and word[0] in self.prefix_consonant and word[1] in self.vocal:
			word = re.sub('('+word[0]+')+$',self.prefix_consonant[word[0]],word)
		return word

	def norm_formalize(self,word):
		suffix = ""
		if ',' in word:
			word = word.replace(',','')
			suffix+=','
		if '?' in word:
			word = word.replace('?','')
			suffix+='?'
		if len(word)>4 and word[-2:]=="ny":
			word = word[:-2]
			suffix = "nya" +suffix
		if len(word)>5 and (word[-3:]=="nye" or word[-3:]=="nya" or word[-3:]=="nys"):
			word = word[:-3]
			suffix = "nya" +suffix
		word = self.norm_prefix(word)
		if word in self.substitute:
			word = self.substitute[word]

		for r in self.replacement:
			if r[0] in word:
				word = word.replace(r[0],r[1])
		exp_x = ['sex','fox','fax','antarex']
		
		if len(word)>0 and word not in exp_x and word[-1]=='x':
			word = re.sub('(x)+$','',word)

		return word+suffix

	#-------SENTENCE LEVEL--------

	#Normalize repeated punct. E.g:
	# ... : .
	# ?? : ?
	#Input	: text	- target text (lower cased)
	#Output	: normalized text
	def norm_repeated_punct(self,text):
		for s in self.subpunct:
			if s in text:
				if s==',':
					text = re.sub('\,{2,}','. ',text)#front anchor
				else:
					text = re.sub('\\'+s+'+',s+' ',text)#front anchor
		return text

	#Remove multiple-char emoji in sentence/text, replaced with ' '
	#Input	: text	- target text
	#Output	: normalized text
	def norm_remove_emoji(self,text):
		for e in self.emoji:
			text = text.replace(e,".")
		return text

	def clean_norm_sentence(self,text,sentence_break=['!','?','.'],except_list=['.',',','?','!','=','+']):
		text = text.lower().replace(" s2 ", " strata 2 ")
		if text[0]=='"' and text[-1]=='"':
			text = text[1:-1]

		text = self.norm_remove_emoji(text)
		text = self.norm_repeated_punct(text)

		text = text.replace(',',' , ')
		text = text.replace(' ,',' , ')
		words = text.split(" ")
		new_text = ""

		special_punct = [',','?']
		for w in words:
			break_point=" "
			#if token are not number
			if len([i for i in w if (ord(i)>=48 and ord(i)<=57)])!=len(w):

				if w.count('"')==1:
					w = w.replace("\"",'2')
				w = self.norm_remove_nonchar(w,except_list)

				#if word contain sentence-break symbol
				if len([i for i in sentence_break if i in w])>0: 
					break_point = "\n"
					w = self.norm_remove_nonchar(w,special_punct)
				
				lp = list([punct for punct in special_punct if punct in w])
				if len(lp)>0:
					w = self.norm_word_repetition(w.replace(lp[0],""),"2")+" "+lp[0]
				else:
					w = self.norm_word_repetition(w,"2")
				

				if ' ' in w:
					ws = w.split(' ')
					ws[0] = self.norm_substring_corner(ws[0])
					ws[1] = self.norm_substring_corner(ws[1])
					ws[0] = self.norm_remove_repeat_char(ws[0])
					ws[1] = self.norm_remove_repeat_char(ws[1])
					new_text+= self.norm_formalize(ws[0])+' '+self.norm_formalize(ws[1])+break_point
				else:
					w = self.norm_substring_corner(w)
					w = self.norm_remove_repeat_char(w)
					new_text+= self.norm_formalize(w)+break_point
			else:
				new_text+= w+break_point
		return new_text

	#---------TEXT-LEVEL-------------
	def normalize_list_sentence(self,list_sent,sentence_break=['!','?','.'],except_list=['.',',','?','!','=','+']):
		new_text = ""
		for s in list_sent:
			if ' ' in s and len(s.split(" "))>1 and 'http' not in s and '@' not in s:
				new_text += self.clean_norm_sentence(s.lower(),sentence_break,except_list)+"\n"
		while '  ' in new_text:
			new_text = new_text.replace("  "," ")
		while '\n\n' in new_text:
			new_text = new_text.replace("\n\n","\n")

		return new_text.split("\n")
	
	def normalize_text(self,text,sentence_break=['!','?','.'],except_list=['.',',','?','!','=','+']):
		list_sent = text.split("\n")
		new_text = ""
		for s in list_sent:
			if ' ' in s and len(s.split(" "))>1 and 'http' not in s and '@' not in s:
				new_text += self.clean_norm_sentence(s.lower(),sentence_break,except_list)+"\n"
		while '  ' in new_text:
			new_text = new_text.replace("  "," ")
		while '\n\n' in new_text:
			new_text = new_text.replace("\n\n","\n")

		return new_text

	def clean_text(self,text):
		list_sent = text.split("\n")
		new_text = ""
		for sent in list_sent:
			sent = re.sub('^( )+','',sent)
			sent = re.sub('( )+$','',sent)
			if ' ' in sent:
				new_text+= sent+'\n'
		return new_text

	def clean_list_sentence(self,list_sent):
		new_text = ""
		for sent in list_sent:
			sent = re.sub('^( )+','',sent)
			sent = re.sub('( )+$','',sent)
			if ' ' in sent:
				new_text+= sent+'\n'
		return new_text.split("\n")

n= normalizer()
text = loadtxt("youtube_raw30.csv")
text = n.normalize_text(text)
text = n.clean_text(text)
savetxt(text,"y30try.csv")
