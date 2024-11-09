import progressbar

pbar = None


def show_download_progress(blockNum, readSize, totalSize):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=totalSize)
        pbar.start()

    downloaded = blockNum * readSize
    if downloaded < totalSize:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None
