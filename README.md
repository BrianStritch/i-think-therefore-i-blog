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

 after creating database models you can make your migrations
 - python3 manage.py makemigrations
 then 
 - python3 manage.py migrate


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
        we'll use this to connect our app to Cloudinary. 
        
    - Now we can go back to our ide and in our env.py  
        file, we'll add another line at the bottom. "os.environ" 
        We'll set the CLOUDINARY_URL, and then we  can paste in the value that we just copied.  
        It's not quite right though, we need to remove  "CLOUDINARY_URL =" from the beginning,  
        and then we'll copy this value again, so  that we can paste it into Heroku as well.

    - So back to our Heroku dashboard we'll add a new  config variable the same name CLOUDINARY_URL.  
        And we'll paste in the value that we just  copied. 
    
    - Now we also just need to add in one more temporary environment variable  too, which is "disable_collect static".
        And we'll set that to one this is just to get  our skeleton project deploying because we don't  
        actually have any static files yet, we'll remove  this when it comes to deploying our full project.

    - Okay, so back in our settings.py file, let's  go to the installed apps section and add in the  
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

    - Now we also need to tell Django  where our templates will be stored.  
        So back up to the top of settings.py and under the  base directory let's add in a templates directory.
        "TEMPLATES_DIR =  os.path.join(BASE_DIR, 'templates')"
        And now we just need to scroll down midway in  our settings.py file and change the D-I-R-S key,  
        the dirs key, in our template setting to point  towards our new templates directory variable.
        Okay, we're almost ready  to do our first deployment. 
        But before we do, we need to add our Heroku host  name into allowed hosts in our settings.py file,  
        and this is your Heroku app  name followed by herokuapp.com.
        So in my case, 'codestar2021.herokuapp.com'  
        and we'll add in localhost too,  so that we can run it locally.

    - Now we can just create our three  directories that we mentioned earlier.  
        So we're going to create these at the top level,  
        and the directories that we need are going to be  our media, our static and our template folders.
        And we create these on the top  level next to our manage.py file.

    - Now there's just one thing missing  before we can perform our deployment. 
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

    - And we're going to use Github  as our deployment method here.  
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

# __Creating Our Database Diagram__
Now that our skeleton project is successfully  deployed, we can have a think about our database models.
Remember how Django works - it is  a MVT or Model, View, Template framework. 

The model is our database and structure, the  templates are the HTML pages that our user sees,  
and the views are the glue that holds  the two of them together - the logic  
in our code that reads from or updates the  model and then updates what the user sees.

    - In this video, we’re concerned with the model.  So how can we define a database model for our blog posts?
        First, let’s move three of our  User Stories to In Progress. We’re going to  
        deal with the admin side first, so we'll move  the ability to create and manage posts, the  
        ability to create a draft post, and the comment  approval function into our in progress column. 
        And we're away!
        Before creating our database models, let's just take a look at a sample post and see what we can get from it.
        First, as you can see we  have a title. Then an author  
        an updated date, we have our main content and the  number of likes. What kinds of fields are these?  
        Well let's create an entity relationship diagram  so that we can understand our database structure.
        Title is easy it's a character field,  which will have a length of 200 characters  
        which is ample for a title  and it needs to be unique.
        We don't want to have multiple  blog posts with the same title.
        What about our author? Well, this is going  to get the author's name from our built-in  
        user table. So what kind of field do you think  it should be? Pick from the following list and  
        then see if you are right. You can pause  the video if you want to think about it.
        Is it a many-to-one relationship, a one-to-many  relationship or a many-to-many relationship?
        What did you come up with? 
        Well the correct answer is that  it's a one-to-many relationship. 
        Why is that? Well one author may write many  blog posts. In Django terminology a one to  
        many field is called a foreign key field. So  that will be our field type for the author.
        Our date field then can be automatically  generated. And we'll actually add two - one  
        for when the post was created and another for  when it was updated. Our blog post content is a  
        standard Django text field, which is designed  for storing large amounts of text data.  
        We'll also add our featured image and an  excerpt field which we'll use on the index page.
        We also have our likes field. Now this is  another field that needs to be in a relationship.  
        Pause the video again and see if you can pick what  kind of relationship it should be from the list.  
        Again, is it many-to-one,  one-to-many or many-to-many?
        Well how did you get on? The correct answer is many-to-many. 
        Why do we say that? 
        Well the reason is that many  users can like many blog posts,  
        at least we hope that's what will happen. So we'll use a many-to-many field here.
        There are actually two more fields that  we need to add that aren't visible here.
        One is the "slug" field. Django is  betraying its roots in the publishing  
        industry here, because a slug in type  setting is an incidental line of type. 
        In Django, a slug is a label that  can be used as a part of a URL. 
        So we'll auto-generate a slug from the  title to use as our URL for each post,  
        and again this needs to be unique.
        Finally, we have a status field that says  whether the post is draft or published. 
        And that's our relationship diagram complete. 
        In our next video, we'll start building  this into a usable Django model.

# __Creating Our Database Models__
In our previous video, we  created our database diagram.
Now, we'll convert that  into a proper Django model. 
We'll keep the diagram on the screen  as a reference while we code it out.

    - So let's start building our models.py file now. So we'll go to blog, open up our models.py file,  
        and first of all we want to import the user model. So underneath the first import, we'll add 
        "from Django.contrib.auth.models import User". Then we want to import our Cloudinary field  
        for the featured image, so we'll  do that from Cloudinary models.
        Then we'll create a tuple for  our status which is going to  
        be a zero or a one for whether  the post is draft or published. 
        So "STATUS = " zero as draft and  then we'll have one as published.
        Okay, so now that that's in there let's take our  E-R-D and convert this into a usable Django model.
        So the first thing that we'll  do then, is create our class  
        which is going to be the class of Post. And  that's going to inherit from our standard model. 
        So let's do the title we said that  this was going to be a character field,  
        it's going to have the max length of 200  characters, and it needs to be unique.
        We'll do the slug next because that comes  straight under the title and that's going  
        to be again - models, this is a slug field, it's  a special type of field that Django has for slugs.
        Again, max lens 200 which will be  ample and it needs to be unique.  
        Next, we'll do our author and remember that  we said that this needed to be a foreign key  
        relationship, it's a one-to-many  relationship from our user model.
        So that will be based on our user model,  we'll have on delete "models.cascade"  
        and we'll set a related name  which is going to be blog post.
        Then we'll do our updated on date. This is just  going to be a simple Django model date time field.
        And it will automatically default  to the current date and time. 
        Our content is as we said a standard text field.
        Then our featured image is  going to be a Cloudinary field.
        We give it a type, which is image. And we'll  also set a placeholder here which is just  
        going to be set to placeholder, we'll come  to that when we get into doing our templates.
        The excerpt which will be  visible on our index page  
        is just going to be a standard text field again.
        We'll allow it to be blank.
        Then our "created_on". Again, this will  just be a standard date time field.
        And that will automatically default to  the current time when it's been created.
        And then we'll do our status. Which is going to  be an integer field because it can be zero or one.  
        The choices are going to be our  status that we created above  
        and the default is going to be  zero so the default will be draft.
        And then finally we have our likes. Which as we  said is a many-to-many field, this is also going  
        to pull from our user. Related name is going  to be blog likes and it can also be blank.
        Now you might be wondering here what on earth is this "on_delete=models.CASCADE" that we have in our foreign key?
        Well it simply means that if the one record  
        in our one-to-many relationship is deleted,  then the related records will be deleted too.
        In other words, if we delete our user  we'll also delete their blog posts.
        Now we'll just add a couple of extra methods  to our model which can be viewed as helpers.  
        We're going to add the meta class, you can check  the Django documentation for all of these options  
        but the ones that I've used most often are to  do here with ordering, indexing and constraints.
        In this instance, we're going to order  our posts on the created_on field,  
        now the minus sign means to use descending order.
        Then we're going to use this string method  here, it's good practice to put that into your projects.
        The Django documentation says it's a  magic method that returns a string representation  
        of an object and it says you should define  it because the default isn't helpful at all.
        Finally, we have a helper method to return  the total number of likes on a post.

    - Now that our post model is complete  let's add our comment model.
        Remember that these models can be  likened to tables in the database,  
        so we have a separate table  for posts and one for comments.
        In reality Django will automatically  create some extra helper tables for us  
        to manage our foreign key relationships though.
        So now it's time to create the comment  model, and you probably know what's coming.
        Take a look at the diagram for yourself  and then see if you can create the model. 
        Pause the video, it should take you  about 10 minutes and see how you do.
        How did you get on?
        Our comment model contains very few surprises. 
        The post field is a one-to-many relationship  because one post can have many comments.
        And we have an approved field, which defaults  to false. The others are all fairly standard.  
        As you can see, I've added the helpers  too. This time we've ordered by created_on  
        in ascending order, so the oldest  comments will be listed first  
        which makes sense since we  want this to be a conversation.

    - So that's our models created, we can now save  our file and go down to the terminal window  
        because we need to migrate  these changes into our database.
        So you remember the commands how to do this:
        it's "python3 manage.py makemigrations".

        And then we can type "python3 manage.py migrate".

In this video, then we've seen how to go from  a diagram to fully functioning database models.  
We've built models for our posts and our comments  
which are two custom models that  we're going to use in this project.
Finally, we migrated those changes to the database.  Every time you change the model or you need to  
create a new one you'll need to run the make  migrations and the migrate commands again.
In our next video, we'll build  the admin panel so that we can  
create new posts and manage comments and users.

__NOTE__

        If you're concerned that you may have made a typing error, then you can do a dry run of your migrations before you apply them to your database. The command to do this is:

        python3 manage.py makemigrations --dry-run

        This will print out the migrations, so you can check that everything is correct before proceeding.

# __--------------  MAKE SURE YOU CHECK SPELLINGS BEFORE MIGRATING  ------------__

# __Building The Admin Site - part 1__
WHAT IS IT?    -----    The Django admin panel 
WHAT DOES IT DO?   ----  Allows a superuser to administer the site 
HOW DO YOU USE IT?  ----  Log in to the /admin URL with a superuser account

A blog is not much use unless we  have a way to write posts.
Happily, Django comes with a built-in admin  panel that we can use for this purpose.
In this video, we’re going to set up our  admin panel to interact with our Posts  
and Comments models. 

    - We’ll start,  though, by creating a superuser.
        Creating a super user sounds much more exciting  than it actually is. All we're doing is creating  
        a supervisor or administrator user who can  log into Django's built-in admin panel.
        From the terminal window then type:
        "python3 manage.py createsuperuser"

    - Now you'll be prompted for a  username, which can be anything. 
        I'm going to just use admin, an email address  which doesn't need to be real, and a password.  
        And when you type this password it won't be  echoed back to the screen, so you won't be able  
        to see what you're typing. Once we've confirmed  the password then, our superuser is created. 

    - So let's test it we'll run our project  and open it up in a browser window. 
        So "python3 manage.py run server". So we'll open that in a browser window.
        And then add /admin to the end of the URL.
        We'll get our login panel here and  we can type in the credentials that  
        we just created and this will allow us to log in.
        Now at the moment - there's  not much. There's no way to  
        create a blog post and there's  no way to moderate the comments.

    - So let's add the post model to our admin panel. 
        This is very very simple all we need to do  is open up the admin.py file in our editor.
        And then at the top we just import our post model. So "from .models import Post" with a capital p,  
        just delete that and then we can just  type "admin.site.register(Post)".

    - Let's save that and then go back  to our admin panel once again. 
        And when we refresh the page,
        we can see that we now have  the option of adding posts. 
        When I click on that, we can see that  we currently don't have any blog posts  
        but I can click add post here in the corner.
        And now we can see that we have  everything we need to add a blog post.
        But there are a few more  things that we can tweak here. 

    - The first thing is that we want  to use a WYSIWYG or "what you  
        see is what you get" editor for the post.
        We're going to use a handy  library called Summernote. 
        I've put a link to the Summernote  project below the video,  
        so you can read the documentation if  you wish so let's go back to our editor.
        Go to the terminal window we'll just stop the  server clear it and we'll install it by typing:
        -------------     "pip3 install django-summernote"    -----------------

    - Now when this is installed, we'll need  to add this to our requirements.txt file,  
        so that it'll be installed automatically  when we deploy again to Heroku. I know you  
        can remember how to do this, so I'm going to let  you pause the video and do it before continuing. 
        ------------      "pip3 freeze -- local > requirements.txt"  --------------

    - Now that's done, we need to add SummerNote  to our list of installed apps in settings.py.
        Now you can put this wherever you like,  
        but I like to leave user created apps  until the end of the installed app setting.
        So I'm just going to install it here before blog  
        so it's 'django_summernote'. I know  that we installed it with a hyphen  
        and it has an underscore now but that's  often the way with Django libraries.

    - Now let’s set up Summernote’s URLs in our urls.py  file. In our import here 'from django.urls'  
        just add on comma "include" and the "include"  method allows us to include URLs from other files.
        So then we can add our path. So it's going to be
        "path('summernote/',  include('django_summernote.urls')),"

        And that will register our Summernote urls here  with our urls.py file. 
        
    - Now all we need to do is tell our admin panel which field  we want to use Summernote for.
        So basically we're going to  say that our content field  
        which is stored as a text field in the  database is going to be a Summernote field. 
        And this little piece of code in  our admin.py file will add it.
        So we're just going to say:
        "from django_summernote.admin  import SummernoteModelAdmin".

        And then we'll create a new class  we're going to call this PostAdmin.  
        That's going to inherit from  SummernoteModelAdmin that we've just imported.
        And then we're just going to say: "summernote_fields = ('content',)".

        So that's saying that our  content field, our blog content,  
        which we know is a Django text field,  we want to use summer note for this.
        We then need to register  post admin to our admin site. 
        Now instead of adding it to  this admin.site.register method,  
        I'm going to delete that line entirely.
        And instead we're going to add  a decorator above our class. 
        Which is "@admin.register(Post)" 

        And this will register both our post model  and the post admin class with our admin site.
        Now you may be wondering why we're adding  this decorator and not just putting it  
        in the admin.site.register  method at the bottom of the file.
        The reason is that for some reason  the admin.site.register method  
        only allows us to pass in two  arguments so it quickly gets full.
        The decorator is also a more Pythonic  way of handling the registration.
        So that's what we're going to use.

    - Okay save this, and before checking the  admin page again, we need to migrate.
        Now you don't need to make the  migrations because we haven't  
        changed the database format,  we've just installed more apps.
        So pause the video, run the  migrate command and then come back.
        ---------------     "python3 manage.py migrate"  -----------------

        Okay now our migrations are made  we can run the server again.
        "python3 manage.py run server"
        And now, when we go back and refresh our admin panel.

We can see here that our content has now changed to a full  
featured editor, so I'm just going to  add a blog post for testing purposes.
Now even after adding this post, we still  have much to do in order to get our admin  
site as we want. I'm just going to add in the  excerpt, set it to published, and save this.
In our next video, we're going to carry on tweaking our admin site so that it's even more user-friendly.

# __Building The Admin Site - part 2__
WHAT IS IT?  ----   The Django admin panel 
WHAT DOES IT DO?  ----  Allows a superuser to administer the site 
HOW DO YOU USE IT?  ----  Log in to the /admin URL with a superuser account

In our previous video, we got  our basic post admin working,  
but we're not finished  tweaking our admin site yet. 
There's much more left to add. 

    - So let's go back to our admin.py file.
        When we enter the post title, we want the  slug field to be generated automatically.  
        To do that, we'll use the  prepopulated_fields property.  
        Which was specifically designed  for generating slug fields.
        It calls a bit of JavaScript that formats  and populates the slug field for us,   
        so that we don't have to worry about it. To  use it, we pass in a dictionary that maps  
        the field names to the fields that we want to  populate from. In our case, we want to populate  
        the slug field from the title field. 
        
        So above  my summernote_fields property here, I'm going  
        to add "prepopulated_fields =" then my Python  dictionary, we're populating slug from title.
        Now when we save this and refresh the admin  page. We go back as well to add a new blog post.
        Then you can see that as I type  the title, the slug field is  
        automatically generated. This  will form part of our URL  
        so an individual blog posts URL will be  our project's base URL, plus this slug.

    - And we can add a lot of configuration to  the admin panel to make our life easier.  
        For example, if I add "list_filter = status,  'created_on' " then save my file refresh the admin  
        page once again. Then we can see, that I have  now this cool filter box on the right hand side  
        that allows me to filter the posts by  their status or by the created date.
        Isn't that cool? One line of code adds all of this  
        useful functionality, well that's the  batteries included nature of Django.

    - Are you ready for more?
        Well I have a little challenge for you.  
        I've added two links below the video to different  sections of the Django admin panel documentation. 
        Your challenge is to add two lines  of code one will be using the list  
        display property to customize what we  see in the list view of the admin panel. 
        I'd like you to list the title, slug,  status and created_on fields; please.
        The second is to add search fields  that search either the title  
        or the content which will  help us to find a post easily.
        Are you ready?
        We'll pause the video for about five minutes.  Read the documentation and then add the two  
        lines of code to our post admin class. I'll see you on the other side.
        Welcome back! Does your admin  page now look like this?  
        If so, well done! If not, don't worry  
        just compare your code with mine. Your post admin class should now look like this.

    - So finally, in this video I want  to add the comment admin model.
        Now we're going to start it and finish it  together but I'd like you to do the middle bit.
        First then, let's go up to the top of our  file and import our comment model from models. 
        So just after our post import  here we'll also import comment.

        As you've probably figured  we need to add a new class  
        but before that, we're going to  add our admin.register decorator.
        So "@admin.register(Comment)", and then we can create our class  
        that inherits from admin.ModelAdmin,  which is a built-in Django class.
        And now it's your turn. 
        
        - We want  to customize our admin panel view so that the list display shows the name, the body, 
        the post it was made on, the created  date, and whether the comment is approved or not.

        We also want the list filter to show the  option of filtering by approved and created on.  

        And finally, we want the search fields  to be name, email address, and body.

        I'll give you 10 minutes to create this.  
        If you're stuck, then use our  post admin class for inspiration.  
        Afterward, I'll show you what I wrote and then  we'll add the last bit of our class together.
        Welcome back, so here's how my class looks. Now if you save your changes and visit the  
        admin panel again, then you should see  that you can now manage the comments.

    - So the last thing that I want to add here is an  action that allows us to approve the comment. 
        Now remember, that in our model the  approved field is set to false by default. 
        This ensures that all comments  need to be manually approved by an  
        admin before they appear on the site. 
        So now we want to add the  approval action to the admin site.
        To do this, we use another handy  built-in feature of the admin classes,  
        which is actions. The actions method allows you  
        to specify different actions that can be  performed from the action drop-down box.
        Now the default action is just  to delete the selected items  
        but we want to add an approved comment section  too. 
        
    -  So to do this, at the bottom of our class  
        we'll add, "actions = ['approve_comments']". Now actions takes a list of function names as  
        an argument so you could define more  than one action here if you wanted.
        Now, beneath that, we'll create  our approve_comments method.
        Now as you remember, the approved field is a  boolean field that's set to false by default,  
        to approve the comment we just need to  set that field to true. So we'll add our  
        method called approve_comments which accept  self, request, and queryset as parameters.
        Don't worry about those too much, queryset is  the one that we'll use to update our record.  
        Our function then, is a one-liner we just  call the update method on the query set and  
        change our approved field to true and that's it! Our post admin and comments admin is now complete. 
        So now let's review our user stories.  
        Well, we've been able to add the ability to  manage posts, so we can move that to done.   
        We can create draft posts, so that's done. And we  can also approve comments, so that's done too.
        In our next video, we're going  to start building our blog views  
        and we'll move more of our  user stories to in progress.










































































