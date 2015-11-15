function init_code_hierarchy_plot(element_id,data,count_function,color_function,title_function,legend_function)
{
    var plot = document.getElementById(element_id);

    while (plot.hasChildNodes())
    {
        plot.removeChild(plot.firstChild);
    }

    var width = plot.offsetWidth;
    var height = width;
    var x_margin = 40;
    var y_margin = 40;

    var max_depth=3;

    var data_slices = [];
    var max_level = 2;

    var svg = d3.select("#"+element_id).append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    function process_data(data,level,start_deg,stop_deg,category_name)
    {
        var name = data[0];
        var total = count_function(data);
        var children = data[2];
        var current_deg = start_deg;
        if (level > max_level)
        {
            return;
        }
        if (start_deg == stop_deg)
        {
            return;
        }
        if (level > 0) {
            d = [start_deg,stop_deg,name,level,data[1],category_name ? category_name : name];
            data_slices.push(d);
        }
        for (var key in children)
        {
            child = children[key];
            var inc_deg = (stop_deg-start_deg)/total*count_function(child);
            var child_start_deg = current_deg;
            current_deg+=inc_deg;
            var child_stop_deg = current_deg;
            var span_deg = child_stop_deg-child_start_deg;
            process_data(child,level+1,child_start_deg,child_stop_deg,name);
        }
    }

    process_data(data,0,Math.PI*(6.0/7.0),Math.PI*(6.0/7.0) + 360./180.0*Math.PI);

    var ref = data_slices[0];
    var next_ref = ref;
    var last_refs = [];

    var thickness = width/2/(max_level+6)*1.1;

    function radius(level) {
        return (level + 3) * thickness;
    }

    var arc = d3.svg.arc()
    .startAngle(function(d) { if(d[3]==0){return d[0];}return d[0]+0.01; })
    .endAngle(function(d) { if(d[3]==0){return d[1];}return d[1]-0.01; })
    .innerRadius(function(d) { return (radius(d[3])); })
    .outerRadius(function(d) { return (radius(d[3]+0.9)); });

    var innerSlices = svg.selectAll(".form")
        .data(function(d) { return data_slices;})
        .enter()
        .append("g");
        innerSlices.append("path")
        .attr("d", arc)
        .attr("id",function(d,i){return element_id+i;})
        .style("fill", function(d) { return color_function(d);})
        .attr("class","form")
        .attr("opacity", 0.5);
/*
    var outerSlices = svg.selectAll(".form")
        .data(function(d) { return data_slices.filter(function(d) {return true; d[3] == 2;}); })
        .enter()
        .append("g");
        outerSlices.append("path")
        .attr("d", arc)
        .attr("id",function(d,i){return element_id+i;})
        .style("fill", function(d) { console.log(d); return color_function(d);})
        .attr("class","form");
    var outerArc = d3.svg.arc()
    .startAngle(function(d) { if(d[3]==0){return d[0];}return d[0]+0.01; })
    .endAngle(function(d) { if(d[3]==0){return d[1];}return d[1]-0.01; })
    .innerRadius(function(d) { return 1.2*(d[3]+2)*thickness; })
    .outerRadius(function(d) { return (1.2*(d[3]+2)+1)*thickness; });
*/

    /* ------- TEXT LABELS -------*/
    // Add a legendLabel to each arc slice...
    /*
    innerSlices.append("svg:text")
      .attr("transform", function(d) { //set the label's origin to the center of the arc
        console.log(d);
        return "translate(" + arc.centroid(d) + ")";
      })
      .attr("text-anchor", "middle") //center the text on it's origin
      .style("fill", "Black")
      .style("font", "bold 16px Arial")
      .text(function(d, i) { if (d[3]==1) {return d[2];} else {return '';} }); //get the label from our original data array
    */

    var legend = svg.append("svg:text")
      .attr("text-anchor", "middle")
      .style("fill", "Black")
      .style("font", "bold 16px Arial")
      .text("Feelings");

    if (legend_function != undefined)
    {
        innerSlices.on("mouseover",update_legend)
              .on("mouseout",remove_legend);

        function update_legend(d)
        {
            legend.text(legend_function(d));
            legend.transition().duration(200).style("opacity","1");
        }

        function remove_legend(d)
        {
            legend.transition().duration(1000).style("opacity","0");
        }
    }
    /*
    function get_start_angle(d,ref)
    {
        if (ref)
        {
            var ref_span = ref[1]-ref[0];
            return (d[0]-ref[0])/ref_span*Math.PI*2.0
        }
        else
        {
            return d[0];
        }
    }
    */

    function get_stop_angle(d,ref)
    {
        if (ref)
        {
            var ref_span = ref[1]-ref[0];
            return (d[1]-ref[0])/ref_span*Math.PI*2.0
        }
        else
        {
            return d[0];
        }
    }

    function get_level(d,ref)
    {
        if (ref)
        {
            return d[3]-ref[3];
        }
        else
        {
            return d[3];
        }
    }

    var animating = false;


}

function init_plots()
{
  console.log('hello world');
    var sidebar = document.getElementById("sidebar");
    var sidebarButton = document.getElementById("sidebar-button");

    function openSidebar(e) {
      if (sidebar.className.indexOf("slideIn") != -1) {
        sidebar.className = sidebar.className.replace(" slideIn", "");
      } else {
       sidebar.className = sidebar.className + " slideIn";
      }
    }

    sidebarButton.addEventListener("click", openSidebar, false);

    function count_function(d)
    {
        return d[1];
    }

    function label_function(d)
    {
        return d[2]+": "+d[4]+" votes";
    }

    function legend_function(d)
    {
        return d[2];
    }

    var color = d3.scale.category20();

    var color_buckets = {
        'communication': d3.rgb('#FF6103'), // orange
        'productivity': d3.rgb('#FFB90F'), // goldenrod
        'isolation': d3.rgb('#2E0854'), // purple
        'logistics': d3.rgb('#C0FF3E'), // olive
        'nothing': d3.rgb('aaaacc'), // greyish blue
        'pants': d3.rgb('#0000aa'),
        'balance': d3.rgb('#5E2612') // sepia
    }

    function color_function(d)
    {
        if (d[3]==2) {
            return color_buckets[d[5]];
        } else {
            return color_buckets[d[2]];
        }
    }
    d3.select(self.frameElement).style("height", "800px");
    d3.json("/dist/data.json", function(error, json) {
        init_code_hierarchy_plot("code_hierarchy",json,count_function,color_function,label_function,legend_function);
    });
}

window.addEventListener('load', init_plots, false);
