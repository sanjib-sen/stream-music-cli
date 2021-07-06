
def get_list(query):
    queries=""
    if ',' in query:
        queries = query.split(',')
    elif 'plus' in query:
        queries = query.split('plus')
    elif '+' in query:
        queries = query.split('+')
    elif 'then' in query:
        queries = query.split('then')
    elif 'than' in query:
        queries = query.split('than')
    elif 'den' in query:
        queries = query.split('den')    
    else:
        queries = [query]
    
    return queries