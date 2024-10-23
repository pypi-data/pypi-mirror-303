from IPython.display import Markdown

from ire.ire import METADATA_KEY


def MD(md: str, id: str = None, export: bool = True):
    if export is False:
        metadata = None
    else:
        ire = dict(fmt="md")
        if id:
            ire['id'] = id
        metadata = { METADATA_KEY: ire }

    return Markdown(md, metadata=metadata)
