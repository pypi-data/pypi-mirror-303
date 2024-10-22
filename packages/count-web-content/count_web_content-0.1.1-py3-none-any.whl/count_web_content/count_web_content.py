# coding: utf-8
"""webページのコンテンツをカウントするモジュール"""

from time import sleep
from typing import Tuple

import requests
from bs4 import BeautifulSoup


def count_pages(
    root_url: str,
    additional_url: list[str] = None,
    exclude_url: list[str] = None,
    sleep_sec: int = 0.1,
    is_print_working: bool = False,
    output_url_file_name: str = "",
) -> Tuple[int, int, dict[str, int] | None, dict[str, int] | None]:
    """ページのコンテンツをカウントする

    Args:
        root_url (str): 検索したいルートのURL
        additional_url (list[str], optional): 個別にコンテンツ数をカウントしたいURL(root_url配下). Defaults to [].
        exclude_url (list[str], optional): カウント対象外のURL. Defaults to [].
        sleep_sec (int, optional): スクレイピングの時間間隔. Defaults to 0.1.
        is_print_working (bool, optional): 実行中の状態を出力するかどうか. Defaults to False.
        output_url_file_name (str, optional): 検索したルートURL配下のファイル一覧を出力するファイル先. Defaults to "".

    Returns:
        Tuple[int, int, dict[str, int], dict[str, int]]: 前から順に
        hrefのリンク先数, root_url配下のhrefのリンク先数,
        additional_urlで指定したパス配下のhrefのリンク先数, exclude_urlで指定したパス配下のhrefのリンク先数,　が戻る．
        リンク先の数は全て一意のURLでカウントしている.
        戻り値の後ろの2つの辞書は、指定がない場合はNoneが返る.
    """
    not_completed = list()
    not_completed.append(root_url)

    completed_list = list()
    page_count = 0
    in_root_page_count = 0

    additional_url_count_dict = dict()
    if additional_url != None:
        for key in additional_url:
            additional_url_count_dict[key] = 0

    exclude_url_count_dict = dict()
    if exclude_url != None:
        for key in exclude_url:
            exclude_url_count_dict[key] = 0

    while len(not_completed) > 0:
        sleep(sleep_sec)
        current_url = not_completed.pop()

        is_continue = False
        for key in exclude_url:
            if current_url.startswith(key):
                exclude_url_count_dict[key] += 1
                is_continue = True
                continue

        if is_continue:
            continue

        try:
            response = requests.get(current_url, timeout=6.0)
        except requests.exceptions.RequestException as e:
            print(e)
            print("Error: " + current_url)
            continue

        if response.status_code != 200:
            continue

        completed_list.append(current_url)
        page_count += 1
        if is_print_working:
            print("current: " + current_url)

        if not current_url.startswith(root_url):
            continue

        in_root_page_count += 1

        html = BeautifulSoup(response.text, "html.parser")
        a_tags = html.find_all("a", href=True)
        for a_tag in a_tags:
            a_url = a_tag["href"]

            if a_url == "" or a_url == "#":
                continue

            if not a_url.startswith("http") or not a_url.startswith("https"):
                if a_url.startswith("/"):
                    a_url = root_url + a_url[1:]
                else:
                    slash_idx = current_url.rfind("/")
                    a_url = current_url[: slash_idx + 1] + a_url

                # 「..」が含まれているときの処理
                while a_url.find("..") != -1:
                    a_dot_dot_idx = a_url.find("..")
                    a_before_src_from_dot_idx = a_url.rfind("/", 0, a_dot_dot_idx - 1)
                    a_url = (
                        a_url[:a_before_src_from_dot_idx] + a_url[a_dot_dot_idx + 2 :]
                    )

            if a_url.endswith("/"):
                a_url = a_url[:-1]

            if (a_url not in completed_list) and (a_url not in not_completed):
                not_completed.append(a_url)
                for key in additional_url:
                    if a_url.startswith(key):
                        additional_url_count_dict[key] += 1

        if is_print_working:
            print("remain: " + str(len(not_completed)))

    if output_url_file_name != "":
        with open(output_url_file_name, "w", encoding="utf-8") as f:
            for url in completed_list:
                print(url, file=f)

    if len(additional_url_count_dict) == 0:
        additional_url_count_dict = None
    if len(exclude_url_count_dict) == 0:
        exclude_url_count_dict = None

    return (
        page_count,
        in_root_page_count,
        additional_url_count_dict,
        exclude_url_count_dict,
    )
