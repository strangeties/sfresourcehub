# SF Resource Hub

## Background
Girls in Tech SF's 4th Annual Hacking for Humanity hackathon!

We had the opportunity to partner with local 
non-profit organizations to respond to the housing crisis 
in San Francisco, which is disproportionately affecting 
marginalized communities and has been further augmented by 
COVID-19.

The specific issue we chose to focus on was "how might 
non-profit organizations provide people with up-to-date 
information, so they can access essential services?".

Current information is of the essence (since being homeless 
is a full-time job where most people are traveling by foot), 
especially during the COVID-19 pandemic where regulations 
are in flux. 

So to tackle these issues, we built a mobile-friendly 
web application for any organizations (offering essential 
services) to easily post & update information to an interactive 
map. Users can find upcoming events/resources on this site 
in one centralized location. We focused on practicality, 
ease-of-maintenance, user accessible, and quality.

**SF Resource Hub Prototype**

<img src="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/197/361/datas/gallery.jpg">

## Project
#### Users:
- View all public pages and click on a resource they need
- Clicking on a resource will direct them to a page that provides all upcoming events/resources on that need (example: food, shelter, etc)
- Resource page includes a Google map with icons indicating the location of those resources. Icons are specific to that resource category.

#### Non-profits:
- Registration/login page to access their account
- Create, read, update, and delete resources

#### Future features:
- User log-in option to track favorites & send alerts
- Translations
- Calendar for easy scheduling
- Scheduled emails
- Social media to share 

## Usage:
This project was built with Python 3, Django, PostgreSQL, Google Maps API, Bootstrap, JavaScript, and HTML/CSS
- Make sure you have the latest versions of Python 3, Django, and PostgreSQL installed on your OS 

If you do not have Python3 installed, please make sure to follow the directions on 
<a href="https://www.python.org/downloads/" target="_blank">python.org/download</a> to install it.

#### **Clone the repository using the command line**
- Click on the green **Code** button
- To clone the repository using HTTPS, under "Clone with HTTPS", click the clipboard.
- Open Terminal
- Change the current working directory to the location where you want the cloned directory
- Type git clone and then paste the URL you copied earlier

```
git clone https://github.com/rashmika13/sfresourcehub.git
```
Press Enter to create your local clone

#### **Run the program**
Once you have cloned the repository to your local machine, **cd** into the 
sfresourcehub root directory and run the program.
```
python3 manage.py runserver
```