import os
import requests
from dotenv import load_dotenv

load_dotenv()

LINKEDIN_PROFILE_URL = "https://www.linkedin.com/in/shaileshkmr/"
GIST_LINKEDIN_PROFILE = "https://gist.githubusercontent.com/sku1978/0c1f0ef3fefbe600a675ebcf00fc1695/raw/4bce3b5a29601c180f09a7eec75283d92706bf7f/shaileshkmr-linkedin.json"
#GIST_LINKEDIN_PROFILE = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
PROXYCURL_ENDPOINT = "https://nubela.co/proxycurl/api/v2/linkedin"


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """Scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        linkedin_profile_url = GIST_LINKEDIN_PROFILE
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = PROXYCURL_ENDPOINT
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", "None", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    print(scrape_linkedin_profile(LINKEDIN_PROFILE_URL, mock=True))
