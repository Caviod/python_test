from selenium import webdriver
driver = webdriver.Chrome(r'F:\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('http://www.51job.com')

ele = driver.find_element_by_id('kwdselectid')
ele.send_keys('python')

driver.find_element_by_id('work_position_input').click()


#清除别的标签
eles = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000  em[class = on]')
for ele in eles:
    ele.click()

#点杭州
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()
#保存城市选择
driver.find_element_by_id('work_position_click_bottom_save').click()
#点击搜索
driver.find_element_by_css_selector('.ush  button').click()

#保存信息
jobs = driver.find_elements_by_css_selector('#resultList div[class=el]')
for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    stringFilelds = [field.text for field in fields]
    print(' | '.join(stringFilelds))

driver.quit()
