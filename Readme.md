## URL SHORTENER

This project contains a python package for url shortening. 
A Sample file has been provided named `try.py` to demonstrate how to 
run the package functions.

#### Installation

First run the sql init script `shortener/init.sql` file in mysql to 
create database, and instantiate the tables.
use the following commands

#### Importing Package

use the following line to import package

`import shortener`

#### Shortening a long url

1. Establish a sql connection using the foll. lines
   
    `sess = shortener.get_session(username="root", password="pass", 
    host="0.0.0.0", db_name="shortener")`

2. Call the shorten function to get the tiny url
    
    `shortener.shorten(sess, "https://google.com")`
    
#### Shortening from a file

1. Establish a sql connection using the foll. lines
   
    `sess = shortener.get_session(username="root", password="pass", 
    host="0.0.0.0", db_name="shortener")`

2. Call the shorten function to get a list of all tiny urls
    
    `shortener.shorten_from_file(sess, "file_path")`
    
#### Getting a long url from a tinyUrl

1. Establish a sql connection using the foll. lines
   
    `sess = shortener.get_session(username="root", password="pass",
     host="0.0.0.0", db_name="shortener")`

2. Call the get_original_url funtion to get the long url

    `shortener.get_original_url(sess, "tiny_url")`
    
#### Running test cases

1. Your current directory should be url-shortener
2. Run the following cmds to execute test cases
    
    `python -m  unittest shortener.test`