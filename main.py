import requests, json
import matplotlib.pyplot as plt

def findbetween(source, startphrase, endphrase):
    resultstart = source.find(startphrase) + len(startphrase)
    resultend = source.find(endphrase)
    return source[resultstart:resultend]

def getlikes(link, before="like this video along with ", after=" other people"):
    if link.find("?") != -1:
        query = link + "&hl=en"
    else:
        query = link + "?hl=en"

    response = requests.get(query).text
    rawlikes = findbetween(response, before, after)
    numberlikes = ""
    for i in rawlikes:
        try:
            numberlikes += str(int(i))
        except ValueError:
            pass
    numberlikes = int(numberlikes)
    return numberlikes

def showgraph(linkslist):
    likeslist = []
    for i in linkslist:
        likeslist.append(getlikes(i))
    plt.plot(likeslist)

def main():
    args = sys.argv[1:]

    # Single video link
    if "-s" in args:
        print(getlikes(args[args.index("-s") + 1]))

    # List (one link per line)
    elif "-l" in args:  
        with open(args[args.index("-l") + 1]) as file:
            linkfile = file.read()

        entries = linkfile.split("\n")
        for i in entries:
            print(getlikes(i))
    else:
        print("Unexpected arguments!\nUsage:\npython3 main.py -s [LINK]\npython3 main.py -l [LINKS_FILE]")

if __name__ == "__main__":
    main()


