"""
@author: Irina
@summary: Test checking response for URLs SEO pages
"""
import requests
import pytest
from unittestzero import Assert

clients = ["clients/client-projects/bloonn-srl", "clients/client-projects/smartbear",
           "clients/client-projects/instiller", "clients/client-projects/avast",
           "clients/client-projects/vmware", "clients/client-projects/mozilla",
           "clients/client-projects/inuvo-bargainmatch",
           "clients/client-projects/apica-ab", "clients/client-projects/monterosa", "clients/client-projects/songbird",
           "clients/client-projects/research-through-gaming", "clients/client-projects/bloonn-srl",
           "clients/client-projects/zugo-services-ltd"]
technologies = ["technologies/overview", "technologies/javascript", "technologies/javascript/jquery",
                "technologies/javascript/coffeescript",
                "technologies/web-technologies", "technologies/web-technologies/html5",
                "technologies/web-technologies/css3", "technologies/web-technologies/lesssass",
                "technologies/frameworks",
                "technologies/frameworks/bootstrap", "technologies/frameworks/nodejs",
                "technologies/frameworks/angularjs",
                "technologies/frameworks/backbone", "technologies/languages", "technologies/languages/c",
                "technologies/languages/python",
                "technologies/languages/xul", "technologies/databases", "technologies/databases/mongodb",
                "technologies/databases/couchdb", "technologies/databases/sqlite"]
solutions = ["solutions/mobile-apps/phonegap-apps", "solutions/overview", "solutions/web-apps",
             "solutions/web-apps/responsive-design",
             "solutions/web-apps/single-page-apps", "solutions/mobile-apps"]


class TestSeoPages():

    def get_response(self, url):
        r = requests.get(url)
        return r.status_code

    @pytest.mark.parametrize('client',
                             clients
    )
    def test_client(self, client):
        site_url = pytest.config.getoption('url')
        if site_url.endswith("/"):
            url = "%s%s?_escaped_fragment_" % (site_url, client)
        else:
            url = "%s/%s?_escaped_fragment_" % (site_url, client)
        Assert.equal(self.get_response(url), 200, "Code for %s is incorrect" % url)

    @pytest.mark.parametrize('technology',
                             technologies
    )
    def test_technology(self, technology):
        site_url = pytest.config.getoption('url')
        if site_url.endswith("/"):
            url = "%s%s?_escaped_fragment_" % (site_url, technology)
        else:
            url = "%s/%s?_escaped_fragment_" % (site_url, technology)
        Assert.equal(self.get_response(url), 200, "Code for %s is incorrect" % url)

    @pytest.mark.parametrize('solution',
                             solutions
    )
    def test_solution(self, solution):
        site_url = pytest.config.getoption('url')
        if site_url.endswith("/"):
            url = "%s%s?_escaped_fragment_" % (site_url, solution)
        else:
            url = "%s/%s?_escaped_fragment_" % (site_url, solution)
        Assert.equal(self.get_response(url), 200, "Code for %s is incorrect" % url)