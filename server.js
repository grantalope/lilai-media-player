var express = require('express');
var serveStatic = require('serve-static');

var app = express();

app.use(serveStatic('public', {'index': ['index.html']}));
app.listen(process.env.PORT || 5000);

console.log('Server started on port ' + (process.env.PORT || 5000));
