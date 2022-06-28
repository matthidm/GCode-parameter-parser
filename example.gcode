;VAR ZH 0.27
;VAR ER 1.23

;Extrusion settings
M83 ;relative extrusion mode
G91 E0 ;reset extruder
G28 Z ;home Z axis
G1 F5000

;G1 E150
G1 Y20 F800

;Layer one
G1 X10 Y20 ER
G1 X20 ER
G1 Y-20 ER
G1 X-20 

;Layer two
G1 ZH
G1 Y20 ER
G1 X20 
G1 Y-20 ER
G1 X-20 

;Layer three
G1 ZH
G1 Y20 ER
G1 X20 
G1 Y-20 ER
G1 X-20 

;Layer four
G1 ZH
G1 Y20 ER
G1 X20 
G1 Y-20 ER
G1 X-20 

;Layer five
G1 ZH
G1 Y20 ER
G1 X20 
G1 Y-20 ER
G1 X-20 


;End
G1 F5000
G1 X-25 Z5
G1 E-200
