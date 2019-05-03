# from app import app
from app import db
# from flask import jsonify, request
from agency import Agency, agency_schema, agencies_schema
# from ad import Ad, ad_schema, ads_schema

def create_agency(name, parent_id):
	'''
	This function creates a new tupple in Agency table.
	return 0 means everything accomplished successfully.
	return 1 means the operation was unsuccessfull.
	'''
	try:
		agency = Agency(name, parent_id)
		db.session.add(agency)
		db.session.commit()
		return 0
	except Exception as e:
		print('error while creating the agency: ' + str(e))
		return 1
	

def read_agency(id):
	'''
	This function finds the first tuple with id=id in Agency table,
	serializes it to json and returns the result.
	'''
	try:
		agency = Agency.query.filter_by(id=id).first()
		result = agency_schema.dump(agency)
		return result.data
	except Exception as e:
		print('error while reading agency: ' + str(e))
		return None

def read_all_agencies():
	'''
	This function reads, serializes and returns all the tupples in Agency table.
	'''
	try:
		all_agencies = Agency.query.all()
		result = agencies_schema.dump(all_agencies)
		return result.data
	except Exception as e:
		print('error while reading all agencies: ' + str(e))
		return None

def update_agency(id, new_name, new_parent_id):
	'''
	This function finds the first tupple with id=id in Agency table
	and update it's columns.
	return 0 means everything accomplished successfully.
	return 1 means the operation was unsuccessfull.
	'''
	try:
		agency = Agency.query.filter_by(id=id).first()
		agency.name = new_name
		agency.parent_id = new_parent_id
		db.session.commit()
		return 0
	except Exception as e:
		print('error while updating the agency: ' + str(e))
		return 1
	
	