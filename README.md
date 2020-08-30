
<div align="center">
  <h1>Stackflow </h1> <br />
  <h3>Search Stackoverflow</h3>
</div>


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Live at https://stackflowsearch.herokuapp.com/

This django app is wrapper of [Stackoverflow advanced search api](https://api.stackexchange.com/docs/advanced-search#order=desc&sort=activity&filter=default&site=stackoverflow&run=true)

I build this as an assignment I received for an interview process

### Assignment Statement
Please build an Application over StackOverflowAPI for searching questions in StackOverflow [link](https://api.stackexchange.com/docs/advanced-search)

**Requirements:**

    :heavy_check_mark: Should be able to search all available fields/parameters. 
    :heavy_check_mark: List the result with pagination with Django template.
    :heavy_check_mark: Page/Data should be cached. (Application should only call 
        StackOverflowAPI if we didn't pull data already for same query param)
    :heavy_check_mark: Add Search limit per min(5) and per day(100) for each session.
    :heavy_check_mark: Using Restful API and angular/react bonus

