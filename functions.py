# -*- coding: utf-8 -*-
#<site_root>/functions.py

from hyde.plugin import Plugin


# try to change to : resource.prev_by... instead of prev_by...(resource)
def prev_by_time_and_language(resource):
    temp = resource
    while temp.prev_by_time:
        temp = temp.prev_by_time
        if temp.meta.language == resource.meta.language:
            return temp
    return None

def next_by_time_and_language(resource):
    temp = resource
    while temp.next_by_time:
        temp = temp.next_by_time
        if temp.meta.language == resource.meta.language:
            return temp
    return None


class MyJinjaLoader(Plugin):

    def template_loaded(self, template):
        template.env.globals['prev_by_time_and_language'] = prev_by_time_and_language
        template.env.globals['next_by_time_and_language'] = next_by_time_and_language
