# Nullanion

![Null Logo](static/images/nullanion-logo.svg)

Nullanion offers music services for those that need quality, delivered on time.

At Nullanion, one can order a mix or master of a song, EP or full length LP (Album). Other services include Ad. Production, Soundtrack and Sound Design. Follow the form for each service to customise your order down to revisions and next day delivery, then order. After purchase, upload your stems directly to your engineer or producer.

## Contents

1. [UX](#UX)
    - [Project Goals](###Project-goals)
    - [Target Audience Goals](###Target-Audience-Goals)
    - [Site Owner Goals](###Site-OwnerGoals)
    - [User Stories](###User-Stories)
    - [User Requirements and Expectations](###User-Requirements-and-Expectations)
        - [Requirements](####Requirements)
        - [Expectations](####Expectations)
2. [Design Choices](###Design-Choices)
    - [Fonts](###Fonts)
    - [Icons](###Icons)
    - [Icons](###Colours)
    - [Styling](###Styling)
    - [Images](###Images)
    - [Backgrounds](###Backgrounds)
3. [Planning](##Planning)
4. [Wireframes](##Wireframes)
    - [Website Layout](###Website-Layout)
    - [Account Creation Flowchart](###Account-Creation-Flowchart)
    - [Database Design](###Database-Design)
5. [Features](##Features)
    - [Existing Features](###Existing-Features)
    - [Features Left to Implement](###Features-Left-to-Implement)
6. [Technologies Used](##Technologies-Used)
7. [Planning + Testing](##Planning-+-Testing)
8. [Bugs](##Bugs)
9. [Deployment](##Deployment)
10. [Deploying to Heroku](##Deploying-to-Heroku)
11. [Deploy Locally](##Deploy-locally)
12. [Credits](##Credits)

## UX

### Project Goals

The Nullanion project's purpose is to offer multiple music services to customers that need high quality delivery on mix, master or additional production products. Customers will be able to create a bespoke order, pay their quote, communicate with their engingeer and upload / download high quality files. All in an easy to follow user journey and secure environment.

[Back to Top](##Contents)

### Target Audience Goals

- See reference material of previous work in all fields.
- Select a service from a list.
- Customise order and get real time updates on quote price with each change.
- Pay securely for services.
- Upload and download high quality files securely.
- Communicate with their engineer on edits / references / progress.
- Check on progress of product from a user portal.
- Navigate the website easily on any device size.

[Back to Top](##Contents)

### Site Owner Goals

- Create a safe and secure e-commerce site, that can generate revenue.
- Provide clear pricing and service descriptions.
- Demonstrate industry experience to users via a showcase/library area.
- Maintain account product history for optimising future experiences.
- Use work generated from sales as examples on the site.

[Back to Top](##Contents)

### User Stories

#### First-time user

1. As a first-time user, I want to quickly and easily navigate around the site to understand what this company does / can do for me without needing to give any credentials.
2. As a first-time user, I want to hear examples of work.
3. As a first-time user, I want to select a service and follow an easy to use form to customise my order.
4. As a first-time user, I want to see clear changes to quote price, and transparent pricing so as to not feel slighted on price.
5. As a first-time user, I want to make sure I create an account before I pay to ensure a relation between order and my account.
6. As a first-time user, I want to make sure that after I pay, I get a confirmation of payment.
7. As a first-time user, I want to make sure that after I have paid, my files can be uploaded securely.
8. As a first-time user, I want to have an instant and easy communication process with the engineer working on my material.

#### Returning Customer

1. As a returning customer, I want to be able to log in to an account to see the progress of my order.
2. As a returning customer, I want to be able to easily communicate with my engineer.
3. As a returning customer, I want to only share relevant personal details.
4. As a returning customer, I want to have my personal details in my account to be private.
5. As a returning customer, I want to take delivery of versions of my order easily.
6. As a returning customer, I want to be able to share notes and suggested edits on versions easliy with the engineer.

#### Browsing customer

1. As a browsing customer, I want to be able to look around the site without making an account.
2. As a browsing customer, I want to be able to check out the services freely and see how much things would cost without committing to a price.

#### Engineer (Super User)

1. As an engineer, I want to be able to receive an order in an understandable format.
2. As an engineer, I want to be able to access the user files to work on as soon as the order opens.
3. As an engineer, I want to see a clear deadline for an order.
4. As an engineer, I want to see reference text and links from the customer.
5. As an engineer, I want to know what format the customer is expecting their order to come back in.
6. As an engineer, I want to be able to communicate directly with the customer.
7. As an engineer, I want to be able to upload versions to the customer.
8. as an engineer, I want to be able to mark an order as completed/fulfilled.

[Back to Top](##Contents)

### User Requirements and Expectations

Audio art is an amazingly personal product and achieving the techincal requirements to present it publicly have grown more accessible than ever, however, some artists require more experienced technical engineers to get the best out of their creations. Luckily, these days, experienced engineers can be reached from all over the world.

Proving some experience and a legitiate web site to sell these services is the number one priority in creating long lasting customer relationships and quality services.

#### Requirements

- An easy to use design.
- Access to all features on all screensizes.
- Transparent pricing structure with visual representaition of quote amount.
- Safe purchasing of products.
- Feedback of purchase success / failure.
- Communicate with business.

#### Expectations

- The website will not store customers payment details in the database.
- The website will uphold the privacy and expected security of customer personal data.
- The website will be usable on any viewing screen.

[Back to Top](##Contents)

## Design Choices

There are three main form flows to the site. Styling was important - custom icons were designed by [Mikey Rosenfeldt](https://vimeo.com/michaelrosenfeldt). The main aim here was to not allow the site to appear too drearey. With a clear, off white flow design of wave forms.

[Back to Top](##Contents)

### Fonts

#### Title logo

![Nullanion title](static/images/nullanion-logo.svg)

The font for the title was a bespoke creation by [Mikey Rosenfeldt](https://vimeo.com/michaelrosenfeldt) and the complimenting font of [Raleway](https://fonts.google.com/specimen/Raleway?preview.text_type=custom) was used for other text across the site.

[Back to Top](##Contents)

### Icons

More bespoke creations made for the forms were the icons.

![single](static/icons/single.svg)
![ep](static/icons/ep.svg)
![album](static/icons/album.svg)

![mix](static/icons/mix.svg)
![master](static/icons/master.svg)
![productin](static/icons/production.svg)

![guitar](static/icons/guitar.svg)
![bass](static/icons/bass.svg)
![keys](static/icons/keys.svg)
![synth](static/icons/synth.svg)
![drums](static/icons/drums.svg)

[Back to Top](##Contents)

### Colours

The main colour pallete is between these two tones:
![Orange](static/wireframes/orange.png)
![Blue](static/wireframes/blue.png)

[Back to Top](##Contents)

### Styling

[Back to Top](##Contents)

### Images & Backgrounds

Images are mainly used as backgrounds to facilitate the flow of audio creation.

![background1](static/images/nullanion-background-01.jpg)
![background2](static/images/nullanion-background-02.jpg)

[Back to Top](##Contents)

## Wireframes

![LandingPage](static/wireframes/desktop-landing-page.png)

I used [Goodnotes](https://www.goodnotes.com/) to hand draw the wireframes and user flows before commiting anything to [balsamiq](https://balsamiq.com/) for digital recreation. This process always helps to iron out the things you dont think of before commiting to the code. Exporing the wireframes was easy using Balsamiq, and you can find them all here:

[Wireframes Folder](https://github.com/lornebb/NullAnIon/tree/master/static/wireframes)

[Back to Top](##Contents)

### Website Layout

[Back to Top](##Contents)

### Account Creation Flowchart

Account creation is different to anything I hav done before as users don't need an account unless they are purchasing. So the account creation has to be executed during the checkout process. I drew a user flow to help easily explain this. This was hand made with [Goodnotes](https://www.goodnotes.com/).

![User-Flow-Account-Creation](static/wireframes/user-flow-account-creation.jpg)

[Back to Top](##Contents)

### Returning Customer Account Flowchart

Returning customers that want to check up on an order, or share notes / feedback on a revision will need to use a log in / forgotpassword portal, that also has some defensive measures built in to only allow users to log in, and not create a new account. Also, a forgot password link will be available. This was hand made with [Goodnotes](https://www.goodnotes.com/).

![Returning-Customers-User-Flow](static/wireframes/user-flow-returning-customer.jpg)

[Back to Top](##Contents)

### Database Design

[Back to Top](##Contents)

## Features

### Existing Features

- Order a mix - allows users to create a bespoke order for a song / ep or album by following the form and submitting it to the checkout.

- Order a master - allows users to create a bespoke order for a song / ep or album by following the form and submitting it to the checkout.

- Order a Production - allows users to create a bespoke order for a song / ep or album by following the form and submitting it to checkout.

- Create profile by signing up and creating an account.

- Profile to see order progress and orders that have been purchased.

[Back to Top](##Contents)

### Features Left to Implement

- Option for multiple engineers to create some sort of 'engineer profile' to market themselves to their own clients / get their own work / get their own income stream.
- Extended artist profile of Nullanion back catalogue.
- More services offered - such as live event engineer services or on-location studio tracking.
- Collaboration portal.
- Other art types showcased / service offers - eg artwork, music video etc

[Back to Top](##Contents)

## Technologies Used

### Languages

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

- [JavaScript](https://www.w3schools.com/js/)

- [Python](https://www.python.org/)

- [JSON](https://www.json.org/json-en.html)

### Libraries / Frameworks

- [Django](https://www.djangoproject.com/)

- [Bulmer](https://bulma.io/)

- [jQuery](https://jquery.com/)

- [SQLite](https://sqlite.org/index.html)

- [Postgres](https://www.postgresql.org/)

### Tools

- [Git](https://git-scm.com/)

- [Heroku](https://www.heroku.com/)

- [PIP](https://pip.pypa.io/en/stable/installing/)

- [BOTO](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

[Back to Top](##Contents)

## Planning

Since a lot of the technologies I used in this project are brand new to me, planning in the intitial pahses were very important. Making sure that wireframes, user stories, user journies and expected outcome had their expectations managed, was my top priority.

I knew I wanted to make a website to provide a portal for musicans to purchase these services, so as long as that goal is met then I'd be happy.

A brand had to be created for the look and the intricicies of the service I wanted to provide had to be understood before any code was written.

After that, the info panels on the left needed to be created to ensure users knew where they were and what was going on.

## Testing

### Library

> As a first-time user, I want to quickly and easily navigate around the site to understand what this company does / can do for me without needing to give any credentials.

-also-

> As a first-time user, I want to hear examples of work.

- **Plan**

When a user visits the page, information is available to them to view and get an understanding of what is on offer, without having to share any personal details.

- **Implementation**

The landing page is clean and free of clutter, so when a user lands there, they are free to click around and discover what they need. the info panels on the left display what is on offer, and invite the user to visit the library page. Upon arival there, the user is presented with a list of songs that showcase the skills of Nullanion services, all without having to share any personal details.

- **Test**

1. Arrive to site:
    1. Arrive on landing page, view info panels on left.
    2. Click on 'Library'.
    3. View on list of songs.

2. It is also possible at this point to click through on songs to their spotify origins:
    1. Click on the artwork of the song.
    2. Ensure that the link follows to a spotify listing in a new tab.

- **Verdict**

The test works as planned and has therefore passed.

[Back to Top](##contents)

### Order a Mix, Master or Production

> As a first-time user, I want to select a service and follow an easy to use form to customise my order.

-also-

> As a first-time user, I want to see clear changes to quote price, and transparent pricing so as to not feel slighted on price.

- **Plan**

When a user visits their desired order form page, following the form in a logic manner will be the most logical route to completing an order.

- **Implementation**

Each form is created with bespoke icons to simplify the experience and streamline the user to a complete order. Hopfully inviting them to explore more interesting ways to ask for the service.

- **Test**

1. Select a service from the services dropdown in the nav bar:
    1. Arrive on desired form, ensure that layout is of suitable readablity with icons displayed for options for radio selectors.
    2. Fill out forms.
    3. Ensure that each required field is filled.
        1. If required field is not filled in, ensure that form can not be submitted.
        2. Ensure that the total price is displayed and can not be altered.
    4. Submit form.
    5. Sucessful submission will bring you to the checkout page.
        1. Ensure that order details that you just filled out have been carried onto the checkout page.
        2. Ensure that the price displayed on the form page, is reflected in the checkout total price order field.

- **Verdict**

The test works as planned and has therefore passed.

[Back to Top](##contents)

### Checkout and Paying

> As a first-time user, I want to make sure I create an account before I pay to ensure a relation between order and my account.

-also-

> As a first-time user, I want to make sure that after I pay, I get a confirmation of payment.

-also-

> As a first-time user, I want to make sure that after I have paid, my files can be uploaded securely.

-also-

> As a first-time user, I want to have an instant and easy communication process with the engineer working on my material.

- **Plan**

This is the crucial part of the experience, a safe and secure checkout and feedback about what happens next. This needs to be secure, easy to use and instant. The form should only be able to tbe completed by users signed in and registered with a validated email address - this makes sure that the verification, upload, and confirmation correspondance goes to the correct person.

- **Implimention**

Using python and strip in the design and model forms ensureing form validation the form should not submit without the required fields and a log in required. The file upload link will give the user direct access to a secure upload folder for their files.

- **Test**

1. After completeing a mix / master form, follow through to checkout page.
    1. At checkout page, try to complete order without entering any personal or financial details.
    2. If that is unsucessful, sign in or register.
        1. After sign in or register, ensure that you are redirected back to checkout page.
    3. Back at checkout page, ensure that your order form data is still as you ordered it.
    4. Ensure that a personal detail form is now present and that a card details field is visible.
        1. Try to checkout without filling any details in.
    5. Fill out yoru personal details.
        1. Try to complete order without financial details entered.
    6. Fill in your card details (4242 4242 4242 4242) and submit form.
    7. Ensure that you are presented with a completed order page, a link to your dropbox to upload your files to, and an email address for contact, including instructions with how to upload your files.
    8. Ensure that your inbox has an email with a greeting and the exact same details for file upload for files, from the same email address.

- **Verdict**

The test works as planned and has therefore passed.

[Back to Top](##contents)

----

## Bugs

[Back to Top](##Contents)

## Deployment

Nullanion was developed on VS Code code, using Git and GitHub for version control. the runnable version is hosted on Heroku with static and media files stored in an AWS S3 Bucket.

[Back to Top](##Contents)

## Deploying to Heroku

Firstly, create a Heroku account. Select start a new app and chose the location closest to you. Select and appropriate name and create. At this point you need to select POSTGRES from the resources tab, then move to the deploy tab. Connect your github account and select your repo for automatic deployment. For extra documentation on this you can read it [here](https://dashboard.heroku.com/).

Set up your config variables in the settings tab by selecting 'reveal config vars'. For this project change it to:

- SECRET_KEY
- DATABASE_URL
- EMAIL_HOST_PASSWORD
- EMAIL_HOST_USER
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY
- STRIPE_WH_SECRET

Notes on where these variables are found:

- (Your stripe secret keys are found in your stripe account on your dashboard.)
- (Email vars are found in your email provider.)
- (Database key is found in your Heroku account once you have set up your Postgres database.)

In order for these to all work together, a few setting will need to be configured in your Github repo and your requirements.txt file. First of all make sure to install DJ_database and psycopg2 with pip like this:

```cli
pip3 install dj_database_url
```

and

```cli
pip3 install pycopg2-binary
```

finally, to make sure heroku knows to install this in the environment (please do this every time there is a new installation):

```cli
pip3 freeze --local > requirements.txt
```

After this has been done, make sure to point your database settings in django to the new database like this:

```cli
‘default’: dj_database_url.parse(‘URL from Postgres – found in Heroku config var’)
```

At this point, you should update your new database with the local SQLite data with

```cli
python3 manage.py migrate (add the --plan flag first to make sure the right thing is happening)
```

## Running locally

For a local deployment you will need an IDE (I used VS Code, as mentioned above), and also PIP, Python3 (3.+) and Git.

Check your pip version with:

```cli
py -3 -m pip --version
```

check your python version with:

```cli
python -m .mvenv <path to your venv>
```

Download the repo above, take it as a .zip folder and extract the files into your chosen location and open in your IDE.

You will need to create a lightweight virtual environment for python with:

```cli
python -m venv <name of env>
```

and every time you open the project, to change to this env, use:

```cli
source <name of env>/bin/activate
```

at this point, the same as above, you will need to set up your env.py file, add it to the git ignore list to ensure it never ends up in version control, the same as above, but without the database url so django defaults to the SQLite3 database that comes with django.

- SECRET_KEY
- EMAIL_HOST_PASSWORD
- EMAIL_HOST_USER
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY
- STRIPE_WH_SECRET

All the variables above can be found in the same places. EMAIL_HOST_... from your email provider, STRIPE_... from your stripe account, and SECRET_KEY from django.settings.py.

Before starting the server, make sure to make migrations, check then, then migrate with this:

```cli
python3 manage.py makemigrations --dry-run
# check that the output is desired, if so:

python3 manage.py makemigrations
#check that this was executed sucessfully, then:

python3 manage.py migrate --plan
#check that the plan is as desired, if so:

python3 manage.py migrate
#check that this was completed successfully.
```

Now the database has been migrated properly, you can run the server and run the project locally with the command:

```cli
python3 manage.py runserver
```

Click on the link / copy and paste the port that has been opened in the CLI to open a browser tab with the project running in it.

[Back to Top](##Contents)

## Credits

- All icon, background and logo designed by [Mikey Rosenfeldt](https://vimeo.com/michaelrosenfeldt), on commission.

- My peers [Chris Palmer](https://github.com/cgpalmer) and [Fran DeBoo](https://github.com/fdeboo) for so much helpful knowledge and guidance.

- The ultimate thanks have to go to the excellent team at Tutor Support at Code Institute who helped me deep into the night with bugs and helping me figure out logic. Their help was invaluable to getting this project finished.

- [Simen Daehlin](https://github.com/Eventyret) who always goes above and boyond to help nme get my head around the bigger picture.

- The sticky footer in bulma fix code was inspired by [Philip Walton](https://philipwalton.github.io/solved-by-flexbox/demos/sticky-footer/)

[Back to Top](##Contents)
