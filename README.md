# SteamGame-Recommendation

<h1>Architecture</h1>

![image](https://user-images.githubusercontent.com/84762786/204170753-ed04eacb-6927-46da-8277-de21411a9c67.png)

<h1>Collaborative Filtering</h1>

<h3>Since there is no rating column in our data, we calculated the user's rating by comparing the user's play hour with average played hour.</h3>

![image](https://user-images.githubusercontent.com/84762786/204191946-4ba25939-46a7-4600-b44b-ef94986bb432.png)

<h3>Calculated User's rating</h3>

![image](https://user-images.githubusercontent.com/84762786/204191995-96ecf851-b5e9-4fe6-94b2-1b7097e699ca.png)

<h3>CF_recommend_Game function </h3>
<p>Get the user id input -> calculate the estimated score for each game name using svd</p>  

![image](https://user-images.githubusercontent.com/84762786/204191549-bae01bbf-9bcf-4d21-8a50-5eaf225af9d9.png)

<h3>Result of the CF function </h3>

![image](https://user-images.githubusercontent.com/84762786/204192022-228366cf-9bd0-4574-b0c5-e30bede288d2.png)

--------------------------------------------------------------------------------------------------------------------------------
