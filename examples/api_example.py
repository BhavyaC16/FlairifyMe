import requests

# The FlairifyMe API can be accessed by querying as follows

api_endpoint = 'http://flairify-me.herokuapp.com/api/resource?redditURL='
reddit_post = 'https://www.reddit.com/r/india/comments/hi0i9x/what_is_environmental_impact_assessment_eia_2020/'
query = api_endpoint + reddit_post

response = requests.get(query)
print(response.text)

# Sample Output:
# {"status": "successful", "status_code": 200, "result": {"flair": "Policy Economy"}}
