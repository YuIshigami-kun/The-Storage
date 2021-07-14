import re
import urllib.request

class ValidateText:
    def __init__(self, url, targets):
        shorters = ['bit.ly', 'rb.gy', 'tinyurl.com', 'rotf.lol', 'tiny.one', 'cutt.ly', 'exe.io', 'shorturl.at', 'shorturl.gg', 'urlshorter.org', 'onx.la', 't.co', 'ow.ly', 'gestyy.com', 'bit.do']
        #Udemy Courses With A Discount
        if(bool(url.find('https://www.udemy.com/course/') != -1 and url.find('couponCode=') != -1) and targets['udemy-discount-courses']):
            self.result = 'Discount_Udemy'
            return
        #Udemy Courses Without A Discount
        if(url.find('https://www.udemy.com/course/') != -1 and targets['udemy-courses']):
            self.result = 'Free_Udemy'
            return
        #Proxy Servers
        #DON´T CHANGE ORDER!
        if(targets['proxies']):
            if(re.search('(?:(\w+)(?::(\w+))?@)?((?:\d{1,3})(?:\.\d{1,3}){3})(?::(\d{1,5}))?', url) != None):
                self.result = 'Proxy'
                return
        #Credit Cards
        if(targets['credit-cards']):
            card = ''
            for i in url:
                if(i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9' and i != ' ' and i != '\n'):
                    if(i == '|'):
                        card += ' '
                else:
                    card += i
            first = re.search('(?:4[0-9]{12})(?:[0-9]{3})?', card)
            second =  re.search('(?:(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12})', card)
            third = re.search('(?:(?:5[0678]\\d\\d|6304|6390|67\\d\\d)\\d{8,15})', card)
            fourth = re.search('(?:(?:2131|1800|35\\d{3})\\d{11})', card)
            fifth = re.search('(?:6(?:011|5[0-9]{2})(?:[0-9]{12}))', card)
            sixth = re.search('(?:3(?:0[0-5]|[68][0-9])[0-9]{11})', card)
            seventh = re.search('(?:3[47][0-9]{13})', card)

            group = [first, second, third, fourth, fifth, sixth, seventh]
            for i in group:
                if(i != None):
                    self.result = 'Card'
                    self.card = card[i.start() : i.end()]
                    return
        #Mega Links
        if(bool(url.find('https://mega.nz/folder/') != -1 or url.find('https://mega.nz/file/') != -1) and targets['mega-links']):
            self.result = 'Mega'
            return
        #Google Drive Links
        if(bool(url.find('https://drive.google.com/drive/folders/') != -1 or url.find('https://drive.google.com/drive/file/') != -1) and targets['google-drive-links']):
            self.result = 'Drive'
            return
        #Mediafire Links
        if(bool(url.find('https://www.mediafire.com/folder/') != -1 or url.find('https://www.mediafire.com/file/') != -1) and targets['mediafire-links']):
            self.result = 'Mediafire'
            return
        #All Anonfiles Sites Links
        if(url.find('https://anonfiles.') != -1 and targets['anonfiles-links']):
            self.result = 'Anonfiles'
            return
        #All Pastebin Sites Links
        if(url.find('https://pastebin.') != -1 and targets['pastebin-links']):
            self.result = 'Pastebin'
            return
        #Url Shorters
        if(targets['url-shorters']):
            for i in shorters:
                if(url.find(i) != -1 and url.find('http') != -1 and url.find('://') != -1):
                    self.result = 'Shorter'
                    return
        #Custom Text
        if(url.find(targets['custom-text']['match']) != -1 and targets['custom-text']['enabled']):
            self.result = 'Custom_Text'
            return
        #Bins
        if(targets['bins']):
            matches = re.findall('(0|[1-9][0-9]*)', url.strip('x'))
            if(len(matches) <= 0):
                pass
            else:
                for i in matches:
                    if(len(i) == 6):
                        try:
                            conn = urllib.request.urlopen('https://lookup.binlist.net/' + i)
                            if(conn.getcode() != 400):
                                self.result = 'Bin'
                                return
                        except(Exception):
                            print(Exception)

        self.result = False




class ValidateFiles: 
    def __init__(self, extension, targets):
        code_files = ['.css', '.py', '.pyc', '.cpp', '.c', '.php', '.bat', '.sh', '.cs', '.class', '.tar', '.java', '.ts', '.js', '.html', '.go', '.ruby']
        #Open Bullet Configs
        if(bool(extension == '.loli' or extension == '.anom') and targets['open-bullet-configs']):
            self.result = 'Config'
            return
        #Code Files
        if(extension in code_files and targets['code-files']):
            self.result = 'Code_File'
            return
        #Custom Extension
        if(extension == targets['custom-extension']):
            self.result = 'Custom_Extension'
            return
        #PDF
        if(extension == '.pdf' and targets['pdf']):
            self.result = 'PDF'
            return
        #All Files
        if(targets['files']):
            self.result = 'File'
            return
        self.result = False