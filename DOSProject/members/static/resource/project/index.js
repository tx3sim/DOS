/**
 * Created by daddyslab on 2016. 8. 16..
 */
$(document).ready(function () {
    var courseSelect = $('.courseSelect');
    var subjectSelect = $('.subjectSelect');
    var timeSelect = $('.timeSelect');
    var moduleName = $('.moduleName').find('strong').html();
    var module = {moduleName: moduleName};
    var course = "Starter";

    if (moduleName) {
        if (moduleName[1] == "M")
            course = "Maker";
        else if (moduleName[1] == "C")
            course = "Creator";
    }

    if ($('.tab'))
        getTimetable(module, course);

    var IMP = window.IMP;
    IMP.init('imp10434785'); // iamport -> 가맹점식별코드


    $('.tab').click(function () {
        moduleName = $(this).find('.moduleName').find('strong').html();
        module = {moduleName: moduleName};
        course = "Starter";

        if (moduleName[1] == "M")
            course = "Maker";
        else if (moduleName[1] == "C")
            course = "Creator";

        getTimetable(module, course);
    });

    courseSelect.change(function () {
        if ($(this).val() != '-') {
            $.ajax({
                url: '/altCourse',
                type: 'POST',
                data: {course: $(this).val()},
                success: function (data) {
                    var subjects = JSON.parse(data);
                    subjectSelect.find('option:not(:first)').remove();
                    timeSelect.find('option:not(:first)').remove();
                    for (var i in subjects) {
                        var isOverlap = false;
                        var subjectName = subjects[i].subject__name;
                        subjectSelect.find('option').each(function () {
                            if ($(this).html() == subjectName)
                                isOverlap = true;
                        });
                        if (!isOverlap) {
                            subjectSelect.append($("<option value='" + subjectName + "'>" + subjectName + "</option>"));
                        }
                    }
                }
            })
        }
    });

    subjectSelect.change(function () {
        if ($(this).val() != '-') {
            $.ajax({
                url: '/altClass',
                type: 'POST',
                data: {subjectName: $(this).val()},
                success: function (data) {
                    var subjects = JSON.parse(data);
                    timeSelect.find('option:not(:first)').remove();
                    for (var i in subjects) {
                        var time = subjects[i].time;
                        timeSelect.append($("<option value='" + time + "'>" + time + "</option>"));
                    }
                }
            })
        }
    });

    $('.btn_pay_ok').click(function () {
        var subject = $('.applySubject').html().replace(/\s/g,'').replace(/\n/g,'');
        var time = $('.applyTime').html().replace(/\s/g,'').replace(/\n/g,'');
        var childName = '';
        
        if($('.childSelect'))
            childName = $('.childSelect').val();
        else if($('.applyChildName'))
            childName = $('.applyChildName').html().replace(/\s/g,'').replace(/\n/g,'');

        $.ajax({
            type: 'POST',
            url: '/apply_3_2',
            data: {subject: subject, time: time},
            success: function (data) {
                console.log(data);
                IMP.request_pay({
                    pg: 'inicis', // version 1.1.0부터 지원.
                    /*
                     'kakao':카카오페이,
                     'inicis':이니시스, 'html5_inicis':이니시스(웹표준결제),
                     'nice':나이스,
                     'jtnet':jtnet,
                     'uplus':LG유플러스,
                     'danal':다날
                     */
                    pay_method: 'card', // 'card':신용카드, 'trans':실시간계좌이체, 'vbank':가상계좌, 'phone':휴대폰소액결제
                    merchant_uid: 'merchant_' + new Date().getTime(),
                    name: data.semester + ' / ' + data.course + ' / ' + data.subject + ' / ' + time,
                    amount: 100,
                    buyer_email: data.email,
                    buyer_name: data.memberName,
                    buyer_tel: data.phoneNumber,
                    buyer_addr: data.address
                    //buyer_postcode: '123-456'
                }, function (rsp) {
                    if (rsp.success) {
                        var msg = '결제가 완료되었습니다.';
                        msg += '고유ID : ' + rsp.imp_uid;
                        msg += '상점 거래ID : ' + rsp.merchant_uid;
                        msg += '결제 금액 : ' + rsp.paid_amount;
                        msg += '카드 승인번호 : ' + rsp.apply_num;
                        $.ajax({
                            type: 'POST',
                            url: 'payment_result',
                            data: {subject: data.subject, time: data.time, childName: childName},
                            success: function(data) {
                                window.location.href = '/payment_result?name=' + rsp.name + '&applyNum=' + rsp.apply_num + '&amount=' + rsp.paid_amount + '&childName=' + childName
                            }
                        })
                        
                    } else {
                        var msg = '결제에 실패하였습니다.';
                        msg += '에러내용 : ' + rsp.error_msg;
                        alert(msg);
                    }
                });
            }
        });
    });

    if ($('.btn_register'))
        $('.btn_register').css('cursor', 'pointer');
    if ($('.btn_pay_ok'))
        $('.btn_pay_ok').css('cursor', 'pointer');
    $('.btn_prev').css('cursor', 'pointer');
    $('.btn_next').css('cursor', 'pointer');
    $('.btn_newChild').css('cursor', 'pointer');

    $('.btn_register').click(function () {
        if(subjectSelect.val() != subjectSelect.find('option:first').val() && timeSelect.val() != timeSelect.find('option:first').val())
            window.location.href = "apply_2?course=" + courseSelect.val() + "&subject=" + subjectSelect.val() + "&time=" + timeSelect.val();
        else
            alert('클래스 및 시간대를 정확히 선택해주세요.');
    });

    $('.btn_prev').click(function () {
        parent.history.back();
        return false;
    });

    $('.check_all').click(function() {
        if($('.check_all').prop("checked"))
            $('input[type=checkbox]').prop("checked", true);
        else
            $('input[type=checkbox]').prop("checked", false);
    });

    $('.btn_newChild').click(function() {
        var subject = $('.applySubject').html().replace(/\s/g,'').replace(/\n/g,'');
        var time = $('.applyTime').html().replace(/\s/g,'').replace(/\n/g,'');
        window.location.href = '/apply_3_1_1?subject=' + subject + '&time=' + time;
    });
    
    $('.form_newChild').submit(function() {
        $.ajax({
            type: 'POST',
            url: 'apply_3_1_1',
            data: $(this).serialize(),
            success: function(data) {
                console.log(data);
                window.location.href = 'apply_3_1?subject=' + data.subject + '&time=' + data.time;
            }
        })
    });

    $('.form_register').submit(function () {
        if ($('.input_password1').val() == $('.input_password2').val()) {
            $.ajax({
                type: 'POST',
                url: 'apply_2',
                data: $(this).serialize(),
                success: function (data) {
                    window.location.href = '/apply_3_2?course=' + data.course + '&subject=' + data.subject + '&time=' + data.time + '&childName=' + data.childName;
                }
            })
        }
        else
            alert("비밀번호가 일치하지 않습니다. 다시 입력해주세요.");
    });

    $('.form_login').submit(function () {
        $.ajax({
            type: 'POST',
            url: '/login',
            data: $(this).serialize(),
            success: function (data) {
                console.log(data);
                if (data.result == 'error')
                    alert('이메일주소 또는 비밀번호가 올바르지 않습니다');
                else
                    window.location.href = '/apply_3_1?course=' + data.course + '&subject=' + data.subject + '&time=' + data.time;
            }
        })
    })
});

var getTimetable = function (module, course) {
    $('.apply').children().remove();
    $('.apply').append($("<a href='apply_1?course=" + course + "'>신청하기</a>"));

    $.ajax({
        url: '/tt',
        type: 'POST',
        data: module,
        success: function (data) {
            $('tbody').find('tr').find('td:not(:first)').html("");
            var timetable = JSON.parse(data);
            for (var i in timetable) {
                var time = timetable[i].time;
                var name = timetable[i].subject__name;
                var applyTd = $('.' + time);
                var appendSubject = $("<div><a href='apply_1?course=" + course + "&subject=" + name + "&time=" + time + "'>" + name + "</a></div>");
                applyTd.append(appendSubject);
                applyTd.css('color', '#ffffff');
                applyTd.css('background-color', 'rgba(243,166,180,0.60)');
                applyTd.mouseleave(function () {
                    $(this).css('background-color', 'rgba(243,166,180,0.60)')
                });
                applyTd.mouseover(function () {
                    $(this).css('background-color', '#F3A6B4');
                });
            }
        }
    });
};