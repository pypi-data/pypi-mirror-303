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
import json

class SetSecurityPreferenceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ims', '2019-08-15', 'SetSecurityPreference','ims')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EnableSaveMFATicket(self): # Boolean
		return self.get_query_params().get('EnableSaveMFATicket')

	def set_EnableSaveMFATicket(self, EnableSaveMFATicket):  # Boolean
		self.add_query_param('EnableSaveMFATicket', EnableSaveMFATicket)
	def get_LoginNetworkMasks(self): # String
		return self.get_query_params().get('LoginNetworkMasks')

	def set_LoginNetworkMasks(self, LoginNetworkMasks):  # String
		self.add_query_param('LoginNetworkMasks', LoginNetworkMasks)
	def get_AllowUserToChangePassword(self): # Boolean
		return self.get_query_params().get('AllowUserToChangePassword')

	def set_AllowUserToChangePassword(self, AllowUserToChangePassword):  # Boolean
		self.add_query_param('AllowUserToChangePassword', AllowUserToChangePassword)
	def get_LoginSessionDuration(self): # Integer
		return self.get_query_params().get('LoginSessionDuration')

	def set_LoginSessionDuration(self, LoginSessionDuration):  # Integer
		self.add_query_param('LoginSessionDuration', LoginSessionDuration)
	def get_VerificationTypes(self): # Array
		return self.get_query_params().get('VerificationTypes')

	def set_VerificationTypes(self, VerificationTypes):  # Array
		self.add_query_param("VerificationTypes", json.dumps(VerificationTypes))
	def get_AllowUserToManageAccessKeys(self): # Boolean
		return self.get_query_params().get('AllowUserToManageAccessKeys')

	def set_AllowUserToManageAccessKeys(self, AllowUserToManageAccessKeys):  # Boolean
		self.add_query_param('AllowUserToManageAccessKeys', AllowUserToManageAccessKeys)
	def get_AllowUserToManageMFADevices(self): # Boolean
		return self.get_query_params().get('AllowUserToManageMFADevices')

	def set_AllowUserToManageMFADevices(self, AllowUserToManageMFADevices):  # Boolean
		self.add_query_param('AllowUserToManageMFADevices', AllowUserToManageMFADevices)
	def get_OperationForRiskLogin(self): # String
		return self.get_query_params().get('OperationForRiskLogin')

	def set_OperationForRiskLogin(self, OperationForRiskLogin):  # String
		self.add_query_param('OperationForRiskLogin', OperationForRiskLogin)
	def get_MFAOperationForLogin(self): # String
		return self.get_query_params().get('MFAOperationForLogin')

	def set_MFAOperationForLogin(self, MFAOperationForLogin):  # String
		self.add_query_param('MFAOperationForLogin', MFAOperationForLogin)
	def get_AllowUserToManagePersonalDingTalk(self): # Boolean
		return self.get_query_params().get('AllowUserToManagePersonalDingTalk')

	def set_AllowUserToManagePersonalDingTalk(self, AllowUserToManagePersonalDingTalk):  # Boolean
		self.add_query_param('AllowUserToManagePersonalDingTalk', AllowUserToManagePersonalDingTalk)
