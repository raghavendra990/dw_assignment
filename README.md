# dw_assignment

<b>Problem 1 : URL Shortener </b><br>
1. Create a URL shortener library (e.g., bitly). Given a long URL, your program should return a 
shortened URL. Ensure the following: 
a. for a long URL X, your program should always return the shortened URL x 
b. the short URLs your program returns, must not follow any pattern; successive calls to 
your program should return very different short URLs (e.g., GOOD: a1x2l3, zAb3gr, ... BAD: 
a1x213, a1x214, ...)  
c. for two different long URLs X and Y, your program should (ideally) always return two 
different shortened URLs x and y 
d. your program must be able to accept long URLs provided both through console as well 
as from a file of newline separated long URLs 
e. the program should work for input files with up to 100000 URLs without crashing 
f. we should be able to import your code as a module and use it (e.g., import shortener; 
short_url = shortener.shorten(long_url)) 


<b>Problem 2 : Key-Value Data store </b><br>
Design a key-value data store. The key value data store is server which can be  used to store the unique key,value mapping. Multiple machines can access the server to get the "Value" for a particular "Key" 
The key-value data store should have the following properties


1. The following operations are permitted on the data store. ADD(key,Value) Adds the value to the key.   GET(key) returns the value for the key. DELETE(key) deletes the particular key.  


2.  This can also be used for Inter process Communication (IPC). process 1 can send a message to another process through this. 
  for ex : Process 1 : ADD (process_1, {key1,value1})
                              
          	process 2:  GET(process_1) => {key1,value1}


3. It is expected to store around 1L records. 










<b>Problem 3: External Sorting </b><br>
External Sorting techniques are used when the amount of data to be sorted does not fit in main memory. Input will be a directory containing one or more large text files. Each file will have a newline separated element. Your output should be a single file with all elements sorted. 


<b>Problem 4: Web Scraping </b><br>
 Scrape data about products on http://www.shopclues.com/computers/desktops­and­monitors/monitors.html  
Url, title, thumbnail and price are the must fields. You can also include other fields which you think are useful.  
Write extracted data to file in JSON form. 
Take first 10 urls and run product page crawl 
(ex : http://www.shopclues.com/aoc­24­wide­led­e2450swh­monitor.html ​). 
Try to extract as many as data points you can that are relevant to product. 
Also capture availability and estimated delivery time for the pincodes 560070, 575001, 671551.  Again write extracted data to file in JSON form. 
Dont use any headless browsers/selenium/browser objects. To fetch data, you can use requests module.  


<b>Problem 5: Generating IP usage statistics. 	</b><br>
Company "Internet India Pvt Ltd" has 1000 ip addresses. For every request received on the intranet webserver, the company logs the ip address of the originator. 
At the end of the day the server receives around 10M requests. The company generates a report of the number of requests received from each IP address. 
Along with this, it will generate an aggregate count of requests received from an external IP address.


Ex:     IPaddress owned by the company:
IP1
IP2
IP3
.
ip1000


IP address list received by the server
IP1
IP2
IP3
IP1
IP1001
IP1002


Expected output :
IP Address     count
IP1                    2
IP2                    1
IP3                    1
Unknown           2
