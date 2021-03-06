import json
import requests
import os
import facebook
class Facebook:
        @staticmethod
        def get_access_token():
                res={}
                access_token = os.getcwd()+'/website/sj/access_tokens.sh'
                f = open(access_token, 'r+')
                lines = f.readlines()
                for line in lines:
                        tokens = line.strip().split(':')
                        if tokens[0] == 'FACEBOOK_PAGE_ID':
                                res['FACEBOOK_PAGE_ID']=tokens[1].strip()
                        elif tokens[0] == 'FACEBOOK_PAGE_ACCESS_TOKEN':
                                res['FACEBOOK_PAGE_ACCESS_TOKEN']=tokens[1].strip()
                return res
        def __init__(self):
                token=self.get_access_token()
                self.page_id=token['FACEBOOK_PAGE_ID']
                self.page_access_token=token['FACEBOOK_PAGE_ACCESS_TOKEN']

        def publish_photo_msg(self,msg, image_url):
                graph = facebook.GraphAPI(self.page_access_token)
                photo = open(image_url, "rb")
                graph.put_photo(image=photo,message=msg,album_path=self.page_id+"/photos")
                photo.close()
                '''url="https://graph.facebook.com/v5.0/"+self.page_id +"/photos"
                params={"access_token":self.page_access_token,
                "url":image_url,
                "caption":message,
                }
                requests.post(url,params)
                return'''

