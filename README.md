# TOOL1_FINAL_PROJECT

## Data Science Tools 1 Final Project - Jeff Kirkpatrick

### Problem Statement: 

I need to scrape the 2023 sunrise and set times for Las Cruces, NM from a website to create a sunrise set table in a weather database.Also, I would like to see the amount of sunlight available for each day of the month along with an average for the month. This will help me determine how effective my solar panels will be throughout the year.

### Data Attributes: 

The attributes of the data will be in the form month, day, sunrise time, sunset time. The data will be output as a csv file that can be converted into a mySQL table in a database. The timeline to finish data collection will be 1-2 weeks to write the code to scrape the data and an additional week to test the code and output to ensure the final csv is suitable for the project.

### Example of Data: 

The data will be scraped from a website (https://www.sunrisesunsettime.org/north-america/united-states/las-cruces-january.htm) written in html. The data needed resides within the html pages nested inside of html tags. The python code will need to filter out all html and just grab the required data. Also, the data for the entire year of 2023 is needed. Therefore, a method of pagination within the python code is required to gather all of the required data.

Here is an example of the html code from the webpages :

<!--START INCLUDED CONTENT-->
<div id="main">

	<h1>Las Cruces First Light, Sunrise &amp; Sunset Times for January 2023</h1>
	
	<table class="striped-table" width="100%">
		<thead>
			<tr>
				<td></td>
				<th>Sunrise</th>
				<th>Sunset</th>
				<th>Dawn</th>
				<th class="hide-for-small">Dusk</th>
				<th class="hide-for-small">Solar noon</th>
				<th>Day length</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<th>Sat, 31 Dec</th>
				<td>07:09 <span class="azimuth ESE" title="ESE">(117&deg;)</span></td>
				<td>17:13 <span class="azimuth WSW" title="WSW">(243&deg;)</span></td>
				<td>06:42</td>
				<td class="hide-for-small">17:40</td>
				<td class="hide-for-small">12:11</td>
				<td>10:57:52</td>
			</tr>
			<tr>
				<th>Sun, 1 Jan</th>
				<td>07:09 <span class="azimuth ESE" title="ESE">(117&deg;)</span></td>
				<td>17:13 <span class="azimuth WSW" title="WSW">(243&deg;)</span></td>
				<td>06:42</td>
				<td class="hide-for-small">17:40</td>
				<td class="hide-for-small">12:11</td>
				<td>10:58:18</td>
			</tr>

### Feature Engineering: 

I need to extract the month and day for the year 2023. The month is expressed as the three letter abbreviation. I would want that to be extracted as the month number instead of the three letter expression. Also, I would like a column that indicates the amount of sunlight available each day in minutes. This will be used to create some plots that will help me determine how effective my solar panels will be throughout the year. 
