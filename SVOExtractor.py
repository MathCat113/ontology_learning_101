from openie import StanfordOpenIE
import pandas as pd
import os

print(os.environ)
properties = {
    'openie.affinity_probability_cap': 2 / 3,
}


path = "small_teddy.txt"
txt = open(path, 'r').read()
txt = ' '.join(txt.splitlines())


with StanfordOpenIE(properties=properties) as client:
    # print('Text: %s.' % text)
    # for triple in client.annotate(text):
    #     print('|-', triple)
    result = client.annotate(txt)
    df = pd.DataFrame.from_dict(result)
    df.to_excel('small_teddy_SVO.xlsx')
    print('Finished')

# with StanfordOpenIE(properties=properties) as client:
#     text = 'Barack Obama was born in Hawaii. Richard Manning wrote this sentence.'
#     print('Text: %s.' % text)
#     for triple in client.annotate(text):
#         print('|-', triple)

#     graph_image = 'graph.png'
#     client.generate_graphviz_graph(text, graph_image)
#     print('Graph generated: %s.' % graph_image)

#     with open('corpus/pg6130.txt', encoding='utf8') as r:
#         corpus = r.read().replace('\n', ' ').replace('\r', '')

#     triples_corpus = client.annotate(corpus[0:5000])
#     print('Corpus: %s [...].' % corpus[0:80])
#     print('Found %s triples in the corpus.' % len(triples_corpus))
#     for triple in triples_corpus[:3]:
#         print('|-', triple)
#     print('[...]')