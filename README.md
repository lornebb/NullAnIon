# Nullanion

Nullanion offers music services for those that need quality, delivered on time.

At Nullanion, one can order a mix or master of a song, EP or full length LP (Album). Other services include Ad. Production, Soundtrack and Sound Design. Follow the form for each service to customise your order down to bit-rate and next day delivery, then add it to your basket. After purchase, use your account to upload your stems and have direct one to one conversations with your engineer/producer regarding your order and delivery estimations.

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
    - [Content](###Content)
    - [Media](###Media)
    - [Acknowledgements](###Acknowledgements)

## UX

### Project Goals

The Nullanion project's purpose is to offer multiple music services to customers that need high quality delivery on mix, master, additional production, soundtrack and sound design products. Customers will be able to create a bespoke order, pay their quote, communicate directly with their engingeer and upload / download high quality files. All in an easy to follow user journey and secure environment.

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
- Demonstrate industry experience to users via a showcase area.
- Maintain account product history for optimising future experiences.
- Use work generated from sales as examples on the site.

[Back to Top](##Contents)

### User Stories

#### First-time user

1. As a first-time user, I want to quickly and easily nagivate around the site to understand what this company does / can do for me.
2. As a first-time user, I want to hear examples of work.
3. As a first-time user, I want to select a service and follow an easy to use form to customise my order.
4. As a first-time user, I want to see clear chanegs to quote price, and transparant pricing so as to not feel slighted on price.
5. As a first-time user, I want to make sure I create an account before I pay to ensure a relation between order and my account.
6. As a first-time user, I want to make sure that after I pay, I get a confirmation of payment.
7. As a first-time user, I want to make sure that after I have paid, my files can be uploaded securely.
8. As a first-time user, I want to have an easy communication process with the engineer working on my material.

#### Returning Customer

1. As a returning customer, I want to be able to log in to an account to see the progress of my order.
2. As a returning customer, I want to be able to easily communicate with my engineer.
3. As a returning customer, I want to only share relevant personal details.
4. As a returning customer, I want to have my personal details in my account to be private.
5. As a returning customer, I want to take delivery of versions of my order easily.
6. As a returning customer, I want to be able to share notes and suggested edits on versions easliy with the engineer.

#### Browsing customer

1. As a browsing customer, I want to be able to look around the site without making an account.
2. As a browsing customer, I want to be able to check out the services freely and see how much things would cost withotu commiting to a price.

#### Engineer (Super User)

1. As an engineer, I want to be able to recieve an order in an understandable format.
2. As an engineer, I want to be able to access the user files to work on as soon as the order opens.
3. As an engineer, I want to see a clear deadline for an order.
4. As an engineer, I want to see reference text and links from the customer.
5. As an engineer, I want to know what format the cusomter is expecting their order to come back in.
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

lots of forms and form flows, so styling these was important to not have the site appear to dreaery. littered with icons and big button.

[Back to Top](##Contents)

### Fonts

[Back to Top](##Contents)

### Icons

[Back to Top](##Contents)

### Colours

[Back to Top](##Contents)

### Styling

[Back to Top](##Contents)

### Images

[Back to Top](##Contents)

### Backgrounds

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

- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

[Back to Top](##Contents)

### Features Left to Implement

- Option for multiple engineers to create some sort of 'engineer profile' to market themselves to their own clients / get their own work / get their own income stream.
- Extended artist profile of Nullanion back catalogue.
- More services offered - such as live event engineer services or on-location studio tracking.
- Collaboration portal.
- Other art types showcased / service offers - eg artwork, music video etc

[Back to Top](##Contents)

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
  - The project uses **JQuery** to simplify DOM manipulation.

[Back to Top](##Contents)

## Planning + Testing

Since a lot of the technologies I used in this project are brand new to me, planning in the intitial pahses were very important. Making sure that wireframes, user stories, user journies and expected outcome had their expectations managed, was my top priority.

I knew I wanted to make a website to provide a portal for musicans to purchase these services, so as long as that goal is met then I'd be happy.

A brand had to be created for the look and the intricicies of the service I wanted to provide had to be understood before any code was written.


----
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

[Back to Top](##Contents)

## Bugs

[Back to Top](##Contents)

## Deployment

[Back to Top](##Contents)

## Deploying to Heroku

[Back to Top](##Contents)

## Deploy locally

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

[Back to Top](##Contents)

## Credits

[Back to Top](##Contents)

### Content

- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

[Back to Top](##Contents)

### Media

- The photos used in this site were obtained from ...

[Back to Top](##Contents)

### Acknowledgements

- I received inspiration for this project from X.

[Back to Top](##Contents)
