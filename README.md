# 20-Languages
TIOBE provides a monthly index of the most popular programming languages. Write a program that shall collect and save information about the most common keywords (tags) associated with the top 20 most popular languages using questions on stackoverflow.com.

Start by collecting the list of the 20 most popular languages on TIOBE in January 2018 and identifying the major StackOverflow seed tags that correspond to them (you can do this by hand). Choose  only one most general tag for each language (for example, choose python for Python, not python-2.7 or python-3.x).

Your program shall:

Download the main page for each seed tag (e.g., https://stackoverflow.com/questions/tagged/erlang for Erlang) using module urllib. 
Extract the total number of tagged questions (e.g., 7,842 for Erlang).
Extract all questions on the page and their tags using module BeautifulSoup.
Repeat items 1 and 3 for the first 1,000 questions by extracting and following the links at the bottom of each page. Assume that each seed tag has at least 1,000 questions. Leave the downloaded pages in the cache folder as %language%-%n%.html, where %language% is the name of the seed tag and %n% is the page number as a 3-digit, zero-padded-on-the-left integer number (the number of the first page is 001). If the folder does not exist (at the first run), it shall be created.
Find 10 most frequently used sister tags, aside from the seed tag itself. Assume that each seed tag has at least ten associated sister tags.
Write the data into a CSV file named tags.csv using module csv. Each row in the file shall represent one language. The first column shall have the seed tags. The second column shall have the count of tagged questions as an integer number without decimal commas. The next 10 columns shall contain the most frequently used sister tags, one tag per columns, as strings, arranged from the most frequently used tag to the least frequently used tag. The first row of the file shall have column titles: "Language", "Count", "Tag1", "Tag2", ..., "Tag10" (less the quotes). The rows must be ordered by the "Count" column in the decreasing numerical order.
Write a brief, at most one-page long, report that answers the following questions:

Of which of the top 20 languages have you heard before looking at the TIOBE site? Which of them can you read? Which of them can you write? (Please answer as a team.)
Is the order of the languages in your CSV file the same as on the TIOBE index? If not, explain the difference.
Do any languages share any most popular tags? What is the most popular shared tag, if any? Explain what you found. 
The program shall have no GUI and shall not require any command line parameters. Deliverables:

The program
The CSV file
The report as a Google Doc or MS Word/OpenOffice document
