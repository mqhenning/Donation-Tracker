from lxml import html
import requests
import threading


#Campaign URL goes here
def timeloop(url):
    threading.Timer(60.0, timeloop).start()
    page = requests.get(url)
    if page.status_code == 200:
        tree = html.fromstring(page.content)
        #This will find the goal amount
        goal = tree.xpath('//span[@class="amount-raised-value"]/text()')
        goal = [item.replace("\n", "") for item in goal]
    else:
        print("Page responded with "+repr(page.status_code))
    #This prints the currently raised amount out of the total goal
    with open("donation.txt", "w") as text_file:
        print("".join(map(str, goal)), '/$10,000', sep="", file=text_file)



if __name__ == "__main__":
    url = 'http://www.ppaction.org/site/TR?px=9693618&fr_id=1160&pg=personal'
    timeloop(url)
