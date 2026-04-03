import anthropic
import json

client = anthropic.Anthropic()

test_email = """
From: alexei@mail.com
Subject: Team meeting
Body: Hey, our department has a meeting tomorrow at 10:00 to discuss the project.
"""

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    system="You are an email analyzer. Extract meeting info from emails. Respond with ONLY a valid JSON object with keys: is_meeting, subject, date, time. No explanation, no code fences, just the JSON.",
    messages=[
        {
            "role": "user",
            "content": f"Analyze this email:\n{test_email}",
        }
    ],
)

response = message.content[0].text
result = json.loads(response)
print(result)
print(type(result))

