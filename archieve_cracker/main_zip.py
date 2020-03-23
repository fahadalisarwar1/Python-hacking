import optparse
import zipfile
from threading import Thread


def extract_zip(zFile, password):
    """[summary]
    
    Arguments:
        zFile string -- zippef file 
        password {[type]} -- [description]
    """    
    match = False
    try:
        zFile.extractall(pwd=bytes(password, "utf-8"))
        print(password)
        print("[+] Password found : ", password)
        match = True
    except:
        
        pass
    


if __name__ == "__main__":
    print("[+] Cracking ZIP")
    parser = optparse.OptionParser("usuage %prog "+\
            "-f <zip-file> -d <dictionary>")
    parser.add_option("-f", dest="zname", type="string", help="specify zip file")

    parser.add_option("-d", dest="dname", type="string", help="specify dictionary file")

    (options, args) = parser.parse_args()

    if options.zname == None or options.dname == None:
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    
    zFile = zipfile.ZipFile(zname)

    passFile = open(dname, "r")
    for line in passFile.readlines(1000):
        passwd = line.strip("\n")
        
        t = Thread(target=extract_zip, args=(zFile, passwd))
        t.start()