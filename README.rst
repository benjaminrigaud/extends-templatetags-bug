
I have two inclusion templatetags specifying their parent template in their context.

In 1.7.7 I have:

  hello
  
  content 1
  
  hello 2
  
  content 2
  

In 1.8c1 I have:

  hello
  
  content 1
  
  hello 2
  
  content 1
  
  
see https://gist.github.com/benjaminrigaud/e646f51e1a6dfe232c68
