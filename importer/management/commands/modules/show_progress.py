"""
Progress Bar Handlers
"""

import progressbar

PBAR = None


def show_download_progress(block_num, read_size, total_size):
    """
    Show progress bar for download.
    """
    global PBAR
    if PBAR is None:
        PBAR = progressbar.ProgressBar(maxval=total_size)
        PBAR.start()

    downloaded = block_num * read_size
    if downloaded < total_size:
        PBAR.update(downloaded)
    else:
        PBAR.finish()
        PBAR = None
