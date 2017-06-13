# Lecture6

### In this lecture we are going to learn what is Hadoop and how to perform parallel computing using hadoop.

### After this lecture you should be able to:

* understand the structure of HDFS, how files are stored in HDFS and how to exchange files with HDFS;
* understand how MapReduce works and run your own MapReduce program written in python using Hadoop streaming utility;
* write you own PIG script to solve data processing problems in your class project and future research.

**Updated Feb 16 10:00am:**

{

The user names we used before (user1 , user2, ...., user 15) don't have access the the public HDFS space. We created one new account in the test cluster just functioning as the "team" in the main cluster for this lecture. So in this lecture everybody should use username: **class** and password: **hadoop** to login to any of the three machines: **10.29.19.6**, **10.29.19.10** and **10.29.19.11**.
I would recommend: **user 1-7 use 10.29.19.6, user 8-14 use 10.29.19.10 and the rest use 10.29.19.11**.

Then after logging in if you check what's in HDFS now by typing "hdfs dfs -ls", you should see the folder "data_CE650C" which contains all the sample datasets we gona use for in-class exercises.

}


### Here are something you need to prepare before the class:

[//]: # (Image References)

[HDFSin]: ./figures_support/HDFSin.png "HDFSin"
[Putty]: ./figures_support/Putty.png "Putty"
[Puttyin]: ./figures_support/Puttyin.png "Puttyin"
[Puttylogin]: ./figures_support/Puttylogin.png "Puttylogin"
[WinSCP]: ./figures_support/WinSCP.png "WinSCP"
[WinSCPlogin]: ./figures_support/WinSCPlogin.png "WinSCPlogin"
[FileZilla]: ./figures_support/FileZilla.png "FileZilla"
[FileZillain]: ./figures_support/FileZillain.png "FileZillain"
[FileZillalogin]: ./figures_support/FileZillalogin.png "FileZillalogin"
[mac1]: ./figures_support/mac1.png "mac1"
[mac2]: ./figures_support/mac2.png "mac2"
[mac3]: ./figures_support/mac3.png "mac3"
[mac4]: ./figures_support/mac4.png "mac4"
[mac5]: ./figures_support/mac5.png "mac5"

## Required: 

We will be using INTRANS test cluster in this lecture, but you need to install some software on your laptop to support the connection to the cluster.


### **Windows:**

1. Putty 
![alt text][Putty]
2. WinSCP
![alt text][WinSCP]

### **Mac:**

1. FileZilla
![alt text][FileZilla]

###Please search online, download and install the required sofeware according to you laptop system. Then let's try to connnect to the cluster and HDFS:

### **Windows:**

* Connet to cluster:

1. open Putty and login
    ![alt text][Puttylogin]
    
2. type -ls to check the file on local machine (suppose you logged in 10.29.19.10 then 10.29.19.10 is your local machine, which is part of the cluster and we will discuss the whole structure in class) We have three folders and three files on local right now:
    ![alt text][Puttyin]

* exchange file with cluster:

1. open WinSCP and login
    ![alt text][WinSCPlogin]
    
2. WinSCP provide a save file exchange platform between your laptop and the remove linux machine. The left window is your laptop, the right window is the remove linux machine you logged in (in this case it is 10.29.19.10 which we also call it "local" or "server" or "cluster" in different situations.....) You can upload files from you laptop to the cluster by simply dragging and dropping files to the right window, and you can download files to you laptop from the cluster by simply dragging and dropping files from the right window.
    This is the way I upload the three files shown in the picture
    ![alt text][WinSCPin]

* The "Local" or "server" is not actually HDFS and the three folders and three files you have seen are not in HDFS.You can peek the files in HDFS by typing "hdfs dfs -ls" in Putty command line
    ![alt text][HDFSin]
    At this point you can try to create your own folder in HDFS and play inside. But please try not to delete any public files.
    We will explore HDFS in the class together!


### **Mac:**

* Connet to cluster:

1. open Terminal and type "ssh username@URL"
    ![alt text][mac1]

2. input password
    ![alt text][mac2]
    
3. you are in! easy
    ![alt text][mac3]
    
4. type -ls to check the file on local machine (suppose you logged in 10.29.19.10 then 10.29.19.10 is your local machine, which is part of the cluster and we will discuss the whole structure in class) We have three folders and three files on local right now.
    ![alt text][mac4]

* exchange file with cluster:

1. open FileZilla and login: type URL in host, username, password and 22 in port:
    ![alt text][FileZillalogin]
    
2. FileZilla provide a save file exchange platform between your mac and the remove linux machine. The left window is your mac, the right window is the remove linux machine you logged in (in this case it is 10.29.19.10 which we also call it "local" or "server" or "cluster" in different situations.....) You can upload files from you laptop to the cluster by simply dragging and dropping files to the right window, and you can download files to you laptop from the cluster by simply dragging and dropping files from the right window. This is the way I upload the three files shown in the picture
    ![alt text][FileZillain]

* The "Local" or "server" is not actually HDFS and the three folders and three files you have seen are not in HDFS. You can peek the files in HDFS by typing "hdfs dfs -ls" in Terminal command line
    ![alt text][mac5]
     At this point you can try to create your own folder in HDFS and play inside. But please try not to delete any public files.
    We will explore HDFS in the class together!


## Optional: 

If you are going to develop tons of mapreduce programs and want to setup a developing envirionment on you own machine, you can download Eclipse and configure a java environment for Hadoop.

Comparing to Python which is dynamic typing, java is a static typing language. There are some pros and cons of Java comparing to Python. The biggest advantage of Java could be it has a compiler watching you behind and can instantly tell you there is a synax error and how to fix it while you are typing. But because of the over-detailed formalities, java needs way more lines to perform the same function in Python. So it is generally believed that a programmer is 5 times more productive using python than using java...

The aforementioned estimation also depends. In some cases java is more suitable than python and maybe Hadoop is one of these cases. The entire Hadoop thing is built on java so sometime it is easier for you to dig deeper using java.

After all, we are not going to use java in this class. So I am not providing info about using java for hadoop here.


## more options:

What if you don't have access to our INTRANS cluster in some cases and you just happened to want to play with hadoop so desperately ...

There are more options!

1. Cloudera veritual machine
    You can install a "virtual machine" on your own machine. It is kind of a double system but not exactly a double system. Cloudera provides a virtual machine with hadoop configured on for personal uses. So if you are interested you can search cloudra virtual machine and explore more.

2. Cloud service
    Amazon Web service (AWS) or Azure are your typical choices. They claim Azure is bigger than AWS and I believe Azure is also more expensive than AWS. To use these service, you need to go to their webpage, open an account (with credit card information provided), choose a remove machine or a remove cluster, launch it and get charged... For a basic GPU cluster I remembered it's $0.9/hour for AWS and $1.2/hour for Azure and I could be wrong. We can find out more on the Azure workshop on Feb 24, 2017
    
After all, these options are not going to be used or introduced in class.




