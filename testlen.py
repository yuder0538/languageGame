import re
from pathlib import Path
for fn in ['german-listen-quiz.html', 'japanese-listen-quiz.html']:
    txt = Path(fn).read_text(encoding='utf-8')
    arr = re.search(r'const questions = \[([\s\S]*?)\];', txt)
    print('---', fn)
    if not arr:
        continue
    data = arr.group(1)
    qlines = re.findall(r'\{\s*text:\s*([\'\"])(.+?)\1,\s*choices:\s*\[(.+?)\],\s*answer:\s*(\d)\s*\}', data, re.S)
    for i, (quote, text, choices, ans) in enumerate(qlines, 1):
        choices_list = re.findall(r'([\'\"])(.+?)\1', choices)
        choices_list = [c for _, c in choices_list]
        print(i, len(text), [len(c) for c in choices_list], choices_list)
