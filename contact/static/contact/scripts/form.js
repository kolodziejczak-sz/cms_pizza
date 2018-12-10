const formEl = document.getElementById("message-form"),
  emailEl = document.getElementById("message-email"),
  subjectEl = document.getElementById("message-subject"),
  messageEl = document.getElementById("message-message"),
  alertEl = document.getElementById("message-alert")

function onSubmitClick(e) {
  e.stopPropagation();
  e.preventDefault();
  alert('');
  if(validate()) {
    post('/api/message', getFormValue())
      .then(_ => {
        alert('Message sent.');
        formEl.reset();
      })
      .catch(err => alert('Sending message failed. You might wanna try it again.'))
  } else {
    alert('Fill all form controls to send message.');
  }
}

function post(url, body) {
  return fetch(url, {
    method: 'POST',
    cache: 'no-cache',
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'X-CSRFToken': csrf_token,
      'X-Requested-With': 'XMLHttpRequest'
    },
    body: JSON.stringify(body),
  })
  .then(response => response.json());
}

function alert(text) {
  alertEl.textContent = text;
}

function validate() {
  return (emailEl.value && subjectEl.value && messageEl.value);
}

function getFormValue() {
  return {
    email: emailEl.value,
    subject: subjectEl.value,
    message: messageEl.value
  }
}

formEl.onsubmit = onSubmitClick;