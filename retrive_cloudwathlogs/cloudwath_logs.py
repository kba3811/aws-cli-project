import boto3
import time
import json 

def get_ssm_session(sessionId):
    ssm_client = boto3.client('ssm')
    session_response = ssm_client.describe_sessions(
        State='History',
        Filters=[
            {
                'key': 'SessionId',
                'value': sessionId
            },
        ]
    )
    
    return session_response['Sessions']


if __name__ == "__main__":

    ecs_client = boto3.client('ecs')

    exec_resp = ecs_client.execute_command(
        cluster = '<CLUSTER>',
        container = '<CONTAINER>',
        command = 'echo -e "Hello World\nTest Script Output"',
        interactive = True,
        task = '<TASK_ID>'
    )

    print(str(exec_resp))

    session = get_ssm_session(exec_resp['session']['sessionId'])

    output_url = ''

    ## Paginate until Session completes and logs uploaded to CloudWatch logs
    while (len(session) == 0) or (len(output_url) == 0):
        time.sleep(5)
        session = get_ssm_session(exec_resp['session']['sessionId'])

        if(len(session) > 0):
            output_url = session[0]['OutputUrl']

    logs_client = boto3.client('logs')

    # Use the same log group as specified in the task definition
    response = logs_client.get_log_events(
    logGroupName='<LOG_GROUP_NAME>',
    logStreamName=exec_resp['session']['sessionId'],
    startFromHead=True
    )

    for event in response['events']:
        print(event['message'])