# WarcraftLogsPull
Pull data using Warcraft Logs API and turn it into observable trends.  

Started 10/29/18. Ran into raodblock when data was given as JSON.  Assumed that meant I needed to learn Java, so I ran through codecademy only to learn that I could have done this without learning Java.  
11/18/18: Wrote first bits of code that pulled top 100 DPS from US's names and DPS  
11/19/18: Wrote version 1.0.  
11/23/18: Wrote The Full version of WCL which pull all rankings.  However, this is very slow.  
11/23/18: Wrote the xlsx versions of WCL that merge all the data into an xlsx file for analysis.  Orginal versions kept for those who don't want to use excel to analyze the data.

This program currently pulls  the top 100 dps for each boss in Uldir.  It can be changed to pull the top 100 dps for any raid on any difficulty.  These are put into individual CSV files. Future versions will pull complete datasets for bosses and organize them into an xlsx file for analysis.
