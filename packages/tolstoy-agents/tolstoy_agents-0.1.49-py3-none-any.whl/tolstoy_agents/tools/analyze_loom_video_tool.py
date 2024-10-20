import os
import json
import requests
import functools
from pydantic import BaseModel, Field
import boto3

from langchain.tools import StructuredTool

from tolstoy_agents.utils import (
    handle_exceptions,
    log_lumigo_exception,
    log_lumigo_error
    )
from tolstoy_agents.gemini_client import GeminiClient


MODEL_NAME = "gemini-1.5-flash-preview-0514"
VIDEO_SYSTEM_INSTRUCTION = "As an AI agent capable of understanding videos, your task is to analyze the content of the provided video and describe its details. Focus on identifying the main subjects, objects, actions, and any other relevant information that would help comprehend the video. Provide a concise yet comprehensive summary of the video."
VIDEO_ANALYZE_PROMPT = "Please analyze the attached video and provide a detailed summary of its content. The output of your analysis will be used by an AI agent to understand and interpret the video. Include information about the main subjects, objects, actions, and any other relevant details that would aid in comprehending the video. Be concise and precise in your summary, focusing on the most important aspects of the video."

gemini_client = GeminiClient(system_instruction=VIDEO_SYSTEM_INSTRUCTION, model_name=MODEL_NAME)

lambda_client = boto3.client('lambda')

class ToolInput(BaseModel):
    loom_video_id: str = Field(description="Id of the loom video")


def fetch_loom_download_url(video_id):
    api_url = f"https://www.loom.com/api/campaigns/sessions/{video_id}/transcoded-url"
    headers = {
        'authority': 'www.loom.com',
        'accept': 'application/json',
        'content-type': 'application/json',
        'origin': 'https://www.loom.com',
        'referer': f'https://www.loom.com/share/{video_id}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.post(api_url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the download URL. Status code: {response.status_code}")
    content = response.json()
    return content["url"]


def download_loom_video(url):
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception(f"Failed to download the video. Status code: {response.status_code}")
    return response.content


@handle_exceptions
def analyze_loom_video(loom_video_id: str) -> str:
    try:
        if not loom_video_id:
            log_lumigo_error("No video ID provided.", "analyze_video")
            return None

        download_url = fetch_loom_download_url(loom_video_id)
        print(f"Fetching video {loom_video_id} from {download_url}")
        video_data = download_loom_video(download_url)
        
        if not video_data:
            log_lumigo_error("No video data downloaded.", "analyze_video")
            return None

        mime_type = "video/mp4"
        video_file_part = gemini_client.get_part(video_data, mime_type=mime_type)
        contents = [video_file_part, VIDEO_ANALYZE_PROMPT]

        try:
            response = gemini_client.generate(contents)
            return response.text
        except Exception as e:
            log_lumigo_exception(e, "gemini_client.generate")
            return None

    except Exception as e:
        log_lumigo_exception(e, "analyze_video")
        return None


def analyze_loom_video_factory() -> StructuredTool:
    return StructuredTool.from_function(
        func=analyze_loom_video,
        name="analyze_loom_video",
        description= (
            "Use this tool if there's a loom video link in the email, and to understand the context of the loom video. "
            "The response that you get from this tool you should act like you have seen the loom video and not acting that you just read a text"
        ),
        args_schema=ToolInput,
        return_direct=False
    )
