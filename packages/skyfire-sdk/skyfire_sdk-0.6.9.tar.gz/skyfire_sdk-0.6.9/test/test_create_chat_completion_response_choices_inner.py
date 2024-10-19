# coding: utf-8

"""
    Skyfire API

    The Skyfire API is designed to allow agents to interact with the Skyfire platform to enable autonomous payments.

    The version of the OpenAPI document: 1.0.0
    Contact: support@skyfire.xyz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from skyfire_sdk.models.create_chat_completion_response_choices_inner import CreateChatCompletionResponseChoicesInner

class TestCreateChatCompletionResponseChoicesInner(unittest.TestCase):
    """CreateChatCompletionResponseChoicesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateChatCompletionResponseChoicesInner:
        """Test CreateChatCompletionResponseChoicesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateChatCompletionResponseChoicesInner`
        """
        model = CreateChatCompletionResponseChoicesInner()
        if include_optional:
            return CreateChatCompletionResponseChoicesInner(
                finish_reason = '',
                index = 56,
                message = skyfire_sdk.models.chat_completion_response_message.ChatCompletionResponseMessage(
                    content = '', 
                    tool_calls = [
                        skyfire_sdk.models.chat_completion_message_tool_call.ChatCompletionMessageToolCall(
                            id = '', 
                            type = 'function', 
                            function = skyfire_sdk.models.chat_completion_message_tool_call_function.ChatCompletionMessageToolCall_function(
                                name = '', 
                                arguments = '', ), )
                        ], 
                    role = '', 
                    function_call = skyfire_sdk.models.chat_completion_response_message_function_call.ChatCompletionResponseMessage_function_call(
                        arguments = '', 
                        name = '', ), ),
                logprobs = skyfire_sdk.models.create_chat_completion_response_choices_inner_logprobs.CreateChatCompletionResponse_choices_inner_logprobs(
                    content = [
                        skyfire_sdk.models.chat_completion_token_logprob.ChatCompletionTokenLogprob(
                            token = '', 
                            logprob = 1.337, 
                            bytes = [
                                56
                                ], 
                            top_logprobs = [
                                skyfire_sdk.models.chat_completion_token_logprob_top_logprobs_inner.ChatCompletionTokenLogprob_top_logprobs_inner(
                                    token = '', 
                                    logprob = 1.337, 
                                    bytes = [
                                        56
                                        ], )
                                ], )
                        ], )
            )
        else:
            return CreateChatCompletionResponseChoicesInner(
                finish_reason = '',
                index = 56,
                message = skyfire_sdk.models.chat_completion_response_message.ChatCompletionResponseMessage(
                    content = '', 
                    tool_calls = [
                        skyfire_sdk.models.chat_completion_message_tool_call.ChatCompletionMessageToolCall(
                            id = '', 
                            type = 'function', 
                            function = skyfire_sdk.models.chat_completion_message_tool_call_function.ChatCompletionMessageToolCall_function(
                                name = '', 
                                arguments = '', ), )
                        ], 
                    role = '', 
                    function_call = skyfire_sdk.models.chat_completion_response_message_function_call.ChatCompletionResponseMessage_function_call(
                        arguments = '', 
                        name = '', ), ),
                logprobs = skyfire_sdk.models.create_chat_completion_response_choices_inner_logprobs.CreateChatCompletionResponse_choices_inner_logprobs(
                    content = [
                        skyfire_sdk.models.chat_completion_token_logprob.ChatCompletionTokenLogprob(
                            token = '', 
                            logprob = 1.337, 
                            bytes = [
                                56
                                ], 
                            top_logprobs = [
                                skyfire_sdk.models.chat_completion_token_logprob_top_logprobs_inner.ChatCompletionTokenLogprob_top_logprobs_inner(
                                    token = '', 
                                    logprob = 1.337, 
                                    bytes = [
                                        56
                                        ], )
                                ], )
                        ], ),
        )
        """

    def testCreateChatCompletionResponseChoicesInner(self):
        """Test CreateChatCompletionResponseChoicesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
