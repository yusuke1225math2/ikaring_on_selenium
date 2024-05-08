import sys
sys.path.append('./s3s_src')
from s3s_src import s3s
from selenium import webdriver
from time import sleep


if __name__ == '__main__':
    s3s.prefetch_checks(printout=True)

    driver = webdriver.Chrome()
    driver.get("https://api.lp1.av5ja.srv.nintendo.net/?lang=ja-JP")
    sleep(1)
    driver.add_cookie({"name":"_gtoken", "value": s3s.GTOKEN})
    driver.refresh()
    use_input = input("wait for input(quit when some key is pressed)")
    driver.quit()
