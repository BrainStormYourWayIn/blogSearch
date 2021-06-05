#from bs4 import BeautifulSoup
#from bs4.element import Comment
import urllib.request

#if __name__ == '__main__':
    #url = 'https://www.gatesnotes.com/About-Bill-Gates/Holiday-Books-2020'
    #arr = ExtractText(url)
    #arr = [i.split('\\r')[0] for i in arr] 
    
from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyA5p_aEGY96GuUq-tfebM0SyBgqeF1HeWQ"
my_cse_id = "7552ddd9fa05e4120"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

page = 1
nextPage = (page - 1) * 10 + 1

searchinput = input("Enter your search term: ")
searchterm = searchinput + " blog"


results = google_search(
    searchterm, my_api_key, my_cse_id, num = 10, start = nextPage)


with open('myOutFile.html', 'w') as f:
    f.write('')
    f.write("<html>\n")
    f.write("<title>blogSearch | Search Results</title>\n")
    f.write("<link rel='shortcut icon' href='b.ico'>\n")
    f.write("<link rel = 'stylesheet' href = 'style.css'>\n")
    f.write("<link href='https://fonts.googleapis.com/css2?family=Prompt:wght@300&display=swap' rel='stylesheet'>\n")
    f.write("<link href='https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap' rel='stylesheet'>\n")
    f.write("<link href='https://fonts.googleapis.com/css2?family=Righteous&display=swap' rel='stylesheet'>\n")
    f.write("<link href='https://fonts.googleapis.com/css2?family=Cuprum&display=swap' rel='stylesheet'>\n")
    f.write('<link href="https://fonts.googleapis.com/css2?family=PT+Serif&display=swap" rel="stylesheet">\n')
    f.write("<img src='blogSearch-logo.png' alt='blogSearch logo' align='middle'>\n")
    f.write("<br>\n")
    f.write("<pageno>You're on Page " + str(page) + " of 10</pageno>\n")
    f.write("<br>\n")
    f.write("<br>\n")
    f.write("<searchresult>Your search results for '" + searchinput + "' are:</searchresult>\n")
    f.write("<br>\n")
    f.write("<br>\n")

for result in results:
    omitSocials = ['instagram', 'twitter', 'facebook', 'amazon', 'linkedin', 'youtube', 'vimeo', 'google', 'pinterest']
    blog_str = ['blog']
    #omitSocials = ['https://www.instagra', 'https://twitt', 'https://www.faceboo', 'https://www.pinterest', 
                   #'https://business.faceboo', 'https://www.amazon', 'https://m.faceboo', 'https://vimeo', 
                   #'https://www.youtu', 'https://play.google', 'https://support.goog']
    urls = str(result.get('link'))
    #snippo = result.get('snippet')
    keyStr = "blog"
    for_link = "URL: "
    for_title = "Title: "
    for_des = "Description: "
    #url = result.get('link')
    #For getting only socials: if any(social in urls for social in omitSocials):
    #if all(social not in urls for social in omitSocials):   
    
    #if all(social not in urls for social in omitSocials) or keyStr in urls
    if all(social not in urls for social in omitSocials):
        with open("myOutFile.html", "a+") as f:
            
            #f.write("<html>\n")
            #f.write("<title>blogSearch | Search Results</title>\n")
            f.write("<p><result>========== Result ==========</result>\n")
            f.write("<br>\n")
            f.write("<maintitle>" + result.get('title') + "</maintitle><br>" + '\n')
            f.write("<br>\n")
            f.write("<a href='" + urls + "'>" + urls + "</a><br>" + '\n')
            f.write("<br>\n")
            f.write("<description>" + for_des + result.get('snippet') + "</description>")
            f.write("</p>\n")
        #with open("myOutFile.html", "w") as outF:
            #outF.write(for_title + result.get('title'))
    else:
        pass

with open('myOutFile.html', 'a') as f:
    f.write("</body>\n")
    f.write("</html>\n")

    #print(result.get('snippet'))
    #pprint.pprint(result)
    #print(arr)
    #print(ExtractFirstPara(arr))
    #print(url)
    #print(ReturnCount(arr, 'your'))
    
def check_if_digit(input_str):
    #input_str = input("Type 's' to search again or 'p' to go to a different page or 'e' to end the session: ")
    if input_str == 'p':
        input_str = input("Enter a page no from 1-10 you wanna go to: ")
        global searchterm
        global page
        global nextPage
        page = int(input_str)
        nextPage = (page - 1) * 10 + 1
        results = google_search(
        searchterm, my_api_key, my_cse_id, num = 10, start = nextPage)
        with open('myOutFile.html', 'w') as f:
            f.write('')
            f.write("<html>\n")
            f.write("<title>blogSearch | Search Results</title>\n")
            f.write("<link rel='shortcut icon' href='b.ico'>\n")
            f.write("<link rel = 'stylesheet' href = 'style.css'>\n")
            f.write("<link href='https://fonts.googleapis.com/css2?family=Prompt:wght@300&display=swap' rel='stylesheet'>\n")
            f.write("<link href='https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap' rel='stylesheet'>\n")
            f.write("<link href='https://fonts.googleapis.com/css2?family=Righteous&display=swap' rel='stylesheet'>\n")
            f.write("<link href='https://fonts.googleapis.com/css2?family=Cuprum&display=swap' rel='stylesheet'>\n")
            f.write('<link href="https://fonts.googleapis.com/css2?family=PT+Serif&display=swap" rel="stylesheet">\n')
            f.write("<img src='blogSearch-logo.png' alt='blogSearch logo' align='middle'>\n")
            f.write("<br>\n")
            f.write("<pageno>You're on Page " + str(page) + " of 10</pageno>\n")
            f.write("<br>\n")
            f.write("<br>\n")
            f.write("<searchresult>Your search results for '" + searchinput + "' are:</searchresult>\n")
            f.write("<br>\n")
            f.write("<br>\n")

        for result in results:
            omitSocials = ['instagram', 'twitter', 'facebook', 'amazon', 'linkedin', 'youtube', 'vimeo', 'google', 'pinterest']
            blog_str = ['blog']
    #omitSocials = ['https://www.instagra', 'https://twitt', 'https://www.faceboo', 'https://www.pinterest', 
                   #'https://business.faceboo', 'https://www.amazon', 'https://m.faceboo', 'https://vimeo', 
                   #'https://www.youtu', 'https://play.google', 'https://support.goog']
            urls = str(result.get('link'))
    #snippo = result.get('snippet')
            keyStr = "blog"
            for_link = "URL: "
            for_title = "Title: "
            for_des = "Description: "
    #url = result.get('link')
    #For getting only socials: if any(social in urls for social in omitSocials):
    #if all(social not in urls for social in omitSocials):   
    
    #if all(social not in urls for social in omitSocials) or keyStr in urls
            if all(social not in urls for social in omitSocials):
                with open("myOutFile.html", "a+") as f:
            
            #f.write("<html>\n")
            #f.write("<title>blogSearch | Search Results</title>\n")
                    f.write("<p><result>========== Result ==========</result>\n")
                    f.write("<br>\n")
                    f.write("<maintitle>" + result.get('title') + "</maintitle><br>" + '\n')
                    f.write("<br>\n")
                    f.write("<a href='" + urls + "'>" + urls + "</a><br>" + '\n')
                    f.write("<br>\n")
                    f.write("<description>" + for_des + result.get('snippet') + "</description>" + '\n\n')
                    f.write("</p>\n")
        #with open("myOutFile.html", "w") as outF:
            #outF.write(for_title + result.get('title'))
            else:
                pass

        with open('myOutFile.html', 'a') as f:
            f.write("</body>\n")
            f.write("</html>\n")
    elif input_str == 's':
            input_str = input("Enter a search term: ")
            searchterm = input_str + " blog"
            results = google_search(
            searchterm, my_api_key, my_cse_id, num = 10, start = nextPage)
            with open('myOutFile.html', 'w') as f:
                f.write('')
                f.write("<html>\n")
                f.write("<title>blogSearch | Search Results</title>\n")
                f.write("<link rel='shortcut icon' href='b.ico'>\n")
                f.write("<link rel = 'stylesheet' href = 'style.css'>\n")
                f.write("<link href='https://fonts.googleapis.com/css2?family=Prompt:wght@300&display=swap' rel='stylesheet'>\n")
                f.write("<link href='https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap' rel='stylesheet'>\n")
                f.write("<link href='https://fonts.googleapis.com/css2?family=Righteous&display=swap' rel='stylesheet'>\n")
                f.write("<link href='https://fonts.googleapis.com/css2?family=Cuprum&display=swap' rel='stylesheet'>\n")
                f.write('<link href="https://fonts.googleapis.com/css2?family=PT+Serif&display=swap" rel="stylesheet">\n')
                f.write("<img src='blogSearch-logo.png' alt='blogSearch logo' align='middle'>\n")
                f.write("<br>\n")
                f.write("<pageno>You're on Page " + str(page) + " of 10</pageno>\n")
                f.write("<br>\n")
                f.write("<br>\n")
                f.write("<searchresult>Your search results for '" + input_str + "' are:</searchresult>\n")
                f.write("<br>\n")
                f.write("<br>\n")

            for result in results:
                omitSocials = ['instagram', 'twitter', 'facebook', 'amazon', 'linkedin', 'youtube', 'vimeo', 'google', 'pinterest']
                blog_str = ['blog']
    #omitSocials = ['https://www.instagra', 'https://twitt', 'https://www.faceboo', 'https://www.pinterest', 
                   #'https://business.faceboo', 'https://www.amazon', 'https://m.faceboo', 'https://vimeo', 
                   #'https://www.youtu', 'https://play.google', 'https://support.goog']
                urls = str(result.get('link'))
    #snippo = result.get('snippet')
                keyStr = "blog"
                for_link = "URL: "
                for_title = "Title: "
                for_des = "Description: "
    #url = result.get('link')
    #For getting only socials: if any(social in urls for social in omitSocials):
    #if all(social not in urls for social in omitSocials):   
    
    #if all(social not in urls for social in omitSocials) or keyStr in urls
                if all(social not in urls for social in omitSocials):
                    with open("myOutFile.html", "a+") as f:
            
            #f.write("<html>\n")
            #f.write("<title>blogSearch | Search Results</title>\n")
                        f.write("<p><result>========== Result ==========</result>\n")
                        f.write("<br>\n")
                        f.write("<maintitle>" + result.get('title') + "</maintitle><br>" + '\n')
                        f.write("<br>\n")
                        f.write("<a href='" + urls + "'>" + urls + "</a><br>" + '\n')
                        f.write("<br>\n")
                        f.write("<description>" + for_des + result.get('snippet') + "</description>" + '\n\n')
                        f.write("</p>\n")
        #with open("myOutFile.html", "w") as outF:
            #outF.write(for_title + result.get('title'))
            else:
                   pass

            with open('myOutFile.html', 'a') as f:
                f.write("</body>\n")
                f.write("</html>\n")
                
    else:
        print("Thank you for using our service!")
            
                
input_str = input("Type 's' to search again or 'p' to go to a different page or 'e' to end the session: ")
check_if_digit(input_str)


    
