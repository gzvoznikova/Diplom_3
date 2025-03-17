from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    #Номер заказа в ленте заказов
    order_feed_list = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default') and contains(text(), '{}')]")

    # Карточка заказа в истории заказов
    order_card = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')

    # Заголовок карточки заказа с названием бургера
    order_card_title = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')

    # Получение последнего заказа
    last_order_number = (By.XPATH, '//*[contains(@class,"rderHistory_textBox__")]//*[contains(@class,"text_type_digits-default")]')

    # Раздел заказов
    section_orders_list = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')

    # Заголовок ленты заказов
    title_of_orders_feed = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')

    # Карточка заказа в ленте
    order_in_feed = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')

    # Всплывающее окно с деталями заказа
    modal_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                             '(@class, "Modal_orderBox")]')

    # Заголовок всплывающего окна с деталями заказа
    title_of_modal_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                      '"Modal_orderBox")]//h2')

    # Счетчик заказов "Выполнено за все время"
    quantity_of_orders = (By.XPATH, '//*[contains(text(),"Выполнено за все время")]/..//*[contains(@class,"rderFeed_number__")]')

    # Счетчик заказов "Выполнено за сегодня"
    daily_quantity_of_orders = (By.XPATH, '//*[contains(text(),"Выполнено за сегодня")]/..//*[contains(@class,"rderFeed_number__")]')

    # Заказ в разделе "В работе"
    order_in_progress = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')

    # Номер заказа в разделе "В работе"
    number_of_order_in_progress = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li[contains(@class, "text_type_digits-default")]')

    # Все номера заказов в разделе В работе
    orders_in_work = (By.XPATH, '//*[contains(@class,"OrderFeed_orderListReady_")]')

