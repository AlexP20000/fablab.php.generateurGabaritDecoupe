#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Generateur de gcode
Le code généré est sous forme de matrice
'''

def entete():
    return "G21\nG90\nM3\nM106\nG92 X0 Y0 Z0\n"

def footer():
    return "G0 X0 Y0\nM5\nM107\n"

# Main programm ==================================================================
if __name__ == '__main__':
    diametre = 4
    offset_x = 10
    offset_y = 10
    fileName = "Testdecoupe.gcode"



    f = open(fileName, "w")
    f.write( entete() )

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
            f.write("G02 X"+str(deplacement_x * offset_x )+" Y"+str(deplacement_y * offset_y ))

            # cercle
            f.write(" I"+str(diametre / 2)+" J-"+str(diametre / 2)+" E10")

            # speed & power
            f.write(" S"+str(power / 10)+" F"+str(600 * speed)+ "\n")

            deplacement_x += 1
        deplacement_y += 1

    f.write( footer() )


    # Carre de découpe .............................................................
    f.write("\nCarre de decoupe ----------------------\n")
    f.write("G0 X0 Y0\n")
    f.write("G02 X120 Y0 S10 F60000\n")
    f.write("G02 X120 Y120 S10 F60000\n")
    f.write("G02 X0 Y120 S10 F60000\n")
    f.write("G02 X0 Y0 S10 F60000\n")

    f.close()