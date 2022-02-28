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

# __Our First Deployment - part 1__
Important!
Error fix
If you get the error below during the steps to deployment:

django.db.utils.OperationalError: FATAL: role "somerandomletters" does not exist

Please run the following command in the terminal to fix it:

unset PGHOSTADDR

In our previous video, we got our skeleton project  up and running locally. Now, we want to prepare it  
        for deployment to Heroku. In this video, we’re into the third step of our new project checklist.
        Which is setting the project up to use Cloudinary and PostgreSQL.
        But, there are another four steps  involved when deploying an app to Heroku.

Firstly, create the Heroku app. 

Secondly, attach the database.

Thirdly, prepare our environment and settings.py file.

And then fourthly, get our static and media files stored on Cloudinary,
        which we’ll go into  in more detail in the next video.

    - First things first, let’s create a new app  on Heroku. By just clicking on the New button  
        on the Heroku Dashboard and then on “Create  New App”. Give your app a name, and then choose  
        the location nearest to you. I’m going to call  this codestar2021 and choose Europe as my location.

    - Now that my app is provisioned,  I can just click on the Resources tab  
        and then add a database. All we need to do in the addons box is just search for Postgres then we can add Heroku 
        Postgres to our project.
        Now that our database is added we can go back to our Settings tab.
        And click on Reveal Config Vars.
        And this will give us our DATABASE_URL, this is the connection to our Postgres database.
        So just click in the box, copy the string and we'll add this to our project.
        So that’s it for Heroku for now,  let's go back to our code.

    - And what we're just going to do, in the same directory as our manage.py file, we're going to create a file called env.py.  
        We’re going to use this to store our secret environment  variables while we're in development.
        We don’t want these to be publicly visible in GitHub, so we’re just going too use this here.
        If you're using our student template, then the env.py  is already in the .gitignore file.
        If you're not, make sure you add it.

        So in our env.py file, let's  import the operating system library, os.
        And then, we’ll use it to set a couple of  environment variables. So first, we're going to set one called DATABASE_URL.
        And then we can paste in the URL that we just copied from Heroku.
        Notice that the name DATABASE_URL matches the name of our environment variable on Heroku.
        While we’re here, let’s add in our secret key. Every Django project has a secret key,  
        which it uses to encrypt session cookies.  We obviously don’t want this to be visible  
        on GitHub either - in fact, you might get a  warning from GitHub emailed to you if you do.
        So let's add a new one here "os.environ", and then in the square brackets
        "SECRET_KEY = "
        Now your secret key can be whatever you  like. So, for me, I’m going to put: 
        "randomSecretKey1881x!" and then some numbers and characters.
        Save this file, and then copy the value that we've given to SECRET_KEY here.  

        And we're going to add this to our config vars  on Heroku too.
        So, back at the dashboard, enter config vars, let's type SECRET_KEY paste in our value, and then click add.

    - So now that our env.py file is created, we need  to reference that in our settings.py file.
        So let's just do a few imports. Back at the top of our settings.py file.
        Just under the first import there.
        Let's import os again.
        And then we're going to "import dj_database_url "
        So our Database URL library, we'll come to that in a minute.
        And then, we're going to put in an if statement.
        if os.path.isfile("env.py"): import env
        Now our env.py file won’t exist in production since  it’s automatically in the .gitignore file.  
        We don’t want our application  throwing an error if it can’t find it,  
        so this little conditional  import prevents this error.

        Now, in our secret key  section a little further down,  
        remove the insecure key and add  in our environment variable:
        os.environ.get('SECRET_KEY')

        Now that that's done, let’s wire up our Postgres Database. This is where our Database URL library  
        comes in - and the DATABASE_URL  environment variable that we set.
        So scroll down in your settings.py file  for the DATABASES section.  
        And you'll see that midway down, just highlight all of it.
        And then, comment out the entire section. 
        Press control forward slash on a PC or command forward slash on a Mac to do that.
        Now we'll add a new section. So "DATABASES = ".
        This will be a Python dictionary. The key will be default.
        And the value for this will be "dj_database_url.parse"
        And then inside the brackets we're going to get our database url environment variable,
        that's set in our env.py file and also in Heroku in our config vars.

        And that's it! We’re now using our Heroku database as the  backend. Don’t believe me? Well, try it for yourself.
        Go to the terminal window and  perform the migration again.  
        You remember the migrate command from the  previous videos? Well, pause the video and run it again.
        And we can see when we do that, all of the migrations happen. That's because they're happening on our new database. 
        Still don’t believe me? Well, let’s go back  to the Heroku Dashboard. Click on Resources,  
        and then click on the Heroku Postgres link, which  will pop out into a new window. What do you see?
        Well we see that 48 rows and 10 tables have been  created, so our database link is working.
        Now at the beginning, we said there were  4 steps to getting our app deployed  
        before we started building  the actual functionality.
        To create the Heroku app, attach the database,
        prepare our environment and settings.py file 
        And then, get our  static and media files stored on Cloudinary.   
        We've done the first three of these. So in our next video, we're going to get our static and media files stored on Cloudinary.
        and then we’re ready to deploy.  We’ll do that in the next video.  
        In the meantime, feel free to add,  commit and push your project to GitHub.

# Our First Deployment - part 2
In our previous video, we  outlined the four steps to  
        getting our skeleton project deployed to Heroku.
        Firstly, create the Heroku app. Secondly, attach the database. 
        Thirdly, prepare our environment  and settings.py files. 
        And then, finally, get our static  and media files start on Cloudinary.
        We've completed the first three steps and in  this video we'll create our Cloudinary account,  
        link our project and try deployment.

So firstly, let's create a Cloudinary account. It's completely free, no credit card is required. 
        And we've put the steps to do this below the video  

    - when you get to your dashboard which  contains your API authentication information.
        Just click on the copy to clipboard  link next to API environment variable  
        we'll use this to connect our app to Cloudinary. Now we can go back to our ide and in our env.py  
        file, we'll add another line at the bottom. "os.environ" 
        We'll set the CLOUDINARY_URL, and then we  can paste in the value that we just copied.  
        It's not quite right though, we need to remove  "CLOUDINARY_URL =" from the beginning,  
        and then we'll copy this value again, so  that we can paste it into Heroku as well.
        So back to our Heroku dashboard we'll add a new  config variable the same name CLOUDINARY_URL.  
        And we'll paste in the value that we just  copied. Now we also just need to add in  
        one more temporary environment variable  too, which is "disable_collect static".
        And we'll set that to one this is just to get  our skeleton project deploying because we don't  
        actually have any static files yet, we'll remove  this when it comes to deploying our full project.
        Okay, so back in our settings.py file, let's  go to the installed apps section and add in the  
        Cloudinary libraries that we installed before.  So "cloudinary_storage" and this needs to go  
        just above "django.contrib.staticfiles" and then  the regular Cloudinary library can go underneath.
        Now we just need to tell Django to use  Cloudinary to store our media and static files  
        so down near the end of our settings.py  file we can add these few lines.
        First of all, "STATICFILES_STORAGE" and in here we can tell it to use,
        "Cloudinary_storage.storage.StaticHashedCloudinaryStorage",
        so this is coming from the  library that we installed above,
        and put into our installed apps section.
        We also need to set our static files directories,  
        this is going to be a list but it's only going  to contain one item which is "os.path.join"  
        our base directory which is defined  at the top of our settings py file,  
        and we're going to connect that to static and  we'll create our static directory in a moment.
        Then we're just going to set static route, now  
        we don't use that in this project but  it's good practice to set it anyway.
        So "os.path.join" base dir static files. We can do very similar now for the media.  
        Now our media is pictures, things like that, our  static files will be our CSS and our JavaScript.
        So again, we'll set a media URL and  we'll set the default file storage to  
        "Cloudinary_storage.storage.MediaCloudinaryStorage".
        And believe it or not that's all that's  needed to link our app to Cloudinary,  
        it's actually very simple.
        Now we also need to tell Django  where our templates will be stored.  
        So back up to the top of settings.py and under the  base directory let's add in a templates directory.
        "TEMPLATES_DIR =  os.path.join(BASE_DIR, 'templates')"
        And now we just need to scroll down midway in  our settings.py file and change the D-I-R-S key,  
        the dirs key, in our template setting to point  towards our new templates directory variable.
        Okay, we're almost ready  to do our first deployment. 
        But before we do, we need to add our Heroku host  name into allowed hosts in our settings.py file,  
        and this is your Heroku app  name followed by herokuapp.com.
        So in my case, 'codestar2021.herokuapp.com'  
        and we'll add in localhost too,  so that we can run it locally.
        Now we can just create our three  directories that we mentioned earlier.  
        So we're going to create these at the top level,  
        and the directories that we need are going to be  our media, our static and our template folders.
        And we create these on the top  level next to our manage.py file.
        Now there's just one thing missing  before we can perform our deployment. 
        Think back to what you learned  in the Hello Django lessons,  
        can you think what it might be? We'll pause  the video for a second and then come back.
        That's right, we need to create a procfile.
        Remember that Heroku needs a procfile  so that it knows how to run our project.
        So we're going to create one here. Remember the capital P on Procfile. 
        Now procfile is short for process file. So  the first part, web, tells Heroku that this  
        is a process that should accept http traffic. The next part is Gunicon which is the server  
        that we installed earlier, a web services gateway  interface server, wsgi or whiskey for short.  
        And this is a standard that allows Python  services to integrate with web servers.
        Now that's all done let's try  deployment so we'll save our files,  
        add commit and push to our repository.
        And we're going to use Github  as our deployment method here.  
        So let's go back to our Heroku dashboard  and we can click on the deploy tab.
        And we'll click on Github  here for deployment method,  
        you might need to connect your Github  account, mine is already connected.  
        And then search for your blog repo,  mine is just called Django blog.
        I have two here so it's the second one that  I need. Okay, and then all we need to do is  
        scroll down to the bottom of the page and  click on deploy branch. And I like to watch  
        the deployment happening in the build log too,  so we'll pop that out. Now your build log might  
        look a little bit different to mine but as  long as it deploys that's absolutely fine.
        Okay, so it says that our app  has been deployed successfully.
        So let's click on open app to view it and we  can see that it's been deployed successfully.
        Now this might seem like an awful lot of  effort to get a minimal application deployed  
        but there are a couple of very  good reasons why we've done this.
        Firstly, we have a solid platform to build on,  
        all of our main development dependencies are  installed and we know that they're working.
        And secondly, a big mistake  that many students often make  
        is thinking that deploying to Heroku is  as quick as deploying to Github pages. 
        As a result, they often leave it to the  last minute which results in a lot of panic.  
        Early deployment saves a huge amount of stress  later on. Now though, we're ready to actually  
        start writing some code and getting our blog app  off the ground, we'll do that in our next video.



















































































