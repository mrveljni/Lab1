from bottle import *
from collections import OrderedDict

@route('/', method="GET")

def main():
    print "You are now in main"
    word="" #declaring word string
    tablestring=""
    dict=OrderedDict() #declaring ordered dictionary datastructure
    queryresult = request.query['keywords'].lower() #requesting 'keywords' from HTML and making it lowercase
    querylist = queryresult.split(" ")#splitting queryresult by the spaces and reversing it
    print querylist
    
    for word in querylist:
        if word not in dict:
            dict[word]=1
        else:
            dict[word] +=1

    print "this is main dict:"
    print dict
    searchstring = "Search for <i>\"{querystring}\" </i> ".format(querystring=request.query['keywords'])
    tableheader = "<tr> <td> <b> Word </b> </td> <td> <b> Count </b> </td></tr>"
    tablebeginning = "<table id = \"results\">"
    tableend = "</table>"
    
    for k, v in dict.iteritems():
        print "entered the iteration for loop"
        tablestring = tablestring + "<tr> <td> {queryword} </td> <td> {querycount} </td>".format(queryword=k, querycount=v)
    resultstring = searchstring + tablebeginning + tableheader + tablestring + tableend

    results()
#return resultstring

if __name__ == "__main__":
    main()



def results():
    print "You are now in results"
    word="" #declaring word string
    tablestring=""
    dict=OrderedDict() #declaring ordered dictionary datastructure
    queryresult = request.query['keywords'].lower() #requesting 'keywords' from HTML and making it lowercase
    querylist = queryresult.split(" ")#splitting queryresult by the spaces and reversing it
    print querylist
    
    for word in querylist:
        if word not in dict:
            dict[word]=1
        else:
            dict[word] +=1

    print "this is results dict"
    print dict
    searchstring = "Search for <i>\"{querystring}\" </i> ".format(querystring=request.query['keywords'])
    tableheader = "<tr> <td> <b> Word </b> </td> <td> <b> Count </b> </td></tr>"
    tablebeginning = "<table id = \"results\">"
    tableend = "</table>"
    
    for k, v in dict.iteritems():
        print "entered the iteration for loop"
        tablestring = tablestring + "<tr> <td> {queryword} </td> <td> {querycount} </td>".format(queryword=k, querycount=v)
    resultstring = searchstring + tablebeginning + tableheader + tablestring + tableend


run(hosts='localhost', port=8080, debug=True)