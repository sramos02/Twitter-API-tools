# 2- Search user coments in a hashtag and return this users
def search_users_in_hashtag(hashtag, count):
    lng = api.me().lang
    user_list = []
    
    if lng is None:
        lng = "en"

    print("\nTweets for " + hashtag)
    for tweet in api.search(q=hashtag, lang=lng, result_type="mixed", include_entities="false", count=count):
        print('\t' + str(tweet.user.id))
        user_list.insert(-1, tweet)
    return user_list
