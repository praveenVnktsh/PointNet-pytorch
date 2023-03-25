import gdown

# a file
url = "https://drive.google.com/u/0/uc?id=1wXOgwM_rrEYJfelzuuCkRfMmR0J7vLq_&export=download"
output = "dataset.zip"
gdown.download(url, output, quiet=False)