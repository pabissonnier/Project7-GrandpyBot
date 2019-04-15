// Block empty form send and error message

var validation = document.getElementById('send_button');
var elementSent = document.getElementById('quest');
var elementNull = document.getElementById('missing_text');
validation.addEventListener('click', f_valid);

function f_valid(e){
    if (elementSent.validity.valueMissing){
        e.preventDefault();
        elementNull.textContent = "Tu n'as rien écrit !";
        elementNull.style.color = 'red';
    }
}


// Get the text from the form
<script type="text/javascript">
    $(function() {
        $('a#process_input').bind('click', function() {
            $.getJSON('/_answer', {
                quest: $("input[name='quest']").val(),
            }, function(data) {
                $("#result").text(data.result);
            });
            return false;
        });
    });
</script>

