The goal of this project is to look at World Wide food security by country and compare it to the total value of agricultrual production to that country.
Data was pulled from the Food and Agriculture Organization of the United Nations. https://www.fao.org/faostat/en/#data

The biggest issue with these three data sets was the missing values present in each one of them. Each of the original data sets is around 92,000 rows by 15 columns.  
My final data set is 4210 rows by 5 columns.  This is a drastic decrease, but my goal with this project was to first combine all three data sets, and second use a 
Logistic Regression to fill in the missing data.  

This project was completed in a virtual environment.  You can find the exact version of each module used in the requirements.txt file.

I have included the CSV that I produced when I ran the progam, this is where the data for the Tableau dashboard comes from.

**To run the program, run world_food.py

--Code Louisville Project Features--
1. Loading Data-Read TWO data files (JSON, CSV, Excel, etc.)
    - For this project I loaded 3 seperate CSV files
2.Clean and operate on the data while combing them
    -For this project I singled out the usefull columns in each data frame, before combinig them.  
    Once combined I then used a Logistic Regression to fill in the missing data
3. Visualize/Present your data
    -For this project I made a Tableau dashboard to display my data.  It can be found at:https://public.tableau.com/app/profile/kyle.hamsley
4.Best Practices
    - I ultilized a virual environment for this project. 

Future Goals
There are a lot of things I would change about this project to improve it.  Below I will list a few of the biggest ones I will continue to work on.

1. I had to parse a lot of the data down to get a usable data set.  I would really like to look at more options to keep a larger part of the data to ensure better results.
2. As I mentioned for this project I used a Logistic Regrerssion.  Even after decreasing that data set there were still a lot of missing data points.  I want to look at
   different options in regareds to machine learning and filling in this missing data.
3. This was my first time making a Tableau dashboard.  While I was able to get a few representations of the data results, the limited data set was a hinderance in regards to 
   producing great dashboards.  Never the less, I would like to improve my dashboard building skills, and will ensure to continue to learn in that area. 