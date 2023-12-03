# Scrapification

# Scrapification

## This project crawls the given webpage to look for images based on the given search keyword. It filters out a set of 5 images. And then classifies those images into their categories

The project uses Flask with Python. It has two endpoints. The details for both are given below

### The first endpoint is a GET endpoint that takes in a query parameter as a search keyword and returns 5 images with their classifications  -  /search

> We use Selenium to run the scripted page and then read the content from that page using BeautifulSoup

> We then use a pre-trained model using tensorflow to predict what the image is. The model was trained on a limited amount of classes so its prediction might not be great. But it does the task

### The second endpoint is a POST endpoint that takes form data for an uploaded images and returns its analyses  -  /analyze

> We again use the same pre-trained model to return the predictions
