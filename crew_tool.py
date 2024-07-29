from crewai_tools import SeleniumScrapingTool

# Example 1: Initialize the tool without any parameters to scrape the current page it navigates to
tool = SeleniumScrapingTool()

# Example 2: Scrape the entire webpage of a given URL
tool = SeleniumScrapingTool(website_url='https://example.com')

# Example 3: Target and scrape a specific CSS element from a webpage
tool = SeleniumScrapingTool(website_url='https://example.com', css_element='.main-content')

# Example 4: Perform scraping with additional parameters for a customized experience
tool = SeleniumScrapingTool(website_url='https://example.com', css_element='.main-content', cookie={'name': 'user', 'value': 'John Doe'}, wait_time=10)