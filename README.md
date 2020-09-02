
<div align="center">
  <h1>Stackflow </h1>
  <img src="screenshots/stackflow_2.png">
</div>

[![Build Status](https://travis-ci.org/andy1729/Stackflow.svg?branch=master)](https://travis-ci.org/andy1729/Stackflow)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Live at https://stackflowsearch.herokuapp.com/

This django app is wrapper of [Stackoverflow advanced search api](https://api.stackexchange.com/docs/advanced-search)

I built this as an assignment I received for an interview process

### Assignment Statement
Please build an Application over StackOverflowAPI for searching questions in StackOverflow [link](https://api.stackexchange.com/docs/advanced-search)

**Requirements:**

- [x] Should be able to search all available fields/parameters. 
- [x] List the result with pagination with Django template.
- [x] Page/Data should be cached. (Application should only call 
        StackOverflowAPI if we didn't pull data already for same query param)
- [x] Add Search limit per min(5) and per day(100) for each session.
- [ ] Using Restful API and angular/react bonus

### More Screenshot

**Empty View**
![empty view](screenshots/stackflow_1.png)

**Pagination**
![Pagination](screenshots/stackflow_3.png)



