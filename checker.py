import requests

def check(frame):

	# call api and check status
	url = 'https://api.miniai.live/api/bank_credit_check'
	files = {'image': frame}

	r = requests.post(url, files=files)
	status = r.json().get('Status')

	html = None
	images = None

	table_value = ""

	# build tables with html
	for key, value in r.json().items():
		if key == 'Status' or key == 'Images' or key == 'Position':
			continue

		row_value = ("<tr>"
						"<td>{key}</td>"
						"<td>{value}</td>"
					"</tr>".format(key=key, value=value))
		table_value = table_value + row_value

	html = ("<table>"
		  "<tr>"
			  "<th style=""width:20%"">Field</th>"
			  "<th style=""width:40%"">Value</th>"
		  "</tr>"
		  "{table_value}"
		  "</table>".format(table_value=table_value))

	table_value = ""
	for key, value in r.json().items():
		  if key == 'Images':
			  for details_key, details_value in value.items():
				  for image_key, image_value in details_value.items():
					  if image_key == 'image':
						  row_value = ("<tr>"
										  "<td>{key}</td>"
										  "<td><img src=""data:image/png;base64,{base64_image} width = '200'  height= '100' /></td>"
									  "</tr>".format(key=details_key, base64_image=image_value))
						  table_value = table_value + row_value

	images = ('<table>'
		  '<tr>'
			  "<th>Field</th>"
			  "<th>Image</th>"
		  "</tr>"
		  "{table_value}"
		  "</table>".format(table_value=table_value))

	return html
	

#check("openai-icon-1011x1024-uztb7qme.png")