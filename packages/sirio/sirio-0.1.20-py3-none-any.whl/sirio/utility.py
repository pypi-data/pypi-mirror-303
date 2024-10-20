def existsJsonPath(document, paths: list):
    esiste = True
    subDocument = document
    for sub in paths:
        if sub in subDocument:
            subDocument = subDocument[sub]
        else:
            esiste = False
            break
    return esiste