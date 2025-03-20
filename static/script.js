$(document).ready(function() {
    $(".option-btn").click(function(){
        const questionDiv = $(this).closest('.question');
        questionDiv.find('.option-btn').removeClass('selected');
        $(this).addClass('selected');
        const value = $(this).data('value');
        questionDiv.find('.response-input').val(value);
    })

    $("form").submit(function(e){
        let allAnswered = true;
        $('.response-input').each(function(){
            if(!$(this).val()){
                allAnswered = false;
            }
        })
        if(!allAnswered){
            alert('Please answer all the questions before submitting!');
            return false;
        }
        return true;
    })
})