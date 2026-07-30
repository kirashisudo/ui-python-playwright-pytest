class TestBasePage:

    def test_monitors(self,base_page):
        base_page.open()
        base_page.switching_to_monitors()
        base_page.check_cards(2)

    def test_cart(self,base_page):
        base_page.open()
        base_page.switching_to_cart()

    def test_phones(self,base_page):
        base_page.open()
        base_page.switching_to_phones()
        base_page.check_cards(7)
