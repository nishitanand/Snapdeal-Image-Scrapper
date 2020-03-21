<h1>Snapdeal Image Scrapper</h1>
This Program is an Image Scrapper & Downloader which is used to download photos of any product from the online e-commerce website **snapdeal.com**.

First user inputs name of the product and then it uses BeautifulSoup library and requests and does web scrapping on the website from the URL of the website.
It finds the top 20 results of the product and then downloads the images. It uses mimetypes library to get the file extension and writes the files using file handling. It uses lazy loading method to stream the data in chunks instead of loading it all at the same time, so that the system may not run out of memory. It also uses the tqdm library for showing a live progress bar for the download.

To use it, first write this command in the command line

pip install -r requirements.txt

or (for Mac)

pip3 install -r requirements.txt

and then to run the file write

python Snapdeal-Web-Scrapper.py

or (for Mac)

python3 Snapdeal-Web-Scrapper.py


The downloaded images will be saved in the folder named "SnapdealPics"