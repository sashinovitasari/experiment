from file_handler import loadtxt,loadlist,savetxt,savelist,loaddict
from normalizer import normalizer

def crawl_linetoday(file):
	norm = normalizer()
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
	result = norm.normalize_text(result)
	result = norm.clean_text(result)
	savetxt(result,"norm_"+file)

	return (result!='')

crawl_linetoday('line_raw06.txt')