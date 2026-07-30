class TestCartPage:

    def test_cart(self, cart_page):
        cart_page.open()
        cart_page.check_place_order_button()

    def test_add_phone_to_cart(self, base_page, cart_page):
        product_name = "Samsung galaxy s6"

        base_page.open()
        base_page.switching_to_phones()
        base_page.open_product(product_name)
        cart_page.add_current_product_to_cart()
        cart_page.switching_to_cart()
        cart_page.check_product_in_cart(product_name)

    def test_cart_total_and_delete_product(self, base_page, cart_page):
        first_product = "Samsung galaxy s6"
        second_product = "Nokia lumia 1520"

        base_page.open()
        base_page.switching_to_phones()
        base_page.open_product(first_product)
        cart_page.add_current_product_to_cart()

        base_page.open()
        base_page.switching_to_phones()
        base_page.open_product(second_product)
        cart_page.add_current_product_to_cart()

        cart_page.switching_to_cart()
        cart_page.check_products_in_cart([first_product, second_product])
        cart_page.check_total(1180)
        cart_page.remove_product(first_product)
        cart_page.check_products_in_cart([second_product])
        cart_page.check_total(820)
