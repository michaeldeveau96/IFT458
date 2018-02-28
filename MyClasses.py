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

	def setName(self, name):
		self.name = name
	
	def getRegisteredCountry(self):
		return self.registeredCountry

	def setRegisteredCountry(self, registeredCountry):
		self.registeredCountry = registeredCountry
		
	def getContactPerson(self):
		return self.contactPerson

	def setContactPerson(self, contactPerson):
		self.contactPerson = contactPerson
	
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

	def setUsername(self, username):
		self.username = username
	
	def getPassword(self):
		return self.password

	def setPassword(self, password):
		self.password = password
	
	def getFirstName(self):
		return self.firstName
		
	def setFirstName(self, firstName):
		self.firstName = firstName
	
	def getMiddleName(self):
		return self.middleName

	def setMiddleName(self, middleName):
		self.middleName = middleName
	
	def getLastName(self):
		return self.lastName
		
	def setLastName(self, lastName):
		self.lastName = lastName
	
	def getAddress(self):
		return self.address

	def setAddress(self, address):
		self.address = address
	
	def getOfficePhone(self):
		return self.officePhone
	
	def setOfficePhone(self, officePhone):
		self.officePhone = officePhone

	def getCellPhone(self):
		return self.cellphone

	def setCellPhone(self, cellphone):
		self.cellphone = cellphone
	
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

	def setDataSource(self, dataSource):
		self.dataSource = dataSource
	
	def getProduct(self):
		return self.product

	def setProduct(self, product):
		self.product = product
		
	def getReportingCondition(self):
		return self.reportingCondition

	def setReportingCondition(self, reportingCondition):
		self.reportingCondition = reportingCondition
		
	def getTestSequence(self):
		return self.testSequence

	def setTestSequence(self, testSequence):
		self.testSequence = testSequence
		
	def getTestDate(self):
		return self.testDate

	def setTestDate(self, testDate):
		self.testDate = testDate
	
	def getIsc(self):
		return self.isc

	def setIsc(self, isc):
		self.isc = isc
		
	def getVoc(self):
		return self.voc

	def setVoc(self, voc):
		self.voc = voc
		
	def getImp(self):
		return self.imp

	def setImp(self, imp):
		self.imp = imp
		
	def getVmp(self):
		return self.vmp

	def setVmp(self, vmp):
		self.vmp = vmp	
		
	def getPmp(self):
		return self.pmp

	def setPmp(self, pmp):
		self.pmp = pmp
		
	def getFf(self):
		return self.ff

	def setFf(self, ff):
		self.ff = ff
		
	def getNoct(self):
		return self.noct

	def setNoct(self, noct):
		self.noct = noct
		
class TestLab:
	def __init__(self, name='', address='', contactPerson=''):
		self.name = name
		self.address = address
		self.contactPerson = contactPerson
		
	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name
	
	def getAddress(self):
		return self.address

	def setAddress(self, address):
		self.address = address
	
	def getContactPerson(self):
		return contactPerson
		
	def setContactPerson(self, firstName, lastName):
		self.contactPerson = contactPerson
		
	
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

	def setManufacturingDate(self, manufacturingDate):
		self.manufacturingDate = manufacturingDate
		
	def getLength(self):
		return self.length
	
	def setLength(self, length):
		self.length = length

	def getWidth(self):
		return self.width

	def setWidth(self, width):
		self.width = width
		
	def getWeight(self):
		return self.weight

	def setWeight(self, weight):
		self.weight = weight
		
	def getCellArea(self):
		return self.cellArea

	def setCellArea(self, cellArea):
		self.cellArea = cellArea
	
	def getCellTechnology(self):
		return self.cellTechnology
		
	def setCellTechnology(self, cellTechnology):
		self.cellTechnology = cellTechnology
	
	def getTotalNumberOfCells(self):
		return self.totalNumberOfCells

	def setTotalNumberOfCells(self, totalNumberOfCells):
		self.totalNumberOfCells = totalNumberOfCells
		
	def getNumberOfCellsInSeries(self):
		return self.numberOfCellsInSeries

	def setNumberOfCellsInSeries(self, numberOfCellsInSeries):
		self.numberOfCellsInSeries = numberOfCellsInSeries
		
	def getNumberOfSeriesStrings(self):
		return self.numberOfSeriesStrings

	def setNumberOfSeriesStrings(self, numberOfSeriesStrings):
		self.numberOfSeriesStrings = setNumberOfSeriesStrings
		
	def getNumberOfBypassDiodes(self):
		return self.numberOfBypassDiodes

	def setNumberOfBypassDiodes(self, numberOfBypassDiodes):
		self.numberOfBypassDiodes = numberOfBypassDiodes
	
	def getSeriesFuseRating(self):
		return self.seriesFuseRating

	def setSeriesFuseRating(self, seriesFuseRating):
		self.seriesFuseRating = seriesFuseRating
	
	def getInterconnectMaterial(self):
		return self.interconnectMaterial

	def setInterconnectMaterial(self, interconnectMaterial):
		self.interconnectMaterial = interconnectMaterial
	
	def getInterconnectSupplier(self):
		return self.interconnectSupplier

	def setInterconnectSupplier(self, interconnectSupplier):
		self.interconnectSupplier = interconnectSupplier
		
	def getSuperstrateType(self):
		return self.superstrateType
	
	def setSuperstrateType(self, superstrateType):
		self.superstrateType = superstrateType	

	def getSuperstrateManufacturer(self):
		return self.superStrateManufacturer

	def setSuperstrateManufacturer(self, superStrateManufacturer):
		self.superStrateManufacturer = superStrateManufacturer
		
	def getSubstrateType(self):
		return self.substrateType

	def setSubstrateType(self, substrateType):
		self.substrateType = substrateType
		
	def getSubstrateManufacturer(self):
		return self.substrateManufacturer

	def setSubstrateManufacturer(self, substrateManufacturer):
		self.substrateManufacturer = substrateManufacturer
		
	def getFrameMaterial(self):
		return self.frameMaterial

	def setFrameMaterial(self, frameMaterial):
		self.frameMaterial = frameMaterial
		
	def getFrameAdhesive(self):
		return self.frameAdhesive

	def setFrameAdhesive(self, frameAdhesive):
		self.frameAdhesive = frameAdhesive
		
	def getEncapsulantType(self):
		return self.encapsulantType

	def setEncapsulantType(self, encapsulantType):
		self.encapsulantType = encapsulantType
		
	def getEncapsulantManufacturer(self):
		return self.encapsulantManufacture

	def setEncapsulantManufacturer(self, encapsulantManufacture):
		self.encapsulantManufacture = encapsulantManufacture
		
	def getJunctionBoxType(self):
		return self.junctionBoxType

	def setJunctionBoxType(self, junctionBoxType):
		self.junctionBoxType = junctionBoxType
		
	def getJunctionBoxManufacturer(self):
		return self.junctionBoxManufacturer

	def setJunctionBoxManufacturer(self, junctionBoxManufacturer):
		self.junctionBoxManufacturer = junctionBoxManufacturer
		
	def getJunctionBoxAdhesive(self):
		return self.junctionBoxAdhesive

	def setJunctionBoxAdhesive(self, junctionBoxAdhesive):
		self.junctionBoxAdhesive = junctionBoxAdhesive
		
	def getCableType(self):
		return self.cableType

	def setCableType(self, cableType):
		self.cableType = cableType
		
	def getConnectorType(self):
		return self.connectorType

	def setConnectorType(self, connectorType):
		self.connectorType = connectorType
		
	def getMaximumSystemVoltage(self):
		return self.maximumSystemVoltage
		
	def setMaximumSystemVoltage(self, maximumSystemVoltage):
		self.maximumSystemVoltage = maximumSystemVoltage
		
	def getRatedVoc(self):
		return self.ratedVoc

	def setRatedVoc(self, ratedVoc):
		self.ratedVoc = ratedVoc
		
	def getRatedIsc(self):
		return self.ratedIsc

	def setRatedIsc(self, RatedIsc):
		self.ratedVoc = ratedVoc
		
	def getRatedVmp(self):
		return self.ratedVmp

	def setRatedVmp(self, ratedVmp):
		self.ratedVmp = ratedVmp
		
	def getRatedImp(self):
		return self.ratedImp

	def setRatedImp(self, ratedImp):
		self.ratedImp = ratedImp
		
	def getRatedPmp(self):
		return self.ratedPmp
		
	def setRatedPmp(self, ratedPmp):
		self.ratedPmp = ratedPmp
		
	def getRatedFF(self):
		return self.ratedFF

	def setRatedFF(self, ratedFF):
		self.ratedFF = ratedFF
		