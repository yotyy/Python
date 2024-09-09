inputpath=''
outputpath=''

def reverseinputpathoutputpath(inputpath, outputpath):
    with open(inputpath) as f:
        contents = f.read()

    with open(outputpath, 'x') as f:
        f.write(contents[::-1])
    
def copyinputpathoutputpath(inputpath, outputpath): 
    with open(inputpath) as f:
        contents = f.read()

    with open(outputpath, 'w') as f:
        f.write(contents)

def duplicatecontentsinputpath(inputpath, outputpath, n):
    with open(inputpath) as f:
        contents = f.read()

    with open(outputpath, 'w') as f:
        for i in range(n):
            f.write(contents)

def replacestringinputpathneedlenewstring(inputpath):
    with open(inputpath, 'r') as f:
        contents = f.read()

    replaced_contents = contents.replace('needle' , 'newstring')

    with open(inputpath, 'w') as f:
        f.write(replaced_contents)
    
