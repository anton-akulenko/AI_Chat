
    function submitForm() {
    // Створюємо новий об'єкт FormData
    let formData = new FormData(document.getElementById("uploadForm"));

    // Виконуємо запит на сервер
    fetch('{% url 'upload_pdf' %}', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())  // Перетворюємо відповідь у JSON
    .then(data => {
    if (data.error) {
        // Якщо у відповіді є ключ 'error', покажіть повідомлення користувачеві
        Swal.fire({
            icon: 'error',
            title: 'ERROR',
            text: data.error,
        });
    } else if (data.success) {
        // Обробляємо успішну відповідь (наприклад, перезавантаження сторінки)
        location.reload();
    }
})

    .catch(error => {
        console.error('Помилка:', error);
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Unknown error.Try again',
        });
    });
}



function triggerFileSelect() {
    document.getElementById("{{ form.pdf_document.auto_id }}").click();
}

    function toggleNav() {
     var sidenav = document.getElementById("mySidenav");
     if (sidenav.style.width == "0px" || sidenav.style.width == "") {
         sidenav.style.width = "250px";

         // якщо потрібно щоб елемент змістився як меню вистав px
         document.getElementById("main").style.marginLeft = "0px";
     } else {
         sidenav.style.width = "0";
         document.getElementById("main").style.marginLeft= "0";
     }
 }

    document.getElementById("textInput").addEventListener("focus", function() {
    var selectedPdfValue = document.getElementById("sidenav_selected_pdf").value;
    document.getElementById("main_selected_pdf").value = selectedPdfValue;
});

// форматування часу
function formatTimestamp(timestampStr) {
    const timestamp = new Date(timestampStr);
    const options = {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour24: true

    };

    let formatted = new Intl.DateTimeFormat('en-US', options).format(timestamp);

    formatted = formatted.replace(/, (\d{4}),/, ", $1,")
                         .replace(/:\d{2} /, ' ')
                         .replace(" AM", " a.m.")
                         .replace(" PM", " p.m.");

    return formatted;
}

// виводити історію при виборі файлу
document.getElementById("sidenav_selected_pdf").addEventListener("change", function() {
    let selectedPdf = this.value;

    fetch(`/llm_chat/get_chat_history?pdf_id=${selectedPdf}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const chatHistoryList = document.querySelector(".chat-history");
        chatHistoryList.innerHTML = ""; // Очищуємо поточний список повідомлень

        data.forEach(message => {
            let formattedTimestamp = formatTimestamp(message.timestamp);
            let messageItem = `
                    <div class="text-center">
                        <p>${formattedTimestamp}</p>
                    </div>
                    <div class="message sent">
                        {% if avatar_url %}
                        <img src="{{ avatar_url }}" alt="Avatar">
                        {% else %}
                        <img src="{% static 'llm_chat/img/human.png' %}" alt="Avatar">
                        {% endif %}
                        <p>${message.message}</p>
                    </div>
                    <div class="message received">
                        <img src="{% static 'llm_chat/img/bot.png' %}" alt="Avatar" class="right">
                        <p>${message.answer}</p>
                    </div>
            `;
            chatHistoryList.innerHTML += messageItem;
        });
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error.message);
        Swal.fire({
            icon: 'error',
            title: 'Loading failed',
            text: 'Sorry, there was a problem loading the chat history.',

        });
        // Додайте повідомлення про помилку для користувача, якщо це необхідно.
        // Наприклад: alert('Sorry, there was a problem loading the chat history.');
    });
});
</script>
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
<script>
    // повідомлення зникає через 5 сек
    setTimeout(function(){
        var alerts = document.querySelectorAll(".alert");
        alerts.forEach(function(alert){
            alert.style.display = "none";
        });
    }, 5000);
</script>
<script>
    document.getElementById("questionForm").addEventListener("submit", function(event) {
    var textInput = document.getElementById("textInput").value.trim();

    if (!textInput) {
        event.preventDefault();
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Please enter a message before sending.',
            confirmButtonColor: '#3085d6',
        });
    }
});

</script>
<script>
    // Отримуємо посилання на елемент контейнера
    var chatHistoryContainer = document.getElementById("chat-history");
    // Прокручуємо контейнер до нижнього краю
    chatHistoryContainer.scrollTop = chatHistoryContainer.scrollHeight;
</script>