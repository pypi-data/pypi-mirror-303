from getpass import getpass
from random import choice
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm

from .restore import restore
from ..models import Post, Category


def ready_load(driver: webdriver.Chrome):
    while driver.execute_script('return document.readyState') != 'complete': sleep(0.5)


class Tistory:
    host: str
    cookie = {}
    session = requests.Session()
    headers = {'user-agent': 'seolpyo_dstory', 'referer': 'https://www.tistory.com/'}
    dict_url = {
        '글': '/manage/posts.json',
        '공지사항': '/manage/notices.json',
        '페이지': '/manage/pages.json',
        '서식': '/manage/templates.json',
        '카테고리': '/manage/category.json',
    }

    def get_cookie(self):
        print('===\n\n티스토리 상세 복구 기능을 선택하셨습니다.\n티스토리 로그인 정보가 필요하며, 2단계 인증을 사용 중이라면 잠시 해제해주세요.\n이를 원치 않는 경우 Ctrl + C 키를 입력해 코드를 중지하세요.')
        login_id = input('\n\n티스토리 로그인 아이디 : ')
        login_pw = getpass('로그인 비밀번호(키 입력을 받아도 *표시가 나타나지 않을 수 있습니다.) : ')
        print('\n티스토리 블로그 정보를 가져오는 중.. 잠시 기다려주세요.')

        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--log-level=3')
        option.add_argument('user-agent=seolpyo_dstory')
        option.add_argument('--window-size=1100,600')
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=option)
        driver.get('https://www.tistory.com/')

        ready_load(driver)
        driver.find_element(By.CSS_SELECTOR, 'a.btn_login').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.login_tistory > a.btn_login')))

        ready_load(driver)
        driver.find_element(By.CSS_SELECTOR, '.login_tistory > a.btn_login').click()

        while 'kakao.com' not in driver.execute_script('return location.host'): sleep(0.5)
        ready_load(driver)
        driver.find_element(By.CSS_SELECTOR, 'input[name=loginId]').send_keys(login_id)
        driver.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys(login_pw)
        driver.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys(Keys.ENTER)

        for _ in range(10):
            if 'tistory.com' in driver.execute_script('return location.host'): break
            sleep(0.5)
        else:
            driver.quit()
            raise Exception('로그인에 실패했습니다.\n입력한 정보가 올바른지 확인하세요.\n2단계 인증을 사용 중이라면 일시적으로 해제해주세요.')

        ready_load(driver)
        for i in driver.get_cookies(): self.cookie[i['name']] = i['value']

        driver.quit()

        return

    def get_blog(self):
        with self.session.get(
            'https://www.tistory.com/legacy/accio/allBlogs',
            headers=self.headers, cookies=self.cookie
        ) as r: j = r.json()

        list_blog = []
        for i in j['data']:
            list_blog.append(i['defaultUrl'])

        if not list_blog: print('로그인에 실패했습니다. 입력 정보가 올바른지 확인해주세요.')

        if list_blog:
            print('번호  블로그 주소')
            for n, i in enumerate(list_blog, 1): print(f'  {n} : {i}')
            while 1:
                index = input('백업 대상 블로그를 선택해주세요. : ')
                try: self.host = list_blog[int(index) - 1]
                except: pass
                else:
                    if self.host.endswith('/'): self.host = self.host[:-1]
                    break
            print(f'선택된 티스토리 블로그 주소 : "{self.host}"')

    def __init__(self):
        self.get_cookie()
        self.get_blog()

    def request(self, key, params):
        r = self.session.get(f'{self.host}{self.dict_url[key]}', params=params, cookies=self.cookie)
        return r.json()

    def get_post(self, key):
        params = {
            'page': 1,
            'category': -3,
        }
        dict_item = {}
        with tqdm(desc=f'티스토리 {key} 정보 가져오기', total=1) as pbar:
            while 1:
                j = self.request(key, params)

                for i in j['items']:
                    pk = int(i['id'])
                    title = i['title']
                    slug = i['slogan']
                    password = i['postPassword'] if '보호' in i['statusLabel'] else ''
                    category_id = i['categoryId']
                    if category_id == '0': category_id = None
                    if category_id: category_id = int(category_id)
                    is_private = True if '비공개' in i['statusLabel'] else False

                    # print(f'{i=}')
                    dict_item[pk] = {
                        'title': title,
                        'slug': slug,
                        'password': password,
                        'category_id': None,
                        'is_private': is_private,
                        'is_notice': True if key == '공지사항' else False,
                        'is_page': True if key == '페이지' else False,
                        'is_template': True if key == '서식' else False,
                    }
                    if key == '글':
                        dict_item[pk].update({
                            'category_id': category_id
                        })

                pbar.update()

                if len(dict_item) == j['totalCount']: break
                params['page'] += 1
                
                if j['totalCount']:
                    total = j['totalCount'] / j['count']
                    if total % 1: total = int(total) + 1
                    else: total = int(total)
                    pbar.total = total
                sleep(0.5)

        return dict_item
            
    def get_category(self):
        dict_category = {}
        j = self.request('카테고리', {'page': 1})
        for i in j['categories']:
            parent = i['id']
            dict_category[i['id']] = {
                'name': i['name'],
                'parent': None
            }
            for i in i['children']:
                dict_category[i['id']] = {
                    'name': i['name'],
                    'parent': parent
                }
        # for i in dict_category.items(): print(f'  {i}')

        return dict_category

    def run(self):
        dict_item = {}
        for i in [
            '글',
            '공지사항',
            '페이지',
            '서식',
        ]:
            dict_item.update(self.get_post(i))
            # print(f'{len(dict_item)=}')
        dict_category = self.get_category()
        # print(f'{len(dict_category)=}')

        return (dict_item, dict_category)

    def restore(self):
        restore(do_print=False)
        dict_item, dict_category = self.run()

        if len(dict_item) != Post.objects.count():
            raise Exception('티스토리 블로그의 글 수와 백업파일의 글 수가 일치하지 않아 상세 복구 기능을 중단합니다.')

        list_key = list(dict_item.keys())
        for _ in list_key[:3]:
            pk = choice(list_key)
            a = dict_item[pk]['title']
            b = Post.objects.get(pk=pk).title
            if a != b: raise Exception('선택한 블로그와 백업파일 정보가 일치하지 않아 상세 복구 기능을 중단합니다.')

        Category.objects.exclude(name__in=['공지사항', '페이지', '서식']).delete()
        dict_name_category = {}
        # 부모 카테고리 생성
        for i in dict_category.values():
            if i['parent']: continue
            name = i['name']
            category, _ = Category.objects.get_or_create(name=name)
            dict_name_category[name] = category

        # 자식 카테고리 작성
        for i in dict_category.values():
            if not i['parent']: continue
            name = i['name']
            name_parent = dict_category[i['parent']]['name']
            parent = dict_name_category[name_parent]
            category, _ = Category.objects.get_or_create(name=name, parent=parent)
            dict_name_category[name] = category

        # 세부정보 적용
        for i in tqdm(dict_item.items(), desc='글 세부정보 복구'):
            pk, i = i
            post = Post.objects.get(pk=pk)
            if i['is_notice']: post.category = Category.objects.get(name='공지사항')
            if i['is_page']: post.category = Category.objects.get(name='페이지')
            if i['is_template']: post.category = Category.objects.get(name='서식')
            elif i['category_id']: post.category = dict_name_category[dict_category[i['category_id']]['name']]
            post.is_private = i['is_private']
            post.password = i['password']
            post.slug = i['slug']
            post.save()
        

def restore2():
    Tistory().restore()
    print(f'{Post.objects.count():,}개의 게시글을 복구했습니다.')
    return 'Ctrl + Z 키를 입력해 django shell을 종료해주세요.'


if __name__ == '__main__':
    restore2()


