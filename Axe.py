import requests
from colorama import Fore, Style

def find_username(username):
    websites = {
        'Instagram': f'https://www.instagram.com/{username}/',
        'Twitter': f'https://twitter.com/{username}',
        'Facebook': f'https://www.facebook.com/{username}',
        'LinkedIn': f'https://www.linkedin.com/in/{username}',
        'Reddit': f'https://www.reddit.com/user/{username}',
        'Snapchat': f'https://www.snapchat.com/add/{username}',
        'Tumblr': f'https://{username}.tumblr.com/',
        'Pinterest': f'https://www.pinterest.com/{username}/',
        'GitHub': f'https://github.com/{username}',
        'Stack Overflow': f'https://stackoverflow.com/users/{username}',
        'Quora': f'https://www.quora.com/profile/{username}',
        'YouTube': f'https://www.youtube.com/user/{username}',
        'Twitch': f'https://www.twitch.tv/{username}',
        'Vimeo': f'https://vimeo.com/{username}',
        'Flickr': f'https://www.flickr.com/photos/{username}/',
        'Medium': f'https://medium.com/@{username}',
        'WordPress': f'https://{username}.wordpress.com/',
        'SoundCloud': f'https://soundcloud.com/{username}',
        'DeviantArt': f'https://{username}.deviantart.com/',
        'Behance': f'https://www.behance.net/{username}',
        'Dribbble': f'https://dribbble.com/{username}',
        'Fiverr': f'https://www.fiverr.com/{username}',
        'Etsy': f'https://www.etsy.com/shop/{username}',
        'eBay': f'https://www.ebay.com/usr/{username}',
        'Amazon': f'https://www.amazon.com/gp/profile/amzn1.account.{username}',
        'Goodreads': f'https://www.goodreads.com/user/show/{username}',
        'Last.fm': f'https://www.last.fm/user/{username}',
        'Meetup': f'https://www.meetup.com/members/{username}',
        'Blogger': f'https://{username}.blogspot.com/',
        'LiveJournal': f'https://{username}.livejournal.com/',
        'Yelp': f'https://www.yelp.com/user_details?userid={username}',
        'Strava': f'https://www.strava.com/athletes/{username}',
        'CouchSurfing': f'https://www.couchsurfing.com/people/{username}',
        'HackerRank': f'https://www.hackerrank.com/{username}',
        'Kaggle': f'https://www.kaggle.com/{username}',
        'Bitbucket': f'https://bitbucket.org/{username}/',
        'GitLab': f'https://gitlab.com/{username}',
        'SlideShare': f'https://www.slideshare.net/{username}',
        'Imgur': f'https://imgur.com/user/{username}',
        'Patreon': f'https://www.patreon.com/{username}',
        'OnlyFans': f'https://onlyfans.com/{username}',
        'TikTok': f'https://www.tiktok.com/@{username}',
        'MixCloud': f'https://www.mixcloud.com/{username}/',
        'Snapfish': f'https://www.snapfish.com/{username}',
        'WeHeartIt': f'https://weheartit.com/{username}',
        'Clubhouse': f'https://www.joinclubhouse.com/@{username}',
        'Tidal': f'https://tidal.com/browse/artist/{username}',
        


    }

    for site, url in websites.items():
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200 and username.lower() in response.text.lower():
                print(Fore.RED + f"[FOUND!] {site}:" + Style.RESET_ALL, url)
        except requests.RequestException:
            continue
 
print(Fore.RED + """
 █████╗ ██╗  ██╗███████╗
██╔══██╗╚██╗██╔╝██╔════╝
███████║ ╚███╔╝ █████╗  
██╔══██║ ██╔██╗ ██╔══╝  
██║  ██║██╔╝ ██╗███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                  
Made by Goof
""" + Style.RESET_ALL)

input(Fore.RED + "Press Enter to start..." + Style.RESET_ALL)


username_to_find = input(Fore.RED + "Enter the username to search: " + Style.RESET_ALL)
find_username(username_to_find)
