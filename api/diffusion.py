import requests

def generate_image(prompt):
    # Replace with your actual diffusion API endpoint
    diffusion_api_endpoint = "https://api.diffusion.com/generate"

    # Make a POST request to the diffusion API
    response = requests.post(diffusion_api_endpoint, json={"prompt": prompt})

    # Check if the request was successful
    if response.status_code == 200:
        # Get the image URL from the response
        image_url = response.json().get("image_url")

        # Return the image URL
        return image_url
    else:
        # If the request was not successful, return an error message
        return "Error: Could not generate image."