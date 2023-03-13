commentators = set() 
while True:
    comment = input() 
    if not comment: 
        break
    name, text = comment.split(':')  
    commentators.add(name.strip())

print(f'Бірегей комментатор саны: {len(commentators)}')
