#Stuti Rana ID:85039361
#Kennedy Klimek ID:69696915


import os
from pathlib import Path
import shutil


def readFiles() -> (Path, [Path]):
    #reads the path name where the files the user wants are
    i = input()
    while (len(i) < 3)\
        or (i[1] != ' ')\
        or (i[2] == ' ')\
        or ((i[0].upper() != 'D' or Path(i[2::]).is_absolute() == False or Path(i[2::]).is_dir() == False)\
        and (i[0].upper() != 'R' or Path(i[2::]).is_absolute() == False or Path(i[2::]).is_dir() == False)):
        print("ERROR")
        i = input()
    iPath= Path(i[2::])
    flist = []
    if (i[0].upper() == 'D'):
        #passes an empty list to fill
        flist = printFiles(iPath, flist)
    elif (i[0].upper() == 'R'):
        #passes an empty list to fill
        flist = printSub(iPath, flist)
    return flist

def printFiles(dirc: Path, flist: [Path]) -> [Path]:
    #prints files in directory
    sortedList = []
    try:
        for fname in dirc.iterdir():
            if fname.is_file():
                if 'MATLAB' not in fname:
                    sortedList.append(str(fname))
    except (PermissionError, OSError):
        pass
    sortedList.sort()
    for item in sortedList:
        flist.append(Path(item))
        print(item)
    return flist

def printSub(dirc: Path, flist: [Path]) -> [Path]:
    #prints files in subdirectories
    sortedList = []
    try:
        if dirc.is_dir():
            for fname in dirc.iterdir():
                if fname.is_file():
                    if 'MATLAB' not in str(fname):
                        sortedList.append(str(fname))
        sortedList.sort()
        for item in sortedList:
            flist.append(Path(item))
            print(item)
        for fname in dirc.iterdir():
            if fname.is_dir():
                printSub(fname, flist)
    except (PermissionError, OSError):
        pass
    return flist

def fileEnd(fileOfInt: [Path], sInfo: str, sfile: []) -> [Path]:
    #finds files that end with a given input
    for x in fileOfInt:
            if x.exists():
                y = str(x)
                if y.endswith(sInfo):
                    print(y)
                    sfile.append(x)
    return sfile
    
def fileExtension(fileOfInt: [Path], sInfo: str, sfile: []) -> [Path]:
    #finds files that have a given extension
    if '.' not in sInfo:
        sInfo = '.' + sInfo
    for x in fileOfInt:
        if x.exists():
            i = str(x).rfind('.')
            if sInfo == str(x)[i::]:
                print(x)
                sfile.append(x)
    return sfile

def fileText(fileOfInt: [Path], sInfo: str, sfile: []) -> [Path]:
    #finds file if given text is in the file
    for x in fileOfInt:
        if x.exists():
            file = None
            try:
                file = open(x, 'r')
                found = (sInfo in file.read())
                if found:
                    print(x)
                    sfile.append(x)
            except (UnicodeDecodeError, PermissionError,OSError):
                pass
            finally:
                if file != None:
                    file.close()
    return sfile

def fileLess(fileOfInt: [Path], sInfo: str, sfile: []) -> [Path]:
    #finds files less than a given number of bytes
    if sInfo.isdigit():
            for pname in fileOfInt:
                if pname.exists():
                    if os.path.getsize(pname) < int(sInfo):
                        print(pname)
                        sfile.append(pname)
    return sfile

def fileGreater(fileOfInt: [Path], sInfo: str, sfile: []) -> [Path]:
    #finds files more than a given number of bytes
    if sInfo.isdigit():
        for pname in fileOfInt:
            if pname.exists():
                if os.path.getsize(pname) > int(sInfo):
                    print(pname)
                    sfile.append(pname)
    return sfile

def sortFiles(fileOfInt: [Path]) -> [Path]:
    #acts on the files of interest
    s = input()
    sfile = []
    while (s == '')\
        or ((s.upper() != 'A')\
        and (s[0].upper() != 'N' or len(s) < 3 or s[1] != ' ')\
        and (s[0].upper() != 'E' or len(s) < 3 or s[1] != ' ')\
        and (s[0].upper() != 'T' or len(s) < 3 or s[1] != ' ')\
        and (s[0] != '<' or len(s) < 3 or s[1] != ' ' or (s[2].isdigit() == False))\
        and (s[0] != '>' or len(s) < 3 or s[1] != ' ' or (s[2].isdigit() == False))):
        print("ERROR")
        s = input()
    sInfo = s[2::]
    if (s[0].upper() == "A"):
        #prints all of the interesting files
        for x in fileOfInt:
            if x.exists():
                print(x)
                sfile.append(x)
    elif (s[0].upper() == "N"):
        sfile = fileEnd(fileOfInt, sInfo, sfile)
    elif (s[0].upper() == "E"):
        sfile = fileExtension(fileOfInt, sInfo, sfile)
    elif (s[0].upper() == "T"):
        sfile = fileText(fileOfInt, sInfo, sfile)
    elif (s[0] == "<"):
        sfile = fileLess(fileOfInt, sInfo, sfile)
    elif (s[0] == ">"):
        sfile = fileGreater(fileOfInt, sInfo, sfile)
    return sfile

def filePrintline(slist: [Path]) -> None:
    #prints the first line of each file
    for x in slist:
            if x.exists():
                a = None
                try:
                    a = open(x, 'r')
                    firstLine = a.readline()
                    if "\n" in firstLine:
                        print(firstLine, end='')
                    else:
                        print(firstLine)
                except (UnicodeDecodeError, PermissionError, OSError):
                    print("NOT TEXT")
                finally:
                    if a != None:
                        a.close()

def fileDup(slist: [Path]) -> None:
    #duplicates each file
    for x in slist:
            if x.exists():
                cop = str(x) + '.dup'
                shutil.copy(x, cop)
                print(x)
                print(cop)

def fileTouch(slist: [Path]) -> None:
    #touches each file
    for x in slist:
            if x.exists():
                try:
                    x.touch(exist_ok = True)
                except PermissionError:
                    pass

def changeFile(slist: [Path]) -> None:
    #acts on the files of interest
    if len(slist) == 0:
        return
    c = input()
    while (len(c) != 1) or ((c.upper() != 'F') and (c.upper() != 'D') and (c.upper() != 'T')):
        print("ERROR")
        c = input()
    if (c.upper() == 'F'):
        filePrintline(slist)
    elif (c.upper() == 'D'):
        fileDup(slist)
    elif (c.upper() == 'T'):
        fileTouch(slist)
    
if __name__ == '__main__':
    changeFile(sortFiles(readFiles()))

