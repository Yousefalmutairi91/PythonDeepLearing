# Assignment-4
Assignment-4


#### Name: Yousef Almutairi
#### Email: yousefalmutairi@mail.umkc.edu

<br/>


## Part 1 - Machine Learning: NLP:

##### Question 1: a) SVM and see how accuracy changes: <br/>


I've applied the SVM on the data that has been given and print out the accuracy score + classification_report

<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/1.png" alt="">

##### b) KNeighborsClassifier and see how accuracy changes: <br/>

I've applied the KNeighborsClassifier on the data that has been given and print out the accuracy score + classification_report
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/2.png" alt="">

##### c) Set the tfidf vectorizer parameter (TfidfVectorizer(ngram_range=(1,2)) <br/>

In this screenshot I applied the TfidfVectorizer(ngram_range=(1,2) on the SVM to see the result. However, there was no visiable different that I can see on the accurancy score.
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/3.png" alt="">

##### d) Set tfidf vectorizer argument to use stop_words='english' <br/>
For this one, I utilized it on the KNeighborsClassifier and I got the same result.
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/4.png" alt="">

 <br/>  <br/>
 
#####  Question 2:  Extract the following web URL text using BeautifulSoup:  <br/>
I've created the input file if not already created and then asked to extract the data from the given link (as shown)
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/5.png" alt="">



##### • Tokenization </br>
I've printed 3 of the sentence tokens as well as 3 of the word tokens.
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/6.png" alt="">

##### • part-of-speech (POS) </br>
##### • Stemming </br>
In this screenshot, I've printed the pos tag for all the word tokens as well as print the tree types of the Stemmings.
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/7.png" alt="">



##### • Lemmatization </br>
##### • Trigram </br>

I've printed the first 10 lemmatized words and the Trigram
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/8.png" alt="">


 ##### • Named Entity Recognition </br>

<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/9.png" alt="">

  ##### • Plot the Frequencies of words </br>

I plotted the result using the plot function to show the most common or frequencies of words.
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/10.png" alt="">



 
## Part 2 - Basics in Keras: 
  ##### 1. Use the diabetes.csv dataset :  </br>
  read the data and splitted it
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/11.png" alt="">
 
Added two more Dense layers and validation_data=(X_test, Y_test) attribute to .fit() method.
 <img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/12.png" alt="">

Plotted the accuracy and evaluated the model. 
 <img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/13.png" alt="">


  ##### 2. Use the Breast Cancer.csv dataset  :  </br>
read the data and dropped the id attribute and converted the diagnosis values to 1 and 0, so that don't gave me a datatype error.

<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/14.png" alt="">

added one more Dense layer and validation_data=(X_test, Y_test) attribute to .fit() method.
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/15.png" alt="">

Plotted the accuracy and evaluated the model. 
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/16.png" alt="">

Here is the result if I've Normalized the data before feeding the data to the model. Got ZERO on the traning model accurcy. 
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment--4-Yousefalmutairi91/blob/main/Screenshots/17.png" alt="">




<h4> Video link : </h4>
<a href="https://drive.google.com/file/d/1HH3JySJ0oClpVybspnt55n2ccaoqrRqp/view?usp=sharing" rel="nofollow">Video recording link</a> </br>




<h4> References: </h4> <br/>
https://www.journaldev.com/45025/standardscaler-function-in-python
https://medium.com/@kohlishivam5522/understanding-a-classification-report-for-your-machine-learning-model-88815e2ce397


