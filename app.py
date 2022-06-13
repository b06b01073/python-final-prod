from typing import OrderedDict
from flask import Flask, jsonify, request
import json
import get_species as gs
import crawl
import arrangement

app = Flask(__name__)


@app.route("/search", methods=['POST'])
def search():	
	json_data = json.loads(request.get_data().decode())

	# coordinates of user
	latitude = json_data["latitude"]
	longitude = json_data["longitude"]

	files = []
	cat2Files = OrderedDict([
		("EX", "extinct_shp"),
		("EW", "extinct_in_wild_shp"),
		("CR", "critically_endangered_shp"),
		("EN", "endangered_shp"),
		("VU", "vulnerable_shp"),
		("LR", "conservation_dependent_shp"),
		("NT", "near_threatened_shp"),
		("LC", "least_concern_shp"),
		("DD", "data_deficient_shp"),
	])

	cat = json_data["filter"]["category"]
	for k, v in cat.items():
		if v:
			files.append(cat2Files[k])
	

	infoList = gs.loop_files(files, lat=latitude, lon=longitude)

	urlsList = []
	nameList = []
	for info in infoList:
		urlsList.append(info[0])
		nameList.append(info[1])

	speciesDict = crawl.crawler(urlsList, nameList)


	threatsDict = {}
	for k, v in speciesDict.items():
		threatsDict[k] = v["threat"]

	common_threat, counter = arrangement.getCommonThreat(threatsDict)


	speciesList = []
	for url, species in speciesDict.items():
		speciesList.append({'population': species['population'], 'imageURL': species['imageURL'], 'name': species['name'], 'url': url})



	response = jsonify({"commonThreat": common_threat, "speciesList": speciesList, "counter": counter})
	response.headers.set('Access-Control-Allow-Origin', '*')

	return response



if __name__ == '__main__':
	app.run()