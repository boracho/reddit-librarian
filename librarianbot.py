import praw
import time
import json

sub_philo = 'philosophy'
sub_science = 'science'
library = ''
key_flair = 'psychology'
keyword_philo = 'consciousness'
keyword_test = 'snow'
keyword_test_two = 'intersection'
keyword_sci = 'quantum'
already_posted_id = []
already_posted_url = []

r = praw.Reddit(user_agent = 'Librarian Bot')
r.login('', '')
subreddit = r.get_subreddit(sub_science)

def submission_parser(subreddit, keyword):
    with open('log.json', 'r') as data:
        dbase = json.load(data)
    for submission in subreddit.get_hot(limit=10):
        lowercase_title = str(submission).lower()
        if submission.id not in dbase['already posted id'] and submission.url not in dbase['already posted url']:
            if submission.link_flair_text!= None and submission.link_flair_text.lower() == keyword:
                with open('log.json', 'r+') as f:
                    dbase = json.load(f)
                    dbase['already posted id'].append(submission.id)
                    dbase['already posted url'].append(submission.url)
                    f.seek(0)
                    json.dump(dbase, f, indent=4)
                r.submit(library, submission.title, url=submission.url)
                print 'I just added another link to your library!'

while True:
    submission_parser(subreddit, key_flair)
    time.sleep(3600)
