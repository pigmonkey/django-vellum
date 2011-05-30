"""
These blog settings should not be edited directly.
Instead, overwrite them in the main project's setting file.
"""
from django.conf import settings
from django.contrib.sites.models import Site

# The name of the blog.
# This defaults to the name of the site.
BLOG_NAME = getattr(settings, 'BLOG_NAME', Site.objects.get_current().name)

# A short description of what the blog is about.
BLOG_DESCRIPTION = getattr(settings, 'BLOG_DESCRIPTION', 'A basic Django blog')

# How many posts should appear on a single page.
BLOG_PAGESIZE = getattr(settings, 'BLOG_PAGESIZE', 12)

# How many posts should appear in the RSS feed.
# This defaults to the same value as BLOG_PAGESIZE above.
BLOG_FEEDSIZE = getattr(settings, 'BLOG_FEEDSIZE', BLOG_PAGESIZE)

# If set to true, only post excerpts will be shown in page listings.
# This defaults to false, which causes the full post body to be shown.
BLOG_EXCERPTS = getattr(settings, 'BLOG_EXCERPTS', False)

# If set to true, only post excerpts will be shown in feeds.
# This defaults to the same value as BLOG_EXCERPTS above.
BLOG_FEEDEXCERPTS = getattr(settings, 'BLOG_FEEDEXCERPTS', BLOG_EXCERPTS)

# If set to true, the Markdown WMD editor from Django WMD will be used on the
# body field of all posts.
BLOG_WMD = getattr(settings, 'BLOG_WMD', False)