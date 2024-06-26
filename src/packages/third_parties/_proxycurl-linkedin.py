import requests

api_key = "YOUR_API_KEY"
headers = {"Authorization": "Bearer " + "xmLeogDauKByo12MiAqpJQ"}
api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
params = {
    #    'twitter_profile_url': 'https://x.com/shaileshkmr',
    #    'facebook_profile_url': 'https://www.facebook.com/shailesh.kumar.75248795',
    "linkedin_profile_url": "https://www.linkedin.com/in/shaileshkmr/",
    "extra": "include",
    "github_profile_id": "include",
    "facebook_profile_id": "include",
    "twitter_profile_id": "include",
    "personal_contact_number": "include",
    "personal_email": "include",
    "inferred_salary": "include",
    "skills": "include",
    "use_cache": "if-present",
    "fallback_to_cache": "on-error",
}
response = requests.get(api_endpoint, params=params, headers=headers)

print(response.json())
