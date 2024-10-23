import datetime
import requests
import json
from jsonpath import jsonpath
import time
import random
import hmac
from hashlib import sha1
import random


def create_activity(data):
    env = data["env"]
    headers = data["headers"]
    body = data["body"]
    sales_id = data["sales_id"]
    url = "%s/api/posts/activity/%s"%(env,sales_id)
    platform = "FACEBOOK"
    if "platform" in data:
        platform = data["platform"].upper()
    response = requests.post(url,headers=headers,json=body)
    print(response.json())
    if response.status_code==200:
        activity_id = response.json()["data"]
        return activity_id
    else:
        return response

def delate_activity(data):
    env = data["env"]
    headers = data["headers"]
    activity_id = data["activity_id"]
    url = "%s/api/activity/%s" % (env, activity_id)
    response = requests.delete(url,headers=headers).json()
    return response

def start_activity(data):
    env = data["env"]
    headers = data["headers"]
    activity_id = data["activity_id"]
    url = "%s/api/activity/%s/start" % (env, activity_id)
    response = requests.post(url,headers=headers).json()
    return response

def end_activity(data):
    env = data["env"]
    headers = data["headers"]
    activity_id = data["activity_id"]
    url = "%s/api/activity/%s/end" % (env, activity_id)
    response = requests.post(url, headers=headers).json()
    return response

def send__live_comment(data):
    env = data["env"]
    key = data["key"]
    platform = "FACEBOOK"
    page_id = ""
    post_id = ""
    group_id = ""
    if "page_id" in data:
        page_id = data['page_id']
    if "platform" in data:
        platform = data['platform']
    if "post_id" in data:
        post_id = data['post_id']
    if "group_id" in data:
        post_id = data['group_id']
    if page_id == "" or post_id == "":
        info = get_live_info(data)
        platform_list = jsonpath(info, "$..relatedPostList..platform")
        i = platform_list.index(platform)
        page_id = info["data"]["relatedPostList"][i]["page_id"]
        platform = info["data"]["relatedPostList"][i]["platform"]
        post_id = info["data"]["relatedPostList"][i]["post_id"]
        group_id = info["data"]["relatedPostList"][i]["group_id"]
    # info = get_live_info(data)
    # related_post_list = info["data"]["relatedPostList"][0]
    # page_id = related_post_list["page_id"]
    # post_id = related_post_list["post_id"]
    # platform = related_post_list["platform"]
    stamp = int(time.time())
    num = random.randint(100000, 999999)
    user_id = "488864%d" % int(time.time())
    if "user_id" in data:
        user_id = data['user_id']
    name = "test live%d" % int(time.time())
    if "name" in data:
        name = data['name']
    comment_id = "%s_%d%d" % (page_id, stamp, num)
    if "comment_id" in data:
        comment_id = data['comment_id']
    keyword = "接口测试普通留言"
    if "keyword" in data:
        keyword = data['keyword']
    body = {"object": "page", "entry": [{"id": page_id, "time": stamp, "changes": [{"field": "feed", "value": {
            "from": {"id": user_id, "name": name},
            "post": {"status_type": "added_video", "is_published": True, "updated_time": "2022-11-18T09:57:26+0000",
                     "permalink_url": "https://www.facebook.com/permalink.php?story_fbid=pfbid02jLK3e6YdFSXp2DmD7j7vtStLXoBzTi8rxKrp6jFhVMUTTEgz6qvZA8soR9Uwydd8l&id=107977035056574",
                     "promotion_status": "inactive", "id": post_id}, "message": keyword, "item": "comment",
            "verb": "add", "post_id": post_id, "comment_id": comment_id,
            "created_time": stamp, "parent_id": post_id}}]}]}

    if platform.upper() == "INSTAGRAM":
        body = {"entry": [{"id": page_id, "time": stamp, "changes": [{"value": {"from": {"id": user_id,
                 "username": name},
                  "media": {"id": post_id,
                   "media_product_type": "FEED"},
                "id": comment_id, "text": keyword},
                   "field": "comments"}]}], "object": "instagram"}
    elif platform.upper() == "FB_GROUP":
        t_time = stamp*1000
        post_id = post_id.split("_")[-1]
        comment_id = "%d%d" % ( stamp, num)
        body = {"object":"page","entry":[{"id":page_id,"time":t_time,"messaging":[{"recipient":{"id":page_id},"message":keyword,
        "from":{"id":user_id,"name":name},"group_id":group_id,"post_id":post_id,"comment_id":comment_id,"created_time":stamp,"item":"comment",
         "verb":"add","parent_id":post_id,"field":"group_feed"}]}]}
    print(body)
    url = "%s/facebook/webhook" % env
    sign_text = hmac.new(key.encode("utf-8"), json.dumps(body).encode("utf-8"), sha1)
    signData = sign_text.hexdigest()
    # print("body", json.dumps(body))
    header = {"Content-Type": "application/json", "x-hub-signature": "sha1=%s" % signData}
    response = requests.post(url, headers=header, data=json.dumps(body))
    print(response.text)
    return user_id, name, comment_id

def send_mc_message(data):
    env = data["env"]
    key = data["key"]
    stamp = int(time.time()*1000)
    user_id = "488864%d" % int(time.time())
    if "user_id" in data:
        user_id = data['user_id']
    name = "test live%d" % int(time.time())
    if "name" in data:
        name = data['name']
    message = "接口测试普通留言"
    if "message" in data:
        message = data['message']
    page_id = ""
    if "page_id" in data:
        page_id = data['page_id']
    platform = "FACEBOOK"
    if "platform" in data:
        platform = data['platform']
    if page_id=="":
        info = get_live_info(data)
        platform_list = jsonpath(info, "$..relatedPostList..platform")
        i = platform_list.index(platform)
        page_id = info["data"]["relatedPostList"][i]["page_id"]
        platform = info["data"]["relatedPostList"][i]["platform"]
    mid = "m_hhAqPhSlMTY4En2oWjSB59T3BFjeU97DdDV4WHr3DLWnPrO0iCsjQlG3hBN%d-sBlT26-6oNg" % stamp
    body = {"entry": [{"id": "%s" % page_id, "messaging": [{"message":
      {
       "mid": mid,
        "text": "%s" % message},
         "recipient": {"id": "%s" % page_id},
         "sender": {"id": "%s" % user_id}, "timestamp": stamp}],
         "time": stamp}], "object": "page"}
    # if platform.upper()=="FACEBOOK":
    #     body = {"entry":[{"id":"%s"%page_id,"messaging":[{"message":
    #     {"mid":"m_hhAqPhSlMTY4En2oWjSB59T3BFjeU97DdDV4WHr3DLWnPrO0iCsjQlG3hBN%d-sBlT26-6oNg"%stamp,"text":"%s"%message},
    #     "recipient":{"id":"%s"%page_id},"sender":{"id":"%s"%user_id},"timestamp":stamp}],"time":stamp}],"object":"page"}
    if platform.upper()=="INSTAGRAM":
        body={"object":"instagram","entry":[{"time":stamp,"id":"%s"%page_id,"messaging":[{"sender":{"id":"%s"%user_id},"recipient":{"id":"%s"%page_id},
       "timestamp":stamp,"message":{"mid":"aWdfZAG1faXRlbToxOklHTWVzc2FnZAUlEOjE3ODQxNDUwMzgwODgwNTMzOjM0MDI4MjM2Njg0MTcxMDMwMTI0NDI3NjAyNDExMzcwMDc2NTA5MDozMTgzODU0Mzg3NTY4MDYwMTE3ODUxOTE2MD%d"%stamp,"text":"%s"%message}}]}]}
    url = "%s/facebook/webhook" % env
    sign_text = hmac.new(key.encode("utf-8"), json.dumps(body).encode("utf-8"), sha1)
    signData = sign_text.hexdigest()
    header = {"Content-Type": "application/json", "x-hub-signature": "sha1=%s" % signData}
    response = requests.post(url, headers=header, data=json.dumps(body))
    return user_id, name



def get_live_info(data):
    env = data["env"]
    headers = data["headers"]
    sales_id = data["sales_id"]
    url = "%s/api/posts/live/sales/%s" % (env, sales_id)
    response = requests.get(url,headers=headers).json()
    return response

def get_activity_detail(data):
    """
    type:
    luckyDraw,抽奖活动
    voucher--留言抢优惠
    answerFirst--抢答
    bidding--竞标
    vote:投票
    :param data:
    :return:
    """
    env = data["env"]
    headers = data["headers"]
    activity_id = data["activity_id"]
    type = data["type"]
    url = ""
    if type in "luckyDraw":
        url = "%s/api/activity/luckyDraw/%s"% (env, activity_id)
    elif type in "voucher":
        url = "%s/api/activity/voucher/%s" % (env, activity_id)
    elif type in "answerFirst":
        url = "%s/api/activity/answerFirst/%s" % (env, activity_id)
    elif type in "bidding":
        url = "%s/api/activity/bidding/%s" % (env, activity_id)
    elif type in "vote":
        url = "%s/api/activity/vote/%s" % (env, activity_id)
    response = requests.get(url,headers=headers).json()
    return response

def live_search_oa_gift(data):
    """
    查询oa赠品，命名转为驼峰和返回第一个赠品的信息
    :param data:
    :return:
    """
    env = data["env"]
    headers = data["headers"]
    url = "%s/openApi/proxy/v1/gifts"%env
    params = {"page":1}
    response = requests.get(url,headers=headers,params=params).json()
    items = response["data"]["items"]

    if items == []:
        # 新增赠品
        body = {"unlimited_quantity": True, "title_translations": {"zh-cn": "接口自动化新增的赠品%s" % int(time.time())},
                "media_ids": "610d2865ca92cf00264c563c"}
        requests.post(url, headers=headers, json=body).json()
        time.sleep(5)
        #新增后去查询
        response = requests.get(url, headers=headers, params=params).json()
        items = response["data"]["items"]

    # 返回数量不是0的赠品和spu_id
    # print(json.dumps(items))
    quantityList = jsonpath(items,"$..quantity")
    gift_info = items[0]
    for a,b in enumerate(quantityList):
        if b!=0:
            gift_info = items[a]
    spu_id = gift_info["id"]
    return spu_id,gift_info,response

def live_search_oa_product(data):
    """
    查询OA的商品，并返回响应,返回第一个有库存的商品
    spu:返回无规格
    sku:返回多规格
    quantity:0 返回无库存商品
    :param data:
    :return:
    """
    env = data["env"]
    headers = data["headers"]
    url = "%s/openApi/proxy/v1/products?page=1&per_page=20" %env
    type = "spu"
    quantity = 100
    if "type" in data:
        type = data["type"]
    if "quantity" in data:
        quantity = data["quantity"]
    if "query" in data:
        query = data["query"]
        url = "%s/openApi/proxy/v1/products?page=1&per_page=4&query=%s" % (env,query)
    response = requests.get(url, headers=headers).json()
    items = response["data"]["items"]
    variant_options_list = jsonpath(items,"$..variations")
    product_info = ""
    spu_id = ""
    sku_id = ""
    sku_id_quantity =[]
    for a, b in enumerate(variant_options_list):
        if type=="spu" and b==[] and quantity!=0:
            quantitys=items[a]["total_orderable_quantity"]
            unlimited_quantity = items[a]["unlimited_quantity"]
            if quantitys!=0 or unlimited_quantity==True:
                product_info=items[a]
                spu_id = items[a]["id"]
                break
        elif type=="sku" and b!=[] and quantity!=0:
            quantitys = items[a]["total_orderable_quantity"]
            unlimited_quantity = items[a]["unlimited_quantity"]
            if quantitys!=0 or unlimited_quantity==True:
                product_info = items[a]
                spu_id = items[a]["id"]
                sku_id = jsonpath(items[a]["variations"],"$..id")
                sku_id_quantity = jsonpath(items[a]["variations"],"$..total_orderable_quantity")
                break
        elif type == "spu" and b == [] and quantity == 0:
            quantitys = items[a]["total_orderable_quantity"]
            unlimited_quantity = items[a]["unlimited_quantity"]
            if quantitys != 0 or unlimited_quantity == True:
                product_info = items[a]
                spu_id = items[a]["id"]
                break
        elif type == "sku" and b != [] and quantity == 0:
            quantitys = items[a]["total_orderable_quantity"]
            unlimited_quantity = items[a]["unlimited_quantity"]
            if quantitys != 0 or unlimited_quantity == True:
                product_info = items[a]
                spu_id = items[a]["id"]
                sku_id = jsonpath(items[a]["variations"], "$..id")
                sku_id_quantity = jsonpath(items[a]["variations"], "$..total_orderable_quantity")
                break
    return spu_id,sku_id,sku_id_quantity,product_info



def get_merchant_info(data):
    env = data["env"]
    headers = data["headers"]
    merchant_id = data["merchant_id"]
    url = "%s/openApi/proxy/v1/merchants/%s" % (env,merchant_id)
    response = requests.get(url, headers=headers).json()
    base_country_code = response["data"]["base_country_code"]
    currency = ""
    if base_country_code=="TW":
        currency="NT$"
    elif base_country_code=="TH":
        currency = "฿"
    elif base_country_code == "VN":
        #放金额后面
        currency = "₫"
    return base_country_code,currency,response

def delete_broadcast(data):
    env = data["env"]
    headers = data["headers"]
    broadcast_id = data["broadcast_id"]
    url = "%s/admin/api/bff-web/live/broadcast/%s"%(env,broadcast_id)
    response = requests.delete(url,headers=headers).json()
    return response

def get_broadcast_list(data):
    env = data["env"]
    headers = data["headers"]
    sales_id = data["sales_id"]
    name = ""
    platform= data["platform"]
    broadcast_id = ""
    pageNum = 1
    pageSize = 12
    if "pageNum" in data:
        pageNum = data["pageNum"]
    if "pageSize" in data:
        pageSize = data["pageSize"]
    if "name" in data:
        name= data["name"]
    url = "%s/admin/api/bff-web/live/broadcast/query"%env
    body = {
    "businessId": "%s"%sales_id,
    "businessType": "LIVE",
    "businessSubType": "LIVE_STREAM",
    "platform": "%s"%platform,
    "pageNum": pageNum,
    "pageSize": pageSize
    }
    reponse = requests.post(url,headers=headers,json=body).json()
    if name !="":
        name_list = jsonpath(reponse,"$..name")
        broadcast_id_list = jsonpath(reponse,"$..id")
        for i,value in enumerate(name_list):
            if value==name:
                broadcast_id =broadcast_id_list[i]
    return broadcast_id,reponse

def get_broadcast_detail(data):
    env = data["env"]
    headers = data["headers"]
    broadcast_id = data["broadcast_id"]
    platform = data["platform"]
    url = "%s/admin/api/bff-web/live/broadcast/detail"%env
    body = {
    "id": "%s"%broadcast_id,
    "platform": "%s"%platform
        }
    response = requests.post(url,headers=headers,json=body).json()
    return response






if __name__=="__main__":
   pass