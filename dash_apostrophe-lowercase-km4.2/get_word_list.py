import os
import json
import collections
import re

src_path = r'path/to/untokenised/json/corpus/files'

print('getting counts')
token_freqs = collections.Counter()
for folder in os.listdir(src_path):
    for fname in os.listdir(os.path.join(src_path, folder)):
        if not fname.endswith('.json'):
            continue
        print(' ', fname)
        with open(os.path.join(src_path, folder, fname), 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict):
            data = [data]
        assert isinstance(data, list)
        for doc in data:
            assert isinstance(doc, dict)
            for line in doc['text']:
                assert isinstance(line, str)
                for token in re.finditer('[-a-zċġħżàòìèù\']+', line.lower().strip()):
                    token_freqs.update([token.group(0)])

print('outputting')
with open('auto_word_list.txt', 'w', encoding='utf-8') as f:
    for (token, freq) in token_freqs.most_common():
        print(token, file=f)
