import re
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    new_id = re.sub(r'[^a-z0-9-_.]','',new_id)

    while '..' in new_id:
        new_id = new_id.replace('..','.')
    
    new_id = new_id.strip('.')

    if not new_id:
        new_id += 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id.rstrip('.')

    while len(new_id) <= 2:
        new_id += new_id[-1]
    
    return new_id