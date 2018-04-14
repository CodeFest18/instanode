from twilio.rest import Client

account = "xxx"
token = "xxx"
client = Client(account, token)

message = client.messages.create(to="+12159513923", from_="+12675364672",
                                 body="Hey Urja! This is BlocKontribute. Please got to blocKontributed.com to vote for the charity you care about! ")
