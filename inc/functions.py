'''
Functions retournant du gcode pour écrire des nombres.
'''
def lettreSuivante(x, y, largeurLettre):
    chaine = "G0 X0 Y0\n"
    chaine += "G92 X" + str(x) + " Y" + str(y) + "\n"
    chaine += "G0 X" + str(x + largeurLettre) + " Y" + str(y) + "\n"
    chaine += "G92 X0 Y0\n"
    return chaine

def zero():
    return """
G0 X0.8636 Y3.05 F10000
G1 X0.4064 Y2.8976 S0.07 F1200
G1 X0.1016 Y2.4912
G1 X0 Y1.7292
G1 X0 Y1.3228
G1 X0.1016 Y0.6116
G1 X0.4064 Y0.1544
G1 X0.8636 Y0.002
G1 X1.1176 Y0.002
G1 X1.5748 Y0.1544
G1 X1.8288 Y0.6116
G1 X1.9812 Y1.3228
G1 X1.9812 Y1.7292
G1 X1.8288 Y2.4912
G1 X1.5748 Y2.8976
G1 X1.1176 Y3.05
G1 X0.8636 Y3.05
G0 X0 Y0
"""

def un():
    return """
G0 X0 Y2.4912 F10000
G1 X0.254 Y2.5928 S0.07 F1200
G1 X0.7112 Y3.05
G1 X0.7112 Y0.002
G0 X0 Y0
"""

def deux():
    return"""
G0 X0.1016 Y2.3388 F10000
G1 X0.1016 Y2.4912 S0.07 F1200
G1 X0.254 Y2.7452
G1 X0.4064 Y2.8976
G1 X0.7112 Y3.05
G1 X1.27 Y3.05
G1 X1.5748 Y2.8976
G1 X1.7272 Y2.7452
G1 X1.8288 Y2.4912
G1 X1.8288 Y2.1864
G1 X1.7272 Y1.8816
G1 X1.4224 Y1.4752
G1 X0 Y0.002
G1 X1.9812 Y0.002
G0 X0 Y0
"""

def trois():
    return """
G0 X0.254 Y3.05 F10000
G1 X1.8288 Y3.05 S0.07 F1200
G1 X0.9652 Y1.8816
G1 X1.4224 Y1.8816
G1 X1.7272 Y1.7292
G1 X1.8288 Y1.6276
G1 X1.9812 Y1.1704
G1 X1.9812 Y0.8656
G1 X1.8288 Y0.4592
G1 X1.5748 Y0.1544
G1 X1.1176 Y0.002
G1 X0.7112 Y0.002
G1 X0.254 Y0.1544
G1 X0.1016 Y0.3068
G1 X0 Y0.6116
G0 X0 Y0
"""

def quatre():
    return"""
G0 X1.4224 Y3.05 F10000
G1 X0 Y1.018 S0.07 F1200
G1 X2.1336 Y1.018
G0 X1.4224 Y0.002 F10000
G1 X1.4224 Y3.05 F1200
G0 X0 Y0
"""

def cinq():
    return """
G0 X1.7272 Y3.05 F10000
G1 X0.254 Y3.05 S0.07 F1200
G1 X0.1016 Y1.7292
G1 X0.254 Y1.8816
G1 X0.7112 Y2.034
G1 X1.1176 Y2.034
G1 X1.5748 Y1.8816
G1 X1.8288 Y1.6276
G1 X1.9812 Y1.1704
G1 X1.9812 Y0.8656
G1 X1.8288 Y0.4592
G1 X1.5748 Y0.1544
G1 X1.1176 Y0.002
G1 X0.7112 Y0.002
G1 X0.254 Y0.1544
G1 X0.1016 Y0.3068
G1 X0 Y0.6116
G0 X0 Y0
"""

def six():
    return """
G0 X1.7272 Y2.5928 F10000
G1 X1.5748 Y2.8976 S0.07 F1200
G1 X1.1176 Y3.05
G1 X0.8636 Y3.05
G1 X0.4064 Y2.8976
G1 X0.1016 Y2.4912
G1 X0 Y1.7292
G1 X0 Y1.018
G1 X0.1016 Y0.4592
G1 X0.4064 Y0.1544
G1 X0.8636 Y0.002
G1 X0.9652 Y0.002
G1 X1.4224 Y0.1544
G1 X1.7272 Y0.4592
G1 X1.8288 Y0.8656
G1 X1.8288 Y1.018
G1 X1.7272 Y1.4752
G1 X1.4224 Y1.7292
G1 X0.9652 Y1.8816
G1 X0.8636 Y1.8816
G1 X0.4064 Y1.7292
G1 X0.1016 Y1.4752
G1 X0 Y1.018
G0 X0 Y0
"""

def sept():
    return """
G0 X1.9812 Y3.05 F10000
G1 X0.5588 Y0.002 S0.07 F1200
G0 X0 Y3.05 F10000
G1 X1.9812 Y3.05 F1200
G0 X0 Y0
"""

def huit():
    return"""
G0 X0.7112 Y3.05 F10000
G1 X0.254 Y2.8976 S0.07 F1200
G1 X0.1016 Y2.5928
G1 X0.1016 Y2.3388
G1 X0.254 Y2.034
G1 X0.5588 Y1.8816
G1 X1.1176 Y1.7292
G1 X1.5748 Y1.6276
G1 X1.8288 Y1.3228
G1 X1.9812 Y1.018
G1 X1.9812 Y0.6116
G1 X1.8288 Y0.3068
G1 X1.7272 Y0.1544
G1 X1.27 Y0.002
G1 X0.7112 Y0.002
G1 X0.254 Y0.1544
G1 X0.1016 Y0.3068
G1 X0 Y0.6116
G1 X0 Y1.018
G1 X0.1016 Y1.3228
G1 X0.4064 Y1.6276
G1 X0.8636 Y1.7292
G1 X1.4224 Y1.8816
G1 X1.7272 Y2.034
G1 X1.8288 Y2.3388
G1 X1.8288 Y2.5928
G1 X1.7272 Y2.8976
G1 X1.27 Y3.05
G1 X0.7112 Y3.05
G0 X0 Y0
"""

def neuf():
    return """
G0 X1.8288 Y2.034 F10000
G1 X1.7272 Y1.6276 S0.07 F1200
G1 X1.4224 Y1.3228
G1 X0.9652 Y1.1704
G1 X0.8636 Y1.1704
G1 X0.4064 Y1.3228
G1 X0.1016 Y1.6276
G1 X0 Y2.034
G1 X0 Y2.1864
G1 X0.1016 Y2.5928
G1 X0.4064 Y2.8976
G1 X0.8636 Y3.05
G1 X0.9652 Y3.05
G1 X1.4224 Y2.8976
G1 X1.7272 Y2.5928
G1 X1.8288 Y2.034
G1 X1.8288 Y1.3228
G1 X1.7272 Y0.6116
G1 X1.4224 Y0.1544
G1 X0.9652 Y0.002
G1 X0.7112 Y0.002
G1 X0.254 Y0.1544
G1 X0.1016 Y0.4592
G0 X0 Y0
"""

def point():
    return """
G0 X0.6096 Y0.3576 F10000
G1 X0.6604 Y0.5608 S0.07 F1200
G1 X0.8128 Y0.6116
G1 X0.9652 Y0.5608
G1 X1.016 Y0.3576
G1 X0.9652 Y0.2052
G1 X0.8128 Y0.1544
G1 X0.6604 Y0.2052
G1 X0.6096 Y0.3576
G1 X0.6096 Y0.3576
G0 X0 Y0
"""

def textSpeed():
    return"""; Speed -------------
G0 X2.4384 Y4.32 F10000
G1 X2.0828 Y4.6756 S0.07 F1200
G1 X1.5748 Y4.828
G1 X0.9144 Y4.828
G1 X0.4064 Y4.6756
G1 X0.0508 Y4.32
G1 X0.0508 Y4.0152
G1 X0.2032 Y3.6596
G1 X0.4064 Y3.5072
G1 X0.7112 Y3.304
G1 X1.7272 Y2.9992
G1 X2.0828 Y2.796
G1 X2.2352 Y2.6436
G1 X2.4384 Y2.288
G1 X2.4384 Y1.78
G1 X2.0828 Y1.4752
G1 X1.5748 Y1.272
G1 X0.9144 Y1.272
G1 X0.4064 Y1.4752
G1 X0.0508 Y1.78
G0 X3.6068 Y1.78 F10000
G1 X3.9624 Y1.4752 F1200
G1 X4.2672 Y1.272
G1 X4.7752 Y1.272
G1 X5.1308 Y1.4752
G1 X5.4864 Y1.78
G1 X5.6388 Y2.288
G1 X5.6388 Y2.6436
G1 X5.4864 Y3.1516
G1 X5.1308 Y3.5072
G1 X4.7752 Y3.6596
G1 X4.2672 Y3.6596
G1 X3.9624 Y3.5072
G1 X3.6068 Y3.1516
G0 X3.6068 Y3.6596 F10000
G1 X3.6068 Y0.1036 F1200
G0 X6.6548 Y2.6436 F10000
G1 X8.6868 Y2.6436 F1200
G1 X8.6868 Y2.9992
G1 X8.5344 Y3.304
G1 X8.3312 Y3.5072
G1 X8.0264 Y3.6596
G1 X7.5184 Y3.6596
G1 X7.1628 Y3.5072
G1 X6.8072 Y3.1516
G1 X6.6548 Y2.6436
G1 X6.6548 Y2.288
G1 X6.8072 Y1.78
G1 X7.1628 Y1.4752
G1 X7.5184 Y1.272
G1 X8.0264 Y1.272
G1 X8.3312 Y1.4752
G1 X8.6868 Y1.78
G0 X9.7028 Y2.6436 F10000
G1 X11.7348 Y2.6436 F1200
G1 X11.7348 Y2.9992
G1 X11.5824 Y3.304
G1 X11.3792 Y3.5072
G1 X11.0744 Y3.6596
G1 X10.5664 Y3.6596
G1 X10.2108 Y3.5072
G1 X9.8552 Y3.1516
G1 X9.7028 Y2.6436
G1 X9.7028 Y2.288
G1 X9.8552 Y1.78
G1 X10.2108 Y1.4752
G1 X10.5664 Y1.272
G1 X11.0744 Y1.272
G1 X11.3792 Y1.4752
G1 X11.7348 Y1.78
G0 X14.7828 Y1.78 F10000
G1 X14.4272 Y1.4752 F1200
G1 X14.1224 Y1.272
G1 X13.6144 Y1.272
G1 X13.2588 Y1.4752
G1 X12.9032 Y1.78
G1 X12.7508 Y2.288
G1 X12.7508 Y2.6436
G1 X12.9032 Y3.1516
G1 X13.2588 Y3.5072
G1 X13.6144 Y3.6596
G1 X14.1224 Y3.6596
G1 X14.4272 Y3.5072
G1 X14.7828 Y3.1516
G0 X14.7828 Y4.828 F10000
G1 X14.7828 Y1.272 F1200
G0 X0 Y0
"""

def textPower():
    return """; Power -------------
G0 X0.0508 Y3.558 F10000
G1 X0.0508 Y0.1036 S0.07 F1200
G0 X0.0508 Y1.78 F10000
G1 X1.524 Y1.78 F1200
G1 X2.032 Y1.9324
G1 X2.1844 Y2.0848
G1 X2.3876 Y2.4404
G1 X2.3876 Y2.8976
G1 X2.1844 Y3.2532
G1 X2.032 Y3.4056
G1 X1.524 Y3.558
G1 X0.0508 Y3.558
G0 X4.2164 Y2.4404 F10000
G1 X3.8608 Y2.2372 F1200
G1 X3.556 Y1.9324
G1 X3.3528 Y1.4244
G1 X3.3528 Y1.1196
G1 X3.556 Y0.6116
G1 X3.8608 Y0.256
G1 X4.2164 Y0.1036
G1 X4.6736 Y0.1036
G1 X5.0292 Y0.256
G1 X5.334 Y0.6116
G1 X5.5372 Y1.1196
G1 X5.5372 Y1.4244
G1 X5.334 Y1.9324
G1 X5.0292 Y2.2372
G1 X4.6736 Y2.4404
G1 X4.2164 Y2.4404
G0 X6.5024 Y2.4404 F10000
G1 X7.1628 Y0.1036 F1200
G0 X7.1628 Y0.1036 F10000
G1 X7.8232 Y2.4404 F1200
G0 X7.8232 Y2.4404 F10000
G1 X8.4836 Y0.1036 F1200
G0 X8.4836 Y0.1036 F10000
G1 X9.144 Y2.4404 F1200
G0 X10.16 Y1.4244 F10000
G1 X12.1412 Y1.4244 F1200
G1 X12.1412 Y1.78
G1 X11.9888 Y2.0848
G1 X11.7856 Y2.2372
G1 X11.4808 Y2.4404
G1 X10.9728 Y2.4404
G1 X10.668 Y2.2372
G1 X10.3124 Y1.9324
G1 X10.16 Y1.4244
G1 X10.16 Y1.1196
G1 X10.3124 Y0.6116
G1 X10.668 Y0.256
G1 X10.9728 Y0.1036
G1 X11.4808 Y0.1036
G1 X11.7856 Y0.256
G1 X12.1412 Y0.6116
G0 X13.3096 Y0.1036 F10000
G1 X13.3096 Y2.4404 F1200
G0 X13.3096 Y1.4244 F10000
G1 X13.462 Y1.9324 F1200
G1 X13.8176 Y2.2372
G1 X14.1224 Y2.4404
G1 X14.6304 Y2.4404
G0 X0 Y0
"""

def entete():
    return "G21\nG90\nM3\nM106\nG92 X0 Y0 Z0\n"

def footer():
    return "G0 X0 Y0\nM5\nM107\n"


def ecritChiffres(chiffre, X, Y, largeurLettre):
    chaine = ""
    for number in str(chiffre):
        if( number == "0"):
            chaine += zero()
        elif( number =="1" ):
            chaine += un()
        elif (number == "2"):
            chaine += deux()
        elif (number == "3"):
            chaine += trois()
        elif (number == "4"):
            chaine += quatre()
        elif (number == "5"):
            chaine += cinq()
        elif (number == "6"):
            chaine += six()
        elif (number == "7"):
            chaine += sept()
        elif (number == "8"):
            chaine += huit()
        elif (number == "9"):
            chaine += neuf()
        elif (number == "."):
            chaine += point()

        chaine += lettreSuivante(X, Y, largeurLettre)

    return chaine

