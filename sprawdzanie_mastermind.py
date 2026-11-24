def sprawdzenie(wejscie, kod):
    tys=wejscie//1000
    setki=(wejscie//100)%10
    dzies=(wejscie%100)//10
    jedno=wejscie%10
    flagi=""
    if (tys==kod//1000):
        flagi=flagi+"+"
    elif (kod.find(tys) != -1):
        flagi = flagi + "/"
    else:
        flagi=flagi+"-"
    if (setki==(kod//100)%10):
        flagi=flagi+"+"
    elif (kod.find(setki) != -1):
        flagi = flagi + "/"
    else:
        flagi=flagi+"-"
    if (dzies==((kod%100)//10)):
        flagi=flagi+"+"
    elif (kod.find(setki) != -1):
        flagi = flagi + "/"
    else:
        flagi=flagi+"-"
    if (jedno==(kod%10)):
        flagi=flagi+"+"
    elif (kod.find(setki) != -1):
        flagi = flagi + "/"
    else:
        flagi=flagi+"-"
    if (flagi=="++++"):
        return ("Zgadłeś sekretny kod")
    return flagi


    5789
    1290