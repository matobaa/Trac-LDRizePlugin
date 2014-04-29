#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 MATOBA Akihiro <matobaa+trac-hacks@gmail.com>
# All rights reserved.
#
# This software is licensed as described in the file LISENSE, which
# you should have received as part of this distribution.

from trac.core import Component, implements
from trac.web.api import ITemplateStreamFilter
from trac.web.chrome import add_script, ITemplateProvider, add_stylesheet
from pkg_resources import ResourceManager


class LDRize(Component):
    implements(ITemplateStreamFilter, ITemplateProvider)

    # ITemplateProvider methods
    def get_templates_dirs(self):
        return [ResourceManager().resource_filename(__name__, 'templates')]

    def get_htdocs_dirs(self):
        return [('ldrize', ResourceManager().resource_filename(__name__, 'htdocs'))]

    # ITemplateStreamFilter methods
    def filter_stream(self, req, method, filename, stream, data):
        if filename in ["report_list.html", "report_view.html", "query.html", "ticket.html", "timeline.html",
                        "wiki_view.html", "search.html"]:
            add_stylesheet(req, "ldrize/ldrize.css")
            add_script(req, "ldrize/keyboard_nav.js")
        return stream
    # TODO: search result
    # TODO: TitleIndex
