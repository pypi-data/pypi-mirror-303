# -*- coding: utf-8 -*-
import os

from slack_bolt import App
from crontab import CronTab

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

tab = CronTab()
def app_schedule(s):
    def _schedule(f):
        job = tab.new(command='/bin/true')
        job.setall(s)
        job.func = f
        return f
    return _schedule
app.schedule = app_schedule

def check_access(client, group_id, user_id):
    response = client.usergroups_users_list(usergroup=group_id)
    return user_id in response['users']
