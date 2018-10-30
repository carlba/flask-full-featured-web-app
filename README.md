# flask-full-featured-web-app
https://www.youtube.com/watch?v=MwZwr5Tvyxo

## Database

### Creating and observing sample data using the models in this application

```
>>> db.create_all()
>>> from app import User, Post
>>> user_1 = User(username='genzorg', email='genzorg@gmail.com', password='password')
>>> db.session.add(user_1) # This will not add the user until the session is commited
>>> user_2 = User(username='JohnDoe', email='john.doeg@gmail.com', password='password')
>>> db.session.add(user_2)
>>> db.session.commit()
>>> User.query.all() # Get all users
[User('genzorg', 'genzorg@gmail.com', 'default.jpg'), User('JohnDoe', 'john.doeg@gmail.com', 'default.jpg')]
>>> User.query.first() # Get first user
User('genzorg', 'genzorg@gmail.com', 'default.jpg')
>>> User.query.filter_by(username='genzorg').all() # Get all users with username genzorg
[User('genzorg', 'genzorg@gmail.com', 'default.jpg')]
>>> User.query.filter_by(username='genzorg').first() Get first users with username genzorg
User('genzorg', 'genzorg@gmail.com', 'default.jpg')
>>> user = User.query.get(1) # Query by id
>>> user.posts # The user currently has no posts
[]
>>> post_1 = Post(title='Blog 1', content='First post content!', user_id=user.id)
>>> post_1
Post('Blog 1', 'None')
>>> post_1.date_posted # This will be created when the Post is commited
>>> post_2 = Post(title='Blog 2', content='Second post content!', user_id=user.id)
>>> db.session.add(post_1)
>>> db.session.add(post_2)
>>> db.session.commit()
>>> user.posts # Now the user has two posts
[Post('Blog 1', '2018-10-26 20:53:43.989531'), Post('Blog 2', '2018-10-26 20:53:43.990123')]
>>> post = Post.query.first() # Get the first post
>>> post.user_id # Get the user_id of the User that made the post.
1
>>> post.author # This uses the backref configured in the Model to retrive the related user I.E the user that made this post.
User('genzorg', 'genzorg@gmail.com', 'default.jpg')
>>> 

>>> db.drop_all() # Delete everything in the DB
>>> db.create_all() # Recreate the DB structure.
>>> User.query.all() # The data is no longer availible
[]
>>> Post.query.all() # The data is no longer availible
[]
```

## Circular imports
https://youtu.be/44PvX0Yv368?t=255

## Debugging

### How to use the web ui for debugging 
https://youtu.be/CSHx6eCkmv0?t=764

**Never use Flask in debug mode in production mode since it exposes a python interpreter**

## Credentials

### Generate a random hex (suitable for a password)

https://youtu.be/803Ei2Sq-Zs?t=1694

* 3.6
  ```python
  import secrets
  random_hex = secrets.token_hex(8)
   
  ```
  
* 2.7
  ```python
  import os
  import binascii
  binascii.hexlify(os.urandom(8)).decode('ascii')   
  ```
  

## Mail

A working Gmail integration requires you to follow the instructions 
[here](https://myaccount.google.com/lesssecureapps). The username and password should be red from
environment variables check the source of this repo for instructions on how to do this.

**Please note the specific instructions regarding 2-Step Verification enabled** 


