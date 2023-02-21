import praw
from praw.models import MoreComments
import pandas as pd
from secret import password

reddit = praw.Reddit(
    client_id='****',
    client_secret="****",
    password=password,
    user_agent="extraction/meg_avadh",
    username="meg_avadh"
)


url = "https://www.reddit.com/r/interestingasfuck/comments/t5pkhv/ukraine_is_turning_into_ruins_thanks_russia/"
submission = reddit.submission(url=url)

mylist = []
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    mylist.append(top_level_comment.body)

print(mylist[0])
"""df = pd.DataFrame(mylist).to_excel('output.xlsx', header=False, index=False)


df.head()"""
