#### <ins>NOVA Code & Coffee Notes [Sat. 3/25/23 @ 9:00 AM EST]</ins>:

**Model-View-ViewModel**:
* Model < ViewModel < View

**Go Programming Language**:
* Java threads are one-to-one with the OS thread
* The most important feature of Go is: Goroutines
	* Goroutines are logical; one OS thread can have multiple Goroutines
	* It's not a one-to-one relationship with the OS thread
	* The three most important features of Go: **Goroutines**, **Channels**, **Context**
	* Goroutines are great for concurrent programming; I think **Channels** allows threads to talk to each other
	* The Go **Scheduler** is very powerful; the Scheduler controls the threads, which are light-weight
	* Garbage collection is also faster than say in Java
