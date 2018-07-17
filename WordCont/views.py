
from django.http import HttpResponse

from django.shortcuts import render

def temp(Re):
    
    return render(Re,"home.html",{"Req":str(Re)})

def cont(Re):
    orgwords=Re.GET["fulltext"]
    words=orgwords.lower()
    num=int()
    wordlist=words.split()
    num=len(wordlist)
    numword=dict()
    for w in wordlist:
        numword[w]=wordlist.count(w)

    worditem=[(v,k) for k,v in numword.items()]
    worditem.sort()
    worditem.reverse()
    

    
    return render(Re, "cont.html",{"fulltext":orgwords,"num":num,"numword":worditem})



def hh(Re):
    return HttpResponse("""
        <html>
    

        <body bgcolor="white" text="black" link="blue" vlink="green" lang="en">
        <p><a href="http://127.0.0.1:8000/">Home</a>
        <a href="http://127.0.0.1:8000/about/"> About</a>
        <a href="http://127.0.0.1:8000/temp/">Count Word</a></p>
        <hr>

        <h1>Welcome Visitor</h1>

        <blockquote>
        Do you know what is this?<br>
        This is my website.<br>
        Now <br>
        <i>Go FUCK Yourself</i></blockquote>

        <p>Thank you for visiting. please come back and enjoy yourself again.</p>""")

def homepage(Re):
    return HttpResponse("""
        <html>
      

        <body bgcolor="white" text="black" link="blue" vlink="green" lang="en">
        <p><a href="http://127.0.0.1:8000/">Home</a>
        <a href="http://127.0.0.1:8000/hh/"> Welcome visitor</a>
        <a href="http://127.0.0.1:8000/about/"> About</a>
        <a href="http://127.0.0.1:8000/temp/">Count Word</a></p>
        <hr>

        <h1>Welcome</h1>
        <p>Here we have a great advice for you to keep going<br>
        please visit the <b><h3>"welcome visitor"</h3></b> page for the advise<br>
        Thanks.</p>
        
        """)

def about(Re):
    return HttpResponse("""
        <html land="fa">
        <body bgcolor="white" text="black" link="blue" vlink="green" lang="en">
        <p><a href="http://127.0.0.1:8000/">Home</a>
        <a href="http://127.0.0.1:8000/temp/">Count Word</a></p>
        <hr>

        <h1>About</h1>
        <p>This is my first site<br>
        <h3>من حتی می تونم فارسی هم توش بنویسم!!!</h3></b>
        </body>
    
    """)