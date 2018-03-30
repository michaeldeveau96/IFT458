#!/c/Python27/python
####################################################################################
#	Assignment: PD3
#		File Name: PD3.py
#			Author: Michael Deveau
#	Description: Main script for Project Deliverable 3
####################################################################################
import csv, re
import MySQLdb
from MyClasses import Manufacturer, User, TestResults, TestLab, Product

def getTestResults():
	#Open and read results
	results = open('test_results.csv', 'r')
	getTestResults.results = results

def validation():
	i = 0
	while i != 1:
		data = raw_input('Enter an email address, phone number (###-###-####), a number, or date. Enter 1 if you want to quit.: ')
		if '@' in data:
			while True:
				try:
					x = re.match(r'\w+@\w+.\w+', data)
				except TypeError:
					print ('Invalid Email Address')
					continue
				if x == None:
					print ('Invalid Email Address')
					continue
				else:
					print ('email')
					break
		if re.search('\d', data) is not None:
			while True:
				try:
					x = re.match(r'\d+', data)
				except TypeError:
					print ('Invalid Number')
					continue
				if x == None:
					print ('Invalid Number')
					continue
				else:
					print ('number')
					break
		if '-' in data:
			while True:
				try:
					x = re.match('\d{3}-\d{3}-\d{2,4}', data)
				except TypeError:
					print ('Invalid Phone Number')
					continue
				if x == None:
					print ('Invalid Phone Number')
					continue
				else:
					print ('phone')
					break
		if '/' in data:
			while True:
				try:
					x = re.match('\d{2}/\d{2}/\d{4}', data)
				except TypeError:
					print ('Invalid Date')
					continue
				if x == None:
					print ('Invalid Date')
					continue
				else:
					print ('date')
					break
		else:
			i = 1
def registerModule():
	#Create MDS dictionary
	mds = {}
	
	#Gather user raw_input
	manufacturer = raw_input("Manufacturer: ")
	location = raw_input('Location: ')
	contact = raw_input('Contact: ')
	address = raw_input('Address: ')
	while True:
		try:
			email = raw_input('Email: ')
			e = re.match(r'\w+@\w+.\w+', email)
		except TypeError:
			print ('Invalid Email Address')
			continue
		if e == None:
			print ('Invalid Email Address')
			continue
		else:
			print ('email')
			break

	while True:
		try:
			phone = raw_input('Phone Number (###-###-####): ')
			p = re.match('\d{3}-\d{3}-\d{4}', phone)
		except TypeError:
			print ('Invalid Phone Number')
			continue
		if p == None:
			print('Invalid Phone Number')
			continue		
		else:
			print ('Phone')
			break

	moduleTotLenxWid = raw_input('Module Total Length x Width (cm x cm): ')
	moduleWeight = raw_input('Module Weight (kg): ')
	indCellArea = raw_input('Individual Cell Area (cm^2): ')
	cellTech = raw_input('Cell Technology: ')
	cellManufacturer = raw_input('Cell Manufacturer and part #: ')
	cellManuLocation = raw_input('Cell Manufacturing Location : ')
	totNumCells = raw_input('Total Number of Cells: ')
	numCellSeries = raw_input('Number of cells in series: ')
	numSeriesStrings = raw_input('Number of series strings: ')
	numBypassDiodes = raw_input('Number of bypass diodes: ')
	bypassDiodeRating = raw_input('Bypass Diode Rating(A): ')
	bypassDiodeMaxTemp = raw_input('Bypass Diode Max Junction Temperature(C): ')
	seriesFuseRating = raw_input('Series Fuse Rating(A): ')
	interconnectMatSupModNo = raw_input('Interconnect Material and Supplier Model No.: ')
	interconnectDims = raw_input('Interconnect Dimensions (mm x mm): ')
	superstrateType = raw_input('Superstrate Type: ')
	superstrateMan = raw_input('Superstrate Manufacturer and Part #: ')
	substrateType = raw_input('Substrate Type: ')
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
	maxSysVoltage = raw_input('Max System Voltage: ')
	Voc = raw_input('Vmp (V): ')
	Isc = raw_input('Isc (A): ')
	Vmp = raw_input('Vmp (V): ')
	Imp = raw_input('Imp (A): ')
	Pmp = raw_input('Pmp (W): ')
	FF = raw_input('FF (%): ')
	
	#Populate dictionary
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
	
	return mds
	
def userRegister():
	#Create register dictionary
	register = {}
	
	#Gather raw_input from user
	username = raw_input('Username: ')
	password = raw_input('Password: ')
	firstName = raw_input('First Name: ')
	middleName = raw_input('Middle Name (optional): ')
	lastName = raw_input('Last Name: ')
	compName = raw_input('Company Name: ')
	compType = raw_input('Company Type (Test Lab or Manufacturer): ')
	address = raw_input('Address: ')

	while True:
		try:
			officePhoneNo = raw_input('Office Phone Number (###-###-####): ')
			p = re.match('\d{3}-\d{3}-\d{4}', officePhoneNo)
		except TypeError:
			print ('Invalid Phone Number')
			continue
		if p == None:
			print('Invalid Phone Number')
			continue		
		else:
			print ('Phone')
			break

	while True:
		try:
			cellPhoneNo = raw_input('Office Phone Number (###-###-####): ')
			p = re.match('\d{3}-\d{3}-\d{4}', cellPhoneNo)
		except TypeError:
			print ('Invalid Phone Number')
			continue
		if p == None:
			print('Invalid Phone Number')
			continue		
		else:
			print ('Phone')
			break

	while True:
		try:
			email = raw_input('Email: ')
			e = re.match(r'\w+@\w+.\w+', email)
		except TypeError:
			print ('Invalid Email Address')
			continue
		if e == None:
			print ('Invalid Email Address')
			continue
		else:
			print ('email')
			break
	
	#Populate dictionary
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
	
	return register

def main():
	choice = 0
	while choice != '6':
		choice = raw_input('What action would you like to perform: \n1. Upload test results?\n2. Register a PV Module?\n3. Go to user registration.\n4.If you would like to view data in the database\n5. If you want to check for valid data.\n6. If you would like to quit.\nSelect a number: ')
		#Choose which action the user would like to perform
		if choice == '1':
			#Get test results and filter line for 'Baseline' results
			getTestResults()
			for line in getTestResults.results:
				if 'Baseline' in line:
					print line.rstrip('\n')
		elif choice == '2':
			#Create variables for values in the dictionaries
			mds = registerModule()
			register = userRegister()
			
			#Create variables for values in the dictionaries
			manufacturer = mds['Manufacturer']
			firstName = register['First Name']
			lastName = register['Last Name']
			email = register['Email']
			modelNumber = mds['Model Number']
			cellTech = mds['Cell Technology']
			maxSysVoltage = mds['Max System Voltage']
			Pmp = mds['Pmp (W)']
			
			#Apply dictionaries to classes
			m = Product(mds)
			r = User(register)
			t = TestLab(register)
			m.setManufacturer(manufacturer)
			r.setFirstName(firstName)
			r.setLastName(lastName)
			t.setContactPerson(firstName, lastName)
			r.setEmail(email)
			m.setModelNumber(modelNumber)
			m.setCellTechnology(cellTech)
			m.setMaximumSystemVoltage(maxSysVoltage)
			m.setRatedPmp(Pmp)
			
			#Print objects
			print ('Manufacturer: ', m.getManufacturer(), 'Contact Name: ', r.getFirstName() + r.getLastName(), 'Contact Email: ', r.getEmail(), 'Model Number: ', m.getModelNumber(), 'Cell Technology: ', m.getCellTechnology(), 'System Voltage: ', m.getMaximumSystemVoltage(), 'Rated Power (Pmp): ', m.getRatedPmp())
			
			mfs = MySQLdb.connect(user='root')
			mfs.query("CREATE DATABASE PD3")
			mfs.query("GRANT ALL ON PD3.* to ''@'localhost'")
			mfs.commit()
			mfs.close()
			x = MySQLdb.connect(db = 'PD3')
			cur = x.cursor()
			cur.execute('CREATE TABLE mds(manufacturer varchar(20), location varchar(30), contact varchar(30), address varchar(30), email varchar(30), phone varchar(12), moduleTotLenxWid varchar(20), moduleWeight decimal(6,2) not null, indCellArea decimal(6,2) not null, cellTech varchar(20), cellManufacturer varchar(6,2), cellManuLocation varchar(30), totNumCells int not null, numCellSeries int not null, numSeriesStrings int not null, numBypassDiodes int not null, bypassDiodeRating varchar(20), bypassDiodeMaxTemp decimal(6,2) not null, seriesFuseRating decimal(6,2) not null, interconnectMatSupModNo varchar(30), interconnectDims varchar(20), superstrateType varchar(20), superstrateMan varchar(20), substrateType varchar(20), substrateMan varchar(20), frameType varchar(20), frameAdhesive varchar(20), encapsulantType varchar(20), encapsulantMan varchar(20), juncBoxType varchar(20), juncBoxMan varchar(20), juncBoxPottingMat varchar(20), juncBoxAdhesive varchar(20), juncBoxUse varchar(20), cableConnectorType varchar(20), maxSysVoltage decimal(6,2), Voc decimal(6,2), Isc decimal(6,2), Vmp decimal(6,2), Imp decimal(6,2), Pmp decimal(6,2), FF decimal(6,2)')
			cur.execute("INSERT INTO mds VALUES(manufacturer, location, contact, address, email, phone, moduleTotLenxWid, moduleWeight, indCellArea, cellTech, cellManufacturer, cellManuLocation, totNumCells, numCellSeries, numSeriesStrings, numBypassDiodes, bypassDiodeRating, bypassDiodeMaxTemp, seriesFuseRating, interconnectMatSupModNo, interconnectDims, superstrateType, superstrateMan, substrateType, substrateMan, frameType, frameAdhesive, encapsulantType, encapsulantMan, juncBoxType, juncBoxMan, juncBoxPottingMat, juncBoxAdhesive, juncBoxUse, cableConnectorType, maxSysVoltage, Voc, Isc, Vmp, Pmp, FF)")
			cur.commit()
			cur.close()
		elif choice == '3':
			#Create variables for values in the dictionary
			register = userRegister()
			
			#Create variables for values in the dictionary
			username = register['Username']
			password = register['Password']
			firstName = register['First Name']
			middleName = register['Middle Name (optional)']
			lastName = register['Last Name']
			compName = register['Company Name']
			compType = register['Company Type (Test Lab or Manufacturer)']
			address = register['Address']
			officePhoneNo = register['Office Phone Number']
			cellPhoneNo = register['Cell Phone Number']
			email = register['Email']
			
			#Apply dictionaries to classes
			r = User(register)
			r.setUsername(username)
			r.setPassword(password)
			r.setFirstName(firstName)
			r.setMiddleName(middleName)
			r.setLastName(lastName)
			r.setAddress(address)
			r.setOfficePhone(officePhoneNo)
			r.setCellPhone(cellPhoneNo)
			r.setEmail(email)
			
			#Print objects
			print ('Username: ', r.getUsername(), 'Password: ', r.getPassword(), 'First Name: ', r.getFirstName(), 'Middle Name: ', r.getMiddleName(), 'Last Name: ', r.getLastName(), 'Address: ', r.getAddress(), 'Office Phone: ', r.getOfficePhone(), 'Cell Phone: ', r.getCellPhone(), 'Email: ', r.getEmail())
			x = MySQLdb.connect(db = 'PD3')
			cur = x.cursor()
			cur.execute('CREATE TABLE register(username varchar(20), password varchar(20), firstName varchar(20), middleName varchar(20), lastName varchar(20), compName varchar(20), compType varchar(20), address varchar(30), officePhoneNo varchar(12), cellPhoneNo varchar(12), email varchar(30)')
			cur.execute("INSERT INTO register VALUES(username, password, firstName, middleName, lastName, compName, compType, address, officePhoneNo, cellPhoneNo, email)")
			cur.commit()
			cur.close()
		elif choice == '4':
			x = MySQLdb.connect(db = 'PD3')
			cur = x.cursor()
			cur.execute('SELECT manufacturer, contact, email, cellTech, ratedPower, Isc as averageIsc, Voc as averageVoc, Pmp as averagePmax from mds')
			cur.commit()
			cur.close()
			for data in cur.fetchall():
				print '%s\t%s' % data
		elif choice == '5':
			validation()
		elif choice == '6':
			break
		else:
			print 'Invalid Selection'

if __name__ == "__main__":
	main()