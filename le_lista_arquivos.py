import os, fnmatch

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(name)
    return result

arquivos_vmag = find('vmag_node*.csv', '../arquivos_csv/')

print(arquivos_vmag)