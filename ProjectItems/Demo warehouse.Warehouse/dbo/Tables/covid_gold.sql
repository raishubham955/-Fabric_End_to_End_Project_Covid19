CREATE TABLE [dbo].[covid_gold] (

	[country] varchar(8000) NULL, 
	[cases] bigint NULL, 
	[deaths] bigint NULL, 
	[recovered] bigint NULL, 
	[tests] bigint NULL, 
	[population] bigint NULL, 
	[death_rate_pct] float NULL, 
	[test_per_thousand] float NULL, 
	[cases_per_million] bigint NULL
);