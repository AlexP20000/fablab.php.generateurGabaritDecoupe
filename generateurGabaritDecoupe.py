#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Generateur de gcode
Le code généré est sous forme de matrice
'''
from inc import functions as gcode

def ecritChiffres(chiffre, X, Y, largeurLettre):
    chaine = ""
    for number in str(chiffre):
        if( number == "0"):
            chaine += gcode.zero()
        elif( number =="1" ):
            chaine += gcode.un()
        elif (number == "2"):
            chaine += gcode.deux()
        elif (number == "3"):
            chaine += gcode.trois()
        elif (number == "4"):
            chaine += gcode.quatre()
        elif (number == "5"):
            chaine += gcode.cinq()
        elif (number == "6"):
            chaine += gcode.six()
        elif (number == "7"):
            chaine += gcode.sept()
        elif (number == "8"):
            chaine += gcode.huit()
        elif (number == "9"):
            chaine += gcode.neuf()
        elif (number == "."):
            chaine += gcode.point()

        chaine += gcode.lettreSuivante(X, Y, largeurLettre)

    return chaine






# Main programm ==================================================================
if __name__ == '__main__':
    diametre = 4
    largeurMotif = 10
    hauteurMotif = 10
    fileName = "C:/Users/Alex/Documents/GabaritDecoupe.gcode"
    fileName = "GabaritDecoupe.gcode"

    # valeurs possibles
    speedRange = [1,2,5,7,10,11,12,13,14,15]
    powerRange = [6, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9]




    f = open(fileName, "w")
    f.write( gcode.entete() )

    # Matrice de cercles ..........................................................
    deplacement_y = 2
    for speed in speedRange:
        f.write( "; Ligne "+str(speed)+" -----------------------------------\n" )
        deplacement_x = 2


        for power in powerRange:
            f.write( "; Puissance " + str(power) +  ", Speed " + str(speed)+"\n" )

            # Placement
            f.write("G0 X" + str(deplacement_x * largeurMotif) + " Y" + str(deplacement_y * hauteurMotif) + "\n")

            # PATERN : cercle (il prend en paramètre un rayon)
            f.write("G02 X" + str(deplacement_x * largeurMotif) + " Y" + str(deplacement_y * hauteurMotif))
            f.write(" I"+str(diametre / 2)+" J-"+str(diametre / 2)+" E10")

            # speed & power
            f.write(" S"+str(power / 100)+" F"+str(60 * speed)+ "\n")

            deplacement_x += 1
        deplacement_y += 1




    # Legende ..................................................................
    positionY = (len(speedRange) +1) * hauteurMotif
    f.write("G0 X1 Y"+str(positionY)+"\n")
    f.write("G92 X0 Y0\n")
    f.write( gcode.textSpeed() )
    f.write("G0 X0 Y0\n")
    f.write("G92 X1 Y"+str(positionY)+"\n")

    positionX = (len(powerRange) ) * largeurMotif
    f.write("G0 X"+str(positionX)+" Y1 E10 S0.7 F12000\n")
    f.write("G92 X0 Y0\n")
    f.write( gcode.textPower() )
    f.write("G92 X"+str(positionX)+" Y1\n")




    # Ordonnées  ..................................................................
    deplacement_y = 2
    largeurLettre = 2
    positionX = 5
    f.write("; ORDONNEES ================================================\n")
    f.write("G0 X0 Y0\n")
    for speed in speedRange:
        # Placement
        positionY = deplacement_y * hauteurMotif - 3
        f.write("G0 X"+ str(positionX)+" Y" + str(positionY) + "\n")
        f.write("G92 X0 Y0\n")


        # Trace du 1er chiffre (dans nouveau repère)
        f.write("; Speed " + str(speed) + " -------------------------------------\n")
        f.write( ecritChiffres(speed,positionX, positionY, largeurLettre ) )


        # Repositionnement dans l'ancien repère
        f.write("G92 X"+ str(positionX + largeurLettre * len(str(speed)))+" Y" + str(positionY) + "\n")

        deplacement_y += 1



    # Abscisse  ..................................................................
    deplacement_x = 2
    positionY = 5
    f.write("; ABSCISSES ================================================\n")
    f.write("G0 X0 Y0\n")
    for power in powerRange:
        # Placement
        positionX = deplacement_x * largeurMotif + 1
        f.write("G0 X"+ str(positionX)+" Y" + str(positionY) + "\n")
        f.write("G92 X0 Y0\n")


        # Trace du 1er chiffre (dans nouveau repère)
        f.write("; Speed " + str(power) + " -------------------------------------\n")
        f.write( ecritChiffres(power,positionX, positionY, largeurLettre ) )


        # Repositionnement dans l'ancien repère
        f.write("G0 X0 Y0\n")
        f.write("G92 X"+ str(positionX + largeurLettre * len(str(power)))+" Y" + str(positionY) + "\n")

        deplacement_x += 1




    # Carre de découpe .............................................................
    f.write("\n; Decoupe ----------------------\n")
    f.write("G0 X0 Y0 F10000\n")
    f.write("G1 X"+str((len(powerRange)+2) * largeurMotif)+" Y0 S1 F600\n")
    f.write("G1 X"+str((len(powerRange)+2) * largeurMotif)+" Y"+str((len(speedRange) +2) * hauteurMotif)+" \n")
    f.write("G1 X0 Y"+str((len(speedRange)+2) * hauteurMotif)+" \n")
    f.write("G1 X0 Y0 \n")

    f.write( gcode.footer() )

    f.close()