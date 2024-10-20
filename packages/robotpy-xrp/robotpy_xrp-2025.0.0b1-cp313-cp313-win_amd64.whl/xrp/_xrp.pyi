from __future__ import annotations
import typing
import wpilib._wpilib
import wpilib.interfaces._interfaces
import wpimath.geometry._geometry
import wpimath.units
__all__ = ['XRPGyro', 'XRPMotor', 'XRPOnBoardIO', 'XRPRangefinder', 'XRPReflectanceSensor', 'XRPServo']
class XRPGyro:
    """
    Use a rate gyro to return the robots heading relative to a starting position.
    
    This class is for the XRP onboard gyro, and will only work in
    simulation/XRP mode. Only one instance of a XRPGyro is supported.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        Constructs an XRPGyro.
        
        Only one instance of a XRPGyro is supported.
        """
    def getAngle(self) -> float:
        """
        Return the actual angle in degrees that the robot is currently facing.
        
        The angle is based on integration of the returned rate form the gyro.
        The angle is continuous, that is, it will continue from 360->361 degrees.
        This allows algorithms that wouldn't want to see a discontinuity in the
        gyro output as it sweeps from 360 to 0 on the second time around.
        
        :returns: the current heading of the robot in degrees.
        """
    def getAngleX(self) -> float:
        """
        Gets the currently reported angle around the X-axis
        """
    def getAngleY(self) -> float:
        """
        Gets the currently reported angle around the X-axis
        """
    def getAngleZ(self) -> float:
        """
        Gets the currently reported angle around the X-axis
        """
    def getRate(self) -> float:
        """
        Return the rate of rotation of the gyro
        
        The rate is based on the most recent reading of the gyro.
        
        :returns: the current rate in degrees per second
        """
    def getRateX(self) -> float:
        """
        Gets the rate of turn in degrees-per-second around the X-axis
        """
    def getRateY(self) -> float:
        """
        Gets the rate of turn in degrees-per-second around the Y-axis
        """
    def getRateZ(self) -> float:
        """
        Gets the rate of turn in degrees-per-second around the Z-axis
        """
    def getRotation2d(self) -> wpimath.geometry._geometry.Rotation2d:
        """
        Gets the angle the robot is facing.
        
        :returns: A Rotation2d with the current heading.
        """
    def reset(self) -> None:
        """
        Resets the gyro
        """
class XRPMotor(wpilib.interfaces._interfaces.MotorController, wpilib._wpilib.MotorSafety):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, deviceNum: int) -> None:
        """
        Constructs an XRPMotor.
        
        :param deviceNum: the motor channel
        """
    def disable(self) -> None:
        ...
    def get(self) -> float:
        ...
    def getDescription(self) -> str:
        ...
    def getInverted(self) -> bool:
        ...
    def set(self, value: float) -> None:
        ...
    def setInverted(self, isInverted: bool) -> None:
        ...
    def stopMotor(self) -> None:
        ...
class XRPOnBoardIO:
    """
    This class represents the onboard IO of the XRP
    reference robot. This the USER push button and
    LED.
    
    DIO 0 - USER Button (input only)
    DIO 1 - LED (output only)
    """
    kMessageInterval: typing.ClassVar[float] = 1.0
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def getUserButtonPressed(self) -> bool:
        """
        Gets if the USER button is pressed.
        """
    def setLed(self, value: bool) -> None:
        """
        Sets the yellow LED.
        """
    @property
    def m_nextMessageTime(self) -> wpimath.units.seconds:
        ...
class XRPRangefinder:
    """
    This class represents the reflectance sensor pair
    on the XRP robot.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def getDistance(self) -> wpimath.units.meters:
        """
        Return the measured distance in meters. Distances further than 4 meters
        will be reported as 4 meters.
        """
class XRPReflectanceSensor:
    """
    This class represents the reflectance sensor pair
    on the XRP robot.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def getLeftReflectanceValue(self) -> float:
        """
        Return the reflectance value of the left sensor.
        Value ranges from 0.0 (white) to 1.0 (black)
        """
    def getRightReflectanceValue(self) -> float:
        """
        Return the reflectance value of the right sensor.
        Value ranges from 0.0 (white) to 1.0 (black)
        """
class XRPServo:
    """
    XRPServo.
    
    A SimDevice based servo
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, deviceNum: int) -> None:
        """
        Constructs an XRPServo.
        
        :param deviceNum: the servo channel
        """
    def getAngle(self) -> float:
        """
        Get the servo angle.
        
        :returns: Current servo angle
        """
    def getPosition(self) -> float:
        """
        Get the servo position.
        
        :returns: Current servo position
        """
    def setAngle(self, angleDegrees: float) -> None:
        """
        Set the servo angle.
        
        :param angleDegrees: Desired angle in degrees
        """
    def setPosition(self, position: float) -> None:
        """
        Set the servo position.
        
        :param position: Desired position (Between 0.0 and 1.0)
        """
