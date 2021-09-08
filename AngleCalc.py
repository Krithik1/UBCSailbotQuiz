class AngleCalc:
    def __init__(self) -> None:
        pass
    def boundTo180(self,angle:float) -> float:
        angle %= 360
        quad_12 = 0 #checks if angle belongs to first or second quadrant
        if angle<180:
            quad_12 = 1
        if quad_12:
            return angle
        return (-(180-(angle%180)))
    def isAngleBetween(self,first_angle:float,middle_angle:float,second_angle:float) -> bool:
        if abs(second_angle-first_angle)<180:
            if middle_angle>=min(first_angle,second_angle) and middle_angle<max(first_angle,second_angle):
                return True
            return False
        else:
            transform_angles = lambda angle : 180-angle if angle>0 else (-(180+angle))
            #transforms the angles such that the axes with angles -180 -90 0 90 becomes 0 -90 -180 90 in that order
            first_angle,middle_angle,second_angle = map(transform_angles,[first_angle,middle_angle,second_angle])
            if middle_angle>=min(first_angle,second_angle) and middle_angle<max(first_angle,second_angle):
                return True
            return False
