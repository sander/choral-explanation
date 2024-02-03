# Copyright sander.dijkhuis@cleverbase.com 2024; Licensed under the EUPL.

import json
import re
import urllib
from datetime import datetime
from urllib.request import Request

def _read_queries():
    with open("queries.graphql", "r") as reader:
        return reader.read()

def _http_request(queries, operation, variables):
    endpoint = "https://alkem.io/api/private/graphql"
    payload = {
        "query": queries,
        "operationName": operation,
        "variables": variables
    }
    headers = {
        "Content-Type": "application/json"
    }
    body = json.dumps(payload).encode("utf-8")
    return Request(endpoint, body, headers)

def _fetch_json(http_request):
    response = urllib.request.urlopen(http_request)
    text = response.read().decode("utf-8")
    return json.loads(text)

def fetch_question_list_data(space_name_id):
    queries = _read_queries()
    variables = {'spaceNameId': space_name_id}
    request = _http_request(queries, 'questions', variables)
    response = _fetch_json(request)
    return response["data"]["space"]["collaboration"]["callouts"]

def _strip_license(markdown):
    return re.sub(r".*Bijdragen zijn gelicenseerd onder.*"
        + r"\[.*CC BY 4\.0.*\]\(https:\/\/creativecommons\.org"
        + r"\/licenses\/by\/4\.0\/deed\.nl\).*\..*",
        "", markdown.strip()
    ).strip()

def _author(author_data):
    return {
        'author_name': author_data['profile']['displayName'],
        'author_url': author_data['profile']['url'],
    }

def question(question_data):
    description = question_data["framing"]["profile"]["description"]
    question = {
        "id": question_data["nameID"],
        "title": question_data["framing"]["profile"]["displayName"].strip(),
        "url": question_data["framing"]["profile"]["url"],
        "description_md": _strip_license(description),
        "answers": []
    }
    by = question_data["createdBy"]
    if by != None:
        question = question | _author(by)
    for answer_data in question_data["contributions"]:
        answer = {
            "id": answer_data["post"]["nameID"],
            "title": answer_data["post"]["profile"]["displayName"].strip(),
            "url": answer_data["post"]["profile"]["url"],
            "description_md": answer_data["post"]["profile"]["description"],
            "comments": []
        } | _author(answer_data['post']['createdBy'])
        question["answers"].append(answer)
        for comment_data in answer_data["post"]["comments"]["messages"]:
            date = datetime.fromtimestamp(comment_data["timestamp"] / 1000)
            comment = {
                "date": date,
                "content_md": comment_data["message"]
            } | _author(comment_data['sender'])
            answer["comments"].append(comment)
    return question

_INLINE_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_CALLOUT_URL = re.compile(r"^https:\/\/alkem\.io\/tip\/co(?:(?:llaboration"
                          + r"\/(?P<q1>[^/]+)(?:\/posts\/(?P<a1>[^/]+))?)"
                          + r"|(?:ntribute\/callouts\/(?P<q2>[^/]+)))$")
def links(markdown):
    '''returns a dict of connected nodes (q,a) to edge labels'''
    links = {}
    for label, url in _INLINE_LINK.findall(markdown):
        match = _CALLOUT_URL.match(url)
        if match:
            dict = match.groupdict()
            question = dict['q1'] or dict['q2']
            answer = dict['a1']
            if answer:
                link = (question, answer)
            else:
                link = (question,)
            if link in links:
                links[link].append(label)
            else:
                links[link] = {label}
    return links

def _index(question):
    index = {
        (question['id'],): {
            'question': question['title'],
            'outgoing': links(question['description_md'])
        }
    }
    for answer in question['answers']:
        index[(question['id'], answer['id'])] = {
            'question': question['title'],
            'answer': answer['title'],
            'outgoing': links(answer['description_md'])
        }
    return index

def index_all(questions):
    for question in questions:
        for item in _index(question).items():
            yield item

def _alkemio_link(label, url):
    return f"[🏔️ {label}]({url})"

def _linked_author(item):
    return _alkemio_link(item["author_name"], item["author_url"])

def _readable_date(contribution):
    return contribution["date"].strftime("%Y-%m-%d %H:%M UTC")

def _indent(markdown):
    return "".join([f"  {line}\n" for line in markdown.splitlines()])

def _quote(markdown):
    return "".join([f"> {line}\n" for line in markdown.splitlines()])

def _replace_links(markdown, index):
    def replacement(match):
        label, url = match.groups()
        match = _CALLOUT_URL.match(url)
        if match:
            dict = match.groupdict()
            question = dict['q1'] or dict['q2']
            question_title = index[(question,)]['question']
            answer = dict['a1']
            if answer:
                answer_title = index[(question, answer)]['answer']
                return f"[📌 {answer_title}]({question}.md#{answer})"
            else:
                return f"[📄 {question_title}]({question}.md)"
        else:
            return f"[🌐 {label}]({url})"
    return _INLINE_LINK.sub(replacement, markdown)

def write_github_flavored_md(question, dir_path, index):
    file_path = f"{dir_path}/{question['id']}.md"
    with open(file_path, "w") as file:
        file.write("[🏔️ Alkemio](https://welcome.alkem.io/) › "
                   + "[🏔️ TIP](https://alkem.io/tip/dashboard) › Kennisbank\n")
        file.write(f"# 📄 {question['title']}\n")
        file.write(_replace_links(question["description_md"], index))
        file.write("\n\n")
        if "author_name" in question:
            file.write(f"***\nVraag oorspronkelijk gesteld door "
                       + f"{_linked_author(question)}.")
        file.write(f" [`🏔️ Origineel`]({question['url']})\n\n")
        for answer in question["answers"]:
            file.write(f"- ## <a id=\"{answer['id']}\"></a> "
                       + f"📌 {answer['title']}\n")
            file.write(_indent(_replace_links(answer["description_md"], index)))
            file.write(f"\n  ***\n  Antwoord oorspronkelijk geschreven door "
                       + f"{_linked_author(answer)}.")
            file.write(f"  [`🏔️ Origineel`]({answer['url']})\n\n")
            for comment in answer["comments"]:
                file.write(_indent(_indent(f"- #### 💬 Reactie van "
                                           + f"{_linked_author(comment)} op "
                                           + f"{_readable_date(comment)}"
                                           + f"\n      ")))
                file.write(_indent(_indent(_indent(
                    _replace_links(comment["content_md"], index)))))
        incoming = {}
        for src, props in index.items():
            if (question['id'],) in props['outgoing']:
                incoming[src] = props
        if len(incoming) > 0:
            file.write("- ## 📌 Context waarin dit relevant is\n")
            file.write(_indent("Automatisch verzameld op basis van "
                               + "verwijzingen:"))
            for path, props in incoming.items():
                url = f"{path[0]}.md"
                if len(path) == 2:
                    url += f"#{path[1]}"
                label = props['question']
                if 'answer' in props:
                    label = f"📌 {label} {props['answer']}"
                else:
                    label = f"📄 {label}"
                file.write(f"  - [{label}]({url})\n")
        file.write("<details>")
        file.write("<summary><code>Schrijf een antwoord</code></summary>\n\n")
        file.write("1. [Log in op Alkemio](https://identity.alkem.io/login).\n")
        file.write("2. Als je nog niet lid bent van de TIP-space, [vraag en ")
        file.write("wacht op toegang](https://alkem.io/tip/dashboard).\n")
        file.write(f"3. Ga naar de [vraag in Alkemio]({question['url']}).\n")
        file.write("4. Klik op (+).\n")
        file.write("5. Neem kennis van de placeholder-tekst en verwijder ")
        file.write("deze.\n")
        file.write("6. Verstuur je antwoord.\n\n")
        file.write("Je antwoord verschijnt direct op Alkemio. Na ")
        file.write("synchronisatie verschijnt het ook hier.\n\n")
        file.write("</details>\n\n")
        file.write("* * *\n<small>Bijdragen zijn gelicenseerd onder [🌐 CC BY "
                   + "4.0](https://creativecommons.org/licenses/by/4.0/deed.nl)"
                   + ".</small>")
        file.write("\n")

def _obsidian_file_name(title):
    return f"{title.replace('/', " of ")}"

def _replace_obsidian_links(markdown, index):
    def replacement(match):
        label, url = match.groups()
        match = _CALLOUT_URL.match(url)
        if match:
            dict = match.groupdict()
            question = dict['q1'] or dict['q2']
            question_title = index[(question,)]['question']
            question_uri = _obsidian_file_name(question_title)
            answer = dict['a1']
            if answer:
                answer_title = index[(question, answer)]['answer']
                return f"[[{question_uri}#{answer_title}]]"
            else:
                return f"[[{question_uri}]]"
        else:
            return f"[🌐 {label}]({url})"
    return _INLINE_LINK.sub(replacement, markdown)

def write_obsidian_md(question, dir_path, index):
    file_path = f"{dir_path}/{_obsidian_file_name(question['title'])}.md"
    with open(file_path, "w") as file:
        file.write(_replace_obsidian_links(question["description_md"], index))
        file.write("\n\n")
        if "author_name" in question:
            file.write(f"> [!faq] Vraag oorspronkelijk gesteld door "
                       + f"[{question['author_name']}]"
                       + f"({question['author_url']})\n\n")
        for answer in question["answers"]:
            file.write(f"## {answer['title']}\n\n")
            file.write(_indent(
                _replace_obsidian_links(answer["description_md"], index)))
            file.write(f"\n> [!info] Antwoord oorspronkelijk geschreven door "
                       + f"{_linked_author(answer)}\n\n")
            for comment in answer["comments"]:
                file.write(f"> [!note] Reactie van "
                           + f"{_linked_author(comment)} op "
                           + f"{_readable_date(comment)}"
                           + f"\n")
                file.write(_quote(
                    _replace_obsidian_links(comment["content_md"], index)))
                file.write("\n")
        incoming = {}
        for src, props in index.items():
            if (question['id'],) in props['outgoing']:
                incoming[src] = props
        file.write("\n")
        file.write(f"Licentie: CC BY 4.0. ")
        file.write(f"Origineel: {question['url']}\n")
