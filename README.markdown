Hyde implementation of guillaume.dedrie.fr
==========================================
This is the source code of my own website. Powered using [Hyde] You can see the result at [http://guillaume.dedrie.fr].


License
=======
The source code of this website is released under the [MIT License].


How to
======
Setup
-----
 1. Install virtualenv && virtualenwrapper
 2. Create a virtualenv and install Fabric and Hyde
 3. Clone this repository
    ``` 
    git clone https://github.com/guillaumededrie/guillaume.dedrie.fr.git
    ```
 4. Copy and customize the fabfile.py.dist to fabfile.py (at the root of the project)
 5. Copy and customize the nginx.conf.py to content/nginx.conf
 6. Launch your hyde environment

Run the website (local)
-----------------------
In your hyde environment
 1. Use `fab serve` and launch your browser to the `localhost:8080` url
 2. You can use hyde built in command such as :
    * `hyde gen - generate the website`
    * `hyde serve - serve the website to the localhost:8080 url`


Deploy
------
Using fabric (with the fabfile.py.dist you customized), just launch `fab deploy`.


Todo
====
 - English version (Running)
 - Add RSS (Runnig)
 - Add js search engine



[hyde]: https://github.com/hyde/hyde
[http://guillaume.dedrie.fr]: http://guillaume.dedrie.fr
[MIT License]: http://opensource.org/licenses/mit-license
