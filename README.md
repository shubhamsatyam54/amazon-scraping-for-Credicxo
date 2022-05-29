# How I did it?
I have done this project on jupyter notebook using selenium,with the help of pandas and dictionary. I have connected it with Google Colab so that any one can direct run the file. I have also connected it to MySql database but I have commented the MySql section code as it is not very handy to use it on Colab Platform. 

I have used mainy find_by_xpath for finding the elements. just for the product image i have used class. First i had used id/name for finding the elements but it was not succesful so I concluded to Xpath. For the title, image and description i did not had to give much effort but for the cost, it took a lot of time. There were 3 different types of representation of cost. I tried every one byusing them individually but not got the desired output so lastly i had to combine all the three repsentation and bring a code which can work anywhere. 

Most of the links are were not working. First I used request library for finding Error 404 through response code but both the link working/non-working the response code was 503. So i had to use Try-Except block to find out not working links. As it will give error if anyone of the attributes is missing, and in page not found one every element is missing.

I had sorted the data according to country for the use.Lastly I have created a batch of 100 urls so that i can calculate the runtime.

I will also give a try to the Catchpa solver 
