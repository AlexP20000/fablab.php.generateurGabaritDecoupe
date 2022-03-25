#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Generateur de gcode
Le code généré est sous forme de matrice
'''
from inc import functions as gcode

def ecritChiffres(chiffre, X, Y, largeurLettre):
    chaine = ";Chiffre "+ str(chiffre) + "\n"
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

        chaine += gcode.lettreSuivante(X, Y, largeurLettre)

    return chaine






# Main programm ==================================================================
if __name__ == '__main__':
    diametre = 4
    offset_x = 10
    offset_y = 10
    fileName = "C:/Users/Alex/Documents/GabaritDecoupe.gcode"
    # 10 valeur
    speedRange = [1,2,5,7,10,15,20]
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
            f.write("G0 X"+ str(deplacement_x * offset_x )+" Y"+str(deplacement_y * offset_y )+"\n")

            # PATERN : cercle (il prend en paramètre un rayon)
            f.write("G02 X" + str(deplacement_x * offset_x) + " Y" + str(deplacement_y * offset_y))
            f.write(" I"+str(diametre / 2)+" J-"+str(diametre / 2)+" E10")

            # speed & power
            f.write(" S"+str(power / 10)+" F"+str(600 * speed)+ "\n")

            deplacement_x += 1
        deplacement_y += 1




    # Legende ..................................................................
    positionY = 113
    f.write("G0 X1 Y"+str(positionY)+"\n")
    f.write("G92 X0 Y0\n")
    f.write( gcode.textSpeed() )
    f.write("G0 X0 Y0\n")
    f.write("G92 X1 Y"+str(positionY)+"\n")

    positionX = 105
    f.write("G0 X"+str(positionX)+" Y1\n")
    f.write("G92 X0 Y0\n")
    f.write( gcode.textPower() )
    f.write("G0 X0 Y0\n")
    f.write("G92 X"+str(positionX)+" Y1\n")




    # Ordonnées  ..................................................................
    deplacement_y = 2
    largeurLettre = 2
    positionX = 5
    f.write("G0 X0 Y0\n")
    for speed in speedRange:
        # Placement
        positionY = deplacement_y * offset_y -3
        f.write("G0 X"+ str(positionX)+" Y" + str(positionY) + "\n")
        f.write("G92 X0 Y0\n")


        # Trace du 1er chiffre (dans nouveau repère)
        f.write("; Speed " + str(speed) + " -------------------------------------\n")
        f.write( ecritChiffres(speed,positionX, positionY, largeurLettre ) )


        # Repositionnement dans l'ancien repère
        f.write("G0 X0 Y0\n")
        f.write("G92 X"+ str(positionX + largeurLettre * len(str(speed)))+" Y" + str(positionY) + "\n")

        deplacement_y += 1



    # Abscisse  ..................................................................
    deplacement_x = 2
    positionY = 5
    f.write("G0 X0 Y0\n")
    for power in powerRange:
        # Placement
        positionX = deplacement_x * offset_x +1
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
    f.write("\n;Carre de decoupe ----------------------\n")
    f.write("G0 X0 Y0 F10000\n")
    f.write("G1 X120 Y0 S1 F600\n")
    f.write("G1 X120 Y120 \n")
    f.write("G1 X0 Y120 \n")
    f.write("G1 X0 Y0 \n")

    f.write( gcode.footer() )

    f.close()