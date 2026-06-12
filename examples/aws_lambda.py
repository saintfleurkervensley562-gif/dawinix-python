"""
Example: AWS Lambda function.
"""

import os
import json
from dawinix_sdk.build import Agent, Skill


agent = Agent(
    api_key=os.getenv("DAWINIX_API_KEY"),
    model="dawinix-4-mini",
    skills=[Skill.WEB_SEARCH],
    timeout=25,
)


def lambda_handler(event, context):
    """AWS Lambda handler."""
    task = event.get("task")
    if not task:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "task is required"}),
        }

    try:
        result = agent.run(task=task, mode=event.get("mode", "balanced"))
        return {
            "statusCode": 200,
            "body": json.dumps({
                "output": result.output,
                "tokens": result.usage.total_tokens,
                "elapsed_ms": result.elapsed_ms,
            }),
        }
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
