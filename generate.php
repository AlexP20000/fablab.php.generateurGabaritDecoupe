<?php
/** Generateur de Gcode pour faire des teste de découpe
*
**/
$diametre       = 5;
$offset_x       = 10;
$offset_y       = 10;


echo "G21
G90
M3
M106
G92 X0 Y0 Z0";

for( $s=1; $s <= 10; $s++){
        echo "; Ligne ".$s." -----------------------------------\n";
        for( $p=1; $p <= 10; $p++){
                echo ";Puissance ",$p*10," Speed ",$s*10,"\n";
                echo "G0 X".($p * 10 + $offset_x) ." Y".($s * 10 + $offset_y)."\n";
                echo "G02 X".($p *10 + $offset_x)." Y".($s * 10 + $offset_y)." I".$diametre/2 ." J-".$diametre/2 ." E10 S".($p / 10)." F". 600*$s."\n";


        }
}
echo "G0 X0 Y0
M5
M107";
?>
