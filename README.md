# Stock Market Visualizer
**Prelude:** This was one of the first major Python projects I built, all the way back in 2020. I had posted this project to replit and am now adding it to my github, with the original writeup below (edited slightly for clarity). I really enjoyed coding this project and working with the yfinance library, even though half of my time was spent debugging it 🥲, and I hope you all enjoy using *Stock Market Visualizer*!

Link to original replit post: https://replit.com/talk/share/Stock-Market-Visualizer/42786

---

## Intro

Hi everyone, I'm proud to present Stock Market Visualizer, the best way to view stock/ETF statistics from the comfort of the Python terminal. Search by ticker with live dropdown results and view detailed graphs with information. This was a very cool project to make as it combined my interests in stocks/investing and programming. It was also pretty mathematically challenging to create the graphs.

## How to use
Let's say you want to see statistics for an Apple share. Start by typing apple. Then use the dropdown results to figure out the stock ticker - in this case AAPL. After typing the ticker, a graph will pop up with information below. Here's an explanation to help you better understand the information:
+ Ticker: Unique series of letters assigned to security for trading purposes
+ Name: Name of company or security
+ Sector: Sections of an industry or the overall economy
+ Market Cap: Total value of all shares
+ Regular Market Volume: Total number of security traded over a period of time (usually one day)
+ 200 Day Average: Average share price over 200 days
+ 50 Day Average: Average share price over 50 days
+ P/E Ratio: Price to Earning - Share price to earnings per share
+ Trailing P/E: P/E based off last 12 months
+ Forward P/E: P/E based off of projected 12 months


![Screenshot 2020-06-24 at 1.02.40 PM](https://storage.googleapis.com/replit/images/1593028979938_596436f0ac593ced09d1c900077df5d9.png)