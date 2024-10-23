from urllib.parse import parse_qs, urlparse

from earthscale.auth import is_google_drive_url


def running_in_notebook() -> bool:
    try:
        from IPython import get_ipython  # type: ignore

        if get_ipython() is None:  # type: ignore
            return False
        return True
    except ImportError:
        return False


def create_valid_url(url: str) -> str:
    if is_google_drive_url(url):
        parsed = urlparse(url)
        query = parsed.query
        query_parameters = parse_qs(query)
        query_parameters["supportsAllDrives"] = ["true"]
        query_parameters["alt"] = ["media"]
        query = "&".join(f"{key}={value[0]}" for key, value in query_parameters.items())
        url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{query}"
    return url
