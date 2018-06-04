from lxml import html
import requests
import sys

url = sys.argv[1]

print ('Crawling', url, '...')

page = requests.get(url)
content = page.content.decode("utf-8")
hasIssues = False

if 'wp-content' in content :
    hasIssues = True
    print ('Path found with `wp-content`!')

if 'name="generator" content="WordPress' in content :
    hasIssues = True
    print ('Generator meta tag found!')

if 'wp-json' in content: 
    hasIssues = True
    print ('Reference to WP REST API found: `wp-json`')

if 'wp-admin' in content: 
    hasIssues = True
    print ('Reference to the WP Admin found: `wp-admin`')

if hasIssues == False:
    print ('No issues found!')
