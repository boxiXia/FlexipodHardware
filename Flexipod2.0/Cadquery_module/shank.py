import cadquery as cq
import math
shank_joint_length = 10

shank_length = 156
shank_joint_radius = 52 / 2
feet_length = 50
shank_width = 40
feet_hole_radius = 10
feet_hole_depth = 60

sin_a1 = math.sqrt(shank_length ** 2 + (feet_length / 2) ** 2 - shank_joint_radius ** 2) / math.sqrt(shank_length ** 2 + (feet_length / 2) ** 2)
cos_a1 = shank_joint_radius / math.sqrt(shank_length ** 2 + (feet_length / 2) ** 2)
sin_a2 = (feet_length / 2) / math.sqrt(shank_length ** 2 + (feet_length / 2) ** 2)
cos_a2 = shank_length / math.sqrt(shank_length ** 2 + (feet_length / 2) ** 2)

sin_a12 = sin_a1 * cos_a2 + cos_a1 * sin_a2
cos_a12 = cos_a1 * cos_a2 - sin_a1 * sin_a2

sin_a3 = math.sqrt(shank_length ** 2 - shank_joint_radius ** 2) / shank_length
cos_a3 = shank_joint_radius / shank_length

sin_a12_3 = sin_a12 * cos_a3 - cos_a12 * sin_a3
cos_a12_3 = cos_a12 * cos_a3 + sin_a12 * sin_a3

tangent_point_x = shank_joint_radius * sin_a12
tangent_point_y = shank_joint_radius * cos_a12

feet_point_x = shank_length * sin_a12_3
feet_point_y = shank_length * cos_a12_3

flexipod_shank = cq.Workplane("YZ")
flexipod_shank = flexipod_shank.moveTo(-1, shank_length)
flexipod_shank = flexipod_shank.lineTo(0, shank_length, forConstruction = True)
flexipod_shank = flexipod_shank.tangentArcPoint((feet_point_x, -shank_length + feet_point_y))
flexipod_shank = flexipod_shank.lineTo(tangent_point_x, tangent_point_y)

flexipod_shank = flexipod_shank.tangentArcPoint((-tangent_point_x , -shank_joint_radius - tangent_point_y))
flexipod_shank = flexipod_shank.mirrorY().extrude(shank_width + shank_joint_length)

flexipod_shank = flexipod_shank.faces("YZ").workplane()
flexipod_shank = flexipod_shank.moveTo(-1, shank_length)
flexipod_shank = flexipod_shank.lineTo(0, shank_length, forConstruction = True)
flexipod_shank = flexipod_shank.tangentArcPoint((feet_point_x, -shank_length + feet_point_y))
flexipod_shank = flexipod_shank.lineTo(tangent_point_x, tangent_point_y)

flexipod_shank = flexipod_shank.tangentArcPoint((shank_joint_radius - tangent_point_x, -tangent_point_y))
flexipod_shank = flexipod_shank.lineTo(shank_joint_radius, -1, forConstruction=True)
flexipod_shank = flexipod_shank.lineTo(shank_joint_radius, 0, forConstruction=True)

flexipod_shank = flexipod_shank.tangentArcPoint((-shank_joint_radius, shank_joint_radius))


flexipod_shank = flexipod_shank.mirrorY().cutBlind(shank_joint_length)


flexipod_shank = flexipod_shank.faces(">Z").workplane(offset = feet_hole_depth)\
    .moveTo(shank_joint_length + shank_width/2, 0)\
    .circle(feet_hole_radius).cutThruAll( )
cq.exporters.export(flexipod_shank, "shank.step")

show_object(flexipod_shank)