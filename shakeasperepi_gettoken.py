import tweepy

consumer_key="[INSERT YOUR DATA HERE]"
consumer_secret="[INSERT YOUR DATA HERE]"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)


try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print("Failed to get request token")
 
print(redirect_url)    

verifier = input('Verifier:')

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print("Failed to get request token")

print(auth.access_token)
print(auth.access_token_secret)


