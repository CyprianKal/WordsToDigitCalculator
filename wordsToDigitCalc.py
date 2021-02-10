#wybrane zdanie
sentence = "pomnóż przez siebie dwa i dwa"
def oblicz(sentence):
    from text2digits import text2digits
    from googletrans import Translator
    from infix import shift_infix as infix
    #tłumaczy podane zdanie
    translator = Translator()
    translated = translator.translate(sentence).text

    @infix
    def percent(a, b):
        return((a * b)/100)
    #zamienia przetłumaczone słowa opisujące liczby na liczby int
    t2d = text2digits.Text2Digits()
    converted = t2d.convert(translated)
    #zamienia słowa typu plus na operatory typu +
    def strToOperator(word):
        if word =="by" or word =="to" or word == "of" or word == "power" or word == "into" or word == "out" or word == "calculate" or word == "do" or word=="yourself" or word =="and" or word =="enbis" or word =="nbis":
            word = " "
        elif word == "times" or word == "multiply":
            word = "*"
        elif word == "minus":
            word = "-"
        elif word == "add" or word == "plus":
            word = "+"
        elif word =="divided" or word == "divide":
            word = "/"
        elif word == "the":
            word = "**"
        elif word=="percent":
            word = "<<percent>>"
        return(word)
    #rozdziela przekonwertowany wyraz converted na liste, i szuka w niej operatorów, jeśli je znajdzie to zamienia je na odpowiedni znak. Tworzy nową listę toBeGlued - z niej powstanie wyrażenie do obliczenia
    toBeGlued = []
    glue = " "
    splitted = str(converted).split()

    

    for word in splitted:
        try:
            operator = strToOperator(word)
            toBeGlued.append(operator)
        except:
            toBeGlued.append(word)
    #to skleja naszą listę toBeGlued w jednolite wyrażenie matematyczne
    
    for x in toBeGlued:
        if x == " ":
            toBeGlued.remove(x)
        else:
            pass

    if toBeGlued[0] == "+" or toBeGlued[0] == "*" or toBeGlued[0] == "/":
        test = toBeGlued[0]
        toBeGlued[0] = toBeGlued[1]
        toBeGlued[1] = test
    else:
        pass   
    joined = glue.join(toBeGlued)
    try:
        return(print(eval(str(joined)))) #ta linia printuje wynik jeżeli jest git
    except:
        #a ten kod poniżej jeśli jest błąd z procentami
        splitted = joined.split()
        new = []
        newest = []
        final = []
        glue2 = " "
        for word in splitted:
            try:
                converted = int(word)
                new.append(converted)
            except:
                new.append(word)
        for n, i in enumerate(new):
            if i == "<<percent>>":
                new[n-1] = new[n-1] * 0.01
                new[n] = " "
            else:
                pass 
        for x in new:
            try:
                y = str(x)
                newest.append(y)
            except:
                newest.append(x)
        joined = glue.join(newest)
        return(print(eval(joined)))

oblicz(sentence)





