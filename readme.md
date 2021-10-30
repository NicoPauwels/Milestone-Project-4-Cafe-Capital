# Milestone Project 4: Cafe Capital

[View the live project here.](https://cafe-capital.herokuapp.com/)<br>

This project in its current state is purely for educational purposes.

# UX

## Strategy

This project is an ordersystem for a restaurant called Cafe Capital. The purpose of the application is when users are visiting the restaurant they can check the menu on their mobile and place and pay an order.

### Site Goals

* Display Cafe Capitals menu;
* Allow Cafe Capitals guests to place an order;
* Allow Cafe Capitals guests to pay an order;
* Allow Cafe Capitals guests to create an account;
* Allow Cafe Capitals guests to check their order history;
* Allow Cafe Capitals owners to easily add, edit and delete items of their menu.

#### User stories: 

* First time Visitor Goals
    * As a first time visitor, I want to be able to check Cafe Capitals menu;
    * As a first time visitor, I swiftly want to be able to move through the menu;
    * As a first time visitor, I want to be able to place an order in Cafe Capital;
    * As a first time visitor, I want to be able to pay my order to Cafe Capital;
    * As a first time visitor, I want to be able to get review my order once it has been payed and thus placed;
    * As a first time visitor, I want to be able to create a profile;
    * As a first time visitor, I want to be able to register;
    * As a first time visitor, I want to be able to login;
    * As a first time visitor, I want to be able to logout.
* Returning Visitor Goals
    * As a returning visitor, I obviously want the same application experience as a first time visitor;
    * As a returning visitor, I want to check my order history at Cafe Capital.
* Frequent User Goals
    * As a frequent user of this application, I want to same user experience as a returning visitor.

    * As the owner of Cafe Capital I want to easily create, update and remove items from the menu.

### My Strategy

I started with a different project called Oobr which was going to be a multitennant application where business could registers and upload their menu. It would be a kind of portal site for when visiting these registered business you could place an order, pay and get served. I started wireframing the whole database and had it mapped out detailed. I started with creating a landing page and then needed to overwrite allauth functionality to treat various type of users in the database as you would have businesses that wanted to register but also regular clients needed to be able to signup. This took me a serious amount of time but eventually I pulled it off and overrode allauth basic singule user functionality. However I do realised at that point in time I wasn't going to able to create such a big functioning application and meet the deadline. Experienced scope creep so I decided to narrow it down and create an order system for just one restaurant. The big benefit of this new approach was that I could rely heavily on the Boutique Ado project from Code Institute. I had about a month left to create a fully functioning order system for this Milestone Project. I lost a lot of time with typos and forgetting to add a path to urls.py etc. I tried to pull off a complete working order system but there are some issues here and there that will be addressed later.

## Scope 

Planned Features:<br>
* Responsive design (mainly the focus was on having it look good on mobile and desktop, as this application wouldnt be used very much by tablet users)
* Navigation menu;
* Tab;
* Menu with categories;
* CRUD functionality;
* Menu manamgenet for the restaurant owners;
* Profile page; 
* Login functionality;
* Logout functionality.

## Structure

User Story:

> As a first time visitor, I want to be able to check Cafe Capitals Menu;

Acceptance criteria:
* User needs to be able to display Cafe Capitals menu

> As a first time visitor, I swiftly want to be able to move through the menu;

Acceptance criteria:
* I didn't want to allow users to search the site or use any filters; I divided the menu into categories which are always available just below the navbar. I wanted to give users the experience of actually going through the menu as one would when holding a hard copy.

> As a first time visitor, I want to be able to place an order in Cafe Capital;

Acceptance criteria:
* While navigating through the menu, users are able to click through an item and land on a slightly more detailed page. Here the user is able to add a certain amount of that item to the tab. Users can check the tab at any given time, and update the quantities of the items they want or even delete the item from their tab.

> As a first time visitor, I want to be able to pay my order to Cafe Capital;

Acceptance criteria:
* In their tab they are also able to pay for the order. If they choose to do so, They get a final overview of the order, they leave their name and email and payment card details into a form.

> As a first time visitor, I want to be able to get a review of my order once it has been payed and thus placed;

Acceptance criteria:
* Once the payment has been successfully handled, a user gets a final notification of the order itself and a link to go back to the menu.

> As a first time visitor, I want to be able to register and create a profile;

Acceptance criteria:
* You can register to the website and create a profile, most fields are optional when doing so as we basically only need an e-mail address to send the receipt to.

> As a first time visitor, I want to be able to login;

Acceptance criteria:
* Once registered, you are able to login.

> As a first time visitor, I want to be able to logout.

Acceptance criteria:
* Once logged in, you are able to logout.
    
> As a return visitor, I want to check my order history.

Acceptance criteria:
* Because of the creation of a profile all orders can be saved to the user, and he or she can check his order history via the profile.

> As the owner of Cafe Capital I want to easily create, update and remove items from the menu.

Acceptance criteria:
* Super users can be created for the restaurant owners, that way they have the possibility to add, update or delete items from the menu.

## Skeleton

Below the wireframes:

* Desktop wireframe - [View](https://github.com/NicoPauwels/Milestone-Project-4-Cafe-Capital/blob/d916d8551674bd14f3a954ae93ccf9308d2b97e9/readme/cafe-capital-desktop-wireframes.png)
* Mobile wireframe - [View](https://github.com/NicoPauwels/Milestone-Project-4-Cafe-Capital/blob/d916d8551674bd14f3a954ae93ccf9308d2b97e9/readme/cafe-capital-mobile-wireframes.png)

## Information Architecture

* Information Architecture - [View](https://github.com/NicoPauwels/Milestone-Project-4-Cafe-Capital/blob/1318b1f910883c5d6d3c3b4be75d8790e13d3f53/readme/cafe-capital-information-architecture.png)


## Security

Database connection details are set up in env.py for development, for security reasons this is not uploaded to GitHub so that database and connectiondetails are not visible to users. In production these are stored in Heroku.

## Defensive Design

Defensive Design was implemented using Webhooks and Python Decorators from Django. Using The Python decorator @require_login add, edit and delete items is only available to SuperUsers.

## Surface

* Colour scheme
    * I chose bright contrast for Cafe Capital
        * for backgrounds:
            * #FFFFFF / White;
        * for text: 
            * #666666 / grey;
        * for elements that needed contrast:
            * #2ECC71 / green;
            * #111111 / black;
    
* Typography
    * The main font used is Lato

# Features and who can use them

## Existing Features - Admin / Super User

Everything regular users can do plus:

* Access Admin Hub
* Add a Category (Can only be done via the Admin)
* Add an item
* Edit an item
* Delete an item (Can be done via item_details)

## Existing Features - Regular User

* Make a purchase without having to register an account
* Register
* Login
* View Order History
* Add/Update their profile information
* Browse items
* Navigate directly to specific item category
* Add items to the tab
* Add multiples of one item if they want
* See the tab total cost of all their selected items at any time
* Adjust how many of each item is in the tab
* Remove items from the tab
* See a summary of their order before completing the order
* See a final warning regarding how much money will be charged to their card before confirming and completing the order
* Get a notification when a successful order has gone through
* Get an email with an order summary sent to them on completion of a successful order
* Get notification when something goes working

## Features left to implement

* A model that is used to create all the tables in the restaurant so that a URL can be generated for each table and the application takes in immediately where the user is sitting and so the order can be served.

## Known Bugs

* The receipt is not being sent to the user when an order has been placed. This has probably to do that with the fact that the app does not fetch the webhook coming from stripe. I went through the process of setting up the webhook's endpoint multiple times; changed the url in the urls.py checkout app, printed multiple print statements in the view handler to see where it breaks. The customer email is never printed to the terminal thus the the send confirmation email function is never called upon. Furthermore, in the Developers tab of stripe you can see clearly that the events fail to deliver. 

* There are some layout issues that will be addressed in the next update of the project. For example: the content of the allauth templates isn't rendered properly on mobile, the templates are hidden behind the navbar. Also there are some style issues on medium and tablet screens, like the text of the items in the menu overlapping the picture. Also the messages can be styled better in a future version of the project. Many of these issues were not properly addressed in the final rush to submit the project by the hard deadline.

# Technologies 

* [HTML5](https://en.wikipedia.org/wiki/HTML) 
    * This project uses HTML as the main language used to complete the structure of the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS)
    * This project uses custom written CSS to style the website.
* [Bootstrap](https://getbootstrap.com/)
    * Bootstrap was mainly used for button and dropdown menu functionality.
* [Font Awesome](https://fontawesome.com/start) 
    * Font Awesome was used to import some icons.
* [Google Fonts](https://fonts.google.com/)
    * Google fonts was used to import some fonts.
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    * A few lines of Javascript were used for the slider used in the forms.
* [jQuery](https://jquery.com/)
    * Supports bootstrap functionality
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    * This projects core was created using Python, the back-end logic and the means to run/view the website.
* [Django](https://www.djangoproject.com/)
    * High level Python web framework
* [Heroku](https://www.heroku.com/)
    * Heroku was used to deploy the live website and the db (PostgreSQL) is stored.
* [Git](https://git-scm.com/) 
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to Github.
* [Github](https://github.com/) 
    * GitHub is used to store the projects code after being pushed from Git.
* [Balsamiq](https://balsamiq.com/) 
    * Balsamiq was used to create the wireframes during the design process.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    * Google chromes built in developer tools were constantly used throughout the development process to inspect page elements.
* [Visual Studio Code](https://code.visualstudio.com/)
    * All code was written in Visual Studio Code.

# Testing

* Testing was done regularly throughout the entire process

* Each function was tested and re-tested

* Defensive Design was tested by manually adding endpoints from areas where access should not be allowed

* Testing done on checkouts/logins/logouts/admin_hub/profile using back and forward buttons, manually adding endpoints and urls

* Site navigation and links tested thoroughly, navigation breaks also tested using the back and forward buttons

* [W3C Markup Validator:](https://validator.w3.org/)<br><br>Some errors were caused by the Jinja syntax but besides that no errors or warnings were found.<br>
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)<br><br>No errors were found in the CSS.
* [jshint.com](https://jshint.com/)<br><br>No errors were found in the script.js.
* [PEP8 Validator](http://pep8online.com/)<br><br>The check resulted in a a few errors.<br>All of them said "line too long", as some of them were a bit longer than 79 characters, none of them exceeded the limit with 30 characters.

## Deployment to Heroku

Create application:

1. Navigate to Heroku.com and login.
2. Click on the new button.
3. Select create new app.
4. Enter the app name.
5. Select region.

Set up connection to Github Repository:

1. Click the deploy tab and select GitHub - Connect to GitHub.
2. A prompt to find a github repository to connect to will then be displayed.
3. Enter the repository name for the project and click search.
4. Once the repo has been found, click the connect button.

Set environment variables:

Click the settings tab and then click the Reveal Config Vars button and add the following:

1. key: AWS_ACCESS_KEY_ID
2. key: AWS_SECRET_ACCESS_KEY
3. key: DATABASE_URL
4. key: EMAIL_HOST_PASS
5. key: EMAIL_HOST_USER
6. key: SECRET_KEY
7. key: STRIPE_PUBLIC_KEY
8. key: STRIPE_SECRET_KEY
9. key: STRIPE_WH_SECRET
10: key: USE_AWS

Enable automatic deployment:

1. Click the Deploy tab
2. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

# Credits

## Code

## Sources and documentation used

* Various issues were solved based on answers on [Stackoverflow](https://www.stackoverflow.com) and [W3Schools](https://www.w3schools.com)
* [Django](https://docs.djangoproject.com/en/3.2/ documentation was constantly used throughout the project.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) documentation was constantly used throughout the project.
* [Python](https://docs.python.org/3/) documentation was constantly used throughout the project.

## Acknowledgments

* Antonio Rodriguez, my mentor for the continuous support and helpful feedback;
* John Traas, Code Institute tutor, for the continuous support and helpful feedback;
* Sean Murphy, Code Institute tutor , for the continuous support an helpful feedback;
* Daisy McGirr, Code Institue mentor, for the continous support and helpful feedback. 