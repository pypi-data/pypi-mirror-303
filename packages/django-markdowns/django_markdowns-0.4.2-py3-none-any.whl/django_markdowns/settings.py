# Copyright (C) 2021-2024 J. Nathanael Philipp (jnphilipp) <nathanael@philipp.land>
#
# This file is part of django_markdowns.
#
# django_markdowns is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django_markdowns is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django_markdowns.  If not, see <http://www.gnu.org/licenses/>.
"""Markdown Django app settings."""

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


USER_SETTINGS = getattr(settings, "MARKDOWNS", {})

EXTENSIONS: list[str] = []
IMG_CLASS: str | None = None
USE_BOOTSTRAP: bool = False

if "EXTENSIONS" in USER_SETTINGS:
    for extension in USER_SETTINGS["EXTENSIONS"]:
        if extension not in [
            "extra",
            "abbr",
            "attr_list",
            "def_list",
            "footnotes",
            "md_in_html",
            "tables",
            "admonition",
            "codehilite",
            "legacy_attrs",
            "legacy_em",
            "meta",
            "nl2br",
            "sane_lists",
            "smarty",
            "toc",
            "wikilinks",
        ]:
            raise ImproperlyConfigured(
                f"Unkown extension: {extension}. Musst be one of: extra, abbr, "
                + "attr_list, def_list, footnotes, md_in_html, tables, admonition, "
                + "codehilite, legacy_attrs, legacy_em, meta, nl2br, sane_lists, "
                + "smarty, toc, wikilinks."
            )
        EXTENSIONS.append(extension)

if "IMG_CLASS" in USER_SETTINGS:
    IMG_CLASS = USER_SETTINGS["IMG_CLASS"]

if "USE_BOOTSTRAP" in USER_SETTINGS:
    USE_BOOTSTRAP = USER_SETTINGS["USE_BOOTSTRAP"]

    if not isinstance(USE_BOOTSTRAP, bool):
        raise ImproperlyConfigured("USE_BOOTSTRAP needs to be a boolean.")

    if USE_BOOTSTRAP:
        IMG_CLASS = "img-fluid"
