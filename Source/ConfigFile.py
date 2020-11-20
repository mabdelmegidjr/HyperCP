
import collections
import json
import os
import shutil

class ConfigFile:
    filename = ""
    settings = collections.OrderedDict()
    products = collections.OrderedDict()

    @staticmethod
    def printd():
        print("ConfigFile - Printd")
        print("bL1aCleanSZA", ConfigFile.settings["bL1aCleanSZA"])
        print("fL1aCleanSZAMax", ConfigFile.settings["fL1aCleanSZAMax"])

        print("bL1cSolarTracker", ConfigFile.settings["bL1cSolarTracker"]) 
        print("fL1cRotatorHomeAngle", ConfigFile.settings["fL1cRotatorHomeAngle"])
        print("bL1cRotatorDelay", ConfigFile.settings["bL1cRotatorDelay"]) 
        print("fL1cRotatorDelay", ConfigFile.settings["fL1cRotatorDelay"]) 
        print("bL1cCleanPitchRoll", ConfigFile.settings["bL1cCleanPitchRoll"])
        print("fL1cPitchRollPitch", ConfigFile.settings["fL1cPitchRollPitch"]) 
        print("fL1cPitchRollRoll", ConfigFile.settings["fL1cPitchRollRoll"]) 
        print("bL1cRotatorAngle", ConfigFile.settings["bL1cRotatorAngle"])
        print("fL1cRotatorAngleMin", ConfigFile.settings["fL1cRotatorAngleMin"])
        print("fL1cRotatorAngleMax", ConfigFile.settings["fL1cRotatorAngleMax"])
        print("bL1cCleanSunAngle", ConfigFile.settings["bL1cCleanSunAngle"])
        print("fL1cSunAngleMin", ConfigFile.settings["fL1cSunAngleMin"])
        print("fL1cSunAngleMax", ConfigFile.settings["fL1cSunAngleMax"])

        print("bL1dDeglitch", ConfigFile.settings["bL1dDeglitch"])
        print("fL1dDeglitch0", ConfigFile.settings["fL1dDeglitch0"])
        print("fL1dDeglitch1", ConfigFile.settings["fL1dDeglitch1"])
        print("fL1dDeglitch2", ConfigFile.settings["fL1dDeglitch2"])
        print("fL1dDeglitch3", ConfigFile.settings["fL1dDeglitch3"])
        print("bL1dAnomalyStep", ConfigFile.settings["bL1dAnomalyStep"])   
        print("bL1dPlotEs", ConfigFile.settings["bL1dPlotEs"])
        print("bL1dPlotLi", ConfigFile.settings["bL1dPlotLi"])
        print("bL1dPlotLt", ConfigFile.settings["bL1dPlotLt"])

        print("fL1eInterpInterval", ConfigFile.settings["fL1eInterpInterval"])
        print("bL1ePlotTimeInterp", ConfigFile.settings["bL1ePlotTimeInterp"])
        print("bL1eSaveSeaBASS", ConfigFile.settings["bL1eSaveSeaBASS"])
        print("seaBASSHeaderFileName", ConfigFile.settings["seaBASSHeaderFileName"])

        print("bL2pGetAnc", ConfigFile.settings["bL2pGetAnc"])
        print("bL2pObpgCreds", ConfigFile.settings["bL2pObpgCreds"])

        print("bL2LtUVNIR", ConfigFile.settings["bL2LtUVNIR"])
        print("fL2MaxWind", ConfigFile.settings["fL2MaxWind"])
        print("fL2SZAMin", ConfigFile.settings["fL2SZAMin"])
        print("fL2SZAMax", ConfigFile.settings["fL2SZAMax"])
        
        print("bL2EnableSpecQualityCheck", ConfigFile.settings["bL2EnableSpecQualityCheck"])
        print("fL2SpecFilterEs", ConfigFile.settings["fL2SpecFilterEs"])
        print("fL2SpecFilterLi", ConfigFile.settings["fL2SpecFilterLi"])
        print("fL2SpecFilterLt", ConfigFile.settings["fL2SpecFilterLt"])
        
        print("bL2EnableQualityFlags", ConfigFile.settings["bL2EnableQualityFlags"])
        print("fL2CloudFlag", ConfigFile.settings["fL2CloudFlag"])
        print("fL2SignificantEsFlag", ConfigFile.settings["fL2SignificantEsFlag"])
        print("fL2DawnDuskFlag", ConfigFile.settings["fL2DawnDuskFlag"])
        print("fL2RainfallHumidityFlag", ConfigFile.settings["fL2RainfallHumidityFlag"]) 

        print("fL2TimeInterval", ConfigFile.settings["fL2TimeInterval"])
        print("bL2EnablePercentLt", ConfigFile.settings["bL2EnablePercentLt"])
        print("fL2PercentLt", ConfigFile.settings["fL2PercentLt"])

        print("fL2RhoSky", ConfigFile.settings["fL2RhoSky"])
        print("fL2DefaultWindSpeed", ConfigFile.settings["fL2DefaultWindSpeed"])   
        print("fL2DefaultAOD", ConfigFile.settings["fL2DefaultAOD"])
        print("fL2DefaultSalt", ConfigFile.settings["fL2DefaultSalt"])
        print("fL2DefaultSST", ConfigFile.settings["fL2DefaultSST"])
        print("bL2RuddickRho", ConfigFile.settings["bL2RuddickRho"])
        print("bL2ZhangRho", ConfigFile.settings["bL2ZhangRho"])                                            
        print("bL2DefaultRho", ConfigFile.settings["bL2DefaultRho"])
        
        print("bL2PerformNIRCorrection", ConfigFile.settings["bL2PerformNIRCorrection"])        
        print("bL2SimpleNIRCorrection", ConfigFile.settings["bL2SimpleNIRCorrection"])    
        print("bL2SimSpecNIRCorrection", ConfigFile.settings["bL2SimSpecNIRCorrection"])

        print("bL2NegativeSpec", ConfigFile.settings["bL2NegativeSpec"])
        
        print("bL2WeightMODISA", ConfigFile.settings["bL2WeightMODISA"])
        print("bL2WeightSentinel3A", ConfigFile.settings["bL2WeightSentinel3A"])
        print("bL2WeightVIIRSN", ConfigFile.settings["bL2WeightVIIRSN"])
        print("bL2WeightMODISA", ConfigFile.settings["bL2WeightMODIST"])
        print("bL2WeightSentinel3A", ConfigFile.settings["bL2WeightSentinel3B"])
        print("bL2WeightVIIRSN", ConfigFile.settings["bL2WeightVIIRSJ"])

        print("bL2PlotRrs", ConfigFile.settings["bL2PlotRrs"])
        print("bL2PlotnLw", ConfigFile.settings["bL2PlotnLw"])
        print("bL2PlotEs", ConfigFile.settings["bL2PlotEs"])
        print("bL2PlotLi", ConfigFile.settings["bL2PlotLi"])
        print("bL2PlotLt", ConfigFile.settings["bL2PlotLt"])

        print("bL2Prodoc3m", ConfigFile.products["bL2Prodoc3m"])
        # print("bL2Prodaot", ConfigFile.products["bL2Prodaot"])
        print("bL2Prodkd490", ConfigFile.products["bL2Prodkd490"])
        print("bL2Prodpic", ConfigFile.products["bL2Prodpic"])
        print("bL2Prodpoc", ConfigFile.products["bL2Prodpoc"])
        print("bL2Prodipar", ConfigFile.products["bL2Prodipar"])
        print("bL2Prodavw", ConfigFile.products["bL2Prodavw"])

        print("bL2Prodgocad", ConfigFile.products["bL2Prodgocad"])
        print("bL2Prodag", ConfigFile.products["bL2Prodag"])
        # print("bL2Prodag275", ConfigFile.products["bL2Prodag275"])
        # print("bL2Prodag355", ConfigFile.products["bL2Prodag355"])
        # print("bL2Prodag380", ConfigFile.products["bL2Prodag380"])
        # print("bL2Prodag412", ConfigFile.products["bL2Prodag412"])
        # print("bL2Prodag443", ConfigFile.products["bL2Prodag443"])
        # print("bL2Prodag488", ConfigFile.products["bL2Prodag488"])
        print("bL2ProdSg", ConfigFile.products["bL2ProdSg"])
        # print("bL2ProdSg275", ConfigFile.products["bL2ProdSg275"])
        # print("bL2ProdSg300", ConfigFile.products["bL2ProdSg300"])
        # print("bL2ProdSg412", ConfigFile.products["bL2ProdSg412"])
        print("bL2ProdDOC", ConfigFile.products["bL2ProdDOC"])


        print("bL2Prodgiop", ConfigFile.products["bL2Prodgiop"])
        print("bL2ProdaGiop", ConfigFile.products["bL2ProdaGiop"])
        print("bL2ProdadgGiop", ConfigFile.products["bL2ProdadgGiop"])
        print("bL2ProdadgSGiop", ConfigFile.products["bL2ProdadgSGiop"])
        print("bL2ProdaphGiop", ConfigFile.products["bL2ProdaphGiop"])
        print("bL2ProdaphSGiop", ConfigFile.products["bL2ProdaphSGiop"])
        print("bL2ProdbbGiop", ConfigFile.products["bL2ProdbbGiop"])
        print("bL2ProdbbpGiop", ConfigFile.products["bL2ProdbbpGiop"])
        print("bL2ProdbbpSGiop", ConfigFile.products["bL2ProdbbpSGiop"])
        print("bL2Prodqaa", ConfigFile.products["bL2Prodqaa"])
        print("bL2ProdaQaa", ConfigFile.products["bL2ProdaQaa"])
        print("bL2ProdadgQaa", ConfigFile.products["bL2ProdadgQaa"])
        print("bL2ProdaphQaa", ConfigFile.products["bL2ProdaphQaa"])
        print("bL2ProdbQaa", ConfigFile.products["bL2ProdbQaa"])
        print("bL2ProdbbQaa", ConfigFile.products["bL2ProdbbQaa"])
        print("bL2ProdbbpQaa", ConfigFile.products["bL2ProdbbpQaa"])
        print("bL2ProdcQaa", ConfigFile.products["bL2ProdcQaa"])

        print("bL2SaveSeaBASS", ConfigFile.settings["bL2SaveSeaBASS"])


    # Creates the calibration file folder if not exist
    @staticmethod
    def createCalibrationFolder():
        #print("ConfigFile - createCalibrationFolder")
        fp = ConfigFile.getCalibrationDirectory()
        os.makedirs(fp, exist_ok=True)


    # Generates the default configuration
    @staticmethod
    def createDefaultConfig(name):
        print("ConfigFile - Create Default Config")

        if not name.endswith(".cfg"):
            name = name + ".cfg"
        ConfigFile.filename = name

        ConfigFile.settings["CalibrationFiles"] = {}

        ConfigFile.settings["bL1aCleanSZA"] = 0
        ConfigFile.settings["fL1aCleanSZAMax"] = 60.0 # e.g. 60:Brewin 2016, 

        ConfigFile.settings["bL1cSolarTracker"] = 1 
        ConfigFile.settings["bL1cCleanPitchRoll"] = 0
        ConfigFile.settings["fL1cPitchRollPitch"] = 5 # 2-5 deg. IOCCG Draft Protocols
        ConfigFile.settings["fL1cPitchRollRoll"] = 5 # 2-5 deg. IOCCG Draft Protocols
        ConfigFile.settings["fL1cRotatorHomeAngle"] = 0.0 # Require knowledge of deployment set-up
        ConfigFile.settings["bL1cRotatorDelay"] = 0 
        ConfigFile.settings["fL1cRotatorDelay"] = 60.0 # Vandenberg 2016
        ConfigFile.settings["bL1cRotatorAngle"] = 0
        ConfigFile.settings["fL1cRotatorAngleMin"] = -40.0 # Require knowledge of deployment set-up
        ConfigFile.settings["fL1cRotatorAngleMax"] = 40.0 # Require knowledge of deployment set-up
        ConfigFile.settings["bL1cCleanSunAngle"] = 0
        ConfigFile.settings["fL1cSunAngleMin"] = 90.0 # Zhang 2017: 45*, Mobley 1999: 90, Zibordi 2009 (and IOCCG Protocols): 90
        ConfigFile.settings["fL1cSunAngleMax"] = 135.0 # Zhang 2017: 90*, Mobley 1999: 135, Zibordi 2009 (and IOCCG Protocols): 90        

        ConfigFile.settings["bL1dDeglitch"] = 0
        ConfigFile.settings["fL1dDeglitch0"] = 9   # These can be experimentally derived with the AnomalyDetection tool
        ConfigFile.settings["fL1dDeglitch1"] = 11     
        ConfigFile.settings["fL1dDeglitch2"] = 2.7
        ConfigFile.settings["fL1dDeglitch3"] = 3.7
        ConfigFile.settings["bL1dAnomalyStep"] = 3
        ConfigFile.settings["bL1dPlotEs"] = 0
        ConfigFile.settings["bL1dPlotLi"] = 0
        ConfigFile.settings["bL1dPlotLt"] = 0

        ConfigFile.settings["fL1eInterpInterval"] = 3.5 # Brewin 2016 uses 3.5 nm
        ConfigFile.settings["bL1ePlotTimeInterp"] = 0
        ConfigFile.settings["bL1eSaveSeaBASS"] = 0
        ConfigFile.settings["seaBASSHeaderFileName"] = os.path.splitext(name)[0] + ".hdr" # 

        ConfigFile.settings["bL2pGetAnc"] = 0
        ConfigFile.settings["bL2pObpgCreds"] = 0
                
        ConfigFile.settings["bL2LtUVNIR"] = 1
        ConfigFile.settings["fL2MaxWind"] = 7.0 # 6-7 m/s: IOCCG Draft Protocols, D'Alimonte pers. comm. 2019; 10 m/s: NASA SeaWiFS Protocols; 15 m/s: Zibordi 2009, 
        ConfigFile.settings["fL2SZAMin"] = 20 # e.g. 20: Zhang 2017, depends on wind
        ConfigFile.settings["fL2SZAMax"] = 60 # e.g. 60:Brewin 2016,
        
        ConfigFile.settings["bL2EnableSpecQualityCheck"] = 1
        ConfigFile.settings["fL2SpecFilterEs"] = 5
        ConfigFile.settings["fL2SpecFilterLi"] = 8
        ConfigFile.settings["fL2SpecFilterLt"] = 3

        ConfigFile.settings["bL2EnableQualityFlags"] = 1
        ConfigFile.settings["fL2CloudFlag"] = 1.0 # 1.0 basically disregards this, though cloud cover can still be used in glint correction; 0.05 Ruddick 2006, IOCCG Protocols
        ConfigFile.settings["fL2SignificantEsFlag"] = 2.0 # Wernand 2002
        ConfigFile.settings["fL2DawnDuskFlag"] = 1.0 # Wernand 2002
        ConfigFile.settings["fL2RainfallHumidityFlag"] = 1.095  # ?? Wang? # Wernand 2002 uses Es(940/370), with >0.25 dry, 0.2-0.25 humid, <=0.25 rain      

        ConfigFile.settings["bL2Stations"] = 0
        ConfigFile.settings["fL2TimeInterval"] = 300
        ConfigFile.settings["bL2EnablePercentLt"] = 0
        ConfigFile.settings["fL2PercentLt"] = 5 # 5% Hooker et al. 2002, Hooker and Morel 2003; <10% IOCCG Protocols

        ConfigFile.settings["fL2RhoSky"] = 0.0256 # Mobley 1999
        ConfigFile.settings["fL2DefaultWindSpeed"] = 5.0        
        ConfigFile.settings["fL2DefaultAOD"] = 0.5
        ConfigFile.settings["fL2DefaultSalt"] = 35.0
        ConfigFile.settings["fL2DefaultSST"] = 26.0
        ConfigFile.settings["bL2RuddickRho"] = 1
        ConfigFile.settings["bL2ZhangRho"] = 0        
        ConfigFile.settings["bL2DefaultRho"] = 0   
                
        ConfigFile.settings["bL2PerformNIRCorrection"] = 1
        ConfigFile.settings["bL2SimpleNIRCorrection"] = 0 # Mobley 1999 adapted to minimum 700-800, not 750 nm
        ConfigFile.settings["bL2SimSpecNIRCorrection"] = 1 # Ruddick 2005, Ruddick 2006 similarity spectrum

        ConfigFile.settings["bL2NegativeSpec"] = 1
       
        ConfigFile.settings["bL2WeightMODISA"] = 0
        ConfigFile.settings["bL2WeightSentinel3A"] = 0
        ConfigFile.settings["bL2WeightVIIRSN"] = 0        
        ConfigFile.settings["bL2WeightMODIST"] = 0
        ConfigFile.settings["bL2WeightSentinel3B"] = 0
        ConfigFile.settings["bL2WeightVIIRSJ"] = 0        
        ConfigFile.settings["bL2PlotRrs"] = 0
        ConfigFile.settings["bL2PlotnLw"] = 0
        ConfigFile.settings["bL2PlotEs"] = 0
        ConfigFile.settings["bL2PlotLi"] = 0
        ConfigFile.settings["bL2PlotLt"] = 0

        ConfigFile.products["bL2Prodoc3m"] = 0
        # ConfigFile.products["bL2Prodaot"] = 0
        ConfigFile.products["bL2Prodkd490"] = 0
        ConfigFile.products["bL2Prodpic"] = 0
        ConfigFile.products["bL2Prodpoc"] = 0
        ConfigFile.products["bL2Prodipar"] = 0
        ConfigFile.products["bL2Prodavw"] = 0

        ConfigFile.products["bL2Prodgocad"] = 0
        ConfigFile.products["bL2Prodag"] = 0
        # ConfigFile.products["bL2Prodag275"] = 0        
        # ConfigFile.products["bL2Prodag355"] = 0
        # ConfigFile.products["bL2Prodag380"] = 0
        # ConfigFile.products["bL2Prodag412"] = 0
        # ConfigFile.products["bL2Prodag443"] = 0
        # ConfigFile.products["bL2Prodag488"] = 0
        ConfigFile.products["bL2ProdSg"] = 0
        # ConfigFile.products["bL2ProdSg275"] = 0        
        # ConfigFile.products["bL2ProdSg300"] = 0
        # ConfigFile.products["bL2ProdSg412"] = 0
        ConfigFile.products["bL2ProdDOC"] = 0

        ConfigFile.products["bL2Prodgiop"] = 0
        ConfigFile.products["bL2ProdaGiop"] = 0
        ConfigFile.products["bL2ProdadgGiop"] = 0
        ConfigFile.products["bL2ProdadgSGiop"] = 0
        ConfigFile.products["bL2ProdaphGiop"] = 0
        ConfigFile.products["bL2ProdaphSGiop"] = 0
        ConfigFile.products["bL2ProdbbGiop"] = 0
        ConfigFile.products["bL2ProdbbpGiop"] = 0
        ConfigFile.products["bL2ProdbbpSGiop"] = 0
        ConfigFile.products["bL2Prodqaa"] = 0
        ConfigFile.products["bL2ProdaQaa"] = 0
        ConfigFile.products["bL2ProdadgQaa"] = 0
        ConfigFile.products["bL2ProdaphQaa"] = 0
        ConfigFile.products["bL2ProdbQaa"] = 0
        ConfigFile.products["bL2ProdbbQaa"] = 0
        ConfigFile.products["bL2ProdbbpQaa"] = 0
        ConfigFile.products["bL2ProdcQaa"] = 0

        ConfigFile.settings["bL2SaveSeaBASS"] = 0
        
        ConfigFile.saveConfig(name)


    # Saves the cfg file
    @staticmethod
    def saveConfig(filename):
        print("ConfigFile - Save Config")
        ConfigFile.filename = filename
        params = dict(ConfigFile.settings, **ConfigFile.products)
        jsn = json.dumps(params)        
        fp = os.path.join("Config", filename)

        #print(os.path.abspath(os.curdir))
        with open(fp, 'w') as f:
            f.write(jsn)
        ConfigFile.createCalibrationFolder()

    # Loads the cfg file
    @staticmethod
    def loadConfig(filename):
        # print("ConfigFile - Load Config")
        configPath = os.path.join("Config", filename)
        if os.path.isfile(configPath):
            ConfigFile.filename = filename
            text = ""
            with open(configPath, 'r') as f:
                text = f.read()
                # ConfigFile.settings = json.loads(text, object_pairs_hook=collections.OrderedDict)
                fullCollection = json.loads(text, object_pairs_hook=collections.OrderedDict)

                for key, value in fullCollection.items():
                    if key.startswith("bL2Prod"):
                        ConfigFile.products[key] = value
                    else:
                        ConfigFile.settings[key] = value
                
                ConfigFile.createCalibrationFolder()


    # Deletes a config
    @staticmethod
    def deleteConfig(filename):
        print("ConfigFile - Delete Config")
        configPath = os.path.join("Config", filename)
        if "seaBASSHeaderFileName" in ConfigFile.settings:
            seaBassConfig = os.path.join("Config", ConfigFile.settings["seaBASSHeaderFileName"])
            if os.path.isfile(seaBassConfig):
                os.remove(seaBassConfig)
        if os.path.isfile(configPath):
            ConfigFile.filename = filename
            calibrationPath = ConfigFile.getCalibrationDirectory()
            os.remove(configPath)
            shutil.rmtree(calibrationPath)
        
        

    @staticmethod
    def getCalibrationDirectory():
        # print("ConfigFile - getCalibrationDirectory")
        calibrationDir = os.path.splitext(ConfigFile.filename)[0] + "_Calibration"
        calibrationPath = os.path.join("Config", calibrationDir)
        return calibrationPath

    @staticmethod
    def refreshCalibrationFiles():
        print("ConfigFile - refreshCalibrationFiles")
        calibrationPath = ConfigFile.getCalibrationDirectory()
        files = os.listdir(calibrationPath)

        newCalibrationFiles = {}
        calibrationFiles = ConfigFile.settings["CalibrationFiles"]
        
        for file in files:
            if file in calibrationFiles:
                newCalibrationFiles[file] = calibrationFiles[file]
            else:
                newCalibrationFiles[file] = {"enabled": 0, "frameType": "Not Required"}

        ConfigFile.settings["CalibrationFiles"] = newCalibrationFiles

    @staticmethod
    def setCalibrationConfig(calFileName, enabled, frameType):
        print("ConfigFile - setCalibrationConfig")
        calibrationFiles = ConfigFile.settings["CalibrationFiles"]
        calibrationFiles[calFileName] = {"enabled": enabled, "frameType": frameType}

    @staticmethod
    def getCalibrationConfig(calFileName):
        print("ConfigFile - getCalibrationConfig")
        calibrationFiles = ConfigFile.settings["CalibrationFiles"]
        return calibrationFiles[calFileName]

