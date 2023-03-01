from flask import Flask,render_template,request 
import re
app=Flask(__name__)
CV_NV=[]
NUQTA = '਼'
HALANT = '੍'
ADDAK = 'ੱ'
CV_NonV=[]
con = {
        'ਕ': 'k', 'ਖ': 'kh', 'ਗ': 'g', 'ਘ': 'gh',
        'ਚ': 'c', 'ਛ': 'ch', 'ਜ': 'j', 'ਝ': 'jh', 'ਞ': '?',
        'ਟ': 'tt', 'ਠ': 'tth', 'ਡ': 'dd', 'ਢ': 'ddh', 'ਣ': 'nn',
        'ਤ': 't', 'ਥ': 'th', 'ਦ': 'd', 'ਧ': 'dh', 'ਨ': 'n',
        'ਪ': 'p', 'ਫ': 'ph', 'ਬ': 'b', 'ਭ': 'bh', 'ਮ': 'm',
        'ਯ': 'y', 'ਰ': 'r', 'ਲ': 'l', 'ਵ': 'v',
        'ਸ': 's', 'ਸ਼': 'sh',
        'ਹ': 'h','ਖ਼': 'x', 'ਗ਼': 'Gh', 'ਜ਼': 'z', 'ਡ਼': 'rr1', 'ਡ਼੍ਹ': 'rrh', 'ਫ਼': 'f', 'ਲ਼': 'll',
        'ੜ': 'rr', 'ੜ੍ਹ': 'rrh'
    }

vow = {
        'ਅ': 'a', 'ਆ': 'aa',
        'ਇ': 'i', 'ਈ': 'ii',
        'ਉ': 'u', 'ਊ': 'uu',
        'ਏ': 'e', 'ਐ': 'E',
        'ਓ': 'o', 'ਔ': 'O',
        'ੰ': 'ng', 'ਂ': 'ng1'
    }
matra = {
        'ਾ': 'aa',
        'ਿ': 'i', 'ੀ': 'ii',
        'ੁ': 'u', 'ੂ': 'uu',
        'ੇ': 'e', 'ੈ': 'E',
        'ੋ': 'o', 'ੌ': 'O'
    }
nuqta = {
        'k': 'q', 'kh': 'x', 'g': 'Gh', 'ph': 'f', 'j': 'z', 'jh': 'Zh',
        'dd': 'rr', 'ddh': 'rrh'
    }


def transliterate(word):
        global res
        res = []
        if word.strip() in CV_NonV or word in CV_NV :
            return True  
        else:
            for char in word:
                if char == HALANT:
                    res.pop()
                elif char in con:
                    res.append(con[char])
                    res.append('a')
                elif char in vow:
                    res.append(vow[char])
                elif char in matra:
                    res.pop()
                    res.append(matra[char])
                elif char == NUQTA:
                    l = res.pop()
                    res.append(nuqta.get(l, l))
        return False
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/phonemes' ,methods=['POST','GET'])
def phonemes():
    word=request.form['any_text']
    Consonants=['ਕ','ਖ','ਗ','ਘ','ਙ','ਚ','ਛ','ਜ','ਝ','ਞ','ਟ','ਠ','ਡ','ਢ','ਣ','ਤ','ਥ','ਦ','ਧ','ਨ','ਪ','ਫ','ਬ','ਭ','ਮ','ਯ','ਰ','ਲ','ਲ਼','ਵ','ਸ਼','ਸ','ਹ','ਖ਼','ਗ਼','ਜ਼','ੜ','ਫ਼']
    NonV=['ਇ','ਈ','ਏ','ਐ','ਅ','ਆ','ਔ','ਉ','ਊ','ਓ']
    NV=['ਇੰ','ਈਂ','ਅੰ','ਆਂ','ਔਂ','ਉਂ','ਊਂ','ਓਂਂ','ਏਂ','ਐਂ']
    # list of combination of consonants with non-nasalized vowels

    for i in Consonants:
        for j in NonV:
            CV_NonV.append(i+j)

    # list of combination of consonants with nasalized vowels

    for i in Consonants:
        for j in NV:
            CV_NV.append(i+j)
        
    # print(CV_NonV)
   
    b = transliterate(word)
    
    if b:
        return render_template('index.html', result=word)
    c = {
        'ਕ': 'k', 'ਖ': 'kh', 'ਗ': 'g', 'ਘ': 'gh', 'ਂ': 'ng1', 'ੰ': 'ng',
        'ਚ': 'c', 'ਛ': 'ch', 'ਜ': 'j', 'ਝ': 'jh', 'ਞ': '?',
        'ਟ': 'tt', 'ਠ': 'tth', 'ਡ': 'dd', 'ਢ': 'ddh', 'ਣ': 'nn',
        'ਤ': 't', 'ਥ': 'th', 'ਦ': 'd', 'ਧ': 'dh', 'ਨ': 'n',
        'ਪ': 'p', 'ਫ': 'ph', 'ਬ': 'b', 'ਭ': 'bh', 'ਮ': 'm',
        'ਯ': 'y', 'ਰ': 'r', 'ਲ': 'l', 'ਵ': 'v',
        'ਸ': 's', 'ਸ਼': 'sh',
        'ਹ': 'h',

        'ਖ਼': 'x', 'ਗ਼': 'Gh', 'ਜ਼': 'z', 'ਡ਼': 'rr1', 'ਡ਼੍ਹ': 'rrh', 'ਫ਼': 'f', 'ਲ਼': 'll',
        'ੜ': 'rr', 'ੜ੍ਹ': 'rrh','ਅ': 'a', 'ਆ': 'aa',
        'ਇ': 'i', 'ਈ': 'ii',
        'ਉ': 'u', 'ਊ': 'uu',
        'ਏ': 'e', 'ਐ': 'E',
        'ਓ': 'o', 'ਔ': 'O'
        }   
    global ph
    ph=[]
    for i in res:
        for key,value in c.items():
            if value==i:
                ph.append(key)

    i = 0
    while i < len(ph) - 1:
        
        if ph[i] == 'ਓ' and ph[i+1] == 'ਂ':
            ph[i:i+2] =['ਓਂਂ']  # replace 'ਓ' and 'ਂ' with 'ਓਂਂ'
            
        elif ph[i] == 'ਆ' and ph[i+1] == 'ਂ':
            # Replace both elements with 'ਆਂ'
            ph[i:i+2] = ['ਆਂ']
            
        elif ph[i] == 'ਇ' and ph[i+1] == 'ੰ':
            ph[i:i+2] = ['ਇੰ']
            
        elif ph[i] == 'ਈ' and ph[i+1] == 'ਂ':
            ph[i:i+2] = ['ਈਂ']
            
        elif ph[i] == 'ਔ' and ph[i+1] == 'ਂ':
            ph[i:i+2] = ['ਔਂ']
            
        elif ph[i] == 'ਐ' and ph[i+1] == 'ਂ':
            ph[i:i+2] = ['ਐਂ']
            
        elif ph[i] == 'ਉ' and (ph[i+1] == 'ਂ' or ph[i+1] == 'ੰ'):
            ph[i:i+2] = ['ਉ']
            
        elif ph[i] == 'ਊ' and (ph[i+1] == 'ਂ' or ph[i+1] == 'ੰ'):
            ph[i:i+2] = ['ਊਂ']
            
        elif ph[i] == 'ਏ' and ph[i+1] == 'ਂ':
            ph[i:i+2] = ['ਏਂ']
            
        elif ph[i] == 'ਅ' and ph[i+1] == 'ੰ':
            ph[i:i+2] = ['ਅੰ']
            
        i += 1


    for i in range(len(ph) - 1):
        if ph[i] in Consonants and ph[i+1] in Consonants:
            ph.insert(i+1, 'ਅ')

    result = []
    for i, elem in enumerate(ph):
        if ph[i] in Consonants and (ph[i+1] in NonV or ph[i+1] in NV):
            a=ph[i]+ph[i+1]
            result.append(a)
            ph.pop(i)
        else:
            result.append(elem)                            
    word=request.form['any_text']

#---------------------------------------------IPA---------------------------------------------------------
    ipa="".join(result)
    
    if len(ipa) >= 2 and ipa[-2] in Consonants and ipa[-1] == 'ਅ':
          ipa = ipa[:-1]
    else:
        pass
       #ipa="".join(result)
        
    def ipa_creation(word):
        word = re.sub(r"ਫ਼", "f", word)
        word = re.sub(r"ਕ਼", "q", word)
        word = re.sub(r"ਸ਼", "ʃ", word)
        word = re.sub(r"ਖ਼", "x", word)
        word = re.sub(r"ਗ਼", "ɣ", word)
        word = re.sub(r"ਜ਼", "z", word)
        word = re.sub(r"ਪਾ", "ɑː", word)
        word = re.sub(r"ਪੇ", "eː", word)
        word = re.sub(r"ਪੈ", "ɛː", word)
        word = re.sub(r"ਪੀ", "iː", word)
        word = re.sub(r"ਪਿ", "ɪ", word)
        word = re.sub(r"ਪੋ", "oː", word)
        word = re.sub(r"ਪੌ", "ɔː", word)
        word = re.sub(r"ਪੂ", "uː", word)
        word = re.sub(r"ਪੁ", "ʊ", word)
        word = re.sub(r"੍ਰ", "ʳ", word)
        word = re.sub(r"੍ਹ", "ʰ", word)
        word = re.sub(r"ਬ", "b", word)
        word = re.sub(r"ਭ", "bʰ", word)
        word = re.sub(r"ਦ", "d", word)
        word = re.sub(r"ਧ", "dʰ", word)
        word = re.sub(r"ਡ", "ɖ", word)
        word = re.sub(r"ਢ", "ɖʰ", word)
        word = re.sub(r"ਜ", "j", word)
        word = re.sub(r"ਝ", "jʰ", word)
        word = re.sub(r"ਗ", "ɡ", word)
        word = re.sub(r"ਘ", "gʰ", word)
        word = re.sub(r"ਹ", "h", word)
        word = re.sub(r"ਯ", "y", word)
        word = re.sub(r"ਕ", "k", word)
        word = re.sub(r"ਖ", "kʰ", word)
        word = re.sub(r"ਲ", "l", word)
        word = re.sub(r"ਮ", "m", word)
        word = re.sub(r"ਨ", "n", word)
        word = re.sub(r"ਣ", "ɳ", word)
        word = re.sub(r"ं", "ŋ", word)
        word = re.sub(r"ਂ", "ŋ", word)
        word = re.sub(r"ਪ", "p", word)
        word = re.sub(r"ਫ", "pʰ", word)
        word = re.sub(r"ਰ", "r", word)
        word = re.sub(r"ੜ", "ɽ", word)
        word = re.sub(r"ੜ੍ਹ", "ɽʱ", word)
        word = re.sub(r"ਸ", "s", word)
        word = re.sub(r"ਤ", "t", word)
        word = re.sub(r"ਥ", "tʰ", word)
        word = re.sub(r"ਟ", "ʈ", word)
        word = re.sub(r"ਠ", "ʈʰ", word)
        word = re.sub(r"ਚ", "c", word)
        word = re.sub(r"ਛ", "cʰ", word)
        word = re.sub(r"ਵ", "v", word)
        word = re.sub(r"ਆ", "ɑː", word)
        word = re.sub(r"ਏ", "eː", word)
        word = re.sub(r"ਐ", "ɛː", word)
        word = re.sub(r"ਅ", "ə", word)
        word = re.sub(r"ਈ", "iː", word)
        word = re.sub(r"ਇ", "ɪ", word)
        word = re.sub(r"ਓ", "oː", word)
        word = re.sub(r"ਔ", "ɔː", word)
        word = re.sub(r"ਊ", "uː", word)
        word = re.sub(r"ਉ", "ʊ", word)
        word = re.sub(r"ੰ", " ̃", word)
        word = re.sub(r"ਿ", "ɪ", word)
        word = re.sub(r"ੀ", "iː", word)
        word = re.sub(r"ੇ", "eː", word)
        word = re.sub(r"ੈ", "ɛː", word)
        word = re.sub(r"ੋ", "oː", word)
        word = re.sub(r"ੌ", "ɔː", word)
        word = re.sub(r"ਾ", "ɑː", word)
        word = re.sub(r"ੁ", "ʊ", word)
        word = re.sub(r"ੂ", "uː", word)
        word = re.sub(r"ੱ", "a", word)
        return word
        
    w=ipa_creation(ipa)
#----------------------------------------------English--------------------------------------------------------------------------

    eng_ph="".join(res)
    eng_ph = ''.join([i for i in eng_ph if not i.isdigit()])
    for k,v in con.items():
        if eng_ph[-2] in v and eng_ph[-1]=='a':
            eng_ph=eng_ph[:-1]
          
    return render_template('index.html',result=" ".join(result),result1=w,result2=eng_ph)
   


if __name__=="__main__":
    app.run(debug=True)


