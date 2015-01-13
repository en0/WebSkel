## SKEL <small>Angularjs/Bootstrap</small>

This is a skeleton for angularjs with bootstrap under python-flask.

### The following files are refrenced from the root of web application

<dl>
    <dt>/templates/index.html</dt>
    <dd>The site template for angularjs. Loads angular, bootstrap and site files</dd>
    <dt>/templates/partials/*</dt>
    <dd>All the partials for the angularjs views</dd>
    <dt>/static/js/*</dt>
    <dd>Site specific javascript files</dd>
    <dt>/static/js/ui-bootstrap-tpls-0.11.2.min.js</dt>
    <dd>Bootstrap components for angularjs</dd>
    <dt>/static/css/site.css</dt>
    <dd>Site wide CSS files (empty).</dd>
</dl>

Since Angular and flask use the same layout variable syntax. ie: {{ VARIABLE }}
    
The Angularjs interpolation has been modified to: [[ Angular_Variable ]]

If you wish to use a diffrent delimiter, you can modify the character in /static/js/app.js

### External Links

*   [Bootstrap CSS](http://getbootstrap.com/css/)
*   [AngularJS Bootstrap Directives](http://angular-ui.github.io/bootstrap/)
*   [Flask Documentation](http://flask.pocoo.org/docs/0.10/)
*   [Flask-RESTful Documentation](https://flask-restful.readthedocs.org/en/0.3.1/)
