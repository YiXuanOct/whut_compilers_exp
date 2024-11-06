testfile=open("testfile.txt","r",encoding="utf-8")
output=open("output.txt","w",encoding="utf-8")
token={
    "const":"CONSTTK",
    "int":"INTTK",
    "char":"CHARTK",
    "void":"VOIDTK",
    "main":"MAINTK",
    "if":"IFTK",
    "else":"ELSETK",
    "do":"DOTK",
    "while":"WHILETK",
    "for":"FORTK",
    "scanf":"SCANFTK",
    "printf":"PRINTFTK",
    "return":"RETURNTK",
    "+":"PLUS",
    "-":"MINU",
    "*":"MULT",
    "/":"DIV",
    "<":"LSS",
    "<=":"LEQ",
    ">":"GRE",
    ">=":"GEQ",
    "==":"EQL",
    "!=":"NEQ",
    "=":"ASSIGN",
    ";":"SEMICN",
    ",":"COMMA",
    "(":"LPARENT",
    ")":"RPARENT",
    "[":"LBRACK",
    "]":"RBRACK",
    "{":"LBRACE",
    "}":"RBRACE",
}
p=r"((\'|\")?[\w\s]+(\'|\")?|\+|\-|\*|/|<|<=|>|>=|==|!=|=|;|,|\(|\)|\[|\]|\{|\})"

for line in testfile:
    p=0
    while p<len(line):
        if line[p].isalpha() or line[p]=='_':
            word=""
            while line[p].isalpha() or line[p].isdigit() or line[p]=="_":
                word+=line[p]
                p+=1
            if word in token:
                output.write(token[word]+' '+word+'\n')
            else:
                output.write("IDENFR "+word+'\n')
        elif line[p].isdigit():
            word = ""
            while line[p].isdigit():
                word += line[p]
                p += 1
            output.write("INTCON "+word+'\n')
        elif line[p]=='"':
            word=""
            p+=1
            while line[p]!='"':
                word += line[p]
                p+=1
            p+=1
            output.write("STRCON "+word+'\n')
        elif line[p]=="'":
            word=""
            p+=1
            while line[p]!="'":
                word += line[p]
                p+=1
            p+=1
            output.write("CHARCON "+word+'\n')
        elif line[p] in ['<','>','=','!'] and line[p+1]=='=':
            word=line[p]+line[p+1]
            output.write(token[word] + ' ' + word + '\n')
            p+=2
        elif line[p] in token:
            output.write(token[line[p]]+' '+line[p]+'\n')
            p+=1
        else:
            p+=1
