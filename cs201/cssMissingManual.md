## Basic about HTML5
For tags in HTML5 like \<audio\> and \<video\>,  it won't work in browser lower than IE9. Add code below to reference external js to make them work.
~~~
<!--[if lt IE 9]>
<script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
<![endif]-->
~~~
This is called "Internet Explorer conditional comment" (IECC)
This code only affects how the browser displays and prints HTML5 tags; it doen't make the browser understand and HTML5 tag that actually does something.

\<div\>in HTML4 and XHTML have more semantic tags like \<article\>, \<section\>, \<aside\>, \<footer\>.
##### HTML to forget
- ditch \<font\> for controlling the display of text
- don't use the \<b\> and \<i\>tags to emphasize text
- skip the \<table\> tag for page layout
- avoid the awkward \<body\> tag attributes
- don't abuse the \<br\> tag

##### HTML to forget -- good part
- \<q\> for short quotes, \<blackquote\> for long quotes
- \<dl\> for definition list, \<dd\> for definition description
- \<cite\> for referencing a book title, newspaper title, or website
- \<address\> for identifying and supplying contact information for the author of the page
- use \<div\> and \<span\> for hard defining area

online validator for HTML: <http://validator.w3.org>

#####compatibility
for IE8, add code below to stop it from the compatible view
~~~
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
~~~
You must implement this on every page of your site.
