def splitmodel(x: str) -> tuple[str, str]:
    if ':' not in x:
        return x, ''
    
    model, specs = x.split(':')
    return model, specs

def modelname(x: str) -> str:
    return splitmodel(x)[0]

def modelspecs(x: str) -> str:
    return splitmodel(x)[1]