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

class SetUserSsoSettingsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ims', '2019-08-15', 'SetUserSsoSettings','ims')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AuxiliaryDomain(self): # String
		return self.get_query_params().get('AuxiliaryDomain')

	def set_AuxiliaryDomain(self, AuxiliaryDomain):  # String
		self.add_query_param('AuxiliaryDomain', AuxiliaryDomain)
	def get_MetadataDocument(self): # String
		return self.get_query_params().get('MetadataDocument')

	def set_MetadataDocument(self, MetadataDocument):  # String
		self.add_query_param('MetadataDocument', MetadataDocument)
	def get_SsoEnabled(self): # Boolean
		return self.get_query_params().get('SsoEnabled')

	def set_SsoEnabled(self, SsoEnabled):  # Boolean
		self.add_query_param('SsoEnabled', SsoEnabled)
