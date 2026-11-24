def sprawdzenie(wejscie, kod):
    tys=wejscie//1000
    setki=(wejscie//100)%10
    dzies=(wejscie%100)//10
    jedno=wejscie%10
    flagi=""
    if (tys==kod//1000):
        flagi=flagi+"+"
        tys=10
    if (setki==(kod//100)%10):
        flagi=flagi+"+"
        setki=10
    if (dzies==((kod%100)//10)):
        flagi=flagi+"+"
        dzies=10
    if (jedno==(kod%10)):
        flagi=flagi+"+"
        jedno=10
    if (len(flagi)<4):
        while (len(flagi)<4):
            flagi=flagi+"-"
    if (flagi=="++++"):
        return ("Zgadłeś sekretny kod")
    else:
        return flagi