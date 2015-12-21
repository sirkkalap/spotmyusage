from selenium import webdriver
urlBase = "https://leponline.spsoy.fi/main"
urlReadingReport = "{0}/default.asp?form=ReadingReport&"\
                   "process=ReadingReport&pstart=true".format(urlBase)
urlEnergyreportingDCS = "{0}/default.asp?form=EnergyReportingDCS&"\
                        "process=EnergyReportingDCS&pstart=true".format(urlBase)

urlEnergyFrame = "https://leponline.spsoy.fi/DCS/Pages/EnergyReporting/EnergyReporting/EnergyReporting.aspx"


browser = webdriver.Firefox()
browser.get(urlBase)

uname = browser.find_element_by_name("CustId")
uname.send_keys("sirkkalap")
pwd = browser.find_element_by_name("pwd")
pwd.send_keys("sabu-chy-the")
cmdLogin = browser.find_element_by_name("cmdLogin")
cmdLogin.click()

browser.get(urlEnergyFrame)
