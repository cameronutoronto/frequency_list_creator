IN_FILES = ["sempe_petitnicolas.txt", "les_recres_du_petit_nicolas.txt", "les_vacances_du_petit_nicolas.txt"]
OUT_FILE = "petit_nicolas_freq.txt"

freq_dict = {}
freq_dicts = []

SPECIAL_CHARS = ['\'', '"', '.', '-', '!', '?', ';', ',', '.', '\n', \
                 '«', '»', ':', '–', '—', ')', '(', ']', '[', '’', '`', '…']
INIT_CHARS = ['j', 'm', 'n', 's', 'd', 'l', 't']

VERB_FIX = True
DO_POST_PROCESSING = True

french_verbs_list = []
if VERB_FIX:
    with open("french_verbs.txt", 'r', encoding="utf-8") as f:
        for line in f:
            french_verbs_list.append(line[:-1])
french_verbs_list = set(french_verbs_list)
def fix_word(word):
    word = word.lower()
    if word == '':
        return word
    while word[-1] in SPECIAL_CHARS:
        word = word[:-1]
        if word == '':
            return word
        
    if word == '':
            return word
        
    while word[0] in SPECIAL_CHARS:
        word = word[1:]
        if word == '':
            return word

    if len(word) > 2 and word[1] in ['\'', '’']:
        if word[0] in ['j', 'm', 'n', 's', 'd', 'l', 't']:
            word = word[2:]

    try:
        word = int(word)
        word = ''
    except Exception:
        pass

    if word in ['j', 'm', 'n', 's', 'd', 'l', 't']:
        word = ''

    if VERB_FIX:
        if word in ["suis", "est", "es", "sommes", "êtes", "sont", "été"]:
            word = "être"
        elif word in ["étais", "était", "étions", "étiez", "étaient"]:
            word = "être"
        elif word in ["serai", "seras", "sera", "serons", "serez", "seront"]:
            word = "être"
        elif word in ["vais", "vas", "va", "allons", "allez", "vont", "allé", "irai"]:
            word = "aller"
        elif word in ["ai", "as", "a", "avons", "avez", "ont", "eu"]:
            word = "avoir"
        elif word in ["aurai", "auras", "aura", "aurons", "aurez", "auront"]:
            word = "avoir"
        elif word in ["dis", "dit", "disons", "dites", "disent", "dit"]:
            word = "dire"
        elif word in ["fais", "fait", "faisons", "faites", "font", "ferai"]:
            word = "faire"
        elif word in ["peux", "peut", "pouvons", "pouvez", "peuvent", "pu", "pourrai"]:
            word = "pouvoir"
        elif word in ["sais", "sait", "savons", "savez", "savent", "su", "saurai"]:
            word = "savoir"
        elif word in ["vois", "voit", "voyons", "voyez", "voient", "vu", "verrai"]:
            word = "voir"
        elif word in ["veux", "veut", "voulons", "voulez", "veulent", "voulu", "voudrai"]:
            word = "vouloir"
        elif len(word) > 4:
            if word[-3:] == 'ons' or word[-3:] == 'ent':
                tword = word[:-3] + "er"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-3] + "re"
                if tword in french_verbs_list:
                    word = tword
            if word[-2:] == 'ez':
                tword = word[:-2] + "er"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-2] + "re"
                if tword in french_verbs_list:
                    word = tword
            if word[-1] == 'é':
                tword = word[:-1] + "er"
                if tword in french_verbs_list:
                    word = tword
            if word[-2:] == 'és':
                tword = word[:-2] + "er"
                if tword in french_verbs_list:
                    word = tword
            if word[-2:] in ["is", "it"]:
                tword = word[:-2] + "ir"
                if tword in french_verbs_list:
                    word = tword
            if len(word) > 7 and word[-6:] in ["issons", "issent"]:
                tword = word[:-6] + "ir"
                if tword in french_verbs_list:
                    word = tword
            if len(word) > 6 and word[-5:] == "issez":
                tword = word[:-5] + "ir"
                if tword in french_verbs_list:
                    word = tword
            if word[-1] == 'i':
                tword = word[:-1] + "ir"
                if tword in french_verbs_list:
                    word = tword
            if word[-1] == 's':
                tword = word[:-1] + "re"
                if tword in french_verbs_list:
                    word = tword
            if word[-1] == 'u':
                tword = word[:-1] + "re"
                if tword in french_verbs_list:
                    word = tword
            if word[-1] == 'a':
                tword = word[:-1] + "er"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-1] + "ir"
                if tword in french_verbs_list:
                    word = tword 
                tword = word[:-1] + "re"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-1]
                if tword in french_verbs_list:
                    word = tword
            if word[-2:] in ['as', "ai", "ez"]:
                tword = word[:-2] + "er"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-2] + "ir"
                if tword in french_verbs_list:
                    word = tword 
                tword = word[:-2] + "re"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-2]
                if tword in french_verbs_list:
                    word = tword
            if word[-3:] in ['ons', "ont"]:
                tword = word[:-3] + "er"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-3] + "ir"
                if tword in french_verbs_list:
                    word = tword 
                tword = word[:-3] + "re"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-3]
                if tword in french_verbs_list:
                    word = tword
            if word[-3:] in ["ais", "ait", "iez"]:
                tword = word[:-3] + "er"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-3] + "ir"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-3] + "re"
                if tword in french_verbs_list:
                    word = tword
            if len(word) > 4 and word[-4:] == "ions":
                tword = word[:-4] + "er"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-4] + "ir"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-4] + "re"
                if tword in french_verbs_list:
                    word = tword
            if len(word) > 5 and word[-5:] == "aient":
                tword = word[:-5] + "er"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-5] + "ir"
                if tword in french_verbs_list:
                    word = tword
                tword = word[:-5] + "re"
                if tword in french_verbs_list:
                    word = tword
            tword = word + "re"
            if tword in french_verbs_list:
                word = tword
            
    return word

def get_words(word):
    words = []
    if '-' in word:
        new_words = word.split('-')
        for w in new_words:
            w = fix_word(w)
            words.append(w)
    elif '—' in word:
        new_words = word.split('—')
        for w in new_words:
            w = fix_word(w)
            words.append(w)
    elif '.' in word:
        new_words = word.split('.')
        for w in new_words:
            w = fix_word(w)
            words.append(w)
    elif ',' in word:
        new_words = word.split(',')
        for w in new_words:
            w = fix_word(w)
            words.append(w)
    else:
        word = fix_word(word)
        words.append(word)
    return words

for file_name in IN_FILES:
    freq_dicts.append({})
    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f:
            sline = line.split(' ')
            for word in sline:
                words = get_words(word)
                for w in words:
                    if w == '':
                        continue
                    if w == 'l':
                        print (word)
                    try:
                        freq_dict[w] += 1
                    except KeyError:
                        freq_dict[w] = 1

                    try:
                        freq_dicts[-1][w] += 1
                    except KeyError:
                        freq_dicts[-1][w] = 1


def make_out_file(name, d):
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    total_count = 0
    for val in sorted_d:
        total_count += val[1]
    count = 1
    cur_sum = 0
    with open(name, 'w', encoding="utf-8") as f:
        for val in sorted_d:
            out0 = val[0]
            out1 = str(val[1])
            out2 = str((100*val[1]) / total_count)[:6] + '%'
            cur_sum += val[1]
            out3 = str((100*cur_sum) / total_count)[:6] + '%'
            out4 = str(count)
            count += 1
            f.write(out0 + (20-len(out0))*' ' + out1 + (8-len(out1))* ' ' + out2 + ' '*4 + out3 + ' '*4 + out4 + '\n')
            
def post_process(d):
    new_d = {}
    for key in d.keys():
        if key[-1] in ['s', 'e']:
            try:
                d[key[:-1]] += d[key]
            except Exception:
                pass
        if len(key) > 2 and key[-2:] in ['es']:
            try:
                d[key[:-2]] += d[key]
            except KeyError:
                pass
    for key in d.keys():
        if d[key] > 0:
            new_d[key] = d[key]
    return new_d
            
if DO_POST_PROCESSING:
    for x in range(len(freq_dicts)):
        freq_dicts[x] = post_process(freq_dicts[x])
    freq_dict = post_process(freq_dict)

count = 0
for file_name in IN_FILES:
    out_file_name = file_name[:-4] + "_freq" + ".txt"
    make_out_file(out_file_name, freq_dicts[count])
    count += 1

make_out_file(OUT_FILE, freq_dict)
