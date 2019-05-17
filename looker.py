import lookerapi as looker
import json
import ast
import time
import cloudinary
import cloudinary.uploader
import os

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
		result = look_api.run_look(look_id, result_format='json', apply_vis=True)
		result_json = ast.literal_eval(result)

		if len(result_json) == 0:
			raise Exception("Look {} must return data.".format(look_id))

		if len(result_json[0].keys()) > 1:
			raise Exception("Look {} can't have more than one column.".format(look_id))

		key = list(result_json[0])[0]
		
		return result_json[0][key] 

	def get_look_table(self, look_id):
		
		look_api = looker.LookApi(self.client)
		result = look_api.run_look(look_id, result_format='md', apply_vis=True)

		return result

	def get_look_png(self, look_id, width, height):
		
		render_api = looker.RenderTaskApi(self.client)
		task = render_api.create_look_render_task(look_id, 'png', width, height)

		rendered = False
		while not rendered:
			render = render_api.render_task(task.id)
			if render.finalized_at is not None:
				rendered = True
			else:
				time.sleep(0.5)

		results = render_api.render_task_results(task.id, _preload_content = False)
		data = results.data

		file_name = '{}.png'.format(look_id)
		with open(file_name, 'wb') as f:
			f.write(data)

		cloudinary_cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME')
		cloudinary_api_key = os.environ.get('CLOUDINARY_API_KEY')
		cloudinary_api_secret = os.environ.get('CLOUDINARY_API_SECRET')

		cloudinary.config(
			cloud_name=cloudinary_cloud_name,
			api_key=cloudinary_api_key,
			api_secret=cloudinary_api_secret)
		upload = cloudinary.uploader.upload(file_name)
		upload_url = upload['url']
		html_string = '<img src="{}" alt="look image" >'.format(upload_url)

		return html_string
