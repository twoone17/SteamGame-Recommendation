# SteamGame Recommendation

SteamGame Recommendation is to recommend playable able based on your information.
<br><br>
It's 2022-2 Project of Machine Learning lecture from Department of Computing, Gachon University.

<br><br>

## <b> About </b>

<br>

In the case of movies and music, there're representative recommendation systems :

- Movies for Netflix
- Musics for Spotify

However, there is no representative recommendation system for games!

Therefore, we are going to make a system to recommend games.


<br><br>

## <b> Dataset Introduction </b>

This dataset is combination of 'Steam Video Games', and 'Steam Store Games (Clean dataset)'.

<br>

<b> Dataset 'Steam Store Games (Clean dataset)' </b>
- [dataset Link](https://www.kaggle.com/datasets/nikdavis/steam-store-game)
- This dataset combined data of 27,000 games scraped from Steam and SteamSpy APIs.
- Copyright Rule : CC BY 4.0
- It has 18 attributes.

| Attribute    	| Type        	| Explanation                                                                                 	| Example                         	|
|--------------	|-------------	|---------------------------------------------------------------------------------------------	|---------------------------------	|
| appid        	| Nomial      	| Unique identifier for each title                                                            	| 10, 20, 30, ...                 	|
| name         	| Nomial      	| Title of app (game)                                                                         	| Left 4 Dead, Dota 2, ...        	|
| release_date 	| Nomial      	| Release date in format YYYY-MM-DD                                                           	| 2008-11-17, 2009-11-19, ...     	|
| english      	| Categorical 	| Language support: 1 if is in English                                                        	| 0, 1                            	|
| developer    	| Categorical 	| Name (or names) of developer(s). Semicolon delimited if multiple                            	| Valve, Mark Healey, ...         	|
| publisher    	| Categorical 	| Name (or names) of publisher(s). Semicolon delimited if multiple                            	| Valve, Mark Healey, ...         	|
| platforms    	| Categorical 	| Semicolon delimited list of supported platforms. At most includes: windows;mac;linux        	| windows, windows;mac;linux, ... 	|
| required_age 	| Categorical 	| Minimum required age according to PEGI UK standards. Many with 0 are unrated or unsupplied. 	| 0, 16, 18, ...                  	|
| categories   	| Nomial      	| Semicolon delimited list of game categories, e.g. single-player;multi-player                	| Single-player;Multi-player, ... 	|
| genres       	| Nomial      	| Semicolon delimited list of game genres, e.g. action;adventure                              	| RPG, Strategy, Action;RPG, ...      	|
| steamspy_tags       	| Categorical      	| Semicolon delimited list of top steamspy game tags, similar to genres but community voted, e.g. action;adventure                              	| Action;FPS;Multiplayer, ...       	|
| achievements       	| Discrete      	| Number of in-games achievements, if any	| 0, 147, 54, ...	|
| positive_ratings       	| Discrete      	| Number of positive ratings, from SteamSpy	| 124534, 3318, ...	|
| negative_ratings       	| Discrete      	| Number of negative ratings, from SteamSpy	| 3339, 633, ...	|
| average_playtime       	| Discrete      	| Average user playtime, from SteamSpy	| 17612, 277, 187, ...	|
| median_playtime       	| Discrete      	| Median user playtime, from SteamSpy	| 317, 62, 34, ...	|
| owners       	| Categorical      	| Estimated number of owners. Contains lower and upper bound (like 20000-50000). May wish to take mid-point or lower bound. Included both to give options.	| 5000000-10000000, ...       	|
| price       	| Continuous      	| Current full price of title in GBP, (pounds sterling) 	| 7.19, 3.99, 5.79, ...       	|


<br><br>

<b> Dataset 'Steam Video Games' </b>
- [dataset Link](https://www.kaggle.com/datasets/tamber/steam-video-games)
- This dataset is for recommend video games from 200k steam user interactions.
- Copyright Rule : DbCL v1.0
- It has 4 attributes.

| Attribute     	| Type        	| Explanation                                            	| Example                         	|
|---------------	|-------------	|--------------------------------------------------------	|---------------------------------	|
| user-id       	| Nomial      	| User ID                                                	| 151603712, 187131847, ...       	|
| game-title    	| Nomial      	| Name of the steam game                                 	| Dota 2, FINAL FANTASY XIII, ... 	|
| behavior-name 	| Categorical 	| behavior name                                          	| purchase, play                  	|
| value         	| Continuous  	| Hours if behavior is play, 1.0 if behavior is purchase 	| 1.0, 9.8, 9.7, ...              	|

<br><br>

## <b> Data Exploration</b>

<br>
<b> Steam Store Games (Clean dataset) </b>

</br>

- informations of　<b>positive_ratings</b>　and　<b>negative_ratings</b> 

<img src="https://user-images.githubusercontent.com/31691750/204211724-033c7109-02bc-42f6-9f39-88e7d653c6e0.png"  width="217.5" height="116.5"/>　　
<img src="https://user-images.githubusercontent.com/31691750/204211731-4388b528-4afa-4852-8225-ee3916ae598f.png"  width="217.5" height="116.5"/>


<br>

- <b>Positive Rating Table</b> 

<img src="https://user-images.githubusercontent.com/31691750/204211745-959b767a-ecf8-4170-bf33-1e513a63aec3.png"  width="498" height="237"/>

<br>

- <b>Positive Rating Ratio</b> 

<img src="https://user-images.githubusercontent.com/31691750/204211745-959b767a-ecf8-4170-bf33-1e513a63aec3.png"  width="498" height="237"/>

<br>

- <b>Distributions of columns</b> 

<img src="https://user-images.githubusercontent.com/31691750/204224380-b9cc4698-7609-407f-8759-191fa3af9a87.png"  width="307.2" height="240"/> 
<img src="https://user-images.githubusercontent.com/31691750/204224835-91b07edc-e884-45e4-aa15-b1fe4cfde52e.png"  width="307.2" height="240"/>

<br>
<img src="https://user-images.githubusercontent.com/31691750/204224827-d2a748ea-a484-48d2-914a-5f2809edde50.png"  width="307.2" height="240"/> 
<img src="https://user-images.githubusercontent.com/31691750/204224831-9a2e83b8-e8b6-46d0-b3a2-268f4a73e18b.png"  width="307.2" height="240"/>

<br><br>

<b> Dataset 'Steam Video Games' </b>

</br>

- informations of　<b>value</b>

<img src="https://user-images.githubusercontent.com/31691750/204211816-e65f6664-0c6c-4812-896f-1e6e941954be.png"  width="208" height="144.5"/>

</br>

- Top 10 Users of <b>value</b> (Play-time) + <b> What They Played </b> 

<img src="https://user-images.githubusercontent.com/31691750/204211822-d2683dcd-66d8-464e-854d-9002a9a43152.png"  width="307" height="193.5"/>

<br><br>

## <b> Architecture </b>

<br>

<img src="https://user-images.githubusercontent.com/84762786/204170753-ed04eacb-6927-46da-8277-de21411a9c67.png"  width="395" height="232"/>

<br>

<b> If the group is .... </b> 
- Large : Use Collaborative Filtering
- Small : Use Cotent-Based Filtering
  - For avoiding [long-tail problem](https://rogerheederer.github.io/LongTailProblem/).

<br>

<b> Clustering </b>

(내용 추가 예정)

<br>

<b> Collaborative Filtering </b>

<br> 

<img src = "https://user-images.githubusercontent.com/84762786/204191946-4ba25939-46a7-4600-b44b-ef94986bb432.png"/>
<br> 

There is no rating column in our data.

So, we calculated the user's rating by comparing the user's play hour with average played hour.

<br>

<img src = "https://user-images.githubusercontent.com/84762786/204191995-96ecf851-b5e9-4fe6-94b2-1b7097e699ca.png"/>

<br> 

We calculated user's rating.

<br>

<img src = "https://user-images.githubusercontent.com/84762786/204191549-bae01bbf-9bcf-4d21-8a50-5eaf225af9d9.png"/>

<br> 

We made <b> CF_recommend_Game function</b>. <br>
It gets the user id input and calculates the estimated score for each game name using svd.

<br>

<img src = "https://user-images.githubusercontent.com/84762786/204192022-228366cf-9bd0-4574-b0c5-e30bede288d2.png"/>

<br> 

This is the <b>result</b> of the CF function.

<br><br>

<b> Content-Based Filtering </b>

(내용 추가 예정)
