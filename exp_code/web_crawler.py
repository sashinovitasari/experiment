import re

def save2txt(string,file):
	with open(file,"w",encoding='utf8') as myfile:
		myfile.write(string)

def loadtxt(file):
	with open(file,"r",encoding='utf8') as myfile:
		return myfile.read()

def norm_repeat_word(text,symbol):
	token = text.split(" ")
	new_text = ""
	for i in range (0,len(token)):
		if symbol in token[i][2:]:
			word = token[i].split(symbol)
			new_tok = word[0]+" "+word[0]
			if len(word)>1:
				new_tok+=word[1]
			token[i]=new_tok
		new_text+= token[i]+" "
	return new_text		

def norm_repeat_word_level(word,symbol):
	new_tok = word
	if symbol in word:
		words = word.split(symbol)
		new_tok = words[0]+" "+words[0]
		if len(words)>1:
			new_tok+=" "+words[1]
	return new_tok

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



def norm_profane(text):
	text = text.replace("begok","bego")
	text = text.replace("bgst","bangsat")
	text = text.replace("ngentod","ngentot")
	text = text.replace("goblookkk","goblok")

	return text

def norm_formalize_center(text):
	substitute = []
	substitute.append(["&","dan"])
	substitute.append(["=","sama dengan"])

	substitute.append(["aje","saja"])
	substitute.append(["aje","aja"])
	substitute.append(["aj","saja"])
	substitute.append(["ap","apa"])
	substitute.append(["ato","atau"])
	substitute.append(["atw","atau"])
	substitute.append(["aplg","apalagi"])
	substitute.append(["or","atau"])
	substitute.append(["ane","gue"])
	substitute.append(["ama","sama"])
	substitute.append(["aq","aku"])
	substitute.append(["abng","abang"])

	substitute.append(["blm","belum"])
	substitute.append(["lom","belum"])
	substitute.append(["bnr","benar"])
	substitute.append(["bru","baru"])
	substitute.append(["bnyk","banyak"])
	substitute.append(["byk","banyak"])
	substitute.append(["bkrj","bekerja"])
	substitute.append(["bs","bisa"])
	substitute.append(["bw","bawa"])
	substitute.append(["bgmn","bagaimana"])
	substitute.append(["bhw","bahwa"])
	substitute.append(["brt","berat"])
	substitute.append(["brpa","berapa"])
	substitute.append(["brp","berapa"])
	substitute.append(["bbrp","beberapa"])
	substitute.append(["bbrpa","beberapa"])
	substitute.append(["bapa","bapak"])
	substitute.append(["bpk","bapak"])
	substitute.append(["bgus","bagus"])
	substitute.append(["bgs","bagus"])
	substitute.append(["bngt","banget"])
	substitute.append(["bnget","banget"])
	substitute.append(["bgst","bangsat"])

	substitute.append(["ngmg","ngomong"])

	substitute.append(["cm","cuma"])
	substitute.append(["cuman","cuma"])
	substitute.append(["cmn","cuma"])
	substitute.append(["cacad","cacat"])
	substitute.append(["conto","contoh"])
	substitute.append(["click","klik"])

	substitute.append(["d","di"])
	substitute.append(["dah","sudah"])
	substitute.append(["dluny","dulunya"])
	substitute.append(["dlu","dulu"])
	substitute.append(["dl","dulu"])
	substitute.append(["dpet","dapat"])
	substitute.append(["dapet","dapat"])
	substitute.append(["dpt","dapat"])
	substitute.append(["dgn","dengan"])
	substitute.append(["dg","dengan"])
	substitute.append(["dr","dari"])
	substitute.append(["drpd","daripada"])
	substitute.append(["dlm","dalam"])
	substitute.append(["dy","dia"])
	substitute.append(["dll","dan lain lain"])
	substitute.append(["dsb","dan sebagainya"])
	substitute.append(["jdi","jadi"])

	substitute.append(["fb","facebook"])
	substitute.append(["enggk","ngga"])
	substitute.append(["engga","ngga"])
	substitute.append(["enggak","ngga"])

	substitute.append(["gt","gitu"])
	substitute.append(["gtu","gitu"])
	substitute.append(["gw","gue"])
	substitute.append(["gde","gede"])
	substitute.append(["gwa","gue"])
	substitute.append(["gmn","gimana"])
	substitute.append(["gmna","gimana"])
	substitute.append(["gpp","ngga apa apa"])
	substitute.append(["gub","gubernur"])
	substitute.append(["g","ngga"])
	substitute.append(["gile","gila"])

	substitute.append(["hrs","harus"])
	substitute.append(["hrus","harus"])
	substitute.append(["abis","habis"])
	substitute.append(["abs","habis"])
	substitute.append(["hbs","habis"])

	substitute.append(["indo","indonesia"])
	substitute.append(["ibuk","ibu"])
	substitute.append(["tu","itu"])
	substitute.append(["it","itu"])
	substitute.append(["ntu","itu"])

	substitute.append(["jg","juga"])
	substitute.append(["jgn","jangan"])
	substitute.append(["jngn","jangan"])
	substitute.append(["jln","jalan"])
	substitute.append(["jl","jalan"])
	substitute.append(["jkt","jakarta"])
	substitute.append(["jd","jadi"])
	substitute.append(["jdi","jadi"])
	substitute.append(["jem","jam"])

	substitute.append(["ngasi","ngasih"])
	substitute.append(["kasi","kasih"])
	substitute.append(["ksi","kasih"])

	substitute.append(["kli","kali"])
	substitute.append(["kale","kali"])
	substitute.append(["kalo","kalau"])
	substitute.append(["kl","kalau"])
	substitute.append(["ku","aku"])
	substitute.append(["klo","kalau"])
	substitute.append(["klu","kalau"])
	substitute.append(["krj","kerja"])
	substitute.append(["kcli","kecuali"])
	substitute.append(["kcl","kecil"])
	substitute.append(["krj","kerja"])
	substitute.append(["k","ke"])
	substitute.append(["krs","keras"])
	substitute.append(["kras","keras"])
	substitute.append(["krn","karena"])
	substitute.append(["karna","karena"])
	substitute.append(["krna","karena"])
	substitute.append(["knp","kenapa"])
	substitute.append(["napa","kenapa"])
	substitute.append(["kmn","kemana"])
	substitute.append(["ente","loe"])
	substitute.append(["lw","loe"])
	substitute.append(["lu","loe"])
	substitute.append(["lo","loe"])

	substitute.append(["lg","lagi"])
	substitute.append(["lag","lagi"])
	substitute.append(["lgi","lagi"])
	substitute.append(["lht","lihat"])
	substitute.append(["liat","lihat"])
	substitute.append(["lbh","lebih"])
	substitute.append(["loh","lho"])
	substitute.append(["la","lah"])
	substitute.append(["laen","lain"])

	substitute.append(["mo","mau"])
	substitute.append(["mw","mau"])
	substitute.append(["mtr","motor"])
	substitute.append(["mrk","mereka"])
	substitute.append(["mrka","mereka"])
	substitute.append(["mlz","malas"])
	substitute.append(["mls","malas"])
	substitute.append(["mlh","malah"])
	substitute.append(["msh","masih"])
	substitute.append(["mcm","macam"])
	substitute.append(["cem","macam"])
	substitute.append(["emang","memang"])
	substitute.append(["emng","memang"])
	substitute.append(["emg","memang"])
	substitute.append(["malay","malaysia"])

	substitute.append(["ny","nya"])
	substitute.append(["naek","naik"])
	substitute.append(["ntar","nanti"])
	substitute.append(["nti","nanti"])
	substitute.append(["noh",""])
	substitute.append(["neh","nih"])
	substitute.append(["niy","nih"])
	substitute.append(["ngr","negara"])
	substitute.append(["negri","negeri"])
	substitute.append(["ntn","nonton"])


	substitute.append(["org","orang"])
	substitute.append(["itak","otak"])
	substitute.append(["otk","otak"])

	substitute.append(["pny","punya"])
	substitute.append(["pnya","punya"])
	substitute.append(["pd","pada"])
	substitute.append(["pda","pada"])
	substitute.append(["prnh","pernah"])
	substitute.append(["pake","pakai"])
	substitute.append(["pk","pakai"])
	substitute.append(["pke","pakai"])
	substitute.append(["pli","tolong"])

	substitute.append(["rame","ramai"])
	substitute.append(["rmh","rumah"])

	substitute.append(["ma","sama"])
	substitute.append(["sm","sama"])
	substitute.append(["sllu","selalu"])
	substitute.append(["mpe","sampai"])
	substitute.append(["smpe","sampai"])
	substitute.append(["sampe","sampai"])
	substitute.append(["smua","semua"])
	substitute.append(["sdh","sudah"])
	substitute.append(["sudh","sudah"])
	substitute.append(["udh","sudah"])
	substitute.append(["skrg","sekarang"])
	substitute.append(["skr","sekarang"])
	substitute.append(["udah","sudah"])
	substitute.append(["sndr","sendiri"])
	substitute.append(["sprt","seperti"])
	substitute.append(["spt","seperti"])
	substitute.append(["sngt","sangat"])
	substitute.append(["skul","sekolah"])
	substitute.append(["sklah","sekolah"])
	substitute.append(["sklhan","sekolahan"])
	substitute.append(["shg","sehingga"])
	substitute.append(["bgtu","seperti itu"])
	substitute.append(["bgt","sekali"])
	substitute.append(["ampe","sampai"])
	substitute.append(["setau","setahu"])
	substitute.append(["kyk","seperti"])
	substitute.append(["kya","seperti"])
	substitute.append(["kek","seperti"])
	substitute.append(["ky","seperti"])
	substitute.append(["kayak","seperti"])
	substitute.append(["sbrpa","seberapa"])
	substitute.append(["sbrp","seberapa"])
	substitute.append(["sebrpa","seberapa"])
	substitute.append(["sebrp","seberapa"])
	substitute.append(["sblm","sebelum"])
	substitute.append(["spy","supaya"])
	substitute.append(["skg","sekarang"])
	substitute.append(["skrng","sekarang"])
	substitute.append(["slh","salah"])
	substitute.append(["slg","saling"])

	substitute.append(["tp","tapi"])
	substitute.append(["tpi","tapi"])
	substitute.append(["tspi","tapi"])
	substitute.append(["temen","teman"])
	substitute.append(["tmen","teman"])
	substitute.append(["trus","terus"])
	substitute.append(["trs","terus"])
	substitute.append(["trz","terus"])
	substitute.append(["tdk","tidak"])
	substitute.append(["ndak","tidak"])
	substitute.append(["tw","tahu"])
	substitute.append(["tau","tahu"])
	substitute.append(["th","tahu"])
	substitute.append(["tmpt","tempat"])
	substitute.append(["tsb","tersebut"])
	substitute.append(["tkut","takut"])
	substitute.append(["tkt","takut"])
	substitute.append(["gk","ngga"])
	substitute.append(["ga","ngga"])
	substitute.append(["gak","ngga"])
	substitute.append(["ngak","ngga"])
	substitute.append(["nggak","ngga"])
	substitute.append(["nga","ngga"])
	substitute.append(["gtw","ngga tahu"])
	substitute.append(["gabenar","ngga benar"])
	substitute.append(["gabener","ngga benar"])
	substitute.append(["gada","ngga ada"])
	substitute.append(["gausah","ngga usah"])
	substitute.append(["gaush","ngga usah"])

	substitute.append(["pngn","pengen"])
	substitute.append(["pgn","pengen"])
	substitute.append(["prg","pergi"])
	substitute.append(["utk","untuk"])
	substitute.append(["untk","untuk"])

	substitute.append(["yg","yang"])
	substitute.append(["yak","ya"])
	substitute.append(["jaman","zaman"])

	substitute.append(["="," sama dengan "])
	substitute.append(["+"," ditambah "])
	substitute.append(["-"," dikurang "])

	for sub in substitute:
		if text==sub[0]:
			text=sub[1]

	if text[-2:]=="ny":
		text = text.replace("ny","nya")
	if text[-3:]=="nye":
		text = text.replace("nye","nya")
	text = text.replace("mesti","mesti")
	text = text.replace("bener","benar")
	text = text.replace("pingin","ingin")
	text = text.replace("jatoh","jatuh")
	text = text.replace("bgs","bagus")
	text = text.replace("belom","belum")
	text = text.replace("bljr","belajar")
	text = text.replace("denger","dengar")
	text = text.replace("gimana","bagaimana")
	text = text.replace("inget","ingat")
	text = text.replace("kasian","kasihan")
	text = text.replace("liat","lihat")
	text = text.replace("ngeroko","merokok")	
	text = text.replace("mnrut","menurut")
	text = text.replace("pinter","pintar")
	text = text.replace("bentar","bentar")
	text = text.replace("ancur","hancur")
	text = text.replace("mabok","mabuk")
	text = text.replace("gampang","mudah")
	text = text.replace("gede","besar")	
	text = text.replace("brp","berapa")
	text = text.replace("kliatan","kelihatan")
	text = text.replace("keliatan","kelihatan")
	text = text.replace("tangkep","tangkap")
	text = text.replace("sprti","seperti")
	text = text.replace("jaman","zaman")

	return text

def norm_remove_emoji(text):
	emoji = [':v',':(',':3',':)',"'3'",'<3',':p',':d']
	for e in emoji:
		text = text.replace(e," ")
	return text

def norm_substring(text):
	substring = ['wk','hihi','hehe']
	for s in substring:
		text = re.sub('^('+s+')+',s+' ',text)
	return text

def norm_remove_repeat_char(word):
	word = word.lower()
	#beginning of word

	if len(word)>2 and word[0]==word[1]:
		i=word[0]
		if ((ord(i)>=48 and ord(i)<=57) or (ord(i)>=97 and ord(i)<=122)):
			word = re.sub('^('+word[0]+')+',word[0],word)
		else:
			word = re.sub('^(\\'+word[0]+')+',word[0],word)
	#end of word
	if len(word)>2 and word[-1]==word[-2]:
		i=word[-1]
		if ((ord(i)>=48 and ord(i)<=57) or (ord(i)>=97 and ord(i)<=122)):
			word = re.sub('('+word[-1]+')+$',word[-1],word)
		else:
			word = re.sub('(\\'+word[-1]+')+$',word[-1],word)
	return word


def clean_text(text):
	text = text.replace("("," ( ")
	text = text.replace(")"," ) ")
	while "  " in text:
		text = text.replace("  "," ")
	while "\n " in text:
		text = text.replace("\n ","\n")
	while " \n" in text:
		text = text.replace(" \n","\n")
	while "\n\n" in text:
		text = text.replace("\n\n","\n")


	sentences = text.split("\n")

	idx = 0
	result = ""
	while idx<len(sentences):
		new_sent = ""
		words = sentences[idx].split(" ")

		if len(words)>2:
			for w in words:
				valid = (len([c for c in w if not(ord(c)>=97 and ord(c)<=122)])<1)
				if valid and len(w)>2:
					new_sent+=norm_formalize_center(w)+" "
			result+=new_sent[:-1]+"\n"
		idx+=1
	while "  " in result:
		result = result.replace("  "," ")
	while "\n\n" in result:
		result = result.replace("\n\n","\n")
	return result

def clean_norm_sentence(text,sentence_break,except_list):
	text = re.sub('\.+','. ',text)
	text = norm_substring(text.lower())
	text = norm_remove_emoji(text)
	words = text.split(" ")
	new_text = ""

	for w in words:
		break_point=" "
		if len([i for i in w if (ord(i)>=48 and ord(i)<=57)])!=len(w):
			w.replace("\"",'2')
			w = norm_remove_nonchar(w,except_list)
			if len([i for i in sentence_break if i in w])>0:
				break_point = "\n"
				w = norm_remove_nonchar(w,',')
			w = norm_repeat_word_level(w,"2")
			if ' ' in w:
				ws = w.split(' ')
				ws[0] = norm_remove_repeat_char(ws[0])
				ws[1] = norm_remove_repeat_char(ws[1])
				new_text+= norm_formalize_center(ws[0])+' '+norm_formalize_center(ws[1])+break_point
			else:
				w = norm_remove_repeat_char(w)
				new_text+= norm_formalize_center(w)+break_point
		else:
			new_text+= w+break_point
	#print(new_text)
	return new_text

def clean_raw_text(text):
	while "  " in text:
		text= text.replace("  "," ")
	text = text.replace(" = "," sama dengan ")
	text = text.replace(" + "," ditambah ")
	text = text.replace(" - "," dikurang ")

	text = text.replace("\t"," ")
	text = text.replace("\r"," ")
	text = text.replace("-"," ")
	text = text.replace("!",".")
	text = text.replace("?",".")
	text = text.replace(","," ")
	text = text.replace("="," ")
	text = text.replace("\n",".")
	text = text.replace("'",".")
	text = text.replace("@","")
	text = text.replace("_","")

	text = text.replace("/","atau")
	text = text.replace(" n ","dan")
	text = text.replace("wk","")
	text = norm_repeat_word(text,"2")
	text = norm_repeat_word(text,"\"")
	text = text.replace("\"","")	


	while ".." in text:
		text= text.replace("..",".")
	while "  " in text:
		text= text.replace("  "," ")
	text = text.replace(".","\n")

	return text

def crawl_kaskusarchive(link):
	from urllib.request import urlopen
	from bs4 import BeautifulSoup
	page = urlopen(link)#"https://archive.kaskus.co.id/thread/16998622/2")
	soup = BeautifulSoup(page)
	list_content = soup.get_text()
	result = ""
	cont = ""
	for content in list_content:
		cont += content
	while "\n\n" in cont:
		cont = cont.replace("\n\n","\n")
	while "\t" in cont:
		cont = cont.replace("\t","")

	#print(cont)
	list_content = cont.split("\n")
	id_content = 0

	while id_content<len(list_content):
		sentence = ""
		sent = list_content[id_content].lower()
		if '#' in str(sent) and sent[1].isdigit():
			id_content+=1
			while "view bbcode" not in list_content[id_content].lower():
				sent = list_content[id_content].lower()	
				if (">-" not in sent) and (".com" not in sent) and ("|" not in sent) and (":" not in sent) and ("http" not in sent) and ("download" not in sent) and len(sent)>5 and len(sent.split(" "))>2:
					sentence+=sent+"\n"
				id_content+=1
		id_content+=1
		result+=sentence

	#result = clean_raw_text(result)
	
	return result

def crawl_linetoday(file):
	txt = loadtxt(file)
	txt = txt.replace("><",">\n<")
	txt_list = txt.split("\n")
	result=""
	idx_t = 0
	is_write = 0
	for t in txt_list:
		if '<p class="comm">' in t:
			if "</p>" not in t:
				t = txt_list[idx_t+1]
			t = t.replace('<p class="comm">',"")
			idx = 0
			while '</p>' not in t[idx:(idx+4)]:
				if t[idx]=="<":
					is_write+=1
				elif t[idx]==">":
					is_write-=1
				if is_write==0 and t[idx]!=">":
					result+= t[idx].lower()
				idx+=1
			result+="\n"
		idx_t+=1
	print(result)
	#result = clean_text(result)
	save2txt(result,"clean"+file)
	return result

def clean_list_sentence(text,sentence_break,except_list):
	text = text.replace(',',', ')
	text = text.replace(' ,',', ')
	list_sent = text.split("\n")
	new_text = ""
	for s in list_sent:
		if ' ' in s and len(s.split(" "))>1:
			new_text += clean_norm_sentence(s,sentence_break,except_list)+"\n"	
	while '  ' in new_text:
		new_text = new_text.replace("  "," ")
	while '\n\n' in new_text:
		new_text = new_text.replace("\n\n","\n")

	return new_text

def clean_unrelevant_sent(text):
	list_sent = text.split("\n")
	new_text = ""
	for sent in list_sent:
		print(sent)
		sent = re.sub('^( )+','',sent)
		sent = re.sub('( )+$','',sent)
		print(sent)
		if ' ' in sent:
			new_text+= sent+'\n'
	return new_text
		

text = loadtxt("youtube_raw07.csv")
text = clean_list_sentence(text,['!','?','.'],['.',',','?','!','=','+'])
text = clean_unrelevant_sent(text)
save2txt(text,"y07.csv")


#txt = loadtxt("raw01.txt")
#save2txt(clean_text(txt),"raw01_cleaned.txt")
#crawl_linetoday("raw02.txt")

#result =""
#save2txt(result,"raw02.txt")
