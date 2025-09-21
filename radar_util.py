from datetime import datetime
import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class LatLong():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ImageBoundaries():
    def __init__(self, LowerLeftLong,LowerLeftLat,UpperRightLong,UpperRightLat,VerticalAdjustment,OGImgW,OGImgH,ImagesInterval,Expiration):
        self.LowerLeftLong = LowerLeftLong
        self.LowerLeftLat = LowerLeftLat
        self.UpperRightLong = UpperRightLong
        self.UpperRightLat = UpperRightLat

        self.VerticalAdjustment = VerticalAdjustment

        self.OGImgW = OGImgW
        self.OGImgH = OGImgH
        self.ImageInterval = ImagesInterval
        self.Expiration = Expiration

    def GetUpperRight(self) -> LatLong:
        return LatLong(
            x = self.UpperRightLat,
            y = self.UpperRightLong
        )

    def GetLowerLeft(self) -> LatLong:
        return LatLong(
            x = self.LowerLeftLat,
            y = self.LowerLeftLong
        )

    def GetUpperLeft(self) -> LatLong:
        return LatLong(
            x = self.UpperRightLat, y = self.LowerLeftLong
        )

    def GetLowerRight(self) -> LatLong:
        return LatLong(
            x = self.LowerLeftLat, y = self.UpperRightLong
        )
   

# Utils

def WorldCoordinateToTile(coord: Point) -> Point:
    scale = 1 << 6

    return Point(
        x = math.floor(coord.x * scale / 255),
        y = math.floor(coord.y * scale / 255)
    )

def WorldCoordinateToPixel(coord: Point) -> Point:
    scale = 1 << 6

    return Point(
        x = math.floor(coord.x * scale),
        y = math.floor(coord.y * scale) 
    )

def LatLongProject(lat, long) -> Point:
    siny = math.sin(lat * math.pi / 180)
    siny = min(max(siny, -0.9999), 0.9999)

    return Point(
        x = 256 * (0.5 + long / 360),
        y = 256 * (0.5 - math.log((1 + siny) / (1 - siny)) / (4 * math.pi))
    )