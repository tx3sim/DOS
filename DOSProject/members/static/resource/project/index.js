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

    if(moduleName) {
        if (moduleName[1] == "M")
            course = "Maker";
        else if (moduleName[1] == "C")
            course = "Creator";
    }

    getTimetable(module, course);

    // var IMP = window.IMP;
    // IMP.init('iamport'); // iamport -> 가맹점식별코드
    if($('.btn_register')) {
        $('.btn_register').css('cursor', 'pointer')
    }
    $('.btn_prev').css('cursor', 'pointer');
    $('.btn_next').css('cursor', 'pointer');

    $('.btn_register').click(function() {
        window.location.href = "apply_2_1?course=" + courseSelect.val() + "&subject=" + subjectSelect.val() + "&time=" + timeSelect.val()
    });

    $('.btn_prev').click(function() {
        parent.history.back();
		return false;
    });

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
                        var subjectName = subjects[i].fields.subject;
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
                        var time = subjects[i].fields.time;
                        timeSelect.append($("<option value='" + time + "'>" + time + "</option>"));
                    }
                }
            })
        }
    });

//     $('.btn_pay_ok').click(function () {
//         IMP.request_pay({
//             pg: 'inicis', // version 1.1.0부터 지원.
//             /*
//              'kakao':카카오페이,
//              'inicis':이니시스, 'html5_inicis':이니시스(웹표준결제),
//              'nice':나이스,
//              'jtnet':jtnet,
//              'uplus':LG유플러스,
//              'danal':다날
//              */
//             pay_method: 'card', // 'card':신용카드, 'trans':실시간계좌이체, 'vbank':가상계좌, 'phone':휴대폰소액결제
//             merchant_uid: 'merchant_' + new Date().getTime(),
//             name: '주문명:결제테스트',
//             amount: 14000,
//             buyer_email: 'iamport@siot.do',
//             buyer_name: '구매자이름',
//             buyer_tel: '010-1234-5678',
//             buyer_addr: '서울특별시 강남구 삼성동',
//             buyer_postcode: '123-456'
//         }, function (rsp) {
//             if (rsp.success) {
//                 var msg = '결제가 완료되었습니다.';
//                 msg += '고유ID : ' + rsp.imp_uid;
//                 msg += '상점 거래ID : ' + rsp.merchant_uid;
//                 msg += '결제 금액 : ' + rsp.paid_amount;
//                 msg += '카드 승인번호 : ' + rsp.apply_num;
//                 alert(msg);
//             } else {
//                 var msg = '결제에 실패하였습니다.';
//                 msg += '에러내용 : ' + rsp.error_msg;
//                 alert(msg);
//             }
//         });
//     });
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
                var time = timetable[i].fields.time;
                var name = timetable[i].fields.subject;
                var applyTd = $('.' + time);
                var appendSubject = $("<div><a href='apply_1?course=" + course + "&subject=" + name + "&time=" + time + "'>" + name + "</a></div>");
                applyTd.append(appendSubject);
                applyTd.css('color', '#ffffff');
                applyTd.css('background-color', 'rgba(243,166,180,0.60)');
                applyTd.mouseleave(function() {
                    $(this).css('background-color', 'rgba(243,166,180,0.60)')
                });
                applyTd.mouseover(function() {
                    $(this).css('background-color', '#F3A6B4');
                });
            }
        }
    });
};