from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import sys

def get_data():
    options = Options()
    options.add_argument('--headless')
    url = sys.argv[1]
    driver = webdriver.Chrome(chrome_options=options, executable_path='/Applications/chromedriver')
    driver.get(url)

    # テキスト速報
    text_list = driver.find_elements_by_class_name('spotRightTxt')
    texts = [text.text for text in text_list]
    texts = texts[::-1]

    # ゴール判定
    goal_list = driver.find_elements_by_class_name('spotRightTxt')
    goals = [1 if '<img class=' in goal.get_attribute("innerHTML") else 0 for goal in goal_list]
    goals = goals[::-1]

    # 時刻
    time_list = driver.find_elements_by_class_name('spotLeftTxt')
    times = [time.text for time in time_list]
    times = times[::-1]

    # チーム
    team_list = driver.find_elements_by_class_name('spotCenterTeam')
    teams = [team.text for team in team_list]
    teams = teams[::-1]

    driver.close()
    driver.quit()

    return texts, goals, times, teams

def create_report(texts, goals, times, teams):
    report = ''
    text_length = len(texts)

    # 試合結果（見出し）
    report += '[' + texts[text_length - 1][5:] + ']\n'

    # 得点シーン
    for i in range(text_length):
        if goals[i] == 1:
            if 'キッカー' in texts[i]:
                report += teams[i - 1] + 'は' + times[i - 1] + '、' + texts[i - 1] + '。'
                report += texts[i] + '。'
            else:
                report += teams[i] + 'は' + times[i] + '、' + texts[i] + '。'

    # 試合結果
    report += texts[text_length - 1][5:] + '。'

    return report

if __name__ == '__main__':
    texts, goals, times, teams = get_data()
    report = create_report(texts, goals, times, teams)
    print(report)