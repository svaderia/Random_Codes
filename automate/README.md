# Automate
This script fills a form on website 100 times with random names.
## Description
* Every form has some certain identifier in it's `HTML`. To get those fields you need to inspect the 
source code of the website. To be able to do that you need to press `CLTR + Shift + I` on chrome.
* In the given code, form details are as follows:
    1. `name` = `formMain`
    2. `field 1` = `fname`
    2. `field 2` = `cname1`
    2. `field 3` = `cname2`
    2. `field 4` = `cname3`
## Requirements
```
mechanize
```
`mechanize` library supports `Python2`.