import cadquery as cq

body_length_1 = 330
body_width_1 = 74
body_length_2 = 150
body_width_2 = 200
body_thickness = 80
motor_radius = 39.5
motor_length_distance = 236
motor_width_distance = 137.5/2
wall_thickness = 10
front_thickness = 23

flexipod_body = cq.Workplane("XY").box(body_length_2, body_width_2, body_thickness)
flexipod_body = flexipod_body.faces(">Z").workplane(offset = - body_thickness / 2).box(body_length_1, body_width_1, body_thickness)
flexipod_body = flexipod_body.faces("<Y").workplane(offset = - body_width_2 / 2).moveTo(motor_length_distance / 2, 0)\
                .circle(motor_radius).moveTo(- motor_length_distance / 2, 0).circle(motor_radius)\
                .extrude(motor_width_distance, both = True)

flexipod_body = flexipod_body.faces("<Z").workplane(offset = -wall_thickness)\
                .moveTo(body_length_1 / 2 - front_thickness, 0)\
                .lineTo(body_length_1 / 2 - front_thickness, body_width_1 / 2 - wall_thickness)\
                .lineTo(body_length_2 / 2 - wall_thickness, body_width_1 / 2 - wall_thickness)\
                .lineTo(body_length_2 / 2 - wall_thickness, body_width_2 / 2 - wall_thickness)\
                .lineTo(-body_length_2 / 2 + wall_thickness, body_width_2 / 2 - wall_thickness)\
                .lineTo(-body_length_2 / 2 + wall_thickness, body_width_1 / 2 - wall_thickness)\
                .lineTo(-body_length_1 / 2 + front_thickness, body_width_1 / 2 - wall_thickness)\
                .lineTo(-body_length_1 / 2 + front_thickness, 0).mirrorX().cutBlind(-(body_thickness - 2 * wall_thickness))

cq.exporters.export(flexipod_body, "flexipod_body.step")