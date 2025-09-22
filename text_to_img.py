import openai
import requests
from PIL import Image
from io import BytesIO

#set your openai api key
openai.api_key="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"

def generate_image(prompt,image_size="1024x1024"):
    try:
        print("f Generating image for prompt:'{prompt}'")
        response=openai.Image.create(
        prompt=prompt,
        n=1,
        size=image_size
    )
        image_url=response['data'][0]['url']
        print(f"Image URL:{image_url}")
        
        image_response=requests.get(image_url)
        image=Image.open(BytesIO(image_response.content))
    
        image.save("generated_image.png")
        image.show()
    
        return "Image generated and saved as 'generated_image.png'"
    except Exception as e:
      return f"invalid input:{str(e)}"

prompt_text=input("Enter your prompt for image generation")
result=generate_image(prompt_text)
print(result)