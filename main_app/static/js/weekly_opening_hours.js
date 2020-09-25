function updateEnable() {
for (i = 0; i < 7; i++) {
    prefix = 'id_opening_hours_' + i + '_'
    console.log(prefix)
    opening_time = document.getElementById(prefix + '0')
    closing_time = document.getElementById(prefix + '1')
    toggle = document.getElementById(prefix + '2')
    opening_time.disabled = !toggle.checked
    closing_time.disabled = !toggle.checked
}
}

function initializeOpeningHourBehavior() {
for (i = 0; i < 7; i++) {
    prefix = 'id_opening_hours_' + i + '_'
    console.log(prefix)
    opening_time = document.getElementById(prefix + '0')
    closing_time = document.getElementById(prefix + '1')
    toggle = document.getElementById(prefix + '2')
    toggle.addEventListener("change", updateEnable)
}
}
