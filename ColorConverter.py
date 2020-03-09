print("1 - Normalizar RGB")
print("2 - RGB to HSV")
print("3 - HSV to RGB")
print("4 - RGB to CMYK")
print("5 - CMYK to RGB")
print("6 - RGB to cinza")

while(True):
    menu = input("Digite o numero da opção desejada: ")
    if (menu):
        try:
            menu = int(menu)
        except:
            print("Mas eh um animal!! Isso que vc digitou nao eh um numero!!!")

    def normRGB(R, G, B):
        r = round((R / (R + G + B)), 2)
        g = round((G / (R + G + B)), 2)
        b = round((B / (R + G + B)), 2)
        print("\nR: " + str(r) + "\nG: " + str(g) + "\nB: " + str(b))


    def rgbToHSV(R, G, B):
        r = R/255
        g = G/255
        b = B/255
        cMax = max(r,g,b)
        cMin = min(r,g,b)
        delta = cMax - cMin
        H = 0
        divisor = (cMax - cMin)
        if(divisor > 0):
            if (cMax == r and g >= b):
                H = 60 * ((g-b)/(cMax - cMin)) + 0
            elif(cMax == r and g < b):
                H = 60 * ((g-b)/(cMax - cMin)) + 360
            elif(cMax == g):
                H = 60 * ((g-r)/(cMax - cMin)) + 120
            elif(cMax == b):
                H = 60 * ((r - g) / (cMax - cMin)) + 240
        H = round(H, 2)
        S = round((((cMax - cMin) / cMax) * 100), 2)
        V = round(cMax * 100, 2)
        print("\nH: " + str(H) + "\nS: " + str(S) + "\nV: " + str(V))

    def hsvToRgb(H, S, V):
        c = V * S
        x = c * (1-(abs(((H/60)%2)-1)))
        m = V - c

        if(H >= 0 and H < 60):
            r,g,b = (c,x,0)
        elif(H >= 0 and H < 120):
            r, g, b = (x,c,0)
        elif(H >= 60 and H < 180):
            r, g, b = (0,c,x)
        elif (H >= 120 and H < 240):
            r, g, b = (0,x,c)
        elif(H >= 240 and H < 300):
            r, g, b = (x,0,c)
        elif (H >= 300 and H < 360):
            r, g, b = (c,0,x)

        R, G, B = ((r+m)*255,(g+m)*255,(b+m)*255)

        print("\nR: " + str(R) + "\nG: " + str(G) + "\nB: " + str(B))


    def rgbToCmyk(R, G, B):
        r = R/255
        g = G/255
        b = B/255
        k = round((1 - max(r,g,b)), 2)
        c = round(((1 - r - k) / (1 - k)),2)
        m = round(((1 - g - k) / (1 - k)),2)
        y = round(((1 - b - k) / (1 - k)),2)
        print("\nC: " + str(c) + "\nM: " + str(m) + "\nY: " + str(y) + "\nK: " + str(k))

    def cmykToRgb(C, M, Y, K):
        r = round((255 * (1 - C) * (1 - K)),2)
        g = round((255 * (1 - M) * (1 - K)),2)
        b = round((255 * (1 - Y) * (1 - K)),2)
        print("\nR: " + str(r) + "\nG: " + str(g) + "\nB: " + str(b))

    def rgbToCinza(R, G, B):
        I = round((R + G + B) / 3,2)
        print('I: ' + str(I))

    def lerRGB():
        R = int(input("R: "))
        G = int(input("G: "))
        B = int(input("B: "))
        return (R, G, B)

    def lerHSV():
        H = int(input("H: "))
        S = int(input("S: "))/100
        V = int(input("V: "))/100
        return (H, S, V)

    def lerCMYK():
        C = int(input("C: "))
        M = int(input("M: "))
        Y = int(input("Y: "))
        K = int(input("K: "))
        return (C, M, Y, K)

    if (menu == 1):
        R,G,B = lerRGB()
        normRGB(R, G, B)
    elif(menu == 2):
        R,G,B = lerRGB()
        rgbToHSV(R, G, B)
    elif(menu == 3):
        H, S, V = lerHSV()
        hsvToRgb(H, S, V)
    elif(menu == 4):
        R,G,B = lerRGB()
        rgbToCmyk(R, G, B)
    elif(menu == 5):
        C, M, Y, K = lerCMYK()
        cmykToRgb(C, M, Y, K)
    elif(menu == 6):
        R,G,B = lerRGB()
        rgbToCinza(R, G, B)