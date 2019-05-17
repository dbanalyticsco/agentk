import lookerapi as looker
import json
import ast

class Looker:

	def __init__(self, base_url, client_id, client_secret, port):

		if base_url[-1] == '/':
			base_url = '{}:{}/api/3.0/'.format(base_url[:-1], port)
		else:
			base_url = '{}:{}/api/3.0/'.format(base_url, port)
		
		# instantiate Auth API
		unauthenticated_client = looker.ApiClient(base_url)
		unauthenticated_authApi = looker.ApiAuthApi(unauthenticated_client)

		# authenticate client
		token = unauthenticated_authApi.login(client_id=client_id, client_secret=client_secret)
		client = looker.ApiClient(base_url, 'Authorization', 'token ' + token.access_token)

		self.client = client

	def get_look_single_value(self, look_id):

		look_api = looker.LookApi(self.client)
		result = look_api.run_look(look_id, 'json')
		result_json = ast.literal_eval(result)

		if len(result_json) == 0:
			raise Exception("Look {} must return data.".format(look_id))

		if len(result_json[0].keys()) > 1:
			raise Exception("Look {} can't have more than one column.".format(look_id))

		key = list(result_json[0])[0]
		
		return result_json[0][key] 

	def get_look_table(self, look_id):
		
		look_api = looker.LookApi(self.client)
		result = look_api.run_look(look_id, 'md')

		return result
