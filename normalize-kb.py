import json
import re
from datetime import datetime, timezone


DIR_PATH = f"target/tip"
DEFAULT_AUTHOR_URL = "https://alkem.io/user/sander-dijkhuis-3912"

raw_data = None
with open(f"{DIR_PATH}/raw-data.json") as file:
    raw_data = json.load(file)

def none_if_empty(s):
    if s == "":
        return None
    else:
        return s

def author_reference(author, name):
    result = [reference['uri']
              for reference in author['references']
              if reference['name'] == name
              and reference['uri'] != ""]
    if len(result) == 1:
        return result[0]
    else:
        return None

callouts = \
    raw_data['data']['spaces'][0]['collaboration']['calloutsSet']['callouts']
questions = \
    {callout['framing']['profile']['url']: {
        'slug': callout['nameID'],
        'title': callout['framing']['profile']['displayName'],
        'description_md': callout['framing']['profile']['description'],
        'tags': [tag
                 for ts in callout['framing']['profile']['tagsets']
                 for tag in ts['tags']],
        'author': callout['createdBy']['profile'] \
            if callout['createdBy'] != None else None,
        'created': callout['createdDate'],
        'updated': callout['updatedDate'],
        'children': \
            [contribution['post'] | {
                'parent_url': callout['framing']['profile']['url'],
                'url': contribution['post']['profile']['url']
             }
             for contribution in callout['contributions']
             if contribution['post'] != None]
    }
    for callout in callouts
    if callout['type'] == 'POST_COLLECTION'
    and 'Kennisbank' in [tag
                         for ts in callout['classification']['tagsets']
                         for tag in ts['tags']]}
answers = \
    {post['url']: {
        'slug': post['nameID'],
        'title': post['profile']['displayName'],
        'description_md': post['profile']['description'],
        'created': post['createdDate'],
        'updated': post['updatedDate'],
        'author': post['createdBy']['profile'] \
            if post['createdBy'] != None else None,
        'children': \
            [comment | {
                 'parent_url': post['url'],
                 'url': f"{post['url']}#{comment['id']}"
             }
             for comment in post['comments']['messages']]
    }
    for question in questions.values()
    for post in question['children']}
comments = \
    {comment['id']: {
        'thread_id': comment['threadID'],
        'author': comment['sender']['profile'],
        'created': datetime.fromtimestamp(comment['timestamp']/1000).isoformat(timespec='milliseconds') + 'Z',
        'message_md': comment['message'],
        'children': \
            [reaction | {
                 'parent_url': comment['url'],
                 'url': f"{comment['url']}/{reaction['id']}"
             }
             for reaction in comment['reactions']]
    }
    for answer in answers.values()
    for comment in answer['children']}
reactions = \
    {reaction['id']: {
        'author': reaction['sender']['profile'],
        'created': datetime.fromtimestamp(reaction['timestamp']/1000).isoformat(timespec='milliseconds') + 'Z',
        'emoji': reaction['emoji']
    }
    for comment in comments.values()
    for reaction in comment['children']}
authors = \
    {work['author']['url']: {
        'name': work['author']['displayName'],
        'tagline': work['author']['tagline'] if work['author']['tagline'] != "" else None,
        'created': work['author']['createdDate'],
        'updated': work['author']['createdDate'],
        'description_md': work['author']['description'],
        'avatar': work['author']['visual']['uri'],
        'city': none_if_empty(work['author']['location']['city']),
        'country': none_if_empty(work['author']['location']['country']),
        'github': author_reference(work['author'], 'github'),
        'twitter': author_reference(work['author'], 'twitter'),
        'linkedin': author_reference(work['author'], 'linkedin'),
        'links': [{
            'name': link['name'],
            'description': link['description'],
            'url': link['uri']
        }
        for link in work['author']['references']
        if link['name'] not in ['github', 'twitter', 'linkedin']]
    }
     for work in list(questions.values()) + list(answers.values()) + list(comments.values()) + list(reactions.values())
     if work['author'] != None}

def normalize(work):
    author = work.pop('author')
    if author == None:
        work['author_uri'] = DEFAULT_AUTHOR_URL
    else:
        work['author_uri'] = author['url']
    if 'children' in work:
        work['children'] = [child['url'] for child in work['children']]
    return work

index = {
    'questions': {k: normalize(question) for k, question in questions.items()},
    'answers': {k: normalize(answer) for k, answer in answers.items()},
    'comments': {k: normalize(comment) for k, comment in comments.items()},
    'reactions': {k: normalize(reaction) for k, reaction in reactions.items()},
    'authors': authors
}

print("Questions:", len(questions))
print("Answers:", len(answers))
print("Comments:", len(comments))
print("Reactions:", len(reactions))
print("Authors:", len(authors))

with open(f"{DIR_PATH}/normalized-data.json", 'w', encoding='utf-8') as file:
    json.dump(index, file, indent=2, ensure_ascii=False)
    file.write("\n")
