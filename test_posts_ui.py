import yaml

from webtestsem4.testpage import OperationsHelper

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    titles = testpage.get_titles()
    assert data["titletocheck"] in titles
