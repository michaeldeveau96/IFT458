#!/c/Python27/python
####################################################################################
#	Assignment: PD3
#		File Name: MyClasses.py
#			Author: Michael Deveau
#	Description: Creation of the PD3 classes
####################################################################################
class Manufacturer:
	def __init__(self, name='', registeredCountry='', contactPerson=''):
		self.name = name
		self.registeredCountry = registeredCountry
		self.contactPerson = contactPerson
		
	def getName(self):
		return self.name
	
	def getRegisteredCountry(self):
		return self.registeredCountry
		
	def getContantPerson(self):
		return self.contactPerson
	
class User:
	def __init__(self, username='', password='', firstName='', middleName='', lastName='', address='', officePhone='', cellphone='', email=''):
		self.username = username
		self.password = password
		self.firstName = firstName
		self.middleName = middleName
		self.lastName = lastName
		self.address = address
		self.officePhone = officePhone
		self.cellphone = cellphone
		self.email = email
	
	def getUsername(self):
		return self.username
	
	def getPassword(self):
		return self.password
	
	def getFirstName(self):
		return self.firstName
		
	def setFirstName(self, firstName):
		self.firstName = firstName
	
	def getMiddleName(self):
		return self.middleName
	
	def getLastName(self):
		return self.lastName
		
	def setLastName(self, lastName):
		self.lastName = lastName
	
	def getAddress(self):
		return self.address
	
	def getOfficePhone(self):
		return self.officePhone
	
	def getCellphone(self):
		return self.cellphone
	
	def getEmail(self):
		return self.email
		
	def setEmail(self, email):
		self.email = email

class TestResults:
	def __init__(self, dataSource='', product='', reportingCondition='', testSequence='', testDate='', isc='', voc='', imp='', vmp='', pmp='', ff='', noct=''):
		self.dataSource = dataSource
		self.product = product
		self.reportingCondition = reportingCondition
		self.testSequence = testSequence
		self.testDate = testDate
		self.isc = isc
		self.voc = voc
		self.imp = imp
		self.vmp = vmp
		self.pmp = pmp
		self.ff = ff
		self.noct = noct
	
	def getDataSource(self):
		return self.dataSource
	
	def getProduct(self):
		return self.product
		
	def getReportingCondition(self):
		return self.reportingCondition
		
	def getTestSequence(self):
		return self.testSequence
		
	def getTestDate(self):
		return self.testDate
	
	def getIsc(self):
		return self.isc
		
	def getVoc(self):
		return self.voc
		
	def getImp(self):
		return self.imp
		
	def getVmp(self):
		return self.vmp	
		
	def getPmp(self):
		return self.pmp
		
	def getFf(self):
		return self.ff
		
	def getNoct(self):
		return self.noct
		
class TestLab:
	def __init__(self, name='', address='', contactPerson=''):
		self.name = name
		self.address = address
		self.contactPerson = contactPerson
		
	def getName(self):
		return self.name
	
	def getAddress(self):
		return self.address
	
	def getContantPerson(self):
		return contactPerson
		
	def setContactPerson(self, firstName, lastName):
		return User.firstName + lastName
		
	
class Product:
	def __init__(self, modelNumber='', manufacturer='', manufacturingDate='', length='', width='', weight='', cellArea='', cellTechnology='', totalNumberOfCells='',
		numberOfCellsInSeries='', numberOfSeriesStrings='', numberOfBypassDiodes='', seriesFuseRating='', interconnectMaterial='', interconnectSupplier='', 
		superstrateType='', superStrateManufacturer='', substrateType='', substrateManufacturer='', frameMaterial='', frameAdhesive='', encapsulantType='', 
		encapsulantManufacture='', junctionBoxType='', junctionBoxManufacturer='', junctionBoxAdhesive='', cableType='', connectorType='', maximumSystemVoltage='', 
		ratedVoc='', ratedIsc='', ratedVmp='', ratedImp='', ratedPmp='', ratedFF=''):
		self.modelNumber = modelNumber
		self.manufacturer = manufacturer
		self.manufacturingDate = manufacturingDate
		self.length = length
		self.width = width
		self.weight = weight
		self.cellArea = cellArea
		self.cellTechnology = cellTechnology
		self.totalNumberOfCells = totalNumberOfCells
		self.numberOfCellsInSeries = numberOfCellsInSeries
		self.numberOfSeriesStrings = numberOfSeriesStrings
		self.numberOfBypassDiodes = numberOfBypassDiodes
		self.seriesFuseRating = seriesFuseRating
		self.interconnectMaterial = interconnectMaterial
		self.interconnectSupplier = interconnectSupplier
		self.superstrateType = superstrateType
		self.superStrateManufacturer = superStrateManufacturer
		self.substrateType = substrateType
		self.substrateManufacturer = substrateManufacturer
		self.frameMaterial = frameMaterial
		self.frameAdhesive = frameAdhesive
		self.encapsulantType = encapsulantType
		self.encapsulantManufacture = encapsulantManufacture
		self.junctionBoxType = junctionBoxType
		self.junctionBoxManufacturer = junctionBoxManufacturer
		self.junctionBoxAdhesive = junctionBoxAdhesive
		self.cableType = cableType
		self.connectorType = connectorType
		self.maximumSystemVoltage = maximumSystemVoltage
		self.ratedVoc = ratedVoc
		self.ratedIsc = ratedIsc
		self.ratedVmp = ratedVmp
		self.ratedImp = ratedImp
		self.ratedPmp = ratedPmp
		self.ratedFF = ratedFF
		
	def getModelNumber(self):
		return self.modelNumber
	
	def setModelNumber(self, modelNumber):
		self.modelNumber = modelNumber
		
	def getManufacturer(self):
		return self.manufacturer
		
	def setManufacturer(self, manufacturer):
		self.manufacturer = manufacturer
		
	def getManufacturingDate(self):
		return self.manufacturingDate
		
	def getLength(self):
		return self.length
		
	def getWidth(self):
		return self.width
		
	def getWeight(self):
		return self.weight
		
	def getCellArea(self):
		return self.cellArea
	
	def getCellTechnology(self):
		return self.cellTechnology
		
	def setCellTechnology(self, cellTechnology):
		self.cellTechnology = cellTechnology
	
	def getTotalNumberOfCells(self):
		return self.totalNumberOfCells
		
	def getNumberOfCellsInSeries(self):
		return self.numberOfCellsInSeries
		
	def getNumberOfSeriesStrings(self):
		return self.numberOfSeriesStrings
		
	def getNumberOfBypassDiodes(self):
		return self.numberOfBypassDiodes
	
	def getSeriesFuseRating(self):
		return self.seriesFuseRating
	
	def getInterconnectMaterial(self):
		return self.interconnectMaterial
	
	def getInterconnectSupplier(self):
		return self.interconnectSupplier
		
	def getSuperstrateType(self):
		return self.superstrateType
		
	def getSuperstrateManufacturer(self):
		return self.superStrateManufacturer
		
	def getSubstrateType(self):
		return self.substrateType
		
	def getSubstrateManufacturer(self):
		return self.substrateManufacturer
		
	def getFrameMaterial(self):
		return self.frameMaterial
		
	def getFrameAdhesive(self):
		return self.frameAdhesive
		
	def getEncapsulantType(self):
		return self.encapsulantType
		
	def getEncapsulantManufacturer(self):
		return self.encapsulantManufacture
		
	def getJunctionBoxType(self):
		return self.junctionBoxType
		
	def getJunctionBoxManufacturer(self):
		return self.junctionBoxManufacturer
		
	def getJunctionBoxAdhesive(self):
		return self.junctionBoxAdhesive
		
	def getCableType(self):
		return self.cableType
		
	def getConnectorType(self):
		return self.connectorType
		
	def getMaximumSystemVoltage(self):
		return self.maximumSystemVoltage
		
	def setMaximumSystemVoltage(self, maximumSystemVoltage):
		self.maximumSystemVoltage = maximumSystemVoltage
		
	def getRatedVoc(self):
		return self.ratedVoc
		
	def getRatedIsc(self):
		return self.RatedIsc
		
	def getRatedVmp(self):
		return self.ratedVmp
		
	def getRatedImp(self):
		return self.ratedImp
		
	def getRatedPmp(self):
		return self.ratedPmp
		
	def setRatedPmp(self, ratedPmp):
		self.ratedPmp = ratedPmp
		
	def getRatedFF(self):
		return self.ratedFF
		