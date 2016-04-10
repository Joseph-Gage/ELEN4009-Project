// define chart size (width and height of image set to diameter size)
var diameter = 960,
    format = d3.format(",d"),
    color = d3.scale.category20c();

// create bubble image class
var bubble = d3.layout.pack()
    .sort(null)
    .size([diameter, diameter])
    .padding(1.5);

// create svg (scalable vector graphic) to house the bubbles
var svg = d3.select("body").append("svg")
    .attr("width", diameter)
    .attr("height", diameter)
    .attr("class", "bubble");

// uses d3 function to read in dummy JSON data
d3.json("/static/js/test.json", function(error, root) {
  if (error) throw error;

// create the nodes for the bubble chart
  var node = svg.selectAll(".node")
      .data(bubble.nodes(classes(root))
      .filter(function(d) { return !d.children; }))
    .enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

// create title for each node, which is comprised of the node word and the node word frequency (e.g. Hello: 25)
  node.append("title")
      .text(function(d) { return d.className + ": " + format(d.value); });

// creates the circle image which the node is represented by and in which the text is displayed.
  node.append("circle")
      .attr("r", function(d) { return d.r; })
      .style("fill", function(d) { return color(d.packageName); });

  node.append("text")
      .attr("dy", ".3em")
      .style("text-anchor", "middle")
      .text(function(d) { return d.className.substring(0, d.r / 3); });
});

// Returns a flattened hierarchy containing all leaf nodes under the root.
function classes(root) {
  var classes = [];

  function recurse(name, node) {
    if (node.children) node.children.forEach(function(child) { recurse(node.name, child); });
    else classes.push({packageName: name, className: node.name, value: node.size});
  }

  recurse(null, root);
  return {children: classes};
}

d3.select(self.frameElement).style("height", diameter + "px");
