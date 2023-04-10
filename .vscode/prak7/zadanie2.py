commentators = set() 
def com_add():
    while True:
        comment = input() 
        if not comment: 
            break
        name, text = comment.split(':')  
        commentators.add(name.strip())
com_add()
print(f'Бірегей комментатор саны: {len(commentators)}')
