/**
 * Created by daddyslab on 2016. 8. 16..
 */
$(document).ready(function () {
    var classSelect = $('.className');
    var timeSelect = $('.timeValue');

    var IMP = window.IMP;
    IMP.init('iamport'); // iamport -> 가맹점식별코드


    $('.tab').click(function () {
        var moduleText = $(this).find('p').html();
        var module = {moduleName: moduleText};
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
                    var appendClass = $("<div><a href='pages/payment_1.html'>" + name + "</a></div>");
                    $('.' + code).append(appendClass);
                }

                $('td div a').click(function () {
                    var targetData = {targetClassName: $(this).html(), targetCourseName: ""};

                    if (targetData.targetClassName[1] == 'M')
                        targetData.targetCourseName = 'Maker';
                    else if (targetData.targetClassName[1] == "C")
                        targetData.targetCourseName = 'Creator';
                    else
                        targetData.targetCourseName = 'Starter';

                    $.ajax({
                        url: '/selectedPay',
                        type: "post",
                        data: targetData,
                        success: function (data) {
                            console.log(data);
                            $('.courseName').val(data.courseName);
                            $('.className').val(data.className);
                        }
                    });
                });
            }

        });
    });

    $('.courseName').change(function () {
        if ($(this).val() != '-') {
            $.ajax({
                url: '/pages/payment_1.html',
                type: 'POST',
                data: {levelName: $(this).val()},
                success: function (data) {
                    var classes = JSON.parse(data);
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
                url: '/pages/payment_2.html',
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

    $('.btn_pay_ok').click(function () {
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
            name: '주문명:결제테스트',
            amount: 14000,
            buyer_email: 'iamport@siot.do',
            buyer_name: '구매자이름',
            buyer_tel: '010-1234-5678',
            buyer_addr: '서울특별시 강남구 삼성동',
            buyer_postcode: '123-456'
        }, function (rsp) {
            if (rsp.success) {
                var msg = '결제가 완료되었습니다.';
                msg += '고유ID : ' + rsp.imp_uid;
                msg += '상점 거래ID : ' + rsp.merchant_uid;
                msg += '결제 금액 : ' + rsp.paid_amount;
                msg += '카드 승인번호 : ' + rsp.apply_num;
                alert(msg);
            } else {
                var msg = '결제에 실패하였습니다.';
                msg += '에러내용 : ' + rsp.error_msg;
                alert(msg);
            }
        });
    });
});