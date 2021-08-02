import spacy
from spacy.symbols import ORTH, NORM

# Get a guess where user want to fly

nlp = spacy.load('en_core_web_md')
special_case = [{ORTH: 'Frisco', NORM: 'San Francisco'}]
nlp.tokenizer.add_special_case(u'Frisco', special_case)
doc = nlp('I have flown to LA. Now I am fly to Frisco.')
for sent in doc.sents:
    if 'fly' in sent.lemma_:
        result = {}
        for token in sent:
            if token.dep_ == 'ROOT' and token.tag_ != 'VBN':
                result['travel_method'] = token.lemma_
            elif token.dep_ == 'pobj':
                result['target_city'] = token.norm_
        else:
            if '' in result.values():
                pass
            else:
                print(list(result.values()))
