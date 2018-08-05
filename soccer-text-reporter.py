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

    # ゴール判定
    goal_list = driver.find_elements_by_class_name('spotRightTxt')
    goals = [1 if '<img class=' in goal.get_attribute("innerHTML") else 0 for goal in goal_list]

    # 時刻
    time_list = driver.find_elements_by_class_name('spotLeftTxt')
    times = [time.text for time in time_list]

    # チーム
    team_list = driver.find_elements_by_class_name('spotCenterTeam')
    teams = [team.text for team in team_list]

    driver.close()
    driver.quit()

    # with open("texts.txt", 'wt') as f:
    #     for ele in texts:
    #         f.write(ele+'\n')
    # with open("goals.txt", 'wt') as f:
    #     for ele in goals:
    #         f.write(str(ele)+'\n')
    # with open("times.txt", 'wt') as f:
    #     for ele in times:
    #         f.write(ele+'\n')
    # with open("teams.txt", 'wt') as f:
    #     for ele in teams:
    #         f.write(ele+'\n')

    return texts, goals, times, teams

if __name__ == '__main__':
    texts, goals, times, teams = get_data()