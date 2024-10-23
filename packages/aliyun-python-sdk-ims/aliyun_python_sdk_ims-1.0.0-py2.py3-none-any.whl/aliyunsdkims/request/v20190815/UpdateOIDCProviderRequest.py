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

class UpdateOIDCProviderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ims', '2019-08-15', 'UpdateOIDCProvider','ims')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IssuanceLimitTime(self): # Long
		return self.get_query_params().get('IssuanceLimitTime')

	def set_IssuanceLimitTime(self, IssuanceLimitTime):  # Long
		self.add_query_param('IssuanceLimitTime', IssuanceLimitTime)
	def get_OIDCProviderName(self): # String
		return self.get_query_params().get('OIDCProviderName')

	def set_OIDCProviderName(self, OIDCProviderName):  # String
		self.add_query_param('OIDCProviderName', OIDCProviderName)
	def get_ClientIds(self): # String
		return self.get_query_params().get('ClientIds')

	def set_ClientIds(self, ClientIds):  # String
		self.add_query_param('ClientIds', ClientIds)
	def get_NewDescription(self): # String
		return self.get_query_params().get('NewDescription')

	def set_NewDescription(self, NewDescription):  # String
		self.add_query_param('NewDescription', NewDescription)
