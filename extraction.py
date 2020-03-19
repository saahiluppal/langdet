import os

org_path = './europarl/txt'
des_path = './dataset'
print('Default writting directory:', des_path)

try:
    lst = os.listdir(org_path)
except:
    print("Dataset Not Found")
    print('Kindly Download Dataset First')
    print('http://www.statmt.org/europarl/')
    exit()

language = {
    'fi': 'finnish',
    'bg': 'bulgarian',
    'da': 'danish',
    'sk': 'slovak',
    'lt': 'lithuanian',
    'en': 'english',
    'sl': 'slovenian',
    'pl': 'polish',
    'lv': 'latvian',
    'pt': 'portuguese',
    'ro': 'romanian',
    'de': 'german',
    'es': 'spanish',
    'nl': 'dutch',
    'cs': 'czech',
    'sv': 'swedish',
    'et': 'estonian',
    'el': 'greek',
    'hu': 'hungarian',
    'it': 'italian',
    'fr': 'french'
}

default_char_length = 100_000
print('Warning: Default Char Length set on', default_char_length)

for code, lang in language.items():
    from_path = os.path.join(org_path, code)
    to_path = os.path.join(des_path, lang + '.txt')
    dirs = os.listdir(from_path)
    
    template = ''
    
    for file in dirs:
        path = os.path.join(from_path, file)
        with open(path) as handle:
            output = handle.read()
        template += output
        
        if len(template) >= default_char_length:
            break
    
    with open(to_path, 'w') as handle:
        handle.write(template)
    
    print('Written for', lang,':' ,len(template))
