#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Gcode generator
This generator will give a matrix of circles (or patern) with all the speed and power values you defined.

@author : Alexandre PERETJATKO (2022)
'''
from inc import functions as gcode

# File name for the gcode
fileName = "GabaritDecoupe.gcode"


# Values you want for speed and power
# You can set as many values you want (or generate in this 2 lists)
speedRange = [10,20,30,40,50,60,70,80,90,100]
powerRange = [10,20,30,40,50,60,70,80,90,100]



# Patern or not patern ?
# If the Circle diameter is > 0, the matrix will use a circle
# If diameter =0, the patern will use the gcode defined in the gcode.patern() definition.
circleDiameter = 0

# Define the patern's size (or circle, regarding to the circle value)
paternWidth = 25
paternHeight = 25





# Main programm ==================================================================
# You don't have to modifiy the above lines.
#
if __name__ == '__main__':
    f = open(fileName, "w")
    f.write( gcode.entete() )

    # Circles matrix  ..........................................................
    deplacement_y = 2
    for speed in speedRange:
        f.write( "; Line "+str(speed)+" -----------------------------------\n" )
        deplacement_x = 2


        for power in powerRange:
            f.write( "; Power " + str(power) +  ", Speed " + str(speed)+"\n" )

            # Placement
            f.write("G0 X" + str(deplacement_x * paternWidth) + " Y" + str(deplacement_y * paternHeight) + "\n")

            # PATERN
            if (circleDiameter > 0):
                # We use a circle (defined by his radius parameter)
                f.write("G02 X" + str(deplacement_x * paternWidth) + " Y" + str(deplacement_y * paternHeight))
                f.write(" I" + str(circleDiameter / 2) + " J-" + str(circleDiameter / 2) + " E10")
            else:
                # Patern (gcode defined)
                f.write("G92 X0 Y0\n")
                f.write( gcode.patern() )
                f.write("G0 X0 Y0\n")
                f.write("G92 X" + str(deplacement_x * paternWidth) + " Y" + str(deplacement_y * paternHeight) + "\n")

            # speed & power
            f.write(" S"+str(power / 100)+" F"+str(60 * speed)+ "\n")

            deplacement_x += 1
        deplacement_y += 1




    # Legende ..................................................................
    positionY = (len(speedRange) +1) * paternHeight
    f.write("G0 X1 Y"+str(positionY)+"\n")
    f.write("G92 X0 Y0\n")
    f.write( gcode.textSpeed() )
    f.write("G0 X0 Y0\n")
    f.write("G92 X1 Y"+str(positionY)+"\n")

    positionX = (len(powerRange) ) * paternWidth
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
        positionY = deplacement_y * paternHeight - 3
        f.write("G0 X"+ str(positionX)+" Y" + str(positionY) + "\n")
        f.write("G92 X0 Y0\n")


        # Trace du 1er chiffre (dans nouveau repère)
        f.write("; Speed " + str(speed) + " -------------------------------------\n")
        f.write( gcode.ecritChiffres(speed,positionX, positionY, largeurLettre ) )


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
        positionX = deplacement_x * paternWidth + 1
        f.write("G0 X"+ str(positionX)+" Y" + str(positionY) + "\n")
        f.write("G92 X0 Y0\n")


        # Trace du 1er chiffre (dans nouveau repère)
        f.write("; Power " + str(power) + " -------------------------------------\n")
        f.write( gcode.ecritChiffres(power,positionX, positionY, largeurLettre ) )


        # Repositionnement dans l'ancien repère
        f.write("G0 X0 Y0\n")
        f.write("G92 X"+ str(positionX + largeurLettre * len(str(power)))+" Y" + str(positionY) + "\n")

        deplacement_x += 1




    # Carre de découpe .............................................................
    f.write("\n; Cutting around matrix ----------------------\n")
    f.write("G0 X0 Y0 F10000\n")
    f.write("G1 X" + str((len(powerRange)+2) * paternWidth) + " Y0 S1 F600\n")
    f.write("G1 X" + str((len(powerRange)+2) * paternWidth) + " Y" + str((len(speedRange) + 2) * paternHeight) + " \n")
    f.write("G1 X0 Y" + str((len(speedRange)+2) * paternHeight) + " \n")
    f.write("G1 X0 Y0 \n")

    f.write( gcode.footer() )

    f.close()
