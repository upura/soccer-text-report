from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

URL = 'https://www.jleague.jp/match/j1/2018/080103/livetxt/'

def get_data():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options, executable_path='/Applications/chromedriver')
    driver.get(URL)

    # テキスト速報
    text_list = driver.find_elements_by_class_name('spotRightTxt')
    texts = [text.text for text in text_list]

    # 時刻
    time_list = driver.find_elements_by_class_name('spotLeftTxt')
    times = [time.text for time in time_list]

    # チーム
    team_list = driver.find_elements_by_class_name('spotCenterTeam')
    teams = [team.text for team in team_list]

    driver.close()
    driver.quit()

    print(texts[0])
    print(times[0])
    print(teams[0])
    print(len(texts))
    print(len(times))
    print(len(teams))

    return texts, times, teams

if __name__ == '__main__':
    texts, times, teams = get_data()