import spacy
nlp = spacy.load("zh_core_web_sm")
#import zh_core_web_sm
#nlp = zh_core_web_sm.load()

#doc = nlp("这是一个用于示例的句子。")
#print([(w.text, w.pos_) for w in doc])

text = '''

2024年3月21日，我队接到上级部门下发线索：犯罪分子利用黑客技术手段在洪洞县顺祥房地产有限公司的财务电脑上面植入监控软件，进行“精准投毒”，窃取公司财务和人员信息，进行冒充公司老板实施精准诈骗。我队接到线索立即出警，开展调查。
'''
doc=nlp(text)
people_names=[]
for ent in doc.ents:
    if ent.label_=="PERSON":
        people_names.append(ent.text)

for name in people_names:
    print(name)


