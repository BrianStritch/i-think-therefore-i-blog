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

to install authorisation from allauth
 - pip3 install django-allauth   -- update requirements.txt file after install
 - python3 manage.py migrate     -- make migrations when completed after setting login and logout redirect

when modifying the login.html you need to copy the relevant templates with
- ls ../.pip-modules/lib/     ---- this tells you which version of python you are using
- cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates  --- this copys the templates

when allowing comments to be made we use a django form
- pip3 install django-crispy-forms  -- update requirements and make migrations when completed


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

# __View Creation Checklist__
WHAT IS IT? ---- Our first view 
WHAT DOES IT DO? ---- Allows us to view our blog post list 
HOW DO YOU USE IT?  ---- Follow the three step process to creating new views

In our previous two videos, we set up our blog  admin page. Remember, though, that Django is an  
        MVT-based framework - Model, View, and Template. We’ve set up our database models for posts and  
        comments, now it’s time to create  our first view and template.
        We're going to address another  three of our user stories. 
        So let's move pagination,  
        and the ability to view a post list, 
        and the ability to view likes  to our in progress column. 
        It gives you a great sense of satisfaction  moving things across the columns like this.
        So the models for our blog  lived in the appropriately named  
        models.py file it shouldn't be  too much of a stretch of the  
        imagination then to realize that our  views will live in the views.py file.
#### __Class Based Views__
        Now in the previous videos, you learned  about Django's function based views  
        where you defined each view  as a standard function.
        For the blog, however, we're going  to use class-based views instead.  
        Now before you accuse me of making your life  harder, there is a good reason for doing this.
        Class-based views allow us to make code that's  reusable - one view can inherit from another,  
        which is not possible with  standard function-based views.
        That means we can make use of some of  the cool built-in features with Django,  
        such as generic views, which is  what we're going to use here.
        Generic views is just a fancy way of saying  that you don't need to write very much code  
        and Django will handle it all for you.
        They're built into Django as part of  its batteries included philosophy,  
        so we might as well make good use of them.
        Each time we create a new view,  we need to do three things: 
        - Firstly, create the view code. 
        - Secondly, create the view template. 
        - And thirdly, connect up our URLs file.

    - So let's start with step  one, create the view code.  
        And thanks to our generic view,  this is going to be extremely easy.
        So in our blog directory we're  going to open up our views.py file.
        And the first thing that we want to  do is to import the generic library.
        So right at the top "from  django.views import generic".
        I'm just going to delete this comment here.  
        And then we're going to import our  post model that will base our views on.
        So "from .models import Post".
        
        - And now we can create our class, this is going to be
        a class called PostList and we're going  to base this on the generic list view model.

        Now we're going to tell the class  that it's inheriting from this,  
        if you want to know more about these  generic views and how they work,  
        then I've put a link to the relevant  Django documentation below the video.
        Inside the class we're telling  it to use post as its model  
        and now we can use more of the built-in methods  to quickly and easily render our list of posts.
        So we're going to supply the queryset here,  which will be the contents of our post table.  
        We're going to filter this by status. Remember  that our status field can be set to either 0  
        for draft, or one for published we want only  publish posts to be visible to the users,  
        so we'll filter our posts by status equals one.
        We're then going to order them by created_on  in descending order, like we've done before.  
        The template name is the html file that our  view will render what about paginate_by?
        Well list view provides a built-in  way to paginate the displayed list  
        and paginate just means separate into pages.  
        By setting paginate_by to six, we're limiting the  number of posts that can appear on the front page,  
        if there are more than six then Django  will automatically add page navigation.
        So that's very simple, that's our  view created for the post list.

    - Now we need to create our  templates and wire up the URLs  
        we've provided a starter template  for you at the repo below the video.
        So bring the html files over and drop them into  the templates directory you created earlier.  
        Don't bring the account  directory over at the moment.

    - What we'll do inside our static directory  is create a new folder called css,  
        and then we can copy our style.css file into that.

Let's just briefly consider that the files that we  uploaded, I'm not going to go through everything  
in the css file, if you want to take a look  at it after the video then please feel free.  
But there's absolutely nothing in  here that you don't already know.  
You can see then that we  have a file called base.html.
Now you haven't encountered this in Django yet,  but the principle is exactly the same as in Flask.  
We have a base template which loads Bootstrap  and our fonts. It also contains the navigation  
here and if we scroll down you can see  that it contains our footer as well.
Now it also contains just like  Flask, our block content tags,  
which is where the code from our  other templates will be injected.
When we move into our index.html  file, you can see the same again,  
that it follows the same  conventions we used with Flask.
We're extending base.html and  we have our block content tags.  
Apart from a bit of Bootstrap at the  moment there's nothing else here. 
In our next video, we're going to add content to  this index.html file and wire up our first URL.

# __Creating Our First View__
WHAT IS IT? ---- Our first view
WHAT DOES IT DO? ---- Allows us to view our blog post list 
HOW DO YOU USE IT? ---- Follow the three step process to creating new views

In our previous video, we completed step one  of our checklist and we built the view code.
In this video, we'll finish step two to create  
the template and we'll also do  step three by creating the URL.
At the end of this, you'll be able to open up your  
site and see the temporary  blog post that you created.
We're going to use some advanced features of the  
Django Templating language in  order to format our post list.

    - First, inside our Bootstrap row  here, the blog entries column row.

    - Let's create a for loop to iterate through  
        the list of posts that will  be passed in from our view.
        So {% for post in post_list %} {% endfor %}
        I find it best to do these both at the  same time so that I don't get confused.
        We want our posts to display in rows of three.  
        After six posts, we'll paginate them. So we're  going to use the built-in loop counter to close  
        the existing row div, and add a new one  after three posts have been displayed.
        So {% if forloop.counter|divisibleby:3 %}
        then we're going to close the row div,  we're going to open a new row div.
        Just delete these, it's auto creating  them thanks to the autocomplete.
        And then, we can end {% endif %} here.

    - So Django has a built-in  counter method on our for loop,  
        when it's evenly divisible by three, then we're  going to close our row class and add a new one. 
        And this will be pushed right down to the  
        end of our for loop so that we  don't close the row too early.
        Now up at the top of our for loop, I'm  going to paste in some Bootstrap code here.
        And you can pause the video for a couple of  minutes if you just want to copy this in. 

        Effectively, all I'm doing is creating a  column and I'm also then creating a card. 
        And everything is going to live inside our card  body which is going to contain the post overview.
        So let's start adding that content  now, beginning with the featured image.
        Okay I'm just going to scroll over a little  bit here so we can see what's going on.
        So if the word placeholder is found in the URL,  remember that's our default if we don't supply an image.
        Then, we'll assume that there is no featured image, so we'll just load a default placeholder image.
        You can use the same address  as we have here, I'll put it below the video.
        Otherwise, we'll use the image that we've uploaded
        and we'll do that using  the double curly bracket notation.

        Remember that the curly bracket followed by  the percent sign indicates a control statement.
        Whereas, double curly braces  inserts the content into the html.

        So here we're inserting our  URL from our featured image.
        After the end if tag we'll just add our  image flash div with the author details.
        And underneath that I'm going to  paste in our post title and excerpt.
        Now leave the link in the href just at our # sign there for now we'll return to that a little bit later.
        So there's nothing too surprising here, we're  just formatting the various parts of our post overview.
        Now I'll just put in our horizontal  rule that's going to go underneath the link.
        And a little bit of Font Awesome  code here as well, to display  
        our heart sign and then the number of likes.
        So that completes the main post list display. 
        The last thing we want to do in this  template is to add the pagination code.  
        When we have more than six posts on our blog,  we want them to appear on an extra page.  
        Both the Django list view and Bootstrap  provide easy pagination functionality.  
        So before the very last closing  div tag, just insert this code.
        Okay I'm just going to add in a line break here  so that you can see it a little bit clearer.  
        So list view provides the is_paginated boolean,  
        so if that's set, we'll display these  navigation buttons at the bottom of the page.

This then concludes building our  first view, however it won't work yet. <br>
Remember our list at the beginning?<br>
Create the view code, <br>
create the view  template,<br> 
connect up our URLs file.<br>

So we've done the first two, but  now we need to wire up our URLs. <br>

    - This is a straightforward process so first create  a file in the blog directory called urls.py.
        And then we're going to import  our views "import path",
        because we need that from django.urls and  then create a URL pattern for our home page.  
        This is similar to what you've done  before so "urlpatterns =", this is a list.
        So we'll supply our path, we're  then going to just supply a blank  
        path because that indicates that  it's our default, our home page.
        ("", views.PostList.as_view(), name="home"),
        Now this is similar to what you've done before,  but because we're using class-based views we need  
        to add the as_view method on the end of post list.  So it's going to render this class as a view.

    - Now we just need to import these  URLs in our main Codestar URLs file.
        So open that up from the Codestar directory,  
        after our Summernote path we can then add  in a blank path indicating our home page.  
        We'll include our blog directory dot URLs file, 
        and we'll give this the name of "blog_urls".

Now when we save all of these files, and run our project...
Then we can see when we click on view site,  
that everything is rendering  and our test post is visible.
In our next video, we're going to do the same  process again for our post detail display.
But I'm going to take a more hands-off approach  in the next video, and let you do a lot of the building.
So go back over the code in this  video just to make sure you have it right.  
And then I'll see you in our next one  when we build our post detail view.


Default image URL is: https://codeinstitute.s3.amazonaws.com/fullstack/blog/default.jpg

# __The Post Detail View - part 1__
WHAT IS IT? ---- The post detail view 
WHAT DOES IT DO? ---- Allows us to view the content of our blog post 
HOW DO YOU USE IT? ---- Follow the three step process to creating new views

        You now know the basics of adding views to Django.
        So in these next two videos,  I'm going to set you off,  
        and then ask you to pause  it, to add what we'll need.
        We’re going to build the post detail view. When  a reader clicks on the post they want to see,  
        we’ll bring them to this page,  which will display the entire post.
        We won't add the ability to add  comments or like functionality just yet.  
        We'll do that after we've added authentication.
        First, let's check in on our user stories.  We have these three, now that are done.
        We did the pagination in our previous videos,  
        the ability to view likes, and  the ability to view our post list.
        Now though, we want to add open a  post and view comments to in progress.
        So remember adding a new view checklist,  
        we want to create the view code, create the  template, and then connect up our URLs file.
        Well we're going to follow exactly  the same procedure with this.
        So in our editor, open up our views.py file  again and import View from django.views. 
        We’re also going to import our familiar  get_object_or_404 function from Django shortcuts.
        And then we can add a PostDetail  class, which inherits from the view.
        So PostDetail and view.
        Now this time we're not using one  of Django's helpful generic views,  
        so we have to do everything ourselves.
        And this gives us the opportunity to  talk a bit more about class-based views.  
        When you created function-based views in the Hello  
        Django project you pass the request  object as an argument to your view.
        You then check to see if  the request method was GET  
        or POST so that you could  decide what you wanted to do.
        Now class-based views are different.
        Instead of using an if statement  to check the request method,  
        we simply create class methods called  get or post, or any other HTTP verb.
        So to display our post what  request method will we use?
        Get, Post or a different verb?
        Well pause the video for a  minute and think about it.
        I'm sure you realize that, because we  want to get our blog post and display it  
        then we'll be using a GET method.
        So, let’s create a class method called get. Into  our class method, we're going to pass in self,  
        then request then slug, and the standard other  arguments and keyword arguments as parameters.
        Then we need to get our post object.
        So how do we identify which post we want?
        We're looking at the list of parameters in our  get method what do you think? Again, pause the  
        video for a minute and see if you can figure out  how we'll identify which post we want to display.
        I'm sure you figured out that it was by using  the slug, which is unique for each blog post.  
        So, in our method let's get the post.
        First, we'll filter all of our posts so that we  only have the active ones with status set to one.
        And then, we'll get our published  post with the correct slug.
        By passing in our queryset to get_object_or_404,  and then with the arguments "slug = slug".
        Now the post object contains most of the  helpful things that we're looking for.  
        So using this we can get any comments  that are attached to the post.
        So we'll type "comments =", we're  
        able to get the comments from our post, we'll  filter them to view only those that are approved.
        And we're going to order them this time  in ascending order, so that we have the  
        oldest comment first and we can actually view  this as a conversation. I also want to set a  
        boolean value to say whether our logged-in  user had liked this post or not. If we did,  
        we'll set the boolean to true, otherwise it  will remain false. So we'll say "liked = false"  
        and then we'll check with an if statement here, 
        to see if our post  
        when we filter it out if the user id is actually  there to say that they've liked the post.
        If they are, we'll set it to true,  otherwise it will remain false.
        Finally then, for this view, we can send all  of this information to our render method.  
        So we'll return render, we're  going to send a request through,  
        we're then going to supply the template  that we require post_detail.html.
        Then we'll create a dictionary here to supply  our context. So our post will be simply post,  
        our comments key will be the  comments that we got back, 
        and liked will be our liked boolean.
        Now we are going to add more to this view  a bit later but that will do for now.
        So now what I'd like you to do,  
        is go on to the second item in our new view  checklist which is to create the template.
        Now we've provided you with a starter  template called post_detail.html.  
        Open it up now follow the instructions in the  comments to complete the template yourself,  
        maybe give yourself around  10 or 15 minutes to do that.
        And when you come back, we'll  compare our code in the next video.  
        So for now you can take a break, look through  that, add in all of the template tags in the  
        right place. And then at the beginning of  our next video we'll check the code together.


# __The Post Detail View - part 2__
WHAT IS IT? ---- The post detail view
WHAT DOES IT DO? ---- Allows us to view the content of our blog post
HOW DO YOU USE IT? ---- Follow the three step process to creating new views

In our previous video, I set you the challenge  of adding content to our post_detail.html.
Hopefully, you were able to add  in everything you need. If not,  
please compare your code with the source  code link at the bottom of the video.

        Right now I'll quickly scroll down the code and  
        you can check off if you  got each element in place.
        So we have our featured image, our post content,  just over here then we have a number of likes,
        then we have our total comments.
        And finally, we have a comment name, and  comment created_on and then our comment body.
        Now we will need to add to this template later,  
        especially when we come to adding commenting and  like functionality but it will suffice for now.

    - The third item on our list is to wire up the URLs.
        And that's exactly what  we're going to do right now.
        So open up the blog/URLs py  file and let's add our path.
        So our path is:
        "path('<slug:slug>/',  views.PostDetail.as_view(), name='post_detail'),"
        So let's unpick what's happening here.
        The second and third arguments,  
        we already know about but what's  happening with all of these slugs?
        Well the first slug in angle  brackets is called a path converter. 
        The second slog is a keyword name.
        Now this could be anything we wanted, but  to keep it consistent we're calling it slug.
        The path converter converts this text into a slug  field, it tells Django to match any slug string,  
        which consists of ASCII characters or numbers  plus the hyphen and underscore characters.
        There are a number of these helpful path  converters, which allow you to match numbers,  
        or strings, or characters. I've put a link  to the relevant Django docs below the video.
        This means that, as we said  before, our posts will have  
        friendly URLs that consist of our  Heroku project URL followed by the slug.

    - The final thing that we need to do then is to  add the post detail URL into our index.html file,  
        so that users can click on the title  or the excerpt and read the post.
        So back in index.html, let's  replace our hashtag here  
        with a control statement. So that's the curly  braces and the percent sign, it's a URL which  
        will be the post detail URL we just created,  and that will accept post.slog as an argument.

So let's now save everything and test our project.
And as we can see this is  working absolutely fine now.
So we've completed our three  steps to wire up a new view.
We created the view code, we created our template  file, and we wired that up in our urls.py file. 
We've also completed our two  in progress user stories,  
so we can move those now into the done column.
In our next video, then, we're  going to investigate authentication  
so that our users can register, and  then comment on, and like our posts.


# __Authorisation - part 1__
WHAT IS IT? ---- Django AllAuth 
WHAT DOES IT DO? ---- Allows us to easily add authentication to our project 
HOW DO YOU USE IT? ---- Install and configure the AllAuth library

So far, we’ve been able to build a  basic blog application quite rapidly,
and that’s the beauty of a  batteries-included framework like Django.
It's actually designed for  rapid application development.
If we didn't want any extra functionality such  as allowing commenting or likes, then our project
would already be finished. Because we do want  this, however, we're going to add authentication
which will allow users to register with our  blog, leave comments, and like or unlike posts.
So first, let's move another user  story to our in progress column.
And that's our account registration
of course Django comes with a perfectly  good authentication system built in
you've already used it when we created a super  user and logged into the admin panel we're not
going to use it for this project though instead  we're going to use a library called all auth
why well because all auth offers some distinct  advantages such as being able to send password
and account confirmation emails enforcing password  complexity and providing single sign-on using
google or facebook in this project we'll use the  basic functions of all auth if you'd like to look
at performing single sign-on then leave that until  the end of this project i'll give you some ideas
as to how you could expand the functionality and  some resources too we won't do it in these videos
because you'll need to use a credit or a debit  card to sign up to use the google development
tools although you shouldn't be charged if  you're interested in configuring password
reset and account confirmation emails then we'll  cover that in detail in our e-commerce module for
now though let's get all auth installed 

    - so we type  pip3 space install space django hyphen all auth "pip3 install django-allauth"
        
    - when that's installed update your  requirements.txt file before we forget

    - now we need to add our all auth urls to our main  urls.py file so under the codestar directory
        open our urls.py file and then we'll add a line  inside our url patterns list and this is very
        similar to what we've already done before  we're going to provide the path to accounts
        so this will be our url and then we're  going to include the all auth urls

    - we then need to make some changes to our  settings.py file so let's head over there
        and we can add in the all auth apps that we've  just installed so first of all we need to
        add django.contrib.sites this is a built-in  django package and then our all auth packages
        so all auth all auth dot account  and all auth dot social account

        we also need to add a site id of one this  is so that django can handle multiple sites
        from one database now of course we only  have one site here using our one database
        but we'll still need to explicitly tell django  the site number so site underscore id equals one
        and we'll add in the redirection  urls too so that after we've logged
        in all logged out the site will  redirect us to the home page

        so log in redirect url equals forward slash we'll  just copy that and then change login to log out

    - okay let's save everything and run our migrations  you can remember how to do that at this stage 

    - now we can run our project now when we run  our project we're going to head over to the
        accounts sign up url to see what we get now if you  are currently logged in as admin then make sure
        you log out first via the link in the admin panel  otherwise you'll just keep getting redirected to
        the front page so let's go to forward slash  accounts forward slash sign up and helpfully
        all auth provides these templates to allow us  to sign up log in and log out the urls are
        provided by the path that we added to our urls.py  file now okay it's not pretty but does it work
        well let's give it a go let's sign up  for a new account and see what happens
        and we get redirected back to the home page which  is what we expected because that was the login
        redirect url that we added you'll also notice that  our top navbar has now changed to log out now our
        logout link doesn't do anything yet so let's wire  up those links and then look at customizing the
        templates in our next video
        
    - so let's go back  to our editor first into our base.html file
        and we'll change our navigation so in the if  user is authenticated block in log out here
        let's add this url so our url is going to be  account underscore logout now all of the urls for
        all auth are prefixed with account underscore  so see if you can provide the other two here for
        our register for sign up and for login pause the  video for a couple of minutes while you add them
        so this is what we have account  underscore sign up and account underscore
        login not too difficult was it so let's  run our project again and check if it works
        so as you can see the functionality works but it's  definitely not the ui that we want for our project
        so where do these templates live and  how can we go about customizing them
        well we'll look at that in our next video

# __Authorisation - part 2__
WHAT IS IT? ---- Django AllAuth
WHAT DOES IT DO? ---- Allows us to easily add authentication to our project
HOW DO YOU USE IT? ---- Install and configure the AllAuth library


In our previous video, we got AllAuth installed  and working, but our templates were a bit ugly!
Fortunately, it provides a convenient  way of modifying the templates.  
But we do need a bit of manual copying.

    - Firstly, we need to know what  version of Python you're using.
        So, back in the terminal window  type: 

        **               "ls ../.pip-modules/lib/"          ** 

        And this will list the files in the pip  modules lib directory which lives just  
        above our workspace. On my machine  it says that I'm using Python 3.8  
        which is where all the files for the  modules we've installed with pip will live.
        So we're going to copy all of  those into our templates directory.
        So "cp -r", which means to copy recursively so  that will include any directories, I then have  
        my Python 3.8 thereafter lib. If your version  is different you'll need to change that version.
        The rest of it should be the same. /allauth/templates/* ./templates 

        ***  "cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates"  ***

        Which means to copy everything and I want to  copy that into my templates directory here.

    - Now you'll see that this has created  multiple directories in our templates folder.  
        We can ignore most of these, the one that  we're really interested in is account.

    - So let's navigate to there, and we'll  choose the login.html template first.
        Now you can see when we open it up that  this is a standard Django template.
        I want to show you how to modify  this but I'll supply you with the  
        other completed templates for the others.  
        You'll need to know how to copy and modify  these templates for your own projects, though.
        So first of all, we can see that it says  to extend account forward slash base.html.
        So let's delete the account and the forward slash,  
        so that it's extending the  base.html file that we created.
        So now it just says extends base.html.  

        And if we save that, and we visit  our account/login URL again.
        Let's just run our server again,  because it had stopped, go to login.
        And we can see that it already looks a lot  better but let's improve on it even more.

        We'll go back to our editor. And first of all, we can delete the social account  part, because we're not going to be using that. So from the get, right down here to the else statement we can delete all of that.
        Let's take off the end if as well underneath  there, so that we're not causing any errors.
        We can also delete our forgot password link,  because we're not going to be using that in this particular project.
        As I said, we'll cover that in  detail in our e-commerce module.

    - Okay so the next thing that I want to do now,  then, is to add in some standard Bootstrap classes.
        So I'm going to use emmett to do  this, I'm going to create a container.  
        I'm going to add a row inside that container,  
        a standard md8 column, which has a top margin  set, and an offset of two, so that it's centered. 
        Okay and I'm just going to  take these closing divs and  
        can throw them right down at  the bottom here, out of the way.
        Unfortunately, our auto formatting  doesn't seem to be working here. So  
        we'll try and make this look a little bit  nicer, let's just move that across then,  
        I'm going to change it to a h3 instead of a h1.
        And for my paragraph here I want to change  the text in the paragraph as well to match  
        what we had on our example login page.
        So I'm just going to paste that in. We'll change the formatting here,  
        you can do the same with your project too,  just make it a little bit easier to read.
        Okay, then we can close our  column and close our row div.
        And we want to create another row and another  column, this is going to contain our login form.
        So again, it's going to be a row, it's  going to be a column with the width of 8,
        and it's going to have the same top margin,  and the same offset so that it's centered.
        Okay, just delete those two here,  
        don't need those closing div tags because  we already put them down at the end.
        Okay our form is absolutely fine.  Let's just move it across a little bit  
        and delete that closing div  because we only need two.
        Okay, and I just need to change the class of  my button here now to a standard Bootstrap class.
        I've created a btn sign up class in our  custom css. So it will give it a little bit of  
        a different color and appearance and that's  our template completed. So let's save that.
        We'll go back to our project and  just refresh the login page here,  
        and now everything is looking so much better.

So in this video and the last  one, we've seen how to install,  
integrate, and customize Django AllAuth. 
I've put a link to the other completed templates  below the video and you can just copy and paste  
them into the appropriate files or just copy  the file into the account directory there.
For now then, we can move our user story to  done because we've added our authorization.
In our next few videos, we're  going to add the commenting  
and like features, and then  our blog is almost complete.

# __Commenting - part 1__
WHAT IS IT? ---- Commenting 
WHAT DOES IT DO? ---- Allows logged-in users to leave comments on our blog posts 
HOW DO YOU USE IT? ---- Add the comment form and view

Up to this point, the conversation  on our blog has been a bit one-way.
Now, we want to give our viewers the  opportunity to interact meaningfully with the blog  
by commenting or liking the post.
This means we get to move more user stories over  to In Progress, so let’s go to our kanban board  
and choose: comment on a post  and put that to in progress.
Much of the backend work to get  comments working has already been done.  
We have our model, and we can  approve/disapprove them in the admin panel.

    - So, let’s turn our attention to creating our  comment form. We’re going to use a form library  
        called Crispy forms to help us with formatting.  I’ve linked to the documentation below the video.
        So let's install it to begin with: 
        
        ************    "pip3 install django-crispy-forms"   ***********************

        As usual, update your requirements.txt file and  then we can add crispy_forms to our settings.py.

    - So now we can go over to our settings.py  file and in the installed apps section,  
        I'm just going to add crispy_forms  here beneath Django Summernote,
        We'll also tell Crispy to use  Bootstrap classes for formatting. 
        So: CRISPY_TEMPLATE_PACK = 'bootstrap4' .
        Now, I know that we're using Bootstrap 5 in  this project, but the classes will work the same  
        and at time of recording, Crispy didn't  have a Bootstrap 5 template pack available.

    - Now, we need to create our form  class. So, in our blog directory,  
        we’ll create a new file called forms.py.
        And We need to import our comments  model and the forms base class. So: 
        from .models import Comment from django import forms
        Next, we can create our CommentForm  class that inherits from the base form.
        So: class CommentForm(forms.ModelForm) We'll add a meta class and all we're doing here  
        is telling our comment form what model to use, and  then which fields we want displayed on our form.
        So in this case, body. 
        Now that trailing comma is  important there in fields,  
        otherwise Python will read this as a string  instead of a tuple, and that will cause an error.

    - Okay now that we've added that, we  can head over to our views.py file  
        and we're going to import  the form we just created.
        See if you can figure out how to  do that for a couple of minutes.
        That's right, it's from: .forms import CommentForm
        So with the form imported, we now  need to render it as part of our view.
        To do this, we can simply add it to our context.
        So just under liked in our render method,  we're going to supply a new key comment_form.  
        And the value will just be the comment  form that we imported just now.
        Now that's done, we can turn our attention to our  post_detail template to get the form displaying.  

    - So if you've closed it it's  there in the templates directory.
        First of all, we want to  load Crispy forms at the top. 
        So, inside our block content let's add these tags:
        {% load crispy_forms_tags %}

        And now we can scroll down our  form, and you remember that we  
        had a section which comment of <!-- For later -->, well now is later.

        That's what we're going to turn  our attention to right now.
        So I'm just going to paste  the code in, you can copy it,  
        and then we'll just talk  through what we're doing here.
        So we've added a standard if  block so that our comment box  
        only appears if our user is authenticated.
        Then, we create our form with the method of post,  
        we're rendering the form using the Crispy  filter so that it's formatted nicely.
        And then we’re also adding a CSRF token.  CSRF stands for Cross-Site Request Forgery,  
        and that's a way that attackers could try to find  vulnerabilities in your site. Django comes with a  
        protection against that, which is the CSRF token.  So you need to add this to any form you create.  
        If you want to read more about this,  I’ve linked it below the video. 
        And then we have our submit button.

So let's run our project and see what happens.
As you can see, I'm logged in at the moment.
And so when I click on my test post  then we can see the comment form  
rendered on the right and the comments will appear on the left.
Now at the moment, if you try  to submit this form it'll give you an error.
So in our next video, we're going to fix that  by adding the post method to our views.py file.

# __Commenting - part 2__
WHAT IS IT? ---- Commenting
WHAT DOES IT DO? ---- Allows logged-in users to leave comments on our blog posts
HOW DO YOU USE IT? ---- Add the comment form and view

In our previous video, we got our form  rendering. Now, we need to get it working.

    - So what we're going to do is add a post method to  our PostDetail class back in our views.py file.
        Now a lot of our post method will  be identical to our get method. 
        So what I'm just going to do is copy  this, just select all of it here.
        I'm going to copy it, paste it in, making  sure to get the indentation correct here.
        And then I'm just going to  change the name from get to post.

        When that's done, we need to get the  data from our form and assign it to a variable.
        So I'm going to create a  new variable here called comment_form.
        And that's the value is going to be set to:
        comment_form = CommentForm(data=request.POST)
        So this will get all of the data  that we posted from our form.
        Now our form has a method called is  valid that returns a Boolean value  
        regarding whether the form is valid, as in  all the fields have been completed or not. 
        If it is valid, a comment has been  left and we want to process it. 
        So let's get that: if comment_form.is_valid():
        And what we're going to do is  set our email and our username  
        automatically from the logged in user.
        This is conveniently passed in as part  
        of the request so that we can  get those details from there.
        So we'll set the email to the request.user email.
        We'll set the instance name  to the request username.
        And then, we're going to call  the save method on our form  
        but we're not actually going to  commit it to the database yet.
        The reason is that we want to first assign a  post to it. So comment.post equals our post instance,  
        so that we know which post a comment has  been left on and then we can save it.
        We'll add an else clause here as  well, because if the form is not valid  
        then we just want to return an  empty comment form instance. So:
        else: comment_form = CommentForm()
        Okay, so now we just need  to adjust our render method.
        And what we're going to do is  set a commented value to True.
        So just under our comments here,  
        in our render method I'm going to say commented  and I'm going to set that value to True.
        Now we'll also add a corresponding False value  to our get method, so let's just copy that.
        We'll go back up to render and I'm  going to set commented to False.  
        And we're doing this so that we can tell our  user that their comment is awaiting approval,  
        we're going to use this Boolean  back in our post detail template.

    - So let's go back there now and  we're going to add this condition.
        Now again, I'm going to paste it in  and it needs to go just above the  
        if user is authenticated block here.
        And what we're doing is saying that if our  commented boolean value is set to True. 
        So if commented, then instead  of the comments form, we'll  
        just display a message here saying  your comment is awaiting approval.
        Otherwise, if it's set to False,  we'll display the comment form.
        Don't forget to add the second end if there at the  bottom either, so that both if blocks are closed.
        Okay so let's run our project  and try adding a comment.
        So when we go back we can see that  I'm masquerading as Brian here.
        I'm sure he won't mind.
        I'm going to add a comment and click on submit.
        And then as you can see, we get that message  
        because commented was set to True,  that our comment is waiting approval.
        So where is it?
        Well let's log into our  admin panel and take a look.
        So you'll have to log out if you're  logged in as a non-admin user here  
        and I'm going to go into my  admin panel now as admin.
        When I click on comments then you can see that the comment is there but it's not showing as approved.
        We'll select it, we'll approve  that comment, click on go,  
        and now we can see that our little approved  column has changed to a green check mark.
        When we view the site and  click back on our test post,  
        then we can see that Brian's comment  is there on the left hand side.
        Congratulations! We've added  commenting functionality. 
        Now then, we can add our user  story into the done column.
        And in our next video, we'll start  adding the like functionality.
        After that's added, we just have some  cleaning up and a final deployment to do.  
        Our blog is nearing completion. Well done!

# __Likes__
WHAT IS IT? ---- Likes 
WHAT DOES IT DO? ---- Allows logged-in users to leave like or unlike blog posts 
HOW DO YOU USE IT? ---- Add the like buttons and view

Our blog is getting closer  and closer to completion.
The ability to like or unlike a post is the last  major piece that we're going to add. In fact,  
we're going to move our final  user story into in progress.
After this, we're going to add in  a little bit of extra functionality  
and then clean up before our final deployment.

    - For this, we'll need to create a new view.
        Can you remember the three steps that we need  to take whenever we add a new view in Django?
        That's right,  
         - we need to create the view code,  
         - create the view template, 
         - and connect up our URLs file. 

    - In this case, we won't need to create  the template, since it already exists;  
        however, we will need to modify  our post_detail.html template.

    - So let's start by creating the  view code in our views.py file.
        I'd like you to create a new class-based view. It'll be called PostLike it'll inherit from view.  
        And the method will be called post, which will  take three parameters: self, request, and slug.
        Pause the video for a couple  of minutes while you add that.
        So your new view should look like this.

        class PostLike(View):

            def post(self, request, slug):
        
        Now, we can add the functionality. So again, just stop for a moment  
        and think about what this view needs  to do. As a hint, think about toggling.
        Any ideas?

        Well if we haven't already liked the  post, then we need to mark it as liked. 
        If we have, then we need to mark it as unliked.
        In effect, we're toggling the state.
        So first, let's get the relevant  post using our get_object_or_404 method.
        Then, we'll toggle the state.
        
        We'll use an if statement to check if our post is  already liked and if it is we'll remove the like.
        So remember how we checked if a  post was already liked before?
        We used an if statement, we filtered  our post.likes on the user ID  
        and if the user ID exists, then  it's been liked, so we can remove it.
        If it hasn't already been liked,  then we need to add the like.  
        So we can add an else clause  with: post.likes.add(request.user)
        Now we need to reload our post_detail  template so that we can see the results.
        To do this, we'll use a new response  type called HttpResponseRedirect.  
        So let's go up to the top of our views.py  file and import this from django.http.
        So: from django.http import HttpResponseRedirect
        And we also need to add the reverse shortcut.  This allows us to look up a URL by the name  
        that we give it in our urls.py file. So  add reverse to our django.shortcuts import.
        And now back in our view, we  can put all of this together.
        So let's scroll down to the end  and we're going to just add:
        return HttpResponseRedirect(reverse('post_detail',  args=[slug]))
        And the arguments will be the slugs, so that we know which post to load. So now when we like or unlike a post it will reload our page.
        Okay, now that our view is set  up, let's modify the template. 
        Now, if we scroll down here.
        We can see that we have our heart showing  the number of likes, and we want to turn this  
        heart into a button that we can use to like or  unlike the post - but only if we're logged in.
        So if our user is authenticated, we'll display  the buttons. And we're going to do this in a form.
        The form will have the method of POST,  
        and its action will be the new  view that we've just created.
        So I'm going to add some strong tags, first  of all because I want all of this to be bold.
        We'll add in our if user is  authenticated if statement.
        Then this is just a standard form.
        We're going to give it the class of display  inline because we don't want it to add a line  
        break at the end. Its action will be our new  post likes URL that we haven't created yet.
        It'll take the argument of the slug.
        Its method will be post.
        And of course, we also then  need to add our CSRF token.
        Now we want to display a solid heart  if the user has liked the post,  
        and an outline if they haven't liked it yet.
        So remember that we're passing a Boolean value  from our post detail view that's called liked,  
        we'll check that here.
        So I want you to add an if else block  to check if the liked boolean is set.  
        I'll give you a couple of minutes to do that,  
        don't worry about doing the  buttons, we'll do that together.
        So just create an empty if else  block that checks the liked boolean.
        Okay, so if the post is liked, we  said that we'll display a solid heart  
        and this will actually be a submit  button, so that it triggers our form.
        So inside the if clause let's add our button.
        We can see that it has the type  of submit the value is post.slug  
        and inside that we have a solid heart,  fas class is font awesome solid.
        In the else clause we can add exactly the  same code, but what we're just going to do  
        is change the icon class so that it gives  us an outline rather than a solid heart.
        So to do that, all we actually need to  do is change the class from fas to far.
        Okay so now after our form is closed,  
        what we're going to do is just add in a  heart for if the user is not logged in.
        So we're going to add an else clause here,  
        this is an else clause that refers  to our user is authenticated block.
        So if the user is not authenticated, then we're  just going to display the standard heart outline.
        Okay, now we can close our if statement  for our if user is authenticated.  
        And then I'm just going to create a span  here to display the post number of likes.  
        We already have this below, but I'm just going  to do it in a span rather than a strong class.
        So as you can see just a span with the class of  text-secondary showing the post number of likes.
        And there we go, that's our form created.
        So now, all that we need to  do then is the third step.
        Which is to add our URL.
        And I'm going to let you add this so  here are the parameters you'll need.
        The path is: like/<slug:slug> 
        The view is our 'PostLike' and  remember to cast it as a view.
        And the name matches the  name in our form 'post_like'.
        How did you get on?
        Well this is what your URL should look like.
        Okay, so let's save that and run our project.
        And now when we're logged in, we can like and  unlike the posts from our post_detail page.
        So we've completed our three  steps to adding a new view,  
        and now we can move our final  user story into the Done column.
        Well done! So there are just a couple  of tidy ups that we need to do,  
        and then we can make our final deployment.
















































