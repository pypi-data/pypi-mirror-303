from sawsi.aws import shared
from typing import Any


class LambdaAPI:
    def __init__(self, credentials=None, region=shared.DEFAULT_REGION):
        self.boto3_session = shared.get_boto_session(credentials)
        self.lambda_client = self.boto3_session.client('lambda', region_name=region)

    def invoke(self, function_name: str, payload: Any):
        response = self.lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',  # 'Event' for asynchronous execution
            Payload=payload
        )

        # 응답에서 Payload 추출
        response_payload = response['Payload'].read()
        response_body = response_payload.decode('utf-8')
        return response_body
