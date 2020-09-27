$fn=1000;
module case() {
    linear_extrude(height = 10, center = true, convexity = 10)
        import (file = "4010.dxf", layer = "0");
}

module corners() {
    linear_extrude(height = 9, center = true, convexity = 10)
        import (file = "4010.dxf", layer = "corners");
}

module fanholle() {
    linear_extrude(height = 9, center = true, convexity = 10)
        import (file = "4010.dxf", layer = "fanholle");
}

module inside() {
    linear_extrude(height = 8, center = true, convexity = 10)
        import (file = "4010.dxf", layer = "inside");
}

module fanself() {
    linear_extrude(height = 9, center = true, convexity = 10)
        import (file = "4010.dxf", layer = "fanself");
}

difference() {
     case();
     translate(v=[0,0,1])
        corners();
     translate(v=[0,0,1])
        fanholle();
    
     inside();
}

fanself();

