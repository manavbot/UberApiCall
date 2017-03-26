import urllib2

from lyft_rides.auth import ClientCredentialGrant
from lyft_rides.session import Session

auth_flow = ClientCredentialGrant(
    YOUR_CLIENT_ID,
    YOUR_CLIENT_SECRET,
    public,
    )
session = auth_flow.get_session(
session = Session(server_token = "sVG0_JuX6mRTU1FUTvL8wT1M8-2V51wrLv4sKzxaS")

from lyft_rides.client import LyftRidesClient

client = LyftRidesClient(session)
response = client.get_ride_types(37.7833, -122.4167)
ride_types = response.json.get('ride_types')
