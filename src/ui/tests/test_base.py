class TestBasePage:

    def test_monitors(self,base_page):
        base_page.open()
        base_page.switching_to_monitors()
        base_page.check_cards(2)

    def test_phones(self,base_page):
        base_page.open()
        base_page.switching_to_phones()
        base_page.check_cards(7)

    def test_product_details(self, base_page):
        base_page.open()
        base_page.switching_to_phones()
        base_page.open_product("Samsung galaxy s6")
        base_page.check_product_details("Samsung galaxy s6", "$360")
