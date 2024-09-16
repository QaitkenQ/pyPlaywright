from playwright.sync_api import Page, expect

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.link_about = page.locator('#a:has-text("About")')
        self.link = page.locator("//div[@class='menu']/a")

    def navigate(self):
        self.page.goto('https://couchdb.apache.org/')

    def ver_links(self):
        total = self.link.count()
        expect(self.link).to_have_count(6)
        expect(self.link.nth(0)).to_contain_text("About")
        expect(self.link.nth(1)).to_contain_text("Docs")
        expect(self.link.nth(2)).to_contain_text("Contribute")
        expect(self.link.nth(3)).to_contain_text("News")
        expect(self.link.nth(4)).to_contain_text("Download")
        expect(self.link.nth(5)).to_contain_text("More")


