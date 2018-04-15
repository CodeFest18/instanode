from twilio.rest import Client


def send_sms():
	account = "AC99b4a100f1abb3d020ebd7ed37323cdf"
	token = "20ac0302aa5dd35da66c1ffe5e5c26b5"
	client = Client(account, token)

	message = client.messages.create(to="+12159513923", from_="+12675364672",
                                 body="Hey Urja! This is BlocKontribute. Please got to blocKontributed.com to vote for the charity you care about! ")
