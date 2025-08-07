# Created on Thu Feb 08 10:38:19 EST 2007
Log.info('scmt config started')
# EXP: 1343
# VIW: 12580
# CLN: 17040
#
def scmtRemove(key):
    try:
        dsm.remove(key)
    except:
        pass
#

#
# Beginning of SCMT deployment
import os
dsm.set('scmt_configType', 'domestic',0)
dsm.set('scmt.ProductTypes',['Animated_Logo_Sponsor','Copy_Split','Custom','Logo_Sponsor', 'Dealer'], 0)
#
# MAP: 74097
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(7524,8334),
             mapcutSize=(1440,822),
             mapFinalSize=(240,137),
             mapMilesSize=(152,104),
             datacutType='radar.us',
             datacutCoordinate=(523,683),
             datacutSize=(176,101),
             dataFinalSize=(240,137),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Radar_LocalDoppler', d, 0)
#
# Radar_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDotSmallOutline',0,2,1,),
              ( ( (182,99),),
                ( (147,56),),
                ( (136,71),),
                ( (160,31),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (182,99),),
                ( (147,56),),
                ( (136,71),),
                ( (160,31),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (86,109),'Big Bear Lake',),
                ( (103,52),'Perris',),
                ( (148,78),'Riverside',),
                ( (94,24),'Temecula',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (86,109),'Big Bear Lake',),
                ( (103,52),'Perris',),
                ( (148,78),'Riverside',),
                ( (94,24),'Temecula',),
              ),
             ),
        ],
  vector = [
             (( 6,(20,20,20,96),1,),(('statehighways',),),),
             (( 6,(20,20,20,96),1,),(('ushighways',),),),
             (( 6,(20,20,20,96),1,),(('interstates',),),),
             (( 6,(20,20,20,96),1,),(('otherroutes',),),),
             (( 1,(20,20,20,255),2,),(('counties',),),),
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 1,(20,20,20,255),2,),(('coastlines',),),),
             (( 3,(130,130,130,255),2,),(('statehighways',),),),
             (( 3,(130,130,130,255),2,),(('ushighways',),),),
             (( 3,(130,130,130,255),2,),(('interstates',),),),
             (( 3,(130,130,130,255),2,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Radar_LocalDoppler', d, 0)
# MAP: 50998
# Local_MetroDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(7752,8276),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(152,121),
             datacutType='radar.us',
             datacutCoordinate=(551,676),
             datacutSize=(176,118),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroDopplerRadar', d, 0)
#
# Local_MetroDopplerRadar (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (75,322),'210',),
                ( (213,162),'5',),
                ( (363,83),'15',),
                ( (602,195),'10',),
              ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (149,263),'60',),
                ( (218,228),'91',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (75,322),'210',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (149,263),'60',),
                ( (218,228),'91',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (213,162),'5',),
                ( (363,83),'15',),
                ( (602,195),'10',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
              ( ( (245,277),),
                ( (172,173),),
              ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (523,211),),
                ( (441,338),),
                ( (133,292),),
                ( (351,264),),
                ( (343,208),),
                ( (304,255),),
                ( (244,119),),
                ( (357,193),),
                ( (377,136),),
                ( (336,305),),
                ( (89,210),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (523,211),),
                ( (441,338),),
                ( (133,292),),
                ( (351,264),),
                ( (343,208),),
                ( (304,255),),
                ( (244,119),),
                ( (357,193),),
                ( (377,136),),
                ( (336,305),),
                ( (89,210),),
              ),
             ),
             (
               ('airplane',0,1,0,),
              ( ( (245,277),),
                ( (172,173),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (464,232),'Palm Springs',),
                ( (461,341),'Big Bear Lake',),
                ( (153,295),'El Monte',),
                ( (368,282),'Moreno Valley',),
                ( (360,226),'Perris',),
                ( (207,258),'Riverside',),
                ( (183,102),'San Clemente',),
                ( (377,196),'Sun City',),
                ( (397,139),'Temecula',),
                ( (267,326),'San Bernardino',),
                ( (109,213),'Long Beach',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (464,232),'Palm Springs',),
                ( (461,341),'Big Bear Lake',),
                ( (153,295),'El Monte',),
                ( (368,282),'Moreno Valley',),
                ( (360,226),'Perris',),
                ( (207,258),'Riverside',),
                ( (183,102),'San Clemente',),
                ( (377,196),'Sun City',),
                ( (397,139),'Temecula',),
                ( (267,326),'San Bernardino',),
                ( (109,213),'Long Beach',),
              ),
             ),
        ],
  vector = [
             (( 8,(20,20,20,96),1,),(('statehighways',),),),
             (( 8,(20,20,20,96),1,),(('ushighways',),),),
             (( 8,(20,20,20,96),1,),(('interstates',),),),
             (( 8,(20,20,20,96),1,),(('otherroutes',),),),
             (( 2,(20,20,20,255),2,),(('counties',),),),
             (( 4,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             (( 4,(130,130,130,255),2,),(('statehighways',),),),
             (( 4,(130,130,130,255),2,),(('ushighways',),),),
             (( 4,(130,130,130,255),2,),(('interstates',),),),
             (( 4,(130,130,130,255),2,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Local_MetroDopplerRadar', d, 0)
# MAP: 71678
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(8050,8475),
             mapcutSize=(936,624),
             mapFinalSize=(720,480),
             mapMilesSize=(98,79),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroForecastMap', d, 0)
#
# Local_MetroForecastMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (297,199),'215',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (98,204),'91',),
                ( (324,236),'60',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (192,176),'15',),
                ( (234,291),'10',),
              ),
             ),
        ],
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72286016',(231,180),),
                ( '72286021',(361,117),),
                ( '72286032',(224,80),),
                ( '72286034',(290,310),),
                ( '72286035',(427,217),),
                ( '72286049',(119,274),),
                ( '72286086',(573,156),),
                ( '72286097',(511,312),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72286016',(228,216),),
                ( '72286021',(358,153),),
                ( '72286032',(221,116),),
                ( '72286034',(287,346),),
                ( '72286035',(424,253),),
                ( '72286049',(116,310),),
                ( '72286086',(570,192),),
                ( '72286097',(508,348),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (182,252),'Riverside',),
                ( (331,189),'Perris',),
                ( (152,152),'Lake Elsinore',),
                ( (208,382),'San Bernardino',),
                ( (374,289),'Beaumont',),
                ( (81,346),'Ontario',),
                ( (503,228),'Palm Springs',),
                ( (437,384),'Big Bear Lake',),
              ),
             ),
        ],
  vector = [
             (( 8,(20,20,20,96),1,),(('statehighways',),),),
             (( 8,(20,20,20,96),1,),(('ushighways',),),),
             (( 8,(20,20,20,96),1,),(('interstates',),),),
             (( 8,(20,20,20,96),1,),(('otherroutes',),),),
             (( 2,(20,20,20,255),1,),(('counties',),),),
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             (( 4,(130,130,130,255),1,),(('statehighways',),),),
             (( 4,(130,130,130,255),1,),(('ushighways',),),),
             (( 4,(130,130,130,255),1,),(('interstates',),),),
             (( 4,(130,130,130,255),1,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Local_MetroForecastMap', d, 0)
# MAP: 75182
# Local_MetroObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(8050,8475),
             mapcutSize=(936,624),
             mapFinalSize=(720,480),
             mapMilesSize=(98,79),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroObservationMap', d, 0)
#
# Local_MetroObservationMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (297,199),'215',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (98,204),'91',),
                ( (324,236),'60',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (192,176),'15',),
                ( (234,291),'10',),
              ),
             ),
        ],
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'T72286016',(228,216),),
                ( 'T72286021',(358,153),),
                ( 'T72286032',(221,116),),
                ( 'T72286034',(287,346),),
                ( 'T72286035',(424,253),),
                ( 'T72286049',(116,310),),
                ( 'T72286086',(570,192),),
                ( 'T72286097',(508,348),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72286016',(231,180),),
                ( 'T72286021',(361,117),),
                ( 'T72286032',(224,80),),
                ( 'T72286034',(290,310),),
                ( 'T72286035',(427,217),),
                ( 'T72286049',(119,274),),
                ( 'T72286086',(573,156),),
                ( 'T72286097',(511,312),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (182,252),'Riverside',),
                ( (331,189),'Perris',),
                ( (152,152),'Lake Elsinore',),
                ( (208,382),'San Bernardino',),
                ( (374,289),'Beaumont',),
                ( (81,346),'Ontario',),
                ( (503,228),'Palm Springs',),
                ( (437,384),'Big Bear Lake',),
              ),
             ),
        ],
  vector = [
             (( 8,(20,20,20,96),1,),(('statehighways',),),),
             (( 8,(20,20,20,96),1,),(('ushighways',),),),
             (( 8,(20,20,20,96),1,),(('interstates',),),),
             (( 8,(20,20,20,96),1,),(('otherroutes',),),),
             (( 2,(20,20,20,255),1,),(('counties',),),),
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             (( 4,(130,130,130,255),1,),(('statehighways',),),),
             (( 4,(130,130,130,255),1,),(('ushighways',),),),
             (( 4,(130,130,130,255),1,),(('interstates',),),),
             (( 4,(130,130,130,255),1,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Local_MetroObservationMap', d, 0)
# MAP: 71835
# Local_RegionalForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(5072,7192),
             mapcutSize=(5760,3840),
             mapFinalSize=(720,480),
             mapMilesSize=(604,483),
             vectors=['mercator.us.states.vg','mercator.us.coastlines.vg',],
)
wxdata.setMapData('Config.1.Local_RegionalForecastMap', d, 0)
#
# Local_RegionalForecastMap (PRODUCT DATA)
#
d = twc.Data(
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72286086',(488,151),),
                ( '72290000',(396,79),),
                ( '72295023',(311,178),),
                ( '72384000',(302,285),),
                ( '72386000',(569,305),),
                ( '72394000',(168,239),),
                ( '74611003',(441,265),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72286086',(485,187),),
                ( '72290000',(393,115),),
                ( '72295023',(308,214),),
                ( '72384000',(299,321),),
                ( '72386000',(566,341),),
                ( '72394000',(165,275),),
                ( '74611003',(438,301),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (418,223),'Palm Springs',),
                ( (344,151),'San Diego',),
                ( (246,250),'Los Angeles',),
                ( (243,357),'Bakersfield',),
                ( (515,377),'Las Vegas',),
                ( (104,311),'Santa Maria',),
                ( (400,337),'Barstow',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalForecastMap', d, 0)
# MAP: 71834
# Local_RegionalObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(5072,7192),
             mapcutSize=(5760,3840),
             mapFinalSize=(720,480),
             mapMilesSize=(604,483),
             vectors=['mercator.us.states.vg','mercator.us.coastlines.vg',],
)
wxdata.setMapData('Config.1.Local_RegionalObservationMap', d, 0)
#
# Local_RegionalObservationMap (PRODUCT DATA)
#
d = twc.Data(
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'T72286086',(485,187),),
                ( 'T72290000',(393,115),),
                ( 'T72295000',(308,214),),
                ( 'T72384000',(299,321),),
                ( 'T72386000',(566,341),),
                ( 'T72394000',(165,275),),
                ( 'T74611003',(438,301),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72286086',(488,151),),
                ( 'T72290000',(396,79),),
                ( 'T72295000',(311,178),),
                ( 'T72384000',(302,285),),
                ( 'T72386000',(569,305),),
                ( 'T72394000',(168,239),),
                ( 'T74611003',(441,265),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (418,223),'Palm Springs',),
                ( (344,151),'San Diego',),
                ( (246,250),'Los Angeles',),
                ( (243,357),'Bakersfield',),
                ( (515,377),'Las Vegas',),
                ( (104,311),'Santa Maria',),
                ( (400,337),'Barstow',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalObservationMap', d, 0)
# MAP: 71579
# Local_Satellite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(1879,1114),
             mapcutSize=(1728,1152),
             mapFinalSize=(720,480),
             mapMilesSize=(1626,1095),
             datacutType='satellite.us',
             datacutCoordinate=(484,351),
             datacutSize=(464,310),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Local_Satellite', d, 0)
#
# Local_Satellite (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDot',0,2,0,),
              ( ( (459,189),),
                ( (307,282),),
                ( (316,239),),
                ( (354,223),),
                ( (332,195),),
                ( (403,282),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',21,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (479,192),'Phoenix',),
                ( (190,285),'Bakersfield',),
                ( (191,242),'Los Angeles',),
                ( (374,226),'Palm Springs',),
                ( (228,198),'San Diego',),
                ( (423,285),'Las Vegas',),
              ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_Satellite', d, 0)
# MAP: 50810
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(6912,7715),
             mapcutSize=(3124,2083),
             mapFinalSize=(720,480),
             mapMilesSize=(330,264),
             datacutType='radar.us',
             datacutCoordinate=(448,607),
             datacutSize=(383,256),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_RegionalDopplerRadar', d, 0)
#
# Local_RegionalDopplerRadar (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (287,303),'138',),
              ),
             ),
             (
               (('interstateSignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (146,335),'5',),
                ( (431,94),'8',),
                ( (546,335),'40',),
              ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (287,303),'138',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (146,335),'5',),
                ( (431,94),'8',),
                ( (546,335),'40',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (199,268),),
                ( (435,227),),
                ( (357,100),),
                ( (368,366),),
                ( (243,327),),
                ( (347,229),),
                ( (231,227),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (199,268),),
                ( (435,227),),
                ( (357,100),),
                ( (368,366),),
                ( (243,327),),
                ( (347,229),),
                ( (231,227),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (146,289),'Los Angeles',),
                ( (455,230),'Palm Springs',),
                ( (315,121),'San Diego',),
                ( (334,349),'Barstow',),
                ( (205,348),'Palmdale',),
                ( (325,250),'Perris',),
                ( (181,210),'Long Beach',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (146,289),'Los Angeles',),
                ( (455,230),'Palm Springs',),
                ( (315,121),'San Diego',),
                ( (334,349),'Barstow',),
                ( (205,348),'Palmdale',),
                ( (325,250),'Perris',),
                ( (181,210),'Long Beach',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,96),1,),(('statehighways',),),),
             (( 4,(20,20,20,96),1,),(('ushighways',),),),
             (( 4,(20,20,20,96),1,),(('interstates',),),),
             (( 4,(20,20,20,96),1,),(('otherroutes',),),),
             (( 2,(20,20,20,255),2,),(('counties',),),),
             (( 4,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             (( 2,(130,130,130,255),2,),(('statehighways',),),),
             (( 2,(130,130,130,255),2,),(('ushighways',),),),
             (( 2,(130,130,130,255),2,),(('interstates',),),),
             (( 2,(130,130,130,255),2,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Local_RegionalDopplerRadar', d, 0)
#
wxdata.setInterestList('lambert.us','1',['satellite.us',])
wxdata.setInterestList('mercator.us','1',['radar.us',])
#
#
wxdata.setInterestList('satellite.us.cuts','1',['Config.1.Local_Satellite',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler','Config.1.Local_MetroDopplerRadar','Config.1.Local_RegionalDopplerRadar',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['radar.us','satellite.us',])
# END OF MAPS
# commit for map stuff to avoid missing updates
ds.commit()
#
wxdata.setInterestList('airportId','1',['LGB','ONT','SNA',])
wxdata.setInterestList('coopId','1',['72286000','72286016','72286021','72286032','72286034','72286035','72286049','72286067','72286086','72286097','72290000','72295023','72384000','72386000','72394000','72480014','72481041','74611003',])
wxdata.setInterestList('pollenId','1',['SNA',])
wxdata.setInterestList('indexId','1',['KRIV',])
wxdata.setInterestList('obsStation','1',['KRAL','KRIV','T72286000','T72286008','T72286010','T72286016','T72286021','T72286023','T72286032','T72286034','T72286035','T72286049','T72286050','T72286086','T72286097','T72286099','T72290000','T72295000','T72297000','T72297055','T72384000','T72386000','T72394000','T74611003',])
wxdata.setInterestList('metroId','1',['6',])
wxdata.setInterestList('climId','1',['047470','048655',])
wxdata.setInterestList('zone','1',['CAZ048',])
wxdata.setInterestList('aq','1',['ca016','ca058','ca059',])
wxdata.setInterestList('skiId','1',['619002','909001',])
wxdata.setInterestList('county','1',['CAC065',])
dsm.set('Config.1.countyNameList',[('CAC065','Riverside'),], 0)
#
dsm.set('dmaCode','803', 0)
dsm.set('secondaryObsStation','KRIV', 0)
dsm.set('primaryClimoStation','048655', 0)
dsm.set('primaryIndexId','KRIV', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','CA', 0)
dsm.set('primaryAqStation','ca058', 0)
dsm.set('primPollenSiteName','Orange', 0)
dsm.set('expRev','1301317', 0)
dsm.set('primaryCoopId','72286000', 0)
dsm.set('Config.1.PlaylistOverride','SouthernCalifornia', 0)
dsm.set('wda','RIV', 0)
dsm.set('primaryCounty','CAC065', 0)
dsm.set('primaryObsStation','T72286000', 0)
dsm.set('primaryLat',33.79499, 0)
dsm.set('hasTraffic',1, 0)
dsm.set('primaryPollenStation','SNA', 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',-117.21833, 0)
dsm.set('primaryForecastName','Riverside-Moreno Valley-Perris', 0)
dsm.set('primaryZone','CAZ048', 0)
dsm.set('climoRegion','6', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('onAirName','ADELPHIA', 0)
dsm.set('headendId','021742', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','ADELPHIA', 0)
dsm.set('msoCode','02930', 0)
dsm.set('headendName','DOM - PERRIS - DOM', 0)
dsm.set('affiliateNumber','07453', 0)
dsm.set('zipCode','92570    ', 0)
dsm.set('Config.1.bcNetMask','255.255.255.248', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCD05040062', 0)
dsm.set('Config.1.bcDialInNumber','9516575975', 0)
dsm.set('Config.1.bcExtIpAddress','24.55.36.182', 0)
dsm.set('Config.1.bcGateWay','24.55.36.177', 0)
dsm.set('Config.1.bcIpAddress','24.55.36.182', 0)
#
wxdata.setTimeZone('PST8PDT')
#
# BLOCK BEGIN
d = twc.Data()
dsm.set('Config.1.Override', d, 0)
d = twc.Data()
d.activeVocal = 1
dsm.set('Config.1.Bulletin_Default', d, 0)
# BLOCK END
#
d = twc.Data()
d.sponsorLogo = ''
dsm.set('Config.1', d, 0, 1)
#
scmtRemove('Config.1.Tag.General.airportData')
d = twc.Data()
d.airportId = ['ONT','SNA','LGB',]
d.airportLocName = ['Ontario','Santa Ana','Long Beach',]
d.obsStation = ['T72286049','T72297055','T72297000',]
dsm.set('Config.1.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.1.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['909001','619002',]
d.coopId = ['72286067','72480014',]
d.resortName = ['Snow Summit, CA','Mammoth Mtn, CA',]
dsm.set('Config.1.Tag.General.snowboardData', d, 0, 1)
#
#
#  Non Image Maps
#
d = [
'Config.1.Local_MetroForecastMap',
'Config.1.Local_MetroObservationMap',
'Config.1.Local_RegionalForecastMap',
'Config.1.Local_RegionalObservationMap',
]
dsm.set('Config.1.nonImageMaps', d, 0)
#

#
scmtRemove('Config.1.VocalLocalSchedule')
d = twc.Data()
d.OffTimes = ( )
dsm.set('Config.1.VocalLocalSchedule', d, 0, 1)
#
scmtRemove('Config.1.Ldl_LASCrawl')
scmtRemove('Config.1.LASCrawl')
#
#
scmtRemove('Config.1.Local_OutdoorActivityForecast')
scmtRemove('Config.1.Ldl_LocalStarIDMessage')
scmtRemove('Config.1.Ldl_HurricaneWatch')
scmtRemove('Config.1.Local_Climatology')
scmtRemove('Config.1.Cc_CurrentConditions')
scmtRemove('Config.1.Local_RadarSatelliteComposite')
scmtRemove('Config.1.Local_NWSHeadlines')
scmtRemove('Config.1.Ldl_AirportDelayConditions')
scmtRemove('Config.1.Ldl_CurrentApparentTemp')
scmtRemove('Config.1.Ldl_UVForecast')
scmtRemove('Config.1.Ldl_AirQualityForecast')
scmtRemove('Config.1.Local_EventForecast')
scmtRemove('Config.1.Local_GetawayForecast')
scmtRemove('Config.1.Local_LocalObservations')
scmtRemove('Config.1.TimeTemp_Default')
scmtRemove('Config.1.Local_TrafficReport')
scmtRemove('Config.1.Local_TextForecast')
scmtRemove('Config.1.Ldl_NationalStarIDMessage')
scmtRemove('Config.1.Ldl_TravelForecast')
scmtRemove('Config.1.Ldl_SunriseSunset')
scmtRemove('Config.1.Local_SchoolDayWeather')
scmtRemove('Config.1.Fcst_TextForecast')
scmtRemove('Config.1.Local_RecordHighLow')
scmtRemove('Config.1.Ldl_ExtendedForecast')
scmtRemove('Config.1.Local_7DayForecast')
scmtRemove('Config.1.Local_ExtendedForecast')
scmtRemove('Config.1.Fcst_ExtendedForecast')
scmtRemove('Config.1.Local_MarineForecast')
scmtRemove('Config.1.Local_AirQualityForecast')
scmtRemove('Config.1.Local_HeatSafetyTips')
scmtRemove('Config.1.Local_Almanac')
scmtRemove('Config.1.Ldl_TrafficTripTimes')
scmtRemove('Config.1.Fcst_DaypartForecast')
scmtRemove('Config.1.Local_CurrentConditions')
scmtRemove('Config.1.Local_TrafficOverview')
scmtRemove('Config.1.Local_Tides')
scmtRemove('Config.1.Local_DaypartForecast')
scmtRemove('Config.1.Local_TrafficFlow')
scmtRemove('Config.1.Ldl_CurrentMTDPrecip')
#
d = twc.Data()
d.trafficReverseActive = [1,1,1,1,1,1,]
d.periodBStartTime = '12:00'
d.activeVocalCue = 0
d.periodAStartTime = '00:00'
d.trafficFlowRoute = ['94363-6','94279-6','94337-6','94329-6','94267-6','94277-6',]
d.trafficReverseRoute = ['94362-6','94278-6','94336-6','94328-6','94266-6','94276-6',]
d.routes=[[
             (('6.94363','WB, Jack Rabbit Tr to the 215 (Moreno Valley)','stateHighwaySignLarge','60',(20,20,20,255),0),('6.94362','EB, the 215 (Moreno Valley) to Jack Rabbit Tr','stateHighwaySignLarge','60',(20,20,20,255),0,)),
             (('6.94279','WB, the 215/60 to the 15','stateHighwaySignLarge','91',(20,20,20,255),0),('6.94278','EB, the 15 to the 215/60','stateHighwaySignLarge','91',(20,20,20,255),0,)),
             (('6.94337','SB, the 60 to the 15 (Murrieta)','interstateHighwaySignLarge','215',(212,212,212,255),1),('6.94336','NB, the 15 (Murrieta) to the 60','interstateHighwaySignLarge','215',(212,212,212,255),1,)),
],[
             (('6.94329','SB, the 91 to the 215 (Murrieta)','interstateHighwaySignLarge','15',(212,212,212,255),1),('6.94328','NB, the 215 (Murrieta) to the 91','interstateHighwaySignLarge','15',(212,212,212,255),1,)),
             (('6.94267','WB, the 215/91 to the 15','stateHighwaySignLarge','60',(20,20,20,255),0),('6.94266','EB, the 15 to the 215/91','stateHighwaySignLarge','60',(20,20,20,255),0,)),
             (('6.94277','WB, the 15 to the 5','stateHighwaySignLarge','91',(20,20,20,255),0),('6.94276','EB, the 5 to the 15','stateHighwaySignLarge','91',(20,20,20,255),0,)),
],
]
d.routeDisplayTime=[
             ((0,0),(11,59)),
             ((12,0),(23,59)),
]
dsm.set('Config.1.Local_TrafficFlow', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Riverside-Moreno Valley-Perris'
d.coopId = '72286000'
dsm.set('Config.1.Fcst_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72286010','T72286050','T72286023','T72286099','T72286008','T72286049','T72286016','T72286086',]
d.locName = ['Loma Linda','Chino','Bloomington','Hemet','Nuevo','Ontario','Riverside','Palm Springs',]
dsm.set('Config.1.Local_LocalObservations', d, 0, 1)
#
#
d = twc.Data()
d.crawlRate = 3
dsm.set('Config.1.Ldl_HurricaneWatch', d, 0, 1)
#
#
d = twc.Data()
d.climId = '048655'
d.latitude = 33.7167
d.longitude = -117.1833
dsm.set('Config.1.Local_Almanac', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Los Angeles','San Diego','Barstow',]
d.coopId = ['72295023','72290000','74611003',]
dsm.set('Config.1.Ldl_TravelForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72286000','KRIV',]
d.locName = ['Riverside - March Field','Riverside - March Field',]
d.elementDuration = 6
dsm.set('Config.1.Cc_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Riverside Co.','San Bernardino','Orange Co Coast',]
d.actionDayPhrase = 'Air Quality Action Day'
d.aq = ['ca058','ca059','ca016',]
dsm.set('Config.1.Local_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.activeVocalCue = 1
dsm.set('Config.1.Local_RegionalDopplerRadar', d, 0, 1)
#
#
d = twc.Data()
d.trafficActive = 1
d.trafficReverseActive = [1,1,1,1,1,1,]
d.trafficFlowRoute = ['94363-6','94279-6','94337-6','94329-6','94267-6','94277-6',]
d.trafficReverseRoute = ['94362-6','94278-6','94336-6','94328-6','94266-6','94276-6',]
d.routes=[
             (('6.94363','The 60','WB','Jack Rabbit Tr','the 215 (Moreno Valley)',),
             ('6.94362','The 60','EB','the 215 (Moreno Valley)','Jack Rabbit Tr',)),
             (('6.94279','The 91','WB','the 215/60','the 15',),
             ('6.94278','The 91','EB','the 15','the 215/60',)),
             (('6.94337','The 215','SB','the 60','the 15 (Murrieta)',),
             ('6.94336','The 215','NB','the 15 (Murrieta)','the 60',)),
             (('6.94329','The 15','SB','the 91','the 215 (Murrieta)',),
             ('6.94328','The 15','NB','the 215 (Murrieta)','the 91',)),
             (('6.94267','The 60','WB','the 215/91','the 15',),
             ('6.94266','The 60','EB','the 15','the 215/91',)),
             (('6.94277','The 91','WB','the 15','the 5',),
             ('6.94276','The 91','EB','the 5','the 15',)),
]
d.routeDisplayTime=[
(             ((0,00),(0,59),1,1),
             ((1,00),(1,59),0,1),
             ((2,00),(2,59),0,1),
             ((3,00),(3,59),0,1),
             ((4,00),(4,59),0,1),
             ((5,00),(5,59),0,0),
             ((6,00),(6,59),0,0),
             ((7,00),(7,59),0,0),
             ((8,00),(8,59),0,0),
             ((9,00),(9,59),0,0),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),1,1),
             ((14,00),(14,59),1,1),
             ((15,00),(15,59),1,0),
             ((16,00),(16,59),1,0),
             ((17,00),(17,59),1,0),
             ((18,00),(18,59),1,0),
             ((19,00),(19,59),1,0),
             ((20,00),(20,59),1,0),
             ((21,00),(21,59),1,1),
             ((22,00),(22,59),1,1),
             ((23,00),(23,59),1,1),
),
(             ((0,00),(0,59),0,1),
             ((1,00),(1,59),0,1),
             ((2,00),(2,59),0,1),
             ((3,00),(3,59),0,1),
             ((4,00),(4,59),0,1),
             ((5,00),(5,59),0,0),
             ((6,00),(6,59),0,0),
             ((7,00),(7,59),0,0),
             ((8,00),(8,59),0,0),
             ((9,00),(9,59),0,0),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),1,1),
             ((14,00),(14,59),1,1),
             ((15,00),(15,59),1,0),
             ((16,00),(16,59),1,0),
             ((17,00),(17,59),1,0),
             ((18,00),(18,59),1,0),
             ((19,00),(19,59),1,0),
             ((20,00),(20,59),1,0),
             ((21,00),(21,59),1,1),
             ((22,00),(22,59),1,1),
             ((23,00),(23,59),1,1),
),
(             ((0,00),(0,59),0,1),
             ((1,00),(1,59),0,1),
             ((2,00),(2,59),0,1),
             ((3,00),(3,59),0,1),
             ((4,00),(4,59),0,1),
             ((5,00),(5,59),0,0),
             ((6,00),(6,59),0,0),
             ((7,00),(7,59),0,0),
             ((8,00),(8,59),0,0),
             ((9,00),(9,59),0,0),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),1,1),
             ((14,00),(14,59),1,1),
             ((15,00),(15,59),1,0),
             ((16,00),(16,59),1,0),
             ((17,00),(17,59),1,0),
             ((18,00),(18,59),1,0),
             ((19,00),(19,59),1,0),
             ((20,00),(20,59),1,0),
             ((21,00),(21,59),1,1),
             ((22,00),(22,59),1,1),
             ((23,00),(23,59),1,1),
),
(             ((0,00),(0,59),0,1),
             ((1,00),(1,59),0,1),
             ((2,00),(2,59),0,1),
             ((3,00),(3,59),0,1),
             ((4,00),(4,59),0,1),
             ((5,00),(5,59),0,0),
             ((6,00),(6,59),0,0),
             ((7,00),(7,59),0,0),
             ((8,00),(8,59),0,0),
             ((9,00),(9,59),0,0),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),1,1),
             ((14,00),(14,59),1,1),
             ((15,00),(15,59),1,0),
             ((16,00),(16,59),1,0),
             ((17,00),(17,59),1,0),
             ((18,00),(18,59),1,0),
             ((19,00),(19,59),1,0),
             ((20,00),(20,59),1,0),
             ((21,00),(21,59),1,1),
             ((22,00),(22,59),1,1),
             ((23,00),(23,59),1,1),
),
(             ((0,00),(0,59),0,1),
             ((1,00),(1,59),0,1),
             ((2,00),(2,59),0,1),
             ((3,00),(3,59),0,1),
             ((4,00),(4,59),0,1),
             ((5,00),(5,59),0,0),
             ((6,00),(6,59),0,0),
             ((7,00),(7,59),0,0),
             ((8,00),(8,59),0,0),
             ((9,00),(9,59),0,0),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),1,1),
             ((14,00),(14,59),1,1),
             ((15,00),(15,59),1,0),
             ((16,00),(16,59),1,0),
             ((17,00),(17,59),1,0),
             ((18,00),(18,59),1,0),
             ((19,00),(19,59),1,0),
             ((20,00),(20,59),1,0),
             ((21,00),(21,59),1,1),
             ((22,00),(22,59),1,1),
             ((23,00),(23,59),1,1),
),
(             ((0,00),(0,59),0,2),
             ((1,00),(1,59),0,2),
             ((2,00),(2,59),0,2),
             ((3,00),(3,59),0,2),
             ((4,00),(4,59),0,2),
             ((5,00),(5,59),0,2),
             ((6,00),(6,59),0,2),
             ((7,00),(7,59),0,1),
             ((8,00),(8,59),0,1),
             ((9,00),(9,59),0,1),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),0,1),
             ((14,00),(14,59),0,1),
             ((15,00),(15,59),0,1),
             ((16,00),(16,59),0,1),
             ((17,00),(17,59),0,1),
             ((18,00),(18,59),0,1),
             ((19,00),(19,59),0,1),
             ((20,00),(20,59),0,1),
             ((21,00),(21,59),0,2),
             ((22,00),(22,59),0,2),
             ((23,00),(23,59),0,2),
),
(             ((0,00),(0,59),0,2),
             ((1,00),(1,59),0,2),
             ((2,00),(2,59),0,2),
             ((3,00),(3,59),0,2),
             ((4,00),(4,59),0,2),
             ((5,00),(5,59),0,2),
             ((6,00),(6,59),0,2),
             ((7,00),(7,59),0,1),
             ((8,00),(8,59),0,1),
             ((9,00),(9,59),0,1),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),0,1),
             ((14,00),(14,59),0,1),
             ((15,00),(15,59),0,1),
             ((16,00),(16,59),0,1),
             ((17,00),(17,59),0,1),
             ((18,00),(18,59),0,1),
             ((19,00),(19,59),0,1),
             ((20,00),(20,59),0,1),
             ((21,00),(21,59),0,2),
             ((22,00),(22,59),0,2),
             ((23,00),(23,59),0,2),
),
]
dsm.set('Config.1.Ldl_TrafficTripTimes', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Riverside-Moreno Valley-Perris'
d.coopId = '72286000'
dsm.set('Config.1.Fcst_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.mapName = ['6.3','6.4','6.2',]
d.locName = ['LOS ANGELES AREA','LOS ANGELES AREA','LOS ANGELES AREA',]
d.activeVocalCue = 1
dsm.set('Config.1.Local_TrafficOverview', d, 0, 1)
#
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.1.Ldl_LocalStarIDMessage', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'T72286000'
d.locName = 'MARCH FIELD'
d.heatIndexThreshold = 102
dsm.set('Config.1.Local_HeatSafetyTips', d, 0, 1)
#
#
d = twc.Data()
d.zone = 'CAZ048'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_NWSHeadlines', d, 0, 1)
#
#
d = twc.Data()
d.location = 'RIVERSIDE-MORENO VALLEY-PERRIS'
d.coopId = '72286000'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'RIVERSIDE-MORENO VALLEY-PERRIS'
d.coopId = '72286000'
d.activeVocalCue = 1
dsm.set('Config.1.Local_7DayForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'GREATER LOS ANGELES'
d.maxPages = 3
d.activeVocalCue = 0
d.metroId=['6',]
d.latLongBoxes=[
             ((-117.54959157037908,33.47121253704404),(-117.03749485610433,33.85451846090238)),
             ((-117.54039222820649,33.783990170912446),(-117.04362775088606,34.02317306740006)),
]
d.severityList=[
             ('Incident',2,),
             ('Construction',1,),
             ('Unspecified',1,),
]
dsm.set('Config.1.Local_TrafficReport', d, 0, 1)
#
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.1.Ldl_NationalStarIDMessage', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','T72286000','KRIV',]
d.locName = ['Perris','RIVERSIDE - MARCH FIELD','RIVERSIDE - MARCH FIELD',]
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'RIVERSIDE-MORENO VALLEY-PERRIS'
d.coopId = '72286000'
d.maxPageDuration = 14
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72286000','KRIV',]
d.schedule = [((11,22,16,0,0), (11,24,16,0,0)),((12,15,16,0,0), (1,5,16,0,0)),((5,18,16,0,0), (9,3,16,0,0)),]
d.coopId = '72286000'
dsm.set('Config.1.Local_SchoolDayWeather', d, 0, 1)
#
#
d = twc.Data()
d.climId = '048655'
d.latitude = 33.7167
d.longitude = -117.1833
dsm.set('Config.1.Ldl_SunriseSunset', d, 0, 1)
#
#
d = twc.Data()
d.airportId = ['ONT','SNA','LGB',]
d.obsStation = ['T72286049','T72297055','T72297000',]
d.locName = ['Ontario Int\'l','J. Wayne Arpt','Long Beach Arpt',]
d.displayFlag = [1,1,1,]
dsm.set('Config.1.Ldl_AirportDelayConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['RIVERSIDE-MORENO VALLEY-PERRIS',]
d.coopId = ['72286000',]
dsm.set('Config.1.Local_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KRAL',]
d.climId = ['047470',]
d.latitude = 33.95
d.longitude = -117.38
d.locName = ['Riverside',]
d.coopId = ['72286016',]
d.fcstHighOffset = 0
d.fcstLowOffset = 0
dsm.set('Config.1.Local_RecordHighLow', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','T72286000','KRIV',]
d.timeDuration = 5
d.tempDuration = 8
dsm.set('Config.1.TimeTemp_Default', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Moreno Valley'
d.startDate = (5,1)
d.endDate = (9,30)
d.coopId = '72286000'
dsm.set('Config.1.Ldl_UVForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Moreno Valley'
d.coopId = '72286000'
dsm.set('Config.1.Ldl_ExtendedForecast', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Ldl_HourlyForecast', d, 0, 1)
dsm.set('Config.1.Ldl_Shortcast', d, 0, 1)
dsm.set('Config.1.Ldl_SummaryForecast', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['SENSOR','T72286000','KRIV',]
d.obsLocName = ['Perris','Riverside - March Field','March Field',]
dsm.set('Config.1.Ldl_CurrentApparentTemp', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Ldl_CurrentCeiling', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentDewpoint', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentGusts', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentHumidity', d, 0, 1)
ds.commit()
dsm.set('Config.1.Ldl_CurrentPressure', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentSkyTemp', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentVisibility', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentWinds', d, 0, 1)
#
d = twc.Data()
d.locName = 'Riverside Co.'
d.startDate = (1,1)
d.endDate = (12,31)
d.aq = 'ca058'
dsm.set('Config.1.Ldl_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.locNameList = ['Big Bear Lake, CA','Las Vegas, NV','Yosemite N.P., CA',]
d.coopId = ['72286067','72386000','72481041',]
dsm.set('Config.1.Local_GetawayForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Riverside-Moreno Valley-Perris'
d.coopId = '72286000'
dsm.set('Config.1.Fcst_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.coopId = '72286000'
dsm.set('Config.1.Local_OutdoorActivityForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KRIV','KRAL',]
d.obsLocName = ['Riverside - March Field','Riverside',]
dsm.set('Config.1.Ldl_CurrentMTDPrecip', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'KRAL'
d.climId = ['047470',]
d.latitude = 33.95
d.longitude = -117.38
d.locName = 'RIVERSIDE'
d.coopId = '72286016'
dsm.set('Config.1.Local_Climatology', d, 0, 1)
#
#
# Product statues:
d = twc.Data()
d.activeLocal_AirQualityForecast = 1
d.activeLocal_Climatology = 1
d.activeLocal_GetawayForecast = 1
d.activeLocal_HeatSafetyTips = 1
d.activeLocal_MarineForecast = 0
d.activeLocal_MetroDopplerRadar = 1
d.activeLocal_MetroForecastMap = 1
d.activeLocal_MetroObservationMap = 1
d.activeLocal_OutdoorActivityForecast = 1
d.activeLocal_RadarSatelliteComposite = 0
d.activeLocal_RecordHighLow = 1
d.activeLocal_Satellite = 1
d.activeLocal_SchoolDayWeather = 1
d.activeLocal_Tides = 0
d.activeLocal_TrafficFlow = 1
d.activeLocal_TrafficOverview = 1
d.activeLocal_TrafficReport = 1
# region keys
dsm.set('Config.1.SouthernCalifornia.90.1', d, 0)
dsm.set('Config.1.SouthernCalifornia.120.0', d, 0)
dsm.set('Config.1.SouthernCalifornia.120.2', d, 0)
dsm.set('Config.1.SouthernCalifornia.60.0', d, 0)
dsm.set('Config.1.DefaultUS.120.2', d, 0)
dsm.set('Config.1.DefaultUS.60.1', d, 0)
dsm.set('Config.1.SouthernCalifornia.60.1', d, 0)
dsm.set('Config.1.SouthernCalifornia.90.0', d, 0)
dsm.set('Config.1.SouthernCalifornia.120.1', d, 0)
dsm.set('Config.1.DefaultUS.90.1', d, 0)
dsm.set('Config.1.DefaultUS.90.0', d, 0)
dsm.set('Config.1.DefaultUS.60.0', d, 0)
dsm.set('Config.1.DefaultUS.120.1', d, 0)
dsm.set('Config.1.DefaultUS.120.0', d, 0)
#
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,6,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,9,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,30,30,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,10,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.SouthernCalifornia.90.0', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,7,8,7,1,1,8,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,7,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,3,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,3,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,5,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,8,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,36,36,28,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,11,12,7,1,2,7,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,11,12,7,1,2,2,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,11,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,2,2,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,7,8,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.SouthernCalifornia.120.2', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,3,2,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,4,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,7,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,20,20,16,0,2,2,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,12,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.60.1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,3,2,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,4,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,7,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,20,20,16,0,2,2,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,12,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.SouthernCalifornia.60.1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,7,8,7,1,1,8,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,7,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,5,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,5,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,7,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,4,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,36,36,28,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,11,12,7,1,2,7,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,11,12,7,1,2,2,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,11,12,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,2,2,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,7,8,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.SouthernCalifornia.120.1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,7,8,7,1,1,8,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,7,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,5,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,5,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,8,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,36,36,28,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,11,12,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,11,12,7,1,2,7,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,11,12,7,1,6,8,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.120.2', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,3,2,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,4,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,7,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,20,20,16,0,2,2,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,12,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.60.0', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,3,2,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,4,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,7,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,20,20,16,0,2,2,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,12,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.SouthernCalifornia.60.0', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,7,8,7,1,1,8,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,7,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,6,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,6,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,4,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,4,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,5,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,8,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,36,36,28,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,11,12,7,1,2,7,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,11,12,7,1,2,2,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,11,12,7,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,3,2,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,4,8,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.SouthernCalifornia.120.0', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,7,8,7,1,1,8,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,7,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,5,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,5,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,7,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,4,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,36,36,28,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,11,12,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,11,12,7,1,2,7,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,11,12,7,1,6,8,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.120.1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,6,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,9,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,30,30,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,10,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.90.1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,7,8,7,1,1,8,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,7,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,6,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,4,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,4,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,5,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,8,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,36,36,28,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,11,12,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,11,12,7,1,2,7,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,11,12,7,1,6,8,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.120.0', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,6,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,9,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,30,30,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,10,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.SouthernCalifornia.90.1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,6,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,9,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,30,30,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,10,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.90.0', d, 0)
ds.commit()
#
d = twc.Data()
d.prodPrefix='Local'
d.childPrefixes=["Cc", "Radar", "Fcst", "Logo"]
d.units='percent'
d.loadHeuristic='loadPriority_v1'
d.overHeuristic='overPriority_v1'
d.underHeuristic='underPriority_v1'
d.playlist=[
('SqueezebackFade',0,100,100,100,1,1,0,["cc1","radar1","fcst1","logo1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.57.0', d, 0)
#
ds.commit()
d = twc.Data()
d.prodPrefix='Local'
d.childPrefixes=["Cc", "Radar", "Fcst", "Logo"]
d.units='percent'
d.loadHeuristic='loadPriority_v1'
d.overHeuristic='overPriority_v1'
d.underHeuristic='underPriority_v1'
d.playlist=[
('SqueezebackFade',0,100,100,100,1,1,0,["cc1","radar1","fcst1","logo1"]),
]
dsm.set('Config.1.Playlist.SouthernCalifornia.57.0', d, 0)
#
ds.commit()
d = twc.Data()
d.prodPrefix='Fcst'
d.childPrefixes=[]
d.units='seconds'
d.loadHeuristic='loadPriorityOneOnly_v1'
d.overHeuristic='overPriority_v1'
d.underHeuristic='underPriority_v1'
d.playlist=[
('TextForecast.1',0,14,60,14,1,1,0,[]),
('TextForecast.2',0,14,60,14,1,1,0,[]),
('DaypartForecast',0,14,60,14,1,1,0,[]),
('ExtendedForecast',0,14,60,14,1,1,0,[]),
('Unavailable',0,1,60,1,1,2,0,[]),
]
dsm.set('Config.1.Playlist.Fcst.fcst1', d, 0)
#
ds.commit()
#
# End of SCMT deployment
#
ds.commit()
Log.info('scmt config finished')
# Finished generation on Thu Feb 08 10:38:21 EST 2007
