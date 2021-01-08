import cadquery as cq
thigh_joint_radius = 26.5
thigh_length = 103.5
thigh_thickness = 53
shank_motor_radius = 39.5

flexipod_thigh = cq.Workplane("YZ").moveTo(0, -thigh_length)\
                .lineTo(thigh_joint_radius, -thigh_length)\
                .lineTo(thigh_joint_radius, 0).tangentArcPoint((-thigh_joint_radius, thigh_joint_radius))\
                .mirrorY().extrude(thigh_thickness)
flexipod_thigh = flexipod_thigh.faces("<Y").workplane(offset = - thigh_joint_radius)\
                .moveTo(thigh_thickness / 2, - thigh_length).circle(shank_motor_radius)\
                .extrude(thigh_thickness / 2, both = True)

cq.exporters.export(flexipod_thigh, "flexipod_thigh.step")