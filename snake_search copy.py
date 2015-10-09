from bottle import *
from collections import OrderedDict
from operator import itemgetter

counter = 0
mainword=""
maintablestring=""
maindict=OrderedDict()

@route('/', method="GET")

def main():
    global counter
    counter = counter + 1
    print "This is counter:", counter
    
    print "You are now in main"

    global mainword #declaring word string
    global maintablestring
    global maindict #declaring ordered dictionary datastructure
    mainqueryresult = request.query['keywords'].lower() #requesting 'keywords' from HTML and making it lowercase
    mainquerylist = mainqueryresult.split(" ") #splitting queryresult by the spaces and reversing it
    
    for mainword in mainquerylist:
        if mainword not in maindict:
            maindict[mainword]=1
        else:
            maindict[mainword] +=1

    mainsearchstring = "Search for <i>\"{querystring}\" </i> ".format(querystring=request.query['keywords'])
    maintableheader = "<tr> <td> <b> Word </b> </td> <td> <b> Count </b> </td></tr>"
    maintablebeginning = "<table id = \"results\">"
    maintableend = "</table>"

    for k, v in maindict.iteritems():
        maintablestring = maintablestring + "<tr> <td> {queryword} </td> <td> {querycount} </td>".format(queryword=k, querycount=v)
    mainresultstring = mainsearchstring + maintablebeginning + maintableheader + maintablestring + maintableend

    return results()

def results():
    i=0
    global maindict
    word="" #declaring word string
    tablestring=""
    dict=OrderedDict() #declaring ordered dictionary datastructure
    newdict=OrderedDict()
    queryresult = request.query['keywords'].lower() #requesting 'keywords' from HTML and making it lowercase
    querylist = queryresult.split(" ")#splitting queryresult by the spaces and reversing it
    print querylist
    for word in querylist:
        if word in maindict:
            dict[word]=maindict[word]
        elif word not in dict:
            dict[word]=1
        else:
            dict[word] +=1
    print "this is results dict"
    print dict
    searchstring = "Search for <i>\"{querystring}\" </i> ".format(querystring=request.query['keywords'])
    tableheader = "<tr> <td> <b> Word </b> </td> <td> <b> Count </b> </td></tr>"
    tablebeginning = "<table id = \"results\">"
    tableend = "</table>"
    newdict = sorted(dict, key=dict.get, reverse=True) #returns new dict list of values...not dictionary
    newdict = newdict[:20]
    print "This is new dict:", newdict
    for newdictword in newdict:
        tablestring = tablestring + "<tr> <td> {queryword} </td> <td> {querycount} </td>".format(queryword=newdictword, querycount=dict[newdictword])
    resultstring = searchstring + tablebeginning + tableheader + tablestring + tableend
        #for k, v in dict.iteritems():
            #tablestring = tablestring + "<tr> <td> {queryword} </td> <td> {querycount} </td>".format(queryword=k, querycount=v)
        #resultstring = searchstring + tablebeginning + tableheader + tablestring + tableend
    return resultstring;

run(hosts='localhost', port=8080, debug=True)