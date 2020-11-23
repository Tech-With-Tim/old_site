# Contributing

To see what you can work on please refer to the [issues](https://github.com/Tech-With-Tim/old_site/issues)

Please work only on Issues marked with Contributors allowed
## Formatting
[Please follow pep-8 guidelines](https://www.python.org/dev/peps/pep-0008/)

PR's with pylint score above 6 would be considered this is not a strict rule though.

## Workflow
You have to work on the dev branch on this repo<br>
Please checkout to the dev branch on your cloned repo as well
and commit on that.

## PRs
* Pull requests on dev branch will be reviewed by Sylte, Correct_Skill, Alex-Galaxy, M7MD, Takos and sarzz.
* Once we have a significant update, the dev branch will be merged into the main branch and pulled on the website
* Please read all the docstrings to understand how things are being worked out
## Please remember not to commit:
* our_secrets.py
* TWT/discord.py
* TWT/settings.py <br>
PRs with these files modified will not be accepted

## A global explanation

the TWT/context.py file is being called in every view
```python
def get_context(self, request: WSGIRequest) -> dict:
    return get_discord_context(request=request)
```     
like this
please add this in the context of the view because this loads all the pfp and permissions

## directory structure
The following is the tree representation of the code jam website
```
.
├── CONTRIBUTE.md
├── Dockerfile
├── LICENSE
├── README.md
├── SETUP.md
├── TWT
│   ├── __init__.py
│   ├── apps
│   │   ├── challenges
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── migrations
│   │   │   │   
│   │   │   │   
│   │   │   │   
│   │   │   │   
│   │   │   │   
│   │   │   ├── models
│   │   │   │   ├── __init__.py
│   │   │   │   ├── challenge.py
│   │   │   │   └── custom_pages.py
│   │   │   ├── urls.py
│   │   │   └── views
│   │   │       ├── __init__.py
│   │   │       ├── custom_page_view.py
│   │   │       ├── delete_challenge.py
│   │   │       ├── end.py
│   │   │       ├── home.py
│   │   │       ├── logout.py
│   │   │       ├── new.py
│   │   │       ├── start.py
│   │   │       ├── start_submission.py
│   │   │       ├── start_team.py
│   │   │       ├── start_voting.py
│   │   │       ├── stop_submission.py
│   │   │       ├── stop_team.py
│   │   │       ├── stop_voting.py
│   │   │       ├── test.py
│   │   │       ├── unreleased.py
│   │   │       └── view.py
│   │   ├── timathon
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── migrations
│   │   │   ├── models
│   │   │   │   ├── __init__.py
│   │   │   │   ├── submission.py
│   │   │   │   └── team.py
│   │   │   ├── urls.py
│   │   │   └── views
│   │   │       ├── __init__.py
│   │   │       ├── add_member_view.py
│   │   │       ├── codjam_listview.py
│   │   │       ├── create_team.py
│   │   │       ├── home.py
│   │   │       ├── leave_member_view.py
│   │   │       ├── submission_list_view.py
│   │   │       ├── submission_view.py
│   │   │       ├── unvote.py
│   │   │       ├── view_team.py
│   │   │       └── vote.py
│   │   └── weekly
│   │       ├── __init__.py
│   │       ├── admin.py
│   │       ├── migrations
│   │       │   └── __init__.py
│   │       ├── models
│   │       │   └── __init__.py
│   │       ├── sample-tester.py
│   │       ├── urls.py
│   │       └── views
│   │           ├── __init__.py
│   │           └── home.py
│   ├── asgi.py
│   ├── cache.py
│   ├── context.py
│   ├── discord.py
│   ├── settings.py
│   ├── static
│   │   ├── css
│   │   │   ├── base.css
│   │   │   ├── bootstrap.min.css
│   │   │   ├── index.css
│   │   │   ├── logout.css
│   │   │   ├── new.css
│   │   │   ├── submissions_list.css
│   │   │   ├── timathonHome.css
│   │   │   └── timathonTeam.css
│   │   ├── images
│   │   │   ├── cropped-Tech-With-TimXL-192x192.png
│   │   │   └── discord.png
│   │   └── js
│   │       ├── bootstrap.min.js
│   │       ├── jquery-3.3.1.slim.min.js
│   │       └── popper.min.js
│   ├── templates
│   │   ├── base
│   │   │   ├── base.html
│   │   │   └── navbar.html
│   │   ├── challenges
│   │   │   ├── custom_page.html
│   │   │   ├── index.html
│   │   │   ├── logout.html
│   │   │   ├── new.html
│   │   │   ├── test.html
│   │   │   ├── unreleased.html
│   │   │   └── view.html
│   │   ├── timathon
│   │   │   ├── create_teams.html
│   │   │   ├── index.html
│   │   │   ├── submissions_list.html
│   │   │   ├── submit.html
│   │   │   └── view_team.html
│   │   └── weekly
│   │       └── index.html
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── manage.py
├── nginx.default
├── our_secrets.example.py
├── requirements.txt
└── start-server.sh
```

### If you dont understand something feel free to ping me in #code-jam-website

