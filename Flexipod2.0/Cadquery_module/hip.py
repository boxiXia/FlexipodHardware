import cadquery as cq
hip_link_radius = 28
hip_length = 61
thigh_motor_radius = 39.5
thigh_motor_thickness = 56

flexipod_hip_1 = cq.Workplane("YZ").circle(hip_link_radius).extrude(hip_length)

flexipod_hip_2 = cq.Workplane("XZ").moveTo(hip_length, 0)\
    .circle(thigh_motor_radius).extrude(thigh_motor_thickness / 2, both = True)

flexipod_hip_1 = flexipod_hip_1.union(flexipod_hip_2)

cq.exporters.export(flexipod_hip_1, "flexipod_hip.step")