# Zine

Zine is a small script that works like a simple CMS. It is intended for
allow a group of users on a *nix server to post content to
markdown from your personal accounts and this can be moderated and accepted by a
editor before being published.

We are using zine now in [Agora](http://hipatia.iesjovellanos.org/agora). A small
blog written by students and teachers of a high school. If you want to use it, ask
me for any questions, suggestions or changes.


## Write a new article

In order for a user to publish, they must execute the following command:

```
$ zine new
```

A file will be created in the `~/pub/blog/` directory of your home and you simply
have to edit it using markdown.


## Moderate and publish

The editor will be able to review and moderate the article queue using the
command:

```
$ zineadmin --moderate
```

To publish all accepted articles execute:

```
$ zineadmin --build
```


