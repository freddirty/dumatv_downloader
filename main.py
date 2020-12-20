import configparser
import logging
import urllib.request

def loadini():
    config = configparser.ConfigParser()
    config.read('url.ini')
    global raw_url
    global num
    global logfilename
    raw_url = config['default']['url']
    num = config['default']['num']
    logfilename = config['default']['log']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

raw_url = ''
num = ''
temp_url = ''
loadini()
logging.basicConfig(filename=logfilename, encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')
# segment_error_array: str = "0" * int(num)  # gives n times "0" - init all segment as OK
print("raw url: " + raw_url)
print("hany segment kell: " + num)
# here comes the url magic
segment_start = raw_url.find("segment")
segment_mp4 = raw_url.find(".mp4")
# print("hol kezdodik a segment: "+segment_start)
print("url eleje: " + raw_url[0:segment_start + 7])
print("url vege:" + raw_url[segment_start + 8:len(raw_url)])
index_of_slash = raw_url.rfind("/", 0, segment_mp4)
filenev = raw_url[index_of_slash + 1:segment_mp4 + 4]
print("filenev: " + filenev)
print("Letoltes indul:")
# loop to download files one by one
for i in range(int(num)):
    temp_url = raw_url[0:segment_start + 7] + str(i) + raw_url[segment_start + 8:len(raw_url)]
    try:
        #        print(temp_url, "d:\\temp\\" + filenev + "." + str(i).rjust(5, '0') + ".ts")
        urllib.request.urlretrieve(temp_url, "d:\\temp\\" + filenev + "." + str(i).rjust(5, '0') + ".ts")
        if i % 160 == 0:
            print(bcolors.OKGREEN + "G" + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + "G" + bcolors.ENDC, end='')
    except Exception as e:
        logging.error("Hiba a letoltesben a " + str(i) + " szegmensben")
        logging.error("Letoltendo file: " + temp_url)
        logging.critical(e, exc_info=True)  # log exception info at CRITICAL log level
        print(bcolors.FAIL + "E" + bcolors.ENDC, end='')
        pass
print(" ")
print("letoltes vege")