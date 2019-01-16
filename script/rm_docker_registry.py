import json

import requests

def get_repo_list(docker_registry_proxy):
    r = requests.get(f"http://{docker_registry_proxy}/v2/_catalog")
    r_dict = json.loads(r.text)
    res = r_dict.get("repositories")
    return res

def get_tag_list(docker_registry_proxy, repo):
    r = requests.get(f"http://{docker_registry_proxy}/v2/{repo}/tags/list")
    r_dict = json.loads(r.text)
    #print(r_dict)
    res = r_dict.get("tags")
    return res

def get_digest(docker_registry_proxy, repo, tag):
    #curl -I http://192.168.7.20:5000/v2/appscanner/manifests/2018-12-16223940 -H 'Accept: application/vnd.docker.distribution.manifest.v2+json'
    v2_headers = {"Accept": "application/vnd.docker.distribution.manifest.v2+json"}
    r = requests.get(f"http://{docker_registry_proxy}/v2/{repo}/manifests/{tag}", headers=v2_headers)
    res = r.headers.get("Docker-Content-Digest")
    return res

def delete_digest(docker_registry_proxy, repo, digest):
    r = requests.delete(f"http://{docker_registry_proxy}/v2/{repo}/blobs/{digest}")
    r = requests.delete(f"http://{docker_registry_proxy}/v2/{repo}/manifests/{digest}")
    return

if __name__ == '__main__':
    registry_proxy =  "192.168.7.20:5000"
    repo_list = get_repo_list(registry_proxy)
    print(repo_list)
    tag_list = get_tag_list(registry_proxy, "appscanner")
    print(tag_list)
    digest = get_digest(registry_proxy, "appscanner", "2018-12-17174449")
    print(digest)
    for repo in repo_list:
        tag_list = get_tag_list(registry_proxy, repo)
        for tag in tag_list:
            try:
                year, month, day = tag.split("-")
            except Exception as e:
                print(e)
            if year == "2018":
                print(tag)
                digest = get_digest(registry_proxy, repo, tag)
                print(repo, digest)
                delete_digest(registry_proxy, repo, digest)
