# Assignment_3
Week_3 Assignment_3

#### Complete the following:

#### Name: Yousef Almutairi
#### Email: yousefalmutairi@mail.umkc.edu

<br/>
 

## Part 1:

After imported all the neccessery libraries and read the dataset, I've plotted the GaurageArea field and SalePrice using scatter plot as well as detecting the outliers based on the visual.

<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part1/1.png" alt="">

I plotted again after removing the outliers.
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part1/2.png" alt="">

In this screenshot, I printed all the numbers of Anomalies
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part1/3.png" alt="">

##### 2. Evaluating the model: </br>

I've imported the (mean_absolute_error, r2_score, mean_squared_error) from the sklearn.metrics to help finding the MAE, MSE, RMSE and R2 score.

<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part1/4.png" alt="">


I did this to know how the regression line work on the actual values and predicted price. (Note: This screenshot is not reqired in this assignments)
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part1/5.png" alt="">


##### 3. Plot the regression line (Bonus question (points)): </br>
In this step I found the features that are positively correlated with SalePrice. Then, I chose on feature which is here the "Overallqual" and graph it with Saleprice.

<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part1/6.png" alt="">

Since I've already did this in the practice above, I changed the work with different library to figure the regression line which is (Statemodels regression). In addition, I applied the simple linear regression on the selected feature (Overallqual) and the target (dependent) SalePrice. Then, I drew the regression line on the graph.
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part1/7.png" alt="">



#### Create Multiple Regression for the “Restaurant Revenue Prediction” dataset. </br>

I visualized the skewness (before and after) of the (revenue) and then I used the log transform to improve the linearity of the data.

<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part1/8.png" alt="">

I repeat the same proccess of the evaluation and print the R^2 + RMSE score.
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part1/9.png" alt="">


I removed the null values using the dropna() function and print the top 5 most correlated features to the target label(revenue).
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part1/10.png" alt="">

Lastly,  I built a model on top of those 5 features and print the MAE, MSE, RMSE and R2. As shown in the screen shot the RMSE and R2 that I achieved in question 2 is better fit than this model.
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part1/11.png" alt="">
 
 
## Part 2: 
In this part, I applied K means clustering to the Credit Card Dataset. So, I removed all the null values by mean which was on only MINIMUM_PAYMENTS and CREDIT_LIMIT. Then, I shaped the dataset after removed null values
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part2/1.png" alt="">


I used the elbow method to find a good number of clusters with the K-Means algorithm. In the figure below I notice that the optimal number of cluster is 3. </br>
After than I calculated the silhouette score for the cluster =  0.360147899376414 which indicates that the sample is on or very close to the decision boundary between two neighboring clusters.

<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part2/2.png" alt="">


In the last question of part 2 the instructor asked to apply K-Means algorithm on the PCA and visualize it. As we can see below I started to Standardization method to rescale the value. Then I got the Silhouette Score: 0.06548653720549787 which I observed was not improved. Finally, I visualize the cluster using the plt.scatter.
<img src="https://github.com/UMKC-APL-PythonDeepLearing/assignment-3-Yousefalmutairi91/blob/main/Screenshots/part2/3.png" alt="">




<h4> Video link : </h4>
<a href="https://drive.google.com/file/d/1oaqt_iCnJnpEofNxHbQzadO_KnQ807_c/view?usp=sharing" rel="nofollow">Video recording link</a> </br>




<h4> References: </h4> <br/>
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna
https://analyticsindiamag.com/5-ways-handle-missing-values-machine-learning-datasets/
https://www.journaldev.com/33492/pandas-dropna-drop-null-na-values-from-dataframe








