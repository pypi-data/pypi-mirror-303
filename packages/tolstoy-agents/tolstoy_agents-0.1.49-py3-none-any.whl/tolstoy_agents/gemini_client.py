import os
import json
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting
from google.oauth2 import service_account

from tolstoy_agents.utils import Environment, get_ssm_param

default_safety_settings = [
    {
        "category": "HARM_CATEGORY_UNSPECIFIED",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
]

safety_settings = [SafetySetting.from_dict(s) for s in default_safety_settings]


class GeminiClient:
    def __init__(self, system_instruction, model_name="gemini-1.5-pro-preview-0514"):
        gcp_credentials = json.loads(
            get_ssm_param("gcp_credentials", Environment[os.environ["env"]])
        )

        credentials = service_account.Credentials.from_service_account_info(
            gcp_credentials
        )

        project_id = gcp_credentials["project_id"]
        vertexai.init(project=project_id, location="us-east1", credentials=credentials)

        self.model = GenerativeModel(
            model_name=model_name,
            safety_settings=safety_settings,
            system_instruction=system_instruction,
            generation_config={"max_output_tokens": 8192},
        )

    def generate(self, contents):
        return self.model.generate_content(contents)

    def get_part(self, video_file, mime_type="video/mp4"):
        return Part.from_data(video_file, mime_type=mime_type)
