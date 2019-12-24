# appear

A python package for making hidden details of your application magically appear by streaming them to the browser.

### Installation

Run `pip install appear`

### When and why should you use Appear?

Use appear if you have a python application which has information you want to visualize in a browser whilst the application is running.

- Low overhead on the data sender, only one line to send data.
- The application sending the data doesn't have to alter it's function signatures because information is sent via side effects.
- Low overhead on the frontend, appear takes care of all the data transfer related stuff so you can focus on how to display your data.
- Flexible, handles multiple visualizations in one page.

### Structure

Appear has 3 main parts.
1. A helper function to send data from your application.
2. A server which relays your data to the browser using socket.io
3. A frontend package which makes it easy to receive the data sent from the server and use them for visualizations.

### Usage

##### 1. Send data from your application

First add functions to the codebase you want to instrument by calling the appear helper method.

```python
from appear import helper

###### Your application code here #####

# In the middle of your application code add the following method call to send data
helper(
    url="http://localhost:5000/broadcast",  # This is the url of the Appear server
    target="myVisualizationName",  # Name of the visualization to update
    data={"datapoints":[1,2,3], "title": "My Graph"},  # Data to send to the visualization
)
```

The data sent in the data argument can be any JSON serializable data.

##### 2. Write frontend code

The frontend code needs 3 things;
1. Include socket.io and the server connection code with
```html
<script src="//cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js" integrity="sha256-yr4fRk/GU1ehYJPAs8P4JlTgu0Hdsp4ZKrx8bDEDC3I=" crossorigin="anonymous"></script>
<script src="static/vis_server.js"></script>
```
2. Connect to the server, eg `server = new VisServer()`.
3. Connect a function to a visualization, eg `server.subscribe("visualizationName", update_my_vis)`. You can connect multiple visualizations at once by calling the subscribe method multiple times.

A complete example of what the frontend code can look like is shown below;

```html
<!DOCTYPE HTML>
<html>

<head>
    <title>Appear</title>
    <script src="static/vis_server.js"></script>
    <script type="text/javascript" charset="utf-8">
    // Visualization function
    function update_my_vis(msg) {
        document.getElementById("visualizationName").textContent = "Number of entities " + msg.entities + " out of " + msg.limit
    }

    // Link visualization functions to content
    server = new VisServer()
    server.subscribe("visualizationName", update_my_vis)
    </script>
</head>

<body>
    <h1>Appear</h1>
    <p id="visualizationName"></p>
</body>

</html>
```

Save your html inside a new folder named templates, and call the file index.html. Eg. `templates/index.html`

##### 3. Run appear server

Run the appear server. Make sure that the `templates` directory matches the directory of the frontend code you created.

`python -m appear.app templates`

##### 4. Start using appear

Open a browser to http://localhost:5000 and then start your application. You should see your frontend when the page loads. Each time your application calls the helper method the data in the browser will be updated using the frontend function which you linked.

### Working sample

Try out the sample included in this repo in the samples folder;
1. Run `python -m appear.app sample/templates`
2. Open a browser to http://localhost:5000
3. In another terminal run `python sample/example_app.py`
4. The browser will update with live data from the running application.
