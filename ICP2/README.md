# Assignment-2

#### Name: Yousef Almutairi
#### Email: yousefalmutairi@mail.umkc.edu

<br/>

I am going to explain the first part of the assignment, then I'll move to the second one.


## Part 1

<b> 1. Classes and objects: Employees </b> </br>

In this question, I did not make all the requirements because of the time-consuming. However, I made a good job by creating all the class and functions that the instructor asked for. Since the FullTime and PartTime classes are inherited from the Employee class I did not upload all screenshots because some of the functions and sub-classes are the same. I named the classes as I need them to ensure that when everyone read the class name would know the purpose of it.

 <img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/1.png" alt="">
 <img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/2.png" alt="">
 <img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/3.png" alt="">
 <img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/4.png" alt="">
 <img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/5.png" alt="">
 <img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/6.png" alt="">
 <img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/7.png" alt="">




<b> 2. Web scraping </b> </br>
I've imported the library that we need to scraping, then I created two variables: one for getting the link and the other for Beautiful Soup object to take the HTML content as input. In addition, I asked to print the title of the giving link, and created a for loop to go over all the href links and print it.
 <img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/Web_scraping.png" alt="">


<b> 3. Numpy </b> </br>
I explained each line in the screenshot. As you can see, It replaced the max number in each row to ZERO with using np.where function and save it as .npy file format.
row1: 17 -> 0
row2: 18 -> 0
row3: 18 -> 0
 <img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/Numpy.png" alt="">


</br></br>
## Part 2
<b> (Titanic Dataset) </b>
<br/>
1. Find the correlation between ‘survived’ (target column) and ‘sex’ column for the Titanic use case in class.

After reading the train.csv data of the Titanic Dataset and printing it, I categorizing sex column to [ 'female': 1, 'male': 0]. Then, I asked to print out the correlation between sex and survived which equals = 0.5433513806577555.
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/corr1.png" alt="">

<b> a. Do you think we should keep this feature? </b> <br/>
Since the result is not negative, Yes, I think we should keep it.


<b> 2. Do at least two visualizations to plots to describe or show correlations. (e.g.: Survived: Class and gender). </b> <br/>
In the first visualization, It shows that the correlation between Survived column and 'Sex'. </br>
In the # visualize2, I noticed that (Not survive [0] has less fare than who has survived [1]) 
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/corr2.png" alt="">


This is Extra work for me and is not include in the assignment. I did more practice on showing the correlations between defferent variable.
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/corr3.png" alt="">


<b> (Glass Dataset) </b>
 <br/>
 

<li> Naïve Bayes : </li>
I've Imported the data and split it by using #train_test_split. Then, I evaluate the model on testing part and print the accurancy score = 37.21
 <img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/naviebayes.png" alt="">


<br/>
<li> SVM : </li>
I did same as I did with Naïve Bayes except of calling the function of SVM. SVM score = 20.93
 <img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-2-Yousefalmutairi91/raw/master/Screenshot/SVM.png" alt="">

<br/>

<b> Which algorithm you got better accuracy? Can you justify why? </b> </br>
Naïve Bayes has got better accuracy than SVM model. Regardless the accuracy score is higher in NB than SVM. if we look to [support] we can see that each model has the same number of occurrences of the test part, but the Naïve Bayes did much better on time of correctly classified the data as well as in f1-score.



<h4> Video link : </h4>
<a href="https://drive.google.com/file/d/1-OdteuPBE1CfKZStrVTkonVC-WSPrKMP/view?usp=sharing" rel="nofollow">Video recording link</a>
