This is a cab request app where students are able to request cabs, view available cabs, dispatch and match cabs with students based on seniority and how early they requested it.

To run it keep cabs.csv in the same folder as main.py and run "python3 main.py"

-If the cab is half empty it can still be dispatched
-If there are no cabs left then the user still joins the queue and gets a message saying no cabs are left
-If 2 students are in the same year the one who submitted it earlier is placed earlier in the queue
-Since I've used heaps it's quite fast at adding many requests for example:
1. Adding 1 request O(logn) - For heaps the time complexity is O(logn)
2. Adding 1000 requests O(nlogn) - This is just the first time complexity multipled by no. of requests
3. Dispatching 1 cab O(logn) - Removing and adding to the heap has same time complexity
4. Finding an open cab O(n) - It only depends on no. of cabs which it goes through 1 by 1