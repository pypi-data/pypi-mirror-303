import click
import platform
import re
import webbrowser
from urllib.parse import urljoin
from requests_html import HTMLSession
from typing import List, Union

session = HTMLSession()
match_prefix = "?match="
play_list_regix = r"(?<=src:{hls:\')[\w|\/|\.]+\.m3u8"


def get_matches_list(url: str = 'https://hoofoot.com/?home') -> List[str]:
    """Get matches list.

    Args:
        url (str): website url.

    Returns:
        List[str]: list of matches
    """
    r = session.get(url)
    return sorted([link.removeprefix(match_prefix)
                   for link in r.html.links if link.startswith(match_prefix)])


def get_match_link(match: str,
                   domain: str = 'https://hoofoot.com/') -> Union[None, str]:
    """Get match link.

    Args:
        match (str): match string
        domain (str): domain for the football match highlight video

    Returns:
        Union[None, str]: url to the match, or None if not found.
    """
    r = session.get(urljoin(domain, f"{match_prefix}{match}"))
    for link in r.html.links:
        if "/embed/" in link:
            return link
    return None


def get_video_playlist(url: str) -> str:
    """Get m3u8 play list url.

    Args:
        url (str): match url.

    Returns:
        str: play list url.

    Raises:
        ValueError: if plau list url not found.
    """
    r = session.get(url)
    script_element = None
    for element in r.html.find(containing="m3u8"):
        if element.tag == 'script':
            script_element = element
    if not script_element:
        raise ValueError("No script found")
    play_list = re.findall(play_list_regix,
                           script_element.full_text)[0]
    return f"https:{play_list}"


def get_chrome_path() -> str:
    """Get chrome path depending on the operating system.

    Returns:
        str: chrome path in system

    Raises:
        ValueError: if the operating system is unknown.
    """
    match platform.system():
        case "Darwin":
            # MacOS
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        case "Windows":
            # Windows
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        case "Linux":
            # Linux
            chrome_path = '/usr/bin/google-chrome %s'
        case _:
            raise ValueError("Unknown platform.")
    return chrome_path


@click.command()
@click.option('--with-chrome', is_flag=True)
def play_match_highlights(with_chrome: bool) -> None:
    """Play match highlights.

    Args:
        with_chrome (bool): indicates whether to play the video with chrome directly.

    Returns:
        None

    Raises
        ValueError: if no match link is found.
    """
    match_list = get_matches_list()
    for i, match in enumerate(match_list):
        print(f"{i}: {match}")
    match_idx = input("Enter match index:")
    match = match_list[int(match_idx)]
    match_link = get_match_link(match)
    if not match_link:
        raise ValueError("No match link found")
    play_list_url = get_video_playlist(match_link)

    if with_chrome:
        chrome_path = get_chrome_path()
        chrome = webbrowser.get(chrome_path)
        chrome.open(f"chrome-extension://emnphkkblegpebimobpbekeedfgemhof/player.html#{play_list_url}")
    print(play_list_url)
