'''
	About
	=====
	- NFT Storage API service's usage from uploading to getting IPFS CID (i.e. hash)

	References
	==========
	- Convert cURL to Python requests: https://curl.trillworks.com/

'''

import requests

API_ENDPOINT = "https://api.nft.storage/upload"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGU0QTRhOTNGQzBlZTI4MjEyMjBiQTI0RTgwNTkxNjg2NzY1QUFCNDMiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTYyMTAyMjY0NDQ1OCwibmFtZSI6Imt5Y2JvdCJ9.rkAqB60ANzkwoe5XGIP89fTrxxiyK4zkIRq6bc5NQ7c" 

headers = {
    'accept': 'application/json',
    'Content-Type': 'image/png',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGU0QTRhOTNGQzBlZTI4MjEyMjBiQTI0RTgwNTkxNjg2NzY1QUFCNDMiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTYyMTAyMjY0NDQ1OCwibmFtZSI6Imt5Y2JvdCJ9.rkAqB60ANzkwoe5XGIP89fTrxxiyK4zkIRq6bc5NQ7c',
}

r = requests.post(
	url = API_ENDPOINT, 
	headers= headers, 
	data= open('../img/nft_market.jpg', 'rb').read()
	)

if (r.status_code == 200):
	cid = r.json()['value']['cid']
	# print(cid)			# print IPFS CID
	print(f'Get the image at this url: https://{cid}.ipfs.dweb.link/')		# print the img url
else:
	print(f'Some problem occurred during uploading: {r.status_code}')