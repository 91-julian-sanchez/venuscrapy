# Venuscrapy: Python Project for Chaturbate Scraper and Data Analysis
Venuscrapy is a Python project that aims to gather data from the adult live video streaming platform, Chaturbate, using web scraping and data analysis techniques. With this project, you can gather data from various models, rooms, and categories on Chaturbate and analyze them to gain valuable insights.

## Installation

Before getting started, make sure you have the following installed:

* Python 3.x
* pip

You can install the required Python libraries using the following command in the terminal:

```bash 
pip install -r requirements.txt
```

## How to Use

1. Download or clone this repository onto your local computer.

2. Open the terminal and navigate to the directory where the `schedule.py` file is located.

3. Run the following command in the terminal to start the program:
```python 
python schedule.py --tag <tag_name>
```

Replace `<tag_name>` with the category of Chaturbate that you want to scrape. For example:

```python 
python schedule.py --tag latina
```

4. The program will gather data about the selected category and store it in a CSV file inside a folder named `output` in the current directory. Inside the `output` folder, there will be a sub-folder called `extract`, where the scraped CSV files will be stored.

5. After the data has been extracted, the program will process it and create a new CSV file inside a sub-folder called `transform` in the `output` folder. This CSV file will contain the following data columns: `model`, `age`, `gender`, `link`, `time`, `viewers`, `tags`, `pages`, `impression`, and `date`.

6. To combine all the CSV files in the output/transform folder into a single CSV file, run the following command in the terminal:

```python 
python load.py --tag <tag_name>
```

7. ```bash 
cd analyze && python main.py --tag <tag_name>
```

This will create a new CSV file named <tag_name>.csv in a sub-folder called load inside the output folder.

## Contributing

If you would like to contribute to this project, feel free to open a pull request with your changes. Additionally, make sure to follow Python coding best practices and add proper documentation for your code.

## License
This project is under the MIT License.