#from bs4 import BeautifulSoup
#from bs4.element import Comment
import urllib.request
from googleapiclient.discovery import build
import streamlit as st

#import urllib.request
#import pprint

#if __name__ == '__main__':
    #url = 'https://www.gatesnotes.com/About-Bill-Gates/Holiday-Books-2020'
    #arr = ExtractText(url)
    #arr = [i.split('\\r')[0] for i in arr]

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

global Page, NextPage
Page = 1
NextPage = (Page - 1) * 10 + 1

SearchInput = st.text_input(label="Enter your search term: ")
if st.button('Search', key=1):
    SearchTerm = SearchInput + " blog"


    my_api_key = "AIzaSyBJj-nCW0uWpzvckjyA4AnI0N4PjyDuoq4"
    my_cse_id = "ed0ae2d8ce7eda4e8"


    results = google_search(SearchTerm, my_api_key, my_cse_id, num = 10, start = NextPage)

    def tag_visible(element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def text_from_html(body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)

    with open('myOutFile.html', 'w') as f:
        f.write("<html>\n")
        f.write(f"<title>blogSearch | {SearchInput}</title>\n")
        f.write("<link rel='shortcut icon' href='b.ico'>\n")
        f.write("<link rel = 'stylesheet' href = 'style.css'>\n")
        f.write("<link href='https://fonts.googleapis.com/css2?family=Prompt:wght@300&display=swap' rel='stylesheet'>\n")
        f.write("<link href='https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap' rel='stylesheet'>\n")
        f.write("<link href='https://fonts.googleapis.com/css2?family=Righteous&display=swap' rel='stylesheet'>\n")
        f.write("<link href='https://fonts.googleapis.com/css2?family=Cuprum&display=swap' rel='stylesheet'>\n")
        f.write('<link href="https://fonts.googleapis.com/css2?family=PT+Serif&display=swap" rel="stylesheet">\n')
        f.write("<img src='blogSearch-logo.png' alt='blogSearch logo' align='middle'>\n")
        f.write("<br>\n")
        f.write(f"<Pageno>You're on Page {Page} of 10</Pageno>\n")
        f.write("<br>\n")
        f.write("<br>\n")
        f.write(f"<searchresult>Your search results for {SearchInput} are:</searchresult>\n")
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
                f.write(f"<maintitle> {result.get('title')} </maintitle><br>" + '\n')
                f.write("<br>\n")
                f.write(f"<a href='{urls}'> {urls} </a><br>" + '\n')
                f.write("<br>\n")
                f.write(f"<description> Description: {result.get('snippet')} </description>" + '\n\n')
                f.write("</p>\n")

            #with open("myOutFile.html", "w") as outF:
                #outF.write(for_title + result.get('title'))

        else: pass

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
        global SearchTerm, Page, NextPage
        NextPage = (Page - 1) * 10 + 1

        if input_str == 'p':
            input_str = input("Enter a page no from 1-10 you wanna go to: ")
            #global SearchTerm, Page, NextPage
            Page = int(input_str)
            nextPage = (Page - 1) * 10 + 1
            results = google_search(SearchTerm, my_api_key, my_cse_id, num=10, start=nextPage)
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
                f.write("<Pageno>You're on Page " + str(Page) + " of 10</Pageno>\n")
                f.write("<br>\n")
                f.write("<br>\n")
                f.write("<searchresult>Your search results for '" + SearchInput + "' are:</searchresult>\n")
                f.write("<br>\n")
                f.write("<br>\n")

            for result in results:
                omitSocials = ['instagram', 'twitter', 'facebook', 'amazon', 'linkedin', 'youtube', 'vimeo', 'google', 'pinterest']
                #omitSocials = ['https://www.instagra', 'https://twitt', 'https://www.faceboo', 'https://www.pinterest', 
                                #'https://business.faceboo', 'https://www.amazon', 'https://m.faceboo', 'https://vimeo', 
                                #'https://www.youtu', 'https://play.google', 'https://support.goog']
                urls = str(result.get('link'))
                #snippo = result.get('snippet')

                for_des = "Description: "  
        
                if all(social not in urls for social in omitSocials):
                    with open("myOutFile.html", "a+") as f:
                
                        #f.write("<html>\n")
                        #f.write("<title>blogSearch | Search Results</title>\n")
                        f.write("<p><result>========== Result ==========</result>\n")
                        f.write("<br>\n")
                        f.write(f"<maintitle> {result.get('title')} </maintitle><br>" + '\n')
                        f.write("<br>\n")
                        f.write(f"<a href='{urls}'> {urls} </a><br>" + '\n')
                        f.write("<br>\n")
                        f.write(f"<description> Description: {result.get('snippet')} </description>" + '\n\n')
                        f.write("</p>\n")
                    #with open("myOutFile.html", "w") as outF:
                        #outF.write(for_title + result.get('title'))
                else: pass

            with open('myOutFile.html', 'a') as f:
                f.write("</body>\n")
                f.write("</html>\n")

        elif input_str == 's':
                SearchTerm = f"{input_str} blog"
                results = google_search(SearchTerm, my_api_key, my_cse_id, num = 10, start = NextPage)
                with open('myOutFile.html', 'w+') as f:
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
                    f.write("<Pageno>You're on Page {Page} of 10</Pageno>\n")
                    f.write("<br>\n")
                    f.write("<br>\n")
                    f.write("<searchresult>Your search results for {SearchInput} are:</searchresult>\n")
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

                    for_des = "Description: "

                    if all(social not in urls for social in omitSocials):
                        with open("myOutFile.html", "a+") as f:
                
                            #f.write("<html>\n")
                            #f.write("<title>blogSearch | Search Results</title>\n")
                            f.write(r"<p><result>========== Result ==========</result>\n")
                            f.write(r"<br>\n")
                            f.write(f"<maintitle> {result.get('title')} </maintitle><br>" + '\n')
                            f.write(r"<br>\n")
                            f.write(f"<a href='{urls}'> {urls} </a><br>" + '\n')
                            f.write(r"<br>\n")
                            f.write(f"<description> Description: {result.get('snippet')} </description>" + '\n\n')
                            f.write(r"</p>\n")
                else: st.success("Thank you for using our service!")

                with open('myOutFile.html', 'a') as f:
                    f.write("</body>\n")
                    f.write("</html>\n")
        else: pass

    input_str = st.text_input(label="Type 's' to search again or 'p' to go to a different page or 'e' to end the session: ")

    if st.button('Search', key=2):
        check_if_digit(input_str)
