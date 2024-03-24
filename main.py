import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(login):
    response = requests.get(data["website2"], headers={"X-Auth-Token": login}, params={"owner": "notMe"})
    titles = [obj["title"] for obj in response.json()]
    assert response.status_code == 200 and data["titletocheck"] in titles