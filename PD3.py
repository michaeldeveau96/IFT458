#!/c/Python27/python
####################################################################################
#	Assignment: PD3
#		File Name: PD3.py
#			Author: Michael Deveau
#	Description: Main script for Project Deliverable 3
####################################################################################
import csv
from MyClasses import Manufacturer, User, TestResults, TestLab, Product
def main():
	choice = 0
	while choice != '4':
		choice = raw_input('What action would you like to perform: \n1. Upload test results?\n2. Register a PV Module?\n3. Go to user registration.\n4. If you would like to quit.\nSelect a number: ')
		if choice == '1':
			getTestResults()
			#print getTestResults.results
			for line in getTestResults.results:
				if 'Baseline' in line:
					print line.rstrip('\n')
		elif choice == '2':
			#product = []
			registerModule(mds)
			#print registerModule.mds
			#rec=[]
			#mds=[]
			#for key, value in registerModule.mds.iteritems():
			#	temp = [key,value]
			#	rec.append(temp)
			#print rec
			
			#userRegister()
			#x = []
			#user = []
			#for key, value in userRegister.register.iteritems():
			#	temp = [key,value]
			#	x.append(temp)
			#print x
			#product.insert(Manufacturer(registerModule.mds['Manufacturer']), User(userRegister.register['First Name'], userRegister.register['Last Name'], userRegister.register['Email']), Manufacturer(registerModule.mds['Model Number'], registerModule.mds['Cell Technology'], registerModule.mds['Max System Voltage'], registerModule.mds['Pmp (W)'])) 				
			n = Product(registerModule(mds))
			#print n.modelNumber, n.manufacturer, n.manufacturingDate, n.length, n.width, n.weight, n.cellArea, n.cellTechnology, n.totalNumberOfCells n.numberOfCellsInSeries, n.numberOfSeriesStrings, n.numberOfBypassDiodes, n.seriesFuseRating, n.interconnectMaterial, n.interconnectSupplier, n.superstrateType, n.superStrateManufacturer, n.substrateType, n.substrateManufacturer, n.frameMaterial, n.frameAdhesive, n.encapsulantType, n.encapsulantManufacture, n.junctionBoxType, n.junctionBoxManufacturer, n.junctionBoxAdhesive, n.cableType, n.connectorType, n.maximumSystemVoltage, n.ratedVoc, n.ratedIsc, n.ratedVmp, n.ratedImp, n.ratedPmp, n.ratedFF
			print 'hello', 'wroks'
		elif choice == '3':
			userRegister()
		elif choice == '4':
			break
		else:
			print 'Invalid Selection'

def getTestResults():
	results = open('/Users/Michael/Documents/PD1/IFT458/test_results.csv', 'r')
	#print results.read()
	getTestResults.results = results
def registerModule(mds):
	mds = {}
	manufacturer = raw_input("Manufacturer: ")
	location = raw_input('Location: ')
	contact = raw_input('Contact: ')
	address = raw_input('Address: ')
	email = raw_input('Email: ')
	phone = input('Phone Number: ')
	modelNumber = raw_input('Model Number: ')
	moduleTotLenxWid = raw_input('Module Total Length x Width (cm x cm): ')
	moduleWeight = input('Module Weight (kg): ')
	indCellArea = input('Individual Cell Area (cm^2): ')
	cellTech = raw_input('Cell Technology: ')
	cellManufacturer = raw_input('Cell Manufacturer and part #: ')
	cellManuLocation = raw_input('Cell Manufacturing Location : ')
	totNumCells = input('Total Number of Cells: ')
	numCellSeries = input('Number of cells in series: ')
	numSeriesStrings = input('Number of series strings: ')
	numBypassDiodes = input('Number of bypass diodes: ')
	bypassDiodeRating = raw_input('Bypass Diode Rating(A): ')
	bypassDiodeMaxTemp = input('Bypass Diode Max Junction Temperature(C): ')
	seriesFuseRating = input('Series Fuse Rating(A): ')
	interconnectMatSupModNo = raw_input('Interconnect Material and Supplier Model No.: ')
	interconnectDims = raw_input('Interconnect Dimensions (mm x mm): ')
	superstrateType = raw_input('Superstrate Type: ')
	superstrateMan = raw_input('Superstrate Manufacturer and Part #: ')
	substrateType = raw_input('Substrate Type:' )
	substrateMan = raw_input('Substrate Manufacturer and Part #: ')
	frameType = raw_input('Frame Type/Material: ')
	frameAdhesive = raw_input('Frame Adhesive: ')
	encapsulantType = raw_input('Encapsulant Type: ')
	encapsulantMan = raw_input('Encapsulant Manufacturer and Part #: ')
	juncBoxType = raw_input('Junction Box Type: ')
	juncBoxMan = raw_input('Junction Box Manufacturer and Part #: ')
	juncBoxPottingMat = raw_input('Junction Box Potting Material, if any: ')
	juncBoxAdhesive = raw_input('Junction Box Adhesive: ')
	juncBoxUse = raw_input('Is Junction Box intended for use with Conduit: ')
	cableConnectorType = raw_input('Cable and Connector Type: ')
	maxSysVoltage = input('Max System Voltage: ')
	Voc = input('Vmp (V): ')
	Isc = input('Isc (A): ')
	Vmp = input('Vmp (V): ')
	Imp = input('Imp (A): ')
	Pmp = input('Pmp (W): ')
	FF = input('FF (%): ')
	
	mds['Manufacturer'] = manufacturer
	mds['Location'] = location
	mds['Contact'] = contact
	mds['Address'] = address
	mds['Email'] = email
	mds['Phone'] = phone
	mds['Model Number'] = modelNumber
	mds['Module total length x width (cm x cm)'] = moduleTotLenxWid
	mds['Module weight(kg)'] = moduleWeight
	mds['Individual Cell Area(cm^2)'] = indCellArea
	mds['Cell Technology'] = cellTech
	mds['Cell Manufacturer and part #'] = cellManufacturer
	mds['Cell Manufacturing Location'] = cellManuLocation
	mds['Total Number of Cells'] = totNumCells
	mds['Number of cells in series'] = numCellSeries
	mds['Number of series strings'] = numSeriesStrings
	mds['Number of bypass diodes'] = numBypassDiodes
	mds['Bypass Diode Rating(A)'] = bypassDiodeRating
	mds['Bypass Diode Max Junction Temperature(C)'] = bypassDiodeMaxTemp
	mds['Series Fuse Rating(A)'] = seriesFuseRating
	mds['Interconnect Material and Supplier Model No.'] = interconnectMatSupModNo
	mds['Interconnect Dimensions (mm x mm)'] = interconnectDims
	mds['Superstrate Type'] = superstrateType
	mds['Substrate Manufacturer and Part #'] = superstrateMan
	mds['Substrate Type'] = substrateType
	mds['Substrate Manufacturer and Part #'] = substrateMan
	mds['Frame Type/Material'] = frameType
	mds['Frame Adhesive'] = frameAdhesive
	mds['Encapsulant Type'] = encapsulantType
	mds['Encapsulant Manufacturer and Part #'] = encapsulantMan
	mds['Junction Box Type'] = juncBoxType
	mds['Junction Box Manufacturer and Part #'] = juncBoxMan
	mds['Junction Box Potting Material, if any'] = juncBoxPottingMat
	mds['Junction Box Adhesive'] = juncBoxAdhesive
	mds['Is Junction Box intended for use with Conduit'] = juncBoxUse
	mds['Cable and Connector Type'] = cableConnectorType
	mds['Max System Voltage'] = maxSysVoltage
	mds['Voc (V)'] = Voc
	mds['Isc (A)'] = Isc
	mds['Vmp (V)'] = Vmp
	mds['Imp (A)'] = Imp
	mds['Pmp (W)'] = Pmp
	mds['FF (%)'] = FF
	

def userRegister():
	register = {}
	
	username = raw_input('Username: ')
	password = raw_input('Password: ')
	firstName = raw_input('First Name: ')
	middleName = raw_input('Middle Name (optional): ')
	lastName = raw_input('Last Name: ')
	compName = raw_input('Company Name: ')
	compType = raw_input('Company Type (Test Lab or Manufacturer): ')
	address = raw_input('Address: ')
	officePhoneNo = input('Office Phone Number: ')
	cellPhoneNo = input('Cell Phone Number: ')
	email = raw_input('Email: ')
	
	register['Username'] = username
	register['Password'] = password
	register['First Name'] = firstName
	register['Middle Name (optional)'] = middleName
	register['Last Name'] = lastName
	register['Company Name'] = compName
	register['Company Type (Test Lab or Manufacturer)'] = compType
	register['Address'] = address
	register['Office Phone Number'] = officePhoneNo
	register['Cell Phone Number'] = cellPhoneNo
	register['Email'] = email
	
	userRegister.register = register

if __name__ == "__main__":
	main()