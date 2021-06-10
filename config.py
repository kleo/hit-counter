import os

# Location of database
DATABASE_FILE_PATH = os.path.abspath(os.getenv('DATABASE_FILE_PATH', 'data.db'))

# Amount of time before another view by the same user will count
COOKIE_TIMEOUT = 60 * 5

# Length of cookie value (stored client side). Literally just the cookie size.
COOKIE_RANDOM_VALUE_LENGTH = 12

# Template of SVG with {count} to be provided
SVG_TEMPLATE = """<?xml version="1.0"?>
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="20">
<rect rx="3" width="100" height="20" fill="transparent"/>
	<g fill="#000" text-anchor="start" font-family="Monospace" font-size="10" font-weight="bold">
	<text x="0" y="13">{count}</text>
	</g>
<!-- This count is for the url: {url} -->
</svg>"""

# Whether or not to export Prometheus metrics
EXPOSE_METRICS = os.getenv('EXPOSE_METRICS', 'false').lower() == 'true'

# Prefix for Prometheus metrics
METRICS_PREFIX = os.getenv('METRICS_PREFIX', 'hitcounter')

# Show top n domains on front page
NUM_TOP_DOMAINS = int(os.getenv('NUM_TOP_DOMAINS', '10'))

# Show top n URLs on front page
NUM_TOP_URLS = int(os.getenv('NUM_TOP_URLS', '0'))

# Regular expressions to ignore when getting top sites
TOP_SITES_IGNORE_DOMAIN_RE_MATCH = [
    r'192\.168\.\d{1,3}\.\d{1,3}',
    r'127\.0\.\d{1,3}\.\d{1,3}',
    r'^$'
]

# Whitelist of URL patterns to track. Any URL will be allowed if list is empty
URL_WHITELIST_RE = [
]

# Regular expressions to match URLs to blacklist
URL_BLACKLIST_RE = [
]
