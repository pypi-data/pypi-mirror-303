import os
import requests

def linear_request(query, variables={}):
    url = 'https://api.linear.app/graphql'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': os.environ['LINEAR_API_KEY']
    }
    body = {
        'query': query,
        'variables': variables
    }
    response = requests.post(url, json=body, headers=headers)
    if response.status_code == 200:
        json_response = response.json()
        if 'errors' in json_response:
            raise Exception(f"GraphQL errors: {json_response['errors']}")
        return json_response['data']
    else:
        raise Exception(f"HTTP error {response.status_code}: {response.text}")

def query_issue(issue_identifier):
    query = """
    query Issue($issueId: String!) {
        issue(id: $issueId) {
            id
            identifier
            title
            description
            assignee {
                id
                name
            }
            priorityLabel
            state {
                name
            }
            url
            branchName
            comments {
                nodes {
                    createdAt
                    updatedAt
                    body
                    user {
                        name
                        email
                    }
                }
            }
        }
    }
    """
    res = linear_request(query, {'issueId': issue_identifier})
    return res['issue']

def create_comment(issue_identifier, body):
    query = """
    mutation CommentCreate($input: CommentCreateInput!) {
        commentCreate(input: $input) {
            success
            comment {
                id
                body
            }
        }
    }
    """
    variables = {
        'input': {
            'issueId': issue_identifier,
            'body': body
        }
    }
    res = linear_request(query, variables)
    return res['commentCreate']['comment']

def create_issue_by_team_id(title, description, assignee_id, team_id, priority, due_date, state_id):
    query = """
    mutation IssueCreate($input: IssueCreateInput!) {
        issueCreate(input: $input) {
            success
            issue {
                id
                identifier
                title
                description
                assignee {
                    id
                    name
                }
                priorityLabel
                state {
                    name
                }
                url
            }
        }
    }
    """
    variables = {
        'input': {
            'teamId': team_id,
            'title': title,
            'description': description,
            'assigneeId': assignee_id,
            'priority': priority,
            'dueDate': due_date,
            'stateId': state_id
        }
    }
    res = linear_request(query, variables)
    return res['issueCreate']['issue']