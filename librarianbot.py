import praw
import time

sub_test = 'pics'
sub_test_two = 'funny'
sub_philo = 'philosophy'
sub_science = 'science'
library = 'infiniteknowledge'
key_flair = 'physics'
keyword_philo = 'aristotle'
keyword_test = 'snow'
keyword_test_two = 'intersection'
keyword_sci = 'quantum'
already_posted_id = []
already_posted_url = []

r = praw.Reddit(user_agent = 'Librarian Experiment')
r.login('NSA_Robutt', 'jfetbs170')
subreddit = r.get_subreddit(sub_philo)

def submission_parser(subreddit, keyword):
    for submission in subreddit.get_hot(limit=200):
        lowercase_title = str(submission).lower()
        if submission.id not in already_posted_id and submission.url not in already_posted_url:
            if keyword in lowercase_title:
                already_posted_id.append(submission.id)
                already_posted_url.append(submission.url)
                r.submit(library, submission.title, url=submission.url)
                print 'I just added another link to your library!'

while True:
    submission_parser(subreddit, keyword_philo)
    time.sleep(3600)
