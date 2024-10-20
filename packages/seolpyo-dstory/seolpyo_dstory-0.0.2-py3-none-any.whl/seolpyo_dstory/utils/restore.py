from os import mkdir, listdir
from os.path import exists, isdir
from shutil import rmtree, move
from zipfile import ZipFile

from bs4 import BeautifulSoup
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model

from ..models import Post, Category, Tag


usermodel = get_user_model()
if not (usermodel.objects.filter(is_staff=True)|usermodel.objects.filter(is_superuser=True)).count():
    raise Exception('유저 모델이 생성되지 않았습니다.\n"python manage.py createsuperuser"를 먼저 진행해주세요.')

base_path = getattr(settings, 'BASE_DIR')
path_zipfile = base_path / 'tistory.zip'
path_backup = base_path / 'backup_tistory'

base_media = getattr(settings, 'MEDIA_ROOT')
media_tistory = base_media / 'dstory'

url_media: str = getattr(settings, 'MEDIA_URL')
if url_media.endswith('/'): url_media = url_media[:-1]
if not url_media.startswith('/'): url_media = f'/{url_media}'
url_media = f'{url_media}/dstory'
# print(f'{url_media=}')

def _unzip():
    if not exists(path_zipfile): raise Exception('tistory.zip 파일을 찾을 수 없습니다.')

    if exists(path_backup):
        an = ''
        while an.lower() != 'y':
            an = input('\n===\n\n\n미디어 폴더에 backup_tistory 폴더가 존재합니다.\n복구 진행시 해당 폴더를 제거합니다. 계속하시겠습니까? (Y/N) : ')
            if an.lower() == 'n':
                raise Exception('backup_tistory 폴더 폴더를 제거해주세요.')
        rmtree(path_backup)
    mkdir(path_backup)
    # print('티스토리 백업 파일 디렉토리 생성')

    with ZipFile(path_zipfile) as zipfile:
        zipfile.extractall(path_backup)
        # print('압축 해제 성공')

    return


def _get_path():
    # print(f'{listdir(path_backup)=}')
    backup_name = listdir(path_backup)[0]

    # print(f'{base_media=}')
    if exists(base_media):
        rmtree(base_media)
        # print('미디어 폴더 삭제 완료')
    mkdir(base_media)
    # print('미디어 폴더 생성 완료')
    if not exists(media_tistory): mkdir(media_tistory)

    list_path = []
    for pk in listdir(path_backup / backup_name):
        path_pk = path_backup / backup_name / pk
        if isdir(path_pk): list_path.append((pk, path_pk))

    return list_path


def _convert_filepath(soup: BeautifulSoup, pk):
    for i in soup.select('img'):
        if i['src'].startswith('./'): i['src'] = i['src'].replace('.', f'{url_media}/{pk}', 1)
    for i in soup.select('a[href^="./file"]'):
        if i['href'].startswith('./'): i['href'] = i['href'].replace('.', f'{url_media}/{pk}', 1)
    # print(soup.prettify())
    return

def _convert_datetime(soup: BeautifulSoup):
    djagnotime = timezone.now()
    date_pub = timezone.datetime.strptime(soup.select_one('p.date').text, '%Y-%m-%d %H:%M:%S')
    # print(f'{date_pub=}')
    djagnotime = djagnotime.replace(
        year=date_pub.year, month=date_pub.month, day=date_pub.day,
        hour=date_pub.hour, minute=date_pub.minute, second=date_pub.second,
        microsecond=0
    ) + timezone.timedelta(hours=-9)
    # print(f'{djagnotime=}')
    return djagnotime


def _get_category(soup: BeautifulSoup):
    category = soup.select_one('p.category').text.strip()
    if not category: category = None
    else:
        if '/' not in category:
            category, _ = Category.objects.get_or_create(name=category)
        else:
            category_parent, category = category.split('/', 1)
            category_parent, _ = Category.objects.get_or_create(name=category_parent)
            category, _ = Category.objects.get_or_create(name=category)
            category.parent = category_parent
            category.save()
    return category


def _get_tags(soup: BeautifulSoup):
    tags = []
    for i in soup.select_one('div.tags').text.split('#'):
        name = i.strip()
        if not name: continue
        tag, _ = Tag.objects.get_or_create(name=name)
        tags.append(tag)
    return tags


def restore(author_id=None, do_print=True):
    if not author_id:
        author_id = (usermodel.objects.filter(is_staff=True)|usermodel.objects.filter(is_superuser=True)).first().pk
    if Post.objects.count() or Category.objects.count() or Tag.objects.count():
        an = ''
        while an.lower() != 'y':
            an = input('\n===\n\n\ntistory db를 백업한 것이 확인됩니다.\n복구 진행시 기존 db는 삭제됩니다. 계속하시겠습니까? (Y/N) : ')
            if an.lower() == 'n':
                raise Exception('사용자가 tistory db 복구를 취소하였습니다.')
    if exists(media_tistory):
        an = ''
        while an.lower() != 'y':
            an = input('\n===\n\n\ntistory 미디어 폴더가 존재합니다.\n복구 진행시 tistory 미디어 파일을 제거합니다. 계속하시겠습니까? (Y/N) : ')
            if an.lower() == 'n':
                raise Exception('tistory 미디어 폴더를 제거해주세요.')
        rmtree(media_tistory)

    _unzip()

    Tag.objects.all().delete()
    Category.objects.all().delete()
    Post.objects.all().delete()
    for i in ['공지사항', '페이지', '서식',]: Category.objects.get_or_create(name=i)

    list_path = _get_path()
    # print(f'{djagnotime=}')
    for pk, path_pk in sorted(list_path, key=lambda x: int(x[0])):
        # print()
        # print(f'{pk=}')
        # print(f'{path_pk=}')
        list_filename: list[str] = listdir(path_pk)
        for filename in list_filename:
            if filename in {'img', 'file'} and isdir(path_pk / filename):
                move(path_pk / filename, media_tistory / pk / filename)
            if filename.endswith('.html'):
                with open(path_pk / filename, 'r', encoding='utf-8') as txt:
                    soup = BeautifulSoup(txt.read(), 'html.parser')
                    # print(soup.prettify())
                    _convert_filepath(soup, pk)

                    date_pub = _convert_datetime(soup)
                    category = _get_category(soup)
                    tags = _get_tags(soup)

                    post = Post(
                        pk=pk,
                        author_id=author_id,
                        title=soup.select_one('title').text.strip(),
                        content=str(soup.select_one('div.contents_style')),
                        date_pub=date_pub,
                    )
                    # for i in post.__dict__.items(): print(f'  {i}')

                    if category: post.category = category

                    post.save()

                    post.tags.clear()
                    if tags: post.tags.add(*tags)

    rmtree(path_backup)
    # print('백업 파일 삭제 성공')

    if do_print:
        print(f'{Post.objects.count():,}개의 게시글을 복구했습니다.')
        return 'Ctrl + Z 키를 입력해 django shell을 종료해주세요.'
    return


if __name__ == '__main__':
    restore()

