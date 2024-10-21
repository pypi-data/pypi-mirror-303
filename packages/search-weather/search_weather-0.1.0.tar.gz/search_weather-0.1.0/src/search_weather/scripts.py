import subprocess


def download_ko_core_news_sm():
    subprocess.check_call(["python", "-m", "spacy", "download", "ko_core_news_sm"])