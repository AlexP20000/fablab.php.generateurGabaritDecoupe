#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Generateur de gcode
Le code généré est sous forme de matrice
'''
from inc import functions as gcode

def ecritChiffres(chiffre):
    chaine = ""
    for number in str(chiffre):
        if( number == 0):
            chaine += gcode.zero()
        elif( number ==1 ):
            chaine += gcode.un()

    return chaine



def lettreSuivante(x, y):
    chaine = "G0 X0 Y0\n"
    chaine += "G92 X" + str(x) + " Y" + str(y) + "\n"
    chaine += "G0 X" + str(x + largeurLettre) + " Y" + str(y) + "\n"
    chaine += "G92 X0 Y0\n"
    return chaine


# Main programm ==================================================================
if __name__ == '__main__':
    diametre = 4
    offset_x = 10
    offset_y = 10
    fileName = "Testdecoupe.gcode"



    f = open(fileName, "w")
    f.write( gcode.entete() )

    # Matrice de cercles ..........................................................
    deplacement_y = 2
    pas = 1
    for speed in range(6,15,pas):
        f.write( "; Ligne "+str(speed)+" -----------------------------------\n" )
        deplacement_x = 2


        for power in range(6,15,pas):
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
    f.write("G0 X105 Y1\n")
    f.write("G92 X0 Y0\n")
    f.write( gcode.textPower() )
    f.write("G0 X0 Y0\n")
    f.write("G92 X105 Y1\n")

    f.write("G0 X1 Y105\n")
    f.write("G92 X0 Y0\n")
    f.write( gcode.textSpeed())
    f.write("G0 X0 Y0\n")
    f.write("G92 X1 Y105\n")



    # Abscisse  ..................................................................
    deplacement_y = 2
    largeurLettre = 2
    f.write("G0 X0 Y0\n")
    for speed in range(6, 15, pas):
        # Placement
        f.write("G0 X5 Y" + str(deplacement_y * offset_y -3) + "\n")
        f.write("G92 X0 Y0\n")

        # Trace du 1er chiffre (dans nouveau repère)
        f.write("; Speed " + str(speed) + " -------------------------------------\n")
        ecritChiffres(speed)


        # Repositionnement dans l'ancien repère
        f.write("G0 X0 Y0\n")
        f.write("G92 X5 Y" + str(deplacement_y * offset_y -3) + "\n")

        deplacement_y += 1




    '''
    deplacement_y = 0
    largeurLettre = 2
    f.write("G0 X0 Y0\n")
    for speed in range(6,15,pas):
        deplacement_x = 2
        for power in range(6,15,pas):
            f.write("\n; Puissance " + str(power) + ", Speed " + str(speed) + " --------------------------\n")

            # Placement
            f.write("G0 X" + str(deplacement_x * offset_x) + " Y" + str(deplacement_y * offset_y) + "\n")
            f.write("G92 X0 Y0\n")

            # Trace du 1er chiffre (dans nouveau repère)
            f.write( cinq() )

            # deplacement pour la lettre suivante
            f.write( lettreSuivante(deplacement_x * offset_x, deplacement_y * offset_y))
            f.write( six() )

            f.write(lettreSuivante(deplacement_x * offset_x+ largeurLettre, deplacement_y * offset_y))
            f.write(sept())

            f.write(lettreSuivante(deplacement_x * offset_x+ largeurLettre*2, deplacement_y * offset_y))
            f.write(huit())


            # Repositionnement dans l'ancien repère
            f.write("G0 X0 Y0\n")
            f.write("G92 X" + str(deplacement_x * offset_x + largeurLettre *3) + " Y" + str(deplacement_y * offset_y) + "\n")


            deplacement_x += 1
        deplacement_y += 1
    '''


    # Carre de découpe .............................................................
    f.write("\n;Carre de decoupe ----------------------\n")
    f.write("G0 X0 Y0 F10000\n")
    f.write("G1 X120 Y0 S1 F600\n")
    f.write("G1 X120 Y120 \n")
    f.write("G1 X0 Y120 \n")
    f.write("G1 X0 Y0 \n")

    f.write( gcode.footer() )

    f.close()