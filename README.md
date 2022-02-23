# __I THINK THEREFORE I BLOG WALTHROUGH DJANGO PROJECT__

#### __pakages to be installed__
 - pip3 install Django==3.2 gunicorn
 - pip3 install dj_database_url psycopg2
 - pip3 install dj3-cloudinary-storage
 - pip3 freeze -- local > requirements.txt
 - django-admin startproject codestar .  this is the code to create the new django project
 - python3 manage.py startapp blog
 - python3 manage.py migrate   this migrates all our changes to the DB

 - python3 manage.py runserver    this is the code to run the file


## __ THE DEVELOPMENT PLAN__
    - We're now ready to start  coding out our Django blog. 
        Now our development plan is that we're going  to install all of the libraries that we need  
        straight away, and deploy to Heroku early on.  
        That way, it saves us time later and we know  that our project is working straight away.
        Now remember that we said earlier we want to use  Heroku’s PostgreSQL add-on to store our data,  
        and Cloudinary to store our images. So we're going  to get all of that working right at the start.
        You may be wondering why we don’t just store  images on Heroku? Why do we need a separate hosting provider?
        This is because Heroku has  what’s known as an “ephemeral file system”.
        When you create a Heroku app it provisions  what's known as a dyno. And this is effectively  
        like a small container to run your project  in. When your project has been idle and no  
        one has accessed it for a while, then  the dyno stops to conserve resources.  
        When that happens, any files that have been  uploaded since the project was created are lost. 
        So we don't want visitors to our site  to end up seeing broken image links. 
        Therefore, we're going to upload  them to a persistent file store,  
        which is where Cloudinary comes in. Now we could have chosen to use another  
        provider such as Microsoft Azure or Amazon  S3, but these are more complicated to set up.  
        If you go on to study e-commerce with us, then  you'll learn how to upload images to Amazon S3.
        But for everything we want to do in this  project, Cloudinary is a perfectly good solution.
        So our first tasks for creating  a basic Django project will be: 
        Firstly, installing Django  and the supporting libraries. 
        Secondly, we'll create a  new Django project and app. 
        Third, we'll set the project to  use Cloudinary and PostgreSQL.
        And then fourth, we'll deploy  our empty project to Heroku.
        I suggest following this process  for all of your projects, it'll  
        it'll save you from having nasty surprises later on. We've put all of these steps together in a cheat  
        sheet that's linked below the video. So that you  can use it for your projects going on from here.  
        So now that we know our steps, in our  next video we'll perform the first two.
        Installing Django and then  creating our new empty project.

# __Creating The Empty Django Project__
__Important!__
Terminal command update
Since this video was created Django have introduced a new version that will be automatically installed if you use the command in the video.

To ensure that you get the same version of django and gunicorn used in this video and so that nothing breaks as you do the walkthrough, instead of the command pip3 install django gunicorn, please use this:

pip3 install Django==3.2 gunicorn

Django 3.2 is the LTS (Long Term Support) version of Django and is therefore preferable to use over the newest Django 4

    - In our previous video, we outlined the steps we needed to get our project deployed early.
        Now, we'll do the first two steps which are
        installing Django and all the supporting libraries and creating a new blank Django project.

    - Okay, so in a new workspace based on our Github repo we want to install Django and
        the server we use to run it on Heroku so type: 'pip3 install Django==3.2 gunicorn'
        And gunicorn is the server that we're going to use to run Django on Heroku.
        Now I'm just going to clear the terminal here between each step
        because it makes it a little bit easier to read.

    - So now let's install the supporting libraries. First the library is needed for PostgreSQL
        which is: "dj_database_url" and another library called "pyscopg2".

    - Once all of those are installed, then we can install the libraries that we need to run Cloundinary.
        So I'll just clear the terminal again just to make it easier for you to see what's going on.
        And we'll type "pip3 install dj3-cloudinary-storage".
        Now after this there will be one or two more libraries that we'll need to install,
        but this will get the bare bones of our application working.
        So that's all of the libraries that we need to have installed for now,
        I'll just clear the terminal window one more time.

    - And then we're going to create our requirements.txt file. Now, if you
        can remember how to do that feel free to pause the video and create it for yourself.
        If not, don't worry just come back after the pause and I'll show you how to do it.
        So what we're going to do is type "pip3 freeze -- local > requirements.txt"
        and then we're going to redirect that to the requirements.txt file.

    - Test time again, can you remember from our earlier videos the command to create a new Django project?
        We want to call our project codestar because that will be the name of our blog.
        If you can remember the command, pause the video type it in the terminal now.
        If not, hang tight and I'll show you after the pause.
        So the command is "django-admin startproject codestar ."
        That dot on the end tells Django admin that we want to create our project in the current
        directory, now when we run that command we can see that it's created a manage.py file and a directory
        called codestar. If we look inside that directory we can see our default settings and URL files.

    - So the next thing we'll do is create our blog app. Now again, if you can remember
        the command to do it, pause the video, type it in. If you can't remember, don't panic,
        I'll show you straight after the pause. So the name of our app as we said will be blog.
        So this time we need to use the manage.py file so it's,
        "python3 manage.py startapp blog"

    - So now that our blog app is created we need to add it to the list of installed apps in
        our settings.py file. So navigate back to the codestar directory and open the settings.py file,
        and in the installed app section we want to add in
        our newly created blog app so we'll just scroll down to our installed apps here.
        On the end there, we'll put blog and we'll also put a comma.
        Now my preference normally is to use double quotes around strings.
        Django seems to prefer single, so I'll try to remember that as we write this project together.

    - Okay now that we've added that, let's save the file
        and then we can go back to the terminal and we need to migrate the changes to the database.
        Whenever we add a new app or anything like that migrations are automatically created. So if you
        can remember the command to migrate the changes to the database pause the video go ahead and type it.
        So the command is: python3 manage.py migrate
        This will add all of the changes to our new database.
        
    - Now, when we run our project using
        "python3 manage.py runserver" and open it up in our browser.
        Then, what we should see is that the basic skeleton project is now up and running.
        So open the browser...
        And we can see that we have success.

In this video, then, we got our libraries installed and our basic project up and running.
In the next video, we'll link it to our Heroku database and do our first deployment.























































































