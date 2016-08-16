/**
 * Created by daddyslab on 2016. 8. 16..
 */
$(document).ready(function () {
    $.ajax({
        url: '/tt',
        type: 'get',
        success: function(data) {
            console.log(data);
            var timetable = JSON.parse(data);
            console.log(timetable);
            // for(var i in starterObj) {
            //     var code = starterObj[i].fields.code;
            //     var name = starterObj[i].fields.name;
            //     var appendClass = $("<div>" + name + "</div>");
            //     $('.' + code).append(appendClass);
        }
    })
});