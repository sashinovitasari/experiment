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

def save2txt(string,file):
	with open(file,"w",encoding='utf8') as myfile:
		myfile.write(string)

def loadtxt(file):
	with open(file,"r",encoding='utf8') as myfile:
		return myfile.read()

def norm_profane(text):
	text = text.replace("begok","bego")
	text = text.replace("bgst","bangsat")
	text = text.replace("ngentod","ngentot")
	text = text.replace("goblookkk","goblok")

	return text

def norm_formalize_center(text):
	substitute = []
	substitute.append(["&","dan"])

	substitute.append(["aje","saja"])
	substitute.append(["aje","aja"])
	substitute.append(["aj","saja"])
	substitute.append(["ap","apa"])
	substitute.append(["ato","atau"])
	substitute.append(["atw","atau"])
	substitute.append(["aplg","apalagi"])
	substitute.append(["or","atau"])
	substitute.append(["ane","aku"])

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
	substitute.append(["ngmg","bicara"])

	substitute.append(["cm","cuma"])
	substitute.append(["cuman","cuma"])
	substitute.append(["cmn","cuma"])
	substitute.append(["cacad","cacat"])
	substitute.append(["conto","contoh"])


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

	substitute.append(["gt","gitu"])
	substitute.append(["gtu","gitu"])
	substitute.append(["gw","aku"])
	substitute.append(["gue","aku"])
	substitute.append(["gimana","bagaimana"])
	substitute.append(["gmn","bagaimana"])
	substitute.append(["gmna","bagaimana"])
	substitute.append(["gpp","tidak apa apa"])
	substitute.append(["gub","gubernur"])

	substitute.append(["hrs","harus"])
	substitute.append(["hrus","harus"])
	substitute.append(["abis","habis"])
	substitute.append(["abs","habis"])
	substitute.append(["hbs","habis"])

	substitute.append(["indo","indonesia"])
	substitute.append(["tu","itu"])
	substitute.append(["it","itu"])
	substitute.append(["tuh","itu"])
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

	substitute.append(["ngasi","kasih"])
	substitute.append(["ngasih","kasih"])
	substitute.append(["kasi","kasih"])
	substitute.append(["ksi","kasih"])


	substitute.append(["kali","mungkin"])
	substitute.append(["kli","mungkin"])
	substitute.append(["kale","mungkin"])
	substitute.append(["kalo","kalau"])
	substitute.append(["kl","kalau"])
	substitute.append(["klo","kalau"])
	substitute.append(["krj","kerja"])
	substitute.append(["kcli","kecuali"])
	substitute.append(["kcl","kecil"])
	substitute.append(["krj","kerja"])
	substitute.append(["k","ke"])
	substitute.append(["krs","keras"])
	substitute.append(["kras","keras"])
	substitute.append(["krn","karena"])
	substitute.append(["krna","karena"])
	substitute.append(["knp","kenapa"])
	substitute.append(["napa","kenapa"])
	substitute.append(["kmn","kemana"])
	substitute.append(["ente","kamu"])
	substitute.append(["loe","kamu"])
	substitute.append(["lw","kamu"])
	substitute.append(["lu","kamu"])

	substitute.append(["lg","lagi"])
	substitute.append(["lag","lagi"])
	substitute.append(["lgi","lagi"])
	substitute.append(["lht","lihat"])
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

	substitute.append(["tp","tapi"])
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
	substitute.append(["gk","tidak"])
	substitute.append(["ga","tidak"])
	substitute.append(["gak","tidak"])
	substitute.append(["ngak","tidak"])
	substitute.append(["nggak","tidak"])
	substitute.append(["nga","tidak"])
	substitute.append(["gtw","tidak tahu"])
	substitute.append(["gabenar","tidak benar"])
	substitute.append(["gabener","tidak benar"])
	substitute.append(["gada","tidak ada"])


	substitute.append(["utk","untuk"])
	substitute.append(["untk","untuk"])

	substitute.append(["yg","yang"])
	substitute.append(["yak","ya"])
	substitute.append(["jaman","zaman"])



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

	return text

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
	
	text = text.replace(" gw "," gue ")
	text = text.replace(" lw "," lo ")


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

	result = clean_raw_text(result)
	
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
	result = clean_text(result)
	save2txt(result,"raw02_cleaned.txt")
	return result


#txt = loadtxt("raw01.txt")
#save2txt(clean_text(txt),"raw01_cleaned.txt")
crawl_linetoday("raw02.txt")

#result =""
#save2txt(result,"raw02.txt")
