function updatePhoneNumberForm() {
  var phone0 = document.getElementById('id_phone_0');
  phone0.parentElement.insertBefore(document.createTextNode("+1 ( "), phone0)
  var phone1 = document.getElementById('id_phone_1');
  phone1.parentElement.insertBefore(document.createTextNode(" ) "), phone1)
  var phone2 = document.getElementById('id_phone_2');
  phone2.parentElement.insertBefore(document.createTextNode(" - "), phone2)
}
