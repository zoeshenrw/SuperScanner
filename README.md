# SuperScanner-FinalProject
- The app will mainly focus on shared bikes. Ideally, the user should only register once into our app to have the access to the scanner. 
- The app should scan the QR code properly and redirect the users to the corresponding website after registration. (Under development!)
- The app also includes additional features, such as clickable maps and sending notifications about nearby nikes. 

Our main motivation comes from citibikes and wants to create a more convenience user experiences when it comes to bike sharing. 

The website is deployed on Render: https://superscanner.onrender.com/home

- Clickable maps: data on bike companies for each state. The htmls will redirect users to the bike company's official website for more information.
- Notifications: notification sent in pop-ups about stations nearby. The url in the pop-up will redirect users to Google Maps, which users can get directions to the specific station. 
- Map: used leaflet for interacitve maps. The map reflects real data provided by Citi Bike on how many bikes are at each station. Stations are categorized. Users can use the tool bar on the top right to select what type of stations they want to see, so the map will not be so crowded. A summary of types of stations is provided on the bottom right. Numbers of classic and electric bikes available are provided above the map. 
- These features can be used without user registration and login. Registration and login were designed for the scanner feature. Features will be updated properly when we finish developing the scanner feature!