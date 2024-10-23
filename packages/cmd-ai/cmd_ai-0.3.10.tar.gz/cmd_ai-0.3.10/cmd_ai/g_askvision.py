#!/usr/bin/env python3
"""
We create a unit, that will be the test_ unit by ln -s simoultaneously. Runs with 'pytest'
"""
import datetime as dt
import time
import os
import tiktoken
from console import fg,bg,fx
from fire import Fire

import openai
from cmd_ai import config
from cmd_ai import texts
from cmd_ai.api_key import get_api_key
from cmd_ai.version import __version__

#### ---- functions -----
#from  cmd_ai import function_chmi
#from  cmd_ai import function_goog # google search
#from  cmd_ai import function_webc # web content
import json # for function call

# importing modules
#import urllib.request
#from PIL import Image
#import tempfile

import base64
import requests
import glob

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def g_askvision(
        prompt,
        image_path = None,
        temp=0.0,
        model="gpt-4-turbo",
        # limit_tokens=300,
        total_model_tokens=4096 * 2 - 50, # guess
        size="1024x1024",
        detail="low",
        n=1
):
    """
    upload an image
    """

    print(f"{fg.orange}i... using VISION with prompt, detail {detail}: {fg.default}", prompt )

    # OpenAI API Key
    myapi_key = get_api_key() #"YOUR_OPENAI_API_KEY"


    # Path to your image
    #image_path = "path_to_your_image.jpg"
    # Getting the base64 string


    if image_path is None:
        guess = prompt.split(".jpg")[0]
        image_path = guess+".jpg"

    if not os.path.exists(image_path):
        print(f"{fg.red}X... no image defined{fg.default}")
        print(glob.glob("*.jpg"))
        IMG = input("> input jpg filename without .jpg :")
        image_path = IMG+".jpg"

    if not os.path.exists(image_path):
        print(f"{fg.red}X... no image defined{fg.default}")
        return None
        #return None


    limit_tokens = config.CONFIG['limit_tokens']

    base64_image = encode_image(image_path)

    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {myapi_key}"
    }

    payload = {
      "model": model,
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": prompt
            },
            {
              "type": "image_url",
              "image_url": {
                  "url": f"data:image/jpeg;base64,{base64_image}",
                  "detail": detail
              }
            }
          ]
        }
      ],
      "max_tokens": limit_tokens
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    #print( response.json())
    #print( "res   ",type(response) ) # req models response
    #print( "res js",type(response.json() ) ) # dict

    resdi = response.json()
    #print( type(resdi) )  # dict
    #print( resdi )
    #print( resdi.keys() )
    #print(resdi['choices'] )
    #print( resdi['choices'][0] )
    #print( resdi['choices'][0]['message'] )
    #print( resdi['choices'][0]['message']['content'] )
    res = resdi['choices'][0]['message']['content']
    finish = resdi['choices'][0]['finish_reason'] != "stop"

    #finish = response.choices[0].finish_reason

    return res, finish
