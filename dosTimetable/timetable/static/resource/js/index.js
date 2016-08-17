/**
 * Created by daddyslab on 2016. 8. 16..
 */
$(document).ready(function () {
    var classSelect = $('.className');
    var timeSelect = $('.timeValue');

    $('.tab').click(function () {
        var module = {moduleName: $(this).find('p').html()};
        $.ajax({
            url: '/tt',
            type: 'POST',
            data: module,
            success: function (data) {
                $('tbody').find('tr').find('td:not(:first)').html("");
                var timetable = JSON.parse(data);
                for (var i in timetable) {
                    var code = timetable[i].fields.classCode;
                    var name = timetable[i].fields.className;
                    var appendClass = $("<div>" + name + "</div>");
                    $('.' + code).append(appendClass);
                }
            }
        })
    });

    $('.courseName').change(function () {

        if ($(this).val() != '-') {
            $.ajax({
                url: '/getClass',
                type: 'POST',
                data: {levelName: $(this).val()},
                success: function (data) {
                    var classes = JSON.parse(data);
                    console.log(classes);
                    classSelect.find('option:not(:first)').remove();
                    timeSelect.find('option:not(:first)').remove();
                    for (var i in classes) {
                        var isOverlap = false;
                        var className = classes[i].fields.className;
                        classSelect.find('option').each(function () {
                            if ($(this).html() == className)
                                isOverlap = true;
                        });
                        if (!isOverlap) {
                            classSelect.append($("<option value='" + className + "'>" + className + "</option>"));
                        }
                    }
                }
            })
        }
    });

    $('.className').change(function () {

        if ($(this).val() != '-') {
            $.ajax({
                url: '/getTime',
                type: 'POST',
                data: {className: $(this).val()},
                success: function (data) {
                    var classes = JSON.parse(data);
                    timeSelect.find('option:not(:first)').remove();
                    for (var i in classes) {
                        var classCode = classes[i].fields.classCode;
                        timeSelect.append($("<option value='" + classCode + "'>" + classCode + "</option>"));
                    }
                }
            })
        }
    });
});