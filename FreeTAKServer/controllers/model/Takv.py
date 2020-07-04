#######################################################
# 
# Takv.py
# Python implementation of the Class Takv
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:09 AM
# Original author: Corvo
# 
#######################################################


class Takv:



  # default constructor       
  def __init__(self):
    # the version of TAK running on the device
    self.version = "3.12.0-45691.45691-CIV" 
    # the variant of TAK
    self.platform = "ATAK-CIV" 
    # type of physical device
    self.device = "Pirate Device" 
    # the operating system running TAK
    self.os = "Linux" 

    # os getter 
  def getos(self): 
    return self.os 

    # os setter 
  def setos(self,os=0):  
    self.os=os 


    # version getter 
  def getversion(self): 
    return self.version 

    # version setter 
  def setversion(self, version=0):  
    self.version=version 
    

  def getplatform(self): 
      return self.platform 

    # platform setter 
  def setplatform(self, platform=0):  
      self.platform=platform 

  # device getter 
  def getdevice(self): 
    return self.device 

  # device setter 
  def setdevice(self, device=0):  
    self.device=device 
