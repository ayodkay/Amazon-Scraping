from selenium import webdriver
import pandas as pd


class Amazon:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def set_up(self):
        self.browser.get(url='https://amazon.com')
        self.browser.maximize_window()

    def search_amazon(self):
        dt_list = []
        self.set_up()
        self.browser.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("Iphone")
        self.browser.find_element_by_xpath("//input[@id='twotabsearchtextbox']").submit()
        self.browser.implicitly_wait(5)

        for i in range(1, 17):
            try:
                name = self.browser.find_element_by_xpath(f'//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[{i}]'
                                                          f'/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div['
                                                          f'1]/h2/a/span').text
            except Exception as exception:
                print(exception)
                continue

            try:
                price = self.browser.find_element_by_xpath(
                    f'//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[{i}]/div/span/div/div/div[2]/div['
                    f'2]/div/div[2]/div[1]/div/div/div/span[2]').text
            except Exception as exception:

                price = self.browser.find_element_by_xpath(
                    f'//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[{i}]/div/span/div/div/div[2]/div['
                    f'2]/div/div[2]/div[1]/div/div[1]/div/div/a/span[1]/span[2]/span[2]').text
                print(exception)

            data = {'name': name, "price": price}
            dt_list.append(data)
        return dt_list

    def write_csv(self):
        result = self.search_amazon()

        csv_file = pd.DataFrame(result)

        csv_file.to_csv('csv_files.csv')

        self.exit()

    def exit(self):
        self.browser.close()


if __name__ == '__main__':
    ama = Amazon()
    ama.write_csv()
