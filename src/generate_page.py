



def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('#'):
            return line[1:].strip()
        if line.startswith('# '):
            return line[2:].strip()
        else:
            raise ValueError("No title found in markdown")
        