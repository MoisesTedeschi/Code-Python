from translate import Translator
'''
pip install translate
'''


tradutor = Translator(from_lang='Portuguese', to_lang='English')
resultado = tradutor.translate(
    'Python é uma linguagem de programação de alto nível...')

print(resultado)
