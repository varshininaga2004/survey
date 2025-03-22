$(document).ready(function() {
    $(".option-btn").click(function(){
        const questionDiv = $(this).closest('.question');
        questionDiv.find('.option-btn').removeClass('selected');
        $(this).addClass('selected');
        const value = $(this).data('value');
        questionDiv.find('.response-input').val(value);
    })

    $('#survey-form').submit(function(e){
        e.preventDefault();
        let allAnswered = true;
        let surveyData = [];
        $(".question").each(function(){
            const questionId = $(this).data('question-id');
            const selectedAnswer = $(this).find('.option-btn.selected').data('value');
            if(selectedAnswer){
                surveyData.push({
                    'question_id': questionId,
                    'answer': selectedAnswer
                });
            }else{
                allAnswered = false;
                alert('Please answer all the questions before submitting!');
                return false;
            }
        })

        if(allAnswered){
            $.ajax({
                type: 'POST',
                url: submitSurveyUrl,
                data: JSON.stringify({
                    'survey_data': surveyData
                }),
                contentType: "application/json",
                headers: {
                    "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function(response){
                    $('.option-btn').removeClass('selected');
                    $('#survey-form')[0].reset();
                    alert(response.message);
                },
                error: function(error) {
                    alert("Error submitting survey. Please try again.")
                }
            })
        }
    })
})