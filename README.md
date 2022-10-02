# Zine

Zine is a small script that works like a simple CMS. It is intended for
allow a group of users on a *nix server to post content to
markdown from your personal accounts and this can be moderated and accepted by a
editor before being published.


## Write a new article

In order for a user to publish, they must execute the following command:

```
$ zine --new
New post file created. Edit ~/blog/20220915.md to write your article
```

A file will be created in the `~/blog/` directory of your home and you simply
have to edit it using markdown.


## Moderate and publish

The editor will be able to review and moderate the article queue using the
command:

```
$ zine --moderate
```

To publish all accepted articles execute:

```
$ zine --publish
```


