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

### If you dont understand something feel free to ping me in #code-jam-website

