SUMMARY

I used the Loan Data From Prosper to create my visualization. I was interested to see whether there’s a pattern between the “loan status” of an individual and the “income range”. I used pandas to do some “group by” on the original large dataset and rearrange the data of interest. Finally, I created a split-bar chart using the “loan status” and the “income range” to see if they display any pattern.

DESIGN

The original dataset from Prosper was not included in this folder, it was trimmed using the code trimming_prosper_loan_csv.py which produced trimmed_prosper_loan.csv. The trimmed dataset included all the 113k rows but fewer columns.
Stack_IncomeRange.py and Stack_LoanStatus.py generated IncomeStack.csv and LoanStatusStack.csv, respectively.
IncomeStack.csv was the data used for index1.html (first chart reviewed). LoanStatusStack.csv was the data used for index2.html, index3.html, index4.html and index.html (final chart).

index1.html: I used the “income range” as the layers to be stacked according to the “loan status” on the x-axis. I used Pandas to trim the dataset and to group by “income range” and “loan status”. Then, I calculated the percentage of each “income range” in each “loan status”. After data wrangling of the original dataset, “IncomeStack.csv” was the final dataset I imported with d3.csv to be used in index1.html.
Then, I used d3.layout.stack() to prepare my data for stacking.

index2.html: as per the first feedback suggestion, I switched around the variables and used “loan status” as the layers to be stacked according to the “income range” on the x-axis. To add some animation, I added a tooltip to the top left corner of the bar chart. Since there was less “LoanStatus” variables than “IncomeRange” in the final dataset, stacking the “LoanStatus” layers would be more informative and less confusing and it allowed us to see if there were more defaulted loans in certain income categories.
For this chart, I had to rearrange the data with pandas to prepare it to be stacked with the “loan status” as the layer. The final dataset imported with d3.csv was “LoanStatusStack.csv” which was also used in index3.html, index4.html and index.html (final code).

index3.html: as per the second feedback suggestion, I added a “div” element for the “svg” since it will allow to style the svg with CSS. I chose a light grey background since it will not obscure the chart details and it’s color-blind friendly. I also added a small paragraph at the top of the page to give a synopsis of the data and its source.

index4.html: this was the html code submitted with the project files for review; as per the third feedback suggestion, I used d3.event.pageY and d3.event.pageX to make the tooltip move with the mouse. That created a better animation and allowed the tooltip to move with the mouse. Having the tooltip move with the mouse offers a better viewing experience for the viewer. I also added a bottom paragraph that briefly describes the patterns seen on the bar chart.

index.html: after the project review, I switched the colors to color blind-friendly since the previous colors were not. I chose a reddish color for “Chargedoff” loans and a blue and green color for “completed” and “current” loans, respectively.

FEEDBACK

First feedback to index1.html suggested using “loan status” as layers with “income range” on the x-axis, since it will be more informative. Also, adding tooltips was suggested.
Link to first feedback: https://discussions.udacity.com/t/please-feedback-needed/199553/2

Second feedback to index2.html suggested to use a “div” as the parent element of the “svg” instead of using “body” as the parent element. This would allow for better styling with css. It also recommended explaining the data and its source for people not familiar with it.
Link to second feedback: https://discussions.udacity.com/t/question-about-d3-layout-stack/196564/20

Third feedback to index3.html suggested adding more information to explain the patterns seen to the viewers. It also suggested making the tooltip displayed in a position relative to the mouse movement instead of having it fixed to one corner of the page.
Link to third feedback: https://discussions.udacity.com/t/my-project-visualization/202113/2

RESOURCES

1.https://github.com/curran/screencasts/tree/gh-pages/splittingCharts
https://www.youtube.com/watch?v=6Xynj_pBybc&t=3419s

I used the above resources to create the bar chart, learn the d3.layout.stack and import the d3 legend library.

2.http://stackoverflow.com/questions/10805184/show-data-on-mouseover-of-circle

I learned from this resource how to use d3.event.pageY and pageX to move the tooltip with the mouse.

3.https://www.youtube.com/watch?v=n5NcCoa9dDU&list=PL6il2r9i3BqH9PmbOf5wA5E1wOG3FT22p

I watched youtube videos to learn about d3.

4.http://colorbrewer2.org was helpful link to chose the right colors.

5.Udacity forum coaches, mentors and questions in the forum with the answers were of big help.

6.Myles Callahan answered a lot of my questions and was of great help!
