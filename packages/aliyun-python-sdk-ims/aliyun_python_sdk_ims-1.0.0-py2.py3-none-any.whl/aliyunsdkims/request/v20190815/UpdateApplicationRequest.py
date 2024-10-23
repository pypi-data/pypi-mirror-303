# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkims.endpoint import endpoint_data

class UpdateApplicationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ims', '2019-08-15', 'UpdateApplication','ims')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NewIsMultiTenant(self): # Boolean
		return self.get_query_params().get('NewIsMultiTenant')

	def set_NewIsMultiTenant(self, NewIsMultiTenant):  # Boolean
		self.add_query_param('NewIsMultiTenant', NewIsMultiTenant)
	def get_NewRefreshTokenValidity(self): # Integer
		return self.get_query_params().get('NewRefreshTokenValidity')

	def set_NewRefreshTokenValidity(self, NewRefreshTokenValidity):  # Integer
		self.add_query_param('NewRefreshTokenValidity', NewRefreshTokenValidity)
	def get_NewPredefinedScopes(self): # String
		return self.get_query_params().get('NewPredefinedScopes')

	def set_NewPredefinedScopes(self, NewPredefinedScopes):  # String
		self.add_query_param('NewPredefinedScopes', NewPredefinedScopes)
	def get_NewSecretRequired(self): # Boolean
		return self.get_query_params().get('NewSecretRequired')

	def set_NewSecretRequired(self, NewSecretRequired):  # Boolean
		self.add_query_param('NewSecretRequired', NewSecretRequired)
	def get_NewDisplayName(self): # String
		return self.get_query_params().get('NewDisplayName')

	def set_NewDisplayName(self, NewDisplayName):  # String
		self.add_query_param('NewDisplayName', NewDisplayName)
	def get_NewRequiredScopes(self): # String
		return self.get_query_params().get('NewRequiredScopes')

	def set_NewRequiredScopes(self, NewRequiredScopes):  # String
		self.add_query_param('NewRequiredScopes', NewRequiredScopes)
	def get_NewRedirectUris(self): # String
		return self.get_query_params().get('NewRedirectUris')

	def set_NewRedirectUris(self, NewRedirectUris):  # String
		self.add_query_param('NewRedirectUris', NewRedirectUris)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_NewAccessTokenValidity(self): # Integer
		return self.get_query_params().get('NewAccessTokenValidity')

	def set_NewAccessTokenValidity(self, NewAccessTokenValidity):  # Integer
		self.add_query_param('NewAccessTokenValidity', NewAccessTokenValidity)
