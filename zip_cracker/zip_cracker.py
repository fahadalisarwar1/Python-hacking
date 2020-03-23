import zipfile
import optparse
from threading import Thread


def extract_zip(zFile, passwd):

    try:
        
        zFile.extractall(pwd=bytes(passwd, "utf-8"))
        print("[+] Match Found : "+passwd)
    except:
        pass




if __name__ == "__main__":
    print("[+] Cracking zip using dictionary attack")

    # dictionary attack

    # brute forcing
     
    # hybrid attack

    parser = optparse.OptionParser("usage %prog -f <zipfile> -d <dictionary>")

    parser.add_option("-f", dest="zipname", type="string",help="Specify the zip file")

    parser.add_option("-d", dest="dname", type="string", help="Specify the dictionary file")

    (options, args) = parser.parse_args()

    if options.dname == None or options.zipname == None:
        print(parser.usage)
        exit(0)
    else:
        zname = options.zipname
        dname = options.dname


    zFile = zipfile.ZipFile(zname)

    passFile = open(dname, "r")

    for line in passFile.readlines():
        passwd = line.strip("\n")

        t = Thread(target=extract_zip, args=(zFile, passwd), )

        t.start()
    



