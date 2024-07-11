def encode(text:str):
    import base64 as b
    text = str(b.b64encode(text.encode()))[2:-1]
    x = list(text)
    for i in range(len(x)):
        h = True
        if h and x[i]=="A":x[i]="JOOJOO";h=False
        elif h and x[i]=="a":x[i]="JOOJOo";h=False
        elif h and x[i]=="B":x[i]="JOOJoO";h=False
        elif h and x[i]=="b":x[i]="JOOJoo";h=False
        elif h and x[i]=="C":x[i]="JOOjOO";h=False
        elif h and x[i]=="c":x[i]="JOOjOo";h=False
        elif h and x[i]=="D":x[i]="JOOjoO";h=False
        elif h and x[i]=="d":x[i]="JOOjoo";h=False
        elif h and x[i]=="E":x[i]="JOoJOO";h=False
        elif h and x[i]=="e":x[i]="JOoJOo";h=False
        elif h and x[i]=="F":x[i]="JOoJoO";h=False
        elif h and x[i]=="f":x[i]="JOoJoo";h=False
        elif h and x[i]=="G":x[i]="JOojOO";h=False
        elif h and x[i]=="g":x[i]="JOojOo";h=False
        elif h and x[i]=="H":x[i]="JOojoO";h=False
        elif h and x[i]=="h":x[i]="JOojoo";h=False
        elif h and x[i]=="I":x[i]="JoOJOO";h=False
        elif h and x[i]=="i":x[i]="JoOJOo";h=False
        elif h and x[i]=="J":x[i]="JoOJoO";h=False
        elif h and x[i]=="j":x[i]="JoOJoo";h=False
        elif h and x[i]=="K":x[i]="JoOjOO";h=False
        elif h and x[i]=="k":x[i]="JoOjOo";h=False
        elif h and x[i]=="L":x[i]="JoOjoO";h=False
        elif h and x[i]=="l":x[i]="JoOjoo";h=False
        elif h and x[i]=="N":x[i]="JooJOO";h=False
        elif h and x[i]=="n":x[i]="JooJOo";h=False
        elif h and x[i]=="M":x[i]="JooJoO";h=False
        elif h and x[i]=="m":x[i]="JooJoo";h=False
        elif h and x[i]=="O":x[i]="JoojOO";h=False
        elif h and x[i]=="o":x[i]="JoojOo";h=False
        elif h and x[i]=="P":x[i]="JoojoO";h=False
        elif h and x[i]=="p":x[i]="Joojoo";h=False
        elif h and x[i]=="Q":x[i]="jOOJOO";h=False
        elif h and x[i]=="q":x[i]="jOOJOo";h=False
        elif h and x[i]=="R":x[i]="jOOJoO";h=False
        elif h and x[i]=="r":x[i]="jOOJoo";h=False
        elif h and x[i]=="S":x[i]="jOOjOO";h=False
        elif h and x[i]=="s":x[i]="jOOjOo";h=False
        elif h and x[i]=="T":x[i]="jOOjoO";h=False
        elif h and x[i]=="t":x[i]="jOOjoo";h=False
        elif h and x[i]=="U":x[i]="jOoJOO";h=False
        elif h and x[i]=="u":x[i]="jOoJOo";h=False
        elif h and x[i]=="V":x[i]="jOoJoO";h=False
        elif h and x[i]=="v":x[i]="jOoJoo";h=False
        elif h and x[i]=="W":x[i]="jOojOO";h=False
        elif h and x[i]=="w":x[i]="jOojOo";h=False
        elif h and x[i]=="X":x[i]="jOojoO";h=False
        elif h and x[i]=="x":x[i]="jOojoo";h=False
        elif h and x[i]=="Y":x[i]="joOJOO";h=False
        elif h and x[i]=="y":x[i]="joOJOo";h=False
        elif h and x[i]=="Z":x[i]="joOJoO";h=False
        elif h and x[i]=="z":x[i]="joOJoo";h=False
        elif h and x[i]=="0":x[i]="joOjOO";h=False
        elif h and x[i]=="1":x[i]="joOjOo";h=False
        elif h and x[i]=="2":x[i]="joOjoO";h=False
        elif h and x[i]=="3":x[i]="joOjoo";h=False
        elif h and x[i]=="4":x[i]="jooJOO";h=False
        elif h and x[i]=="5":x[i]="jooJOo";h=False
        elif h and x[i]=="6":x[i]="jooJoO";h=False
        elif h and x[i]=="7":x[i]="jooJoo";h=False
        elif h and x[i]=="8":x[i]="joojOO";h=False
        elif h and x[i]=="9":x[i]="joojOo";h=False
        elif h and x[i]=="=":x[i]="joojoO";h=False
        elif h and x[i]=="/":x[i]="joojoo";h=False
        elif h and x[i]=="+":x[i]="J00J00";h=False
    y = ''
    for i in x:
        y += i + ' '
    return y[:-1]
def decode(text:str):
    x = text.split(' ')
    if not 'joojoo' in text.lower():
        x = ['a']
    for i in range(len(x)):
        h = True
        if h and x[i]=="JOOJOO":x[i]="A";h=False
        elif h and x[i]=="JOOJOo":x[i]="a";h=False
        elif h and x[i]=="JOOJoO":x[i]="B";h=False
        elif h and x[i]=="JOOJoo":x[i]="b";h=False
        elif h and x[i]=="JOOjOO":x[i]="C";h=False
        elif h and x[i]=="JOOjOo":x[i]="c";h=False
        elif h and x[i]=="JOOjoO":x[i]="D";h=False
        elif h and x[i]=="JOOjoo":x[i]="d";h=False
        elif h and x[i]=="JOoJOO":x[i]="E";h=False
        elif h and x[i]=="JOoJOo":x[i]="e";h=False
        elif h and x[i]=="JOoJoO":x[i]="F";h=False
        elif h and x[i]=="JOoJoo":x[i]="f";h=False
        elif h and x[i]=="JOojOO":x[i]="G";h=False
        elif h and x[i]=="JOojOo":x[i]="g";h=False
        elif h and x[i]=="JOojoO":x[i]="H";h=False
        elif h and x[i]=="JOojoo":x[i]="h";h=False
        elif h and x[i]=="JoOJOO":x[i]="I";h=False
        elif h and x[i]=="JoOJOo":x[i]="i";h=False
        elif h and x[i]=="JoOJoO":x[i]="J";h=False
        elif h and x[i]=="JoOJoo":x[i]="j";h=False
        elif h and x[i]=="JoOjOO":x[i]="K";h=False
        elif h and x[i]=="JoOjOo":x[i]="k";h=False
        elif h and x[i]=="JoOjoO":x[i]="L";h=False
        elif h and x[i]=="JoOjoo":x[i]="l";h=False
        elif h and x[i]=="JooJOO":x[i]="N";h=False
        elif h and x[i]=="JooJOo":x[i]="n";h=False
        elif h and x[i]=="JooJoO":x[i]="M";h=False
        elif h and x[i]=="JooJoo":x[i]="m";h=False
        elif h and x[i]=="JoojOO":x[i]="O";h=False
        elif h and x[i]=="JoojOo":x[i]="o";h=False
        elif h and x[i]=="JoojoO":x[i]="P";h=False
        elif h and x[i]=="Joojoo":x[i]="p";h=False
        elif h and x[i]=="jOOJOO":x[i]="Q";h=False
        elif h and x[i]=="jOOJOo":x[i]="q";h=False
        elif h and x[i]=="jOOJoO":x[i]="R";h=False
        elif h and x[i]=="jOOJoo":x[i]="r";h=False
        elif h and x[i]=="jOOjOO":x[i]="S";h=False
        elif h and x[i]=="jOOjOo":x[i]="s";h=False
        elif h and x[i]=="jOOjoO":x[i]="T";h=False
        elif h and x[i]=="jOOjoo":x[i]="t";h=False
        elif h and x[i]=="jOoJOO":x[i]="U";h=False
        elif h and x[i]=="jOoJOo":x[i]="u";h=False
        elif h and x[i]=="jOoJoO":x[i]="V";h=False
        elif h and x[i]=="jOoJoo":x[i]="v";h=False
        elif h and x[i]=="jOojOO":x[i]="W";h=False
        elif h and x[i]=="jOojOo":x[i]="w";h=False
        elif h and x[i]=="jOojoO":x[i]="X";h=False
        elif h and x[i]=="jOojoo":x[i]="x";h=False
        elif h and x[i]=="joOJOO":x[i]="Y";h=False
        elif h and x[i]=="joOJOo":x[i]="y";h=False
        elif h and x[i]=="joOJoO":x[i]="Z";h=False
        elif h and x[i]=="joOJoo":x[i]="z";h=False
        elif h and x[i]=="joOjOO":x[i]="0";h=False
        elif h and x[i]=="joOjOo":x[i]="1";h=False
        elif h and x[i]=="joOjoO":x[i]="2";h=False
        elif h and x[i]=="joOjoo":x[i]="3";h=False
        elif h and x[i]=="jooJOO":x[i]="4";h=False
        elif h and x[i]=="jooJOo":x[i]="5";h=False
        elif h and x[i]=="jooJoO":x[i]="6";h=False
        elif h and x[i]=="jooJoo":x[i]="7";h=False
        elif h and x[i]=="joojOO":x[i]="8";h=False
        elif h and x[i]=="joojOo":x[i]="9";h=False
        elif h and x[i]=="joojoO":x[i]="=";h=False
        elif h and x[i]=="joojoo":x[i]="/";h=False
        elif h and x[i]=="J00J00":x[i]="+";h=False
    y = ''
    for i in x:
        y += i
    import base64 as b
    try: a = str(b.b64decode(y))[2:-1]
    except: a = None;print(f'Error in decode text : {text}')
    return a