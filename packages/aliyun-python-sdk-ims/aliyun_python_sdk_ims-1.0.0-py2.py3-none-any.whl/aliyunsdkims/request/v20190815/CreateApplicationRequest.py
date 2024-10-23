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

class CreateApplicationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ims', '2019-08-15', 'CreateApplication','ims')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_RequiredScopes(self): # String
		return self.get_query_params().get('RequiredScopes')

	def set_RequiredScopes(self, RequiredScopes):  # String
		self.add_query_param('RequiredScopes', RequiredScopes)
	def get_AccessTokenValidity(self): # Integer
		return self.get_query_params().get('AccessTokenValidity')

	def set_AccessTokenValidity(self, AccessTokenValidity):  # Integer
		self.add_query_param('AccessTokenValidity', AccessTokenValidity)
	def get_RefreshTokenValidity(self): # Integer
		return self.get_query_params().get('RefreshTokenValidity')

	def set_RefreshTokenValidity(self, RefreshTokenValidity):  # Integer
		self.add_query_param('RefreshTokenValidity', RefreshTokenValidity)
	def get_RedirectUris(self): # String
		return self.get_query_params().get('RedirectUris')

	def set_RedirectUris(self, RedirectUris):  # String
		self.add_query_param('RedirectUris', RedirectUris)
	def get_SecretRequired(self): # Boolean
		return self.get_query_params().get('SecretRequired')

	def set_SecretRequired(self, SecretRequired):  # Boolean
		self.add_query_param('SecretRequired', SecretRequired)
	def get_AppType(self): # String
		return self.get_query_params().get('AppType')

	def set_AppType(self, AppType):  # String
		self.add_query_param('AppType', AppType)
	def get_DisplayName(self): # String
		return self.get_query_params().get('DisplayName')

	def set_DisplayName(self, DisplayName):  # String
		self.add_query_param('DisplayName', DisplayName)
	def get_PredefinedScopes(self): # String
		return self.get_query_params().get('PredefinedScopes')

	def set_PredefinedScopes(self, PredefinedScopes):  # String
		self.add_query_param('PredefinedScopes', PredefinedScopes)
	def get_IsMultiTenant(self): # Boolean
		return self.get_query_params().get('IsMultiTenant')

	def set_IsMultiTenant(self, IsMultiTenant):  # Boolean
		self.add_query_param('IsMultiTenant', IsMultiTenant)
