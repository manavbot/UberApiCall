import urllib2

request_headers = {
	"Authorization": "Token VG0_JuX6mRTU1FUTvL8wT1M8-2V51wrLv4sKzxaS" 
	}

from uber_rides.session import Session
session = Session(server_token = "sVG0_JuX6mRTU1FUTvL8wT1M8-2V51wrLv4sKzxaS")

request = urllib2.Request("https://api.uber.com/v1.2/estimates/price?start_latitude=37.7752315&start_longitude=-122.418075&end_latitude=37.7752415&end_longitude=-122.518075", headers = request_headers)
content = urllib2.urlopen(request).read()
print content
'''from uber_rides.auth import AuthorizationCodeGrant
auth_flow = AuthorizationCodeGrant(
    "sTvcJfy3Q4-IryZuEdmjlYILm0mOxH9C",
    "",
    "EmCGI1ZIUwUeTchbnXe_4BmJ8I8jQYMfpDX1Djgw,"
    "http://localhost:7000",
)
auth_url = auth_flow.get_authorization_url()

from uber_rides.client import UberRidesClient
client = UberRidesClient(session)
response = client.get_price_estimates(
    start_latitude=37.770,
    start_longitude=-122.411,
    end_latitude=37.791,
    end_longitude=-122.405
   
)

estimate = response.json.get('prices')
print estimate
'''