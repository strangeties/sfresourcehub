function updateEnable() {
for (i = 0; i < 7; i++) {
    prefix = 'id_opening_hours_' + i + '_'
    toggle = document.getElementById(prefix + '0')
    opening_time = document.getElementById(prefix + '1')
    closing_time = document.getElementById(prefix + '2')
    opening_time.disabled = !toggle.checked
    closing_time.disabled = !toggle.checked
    opening_time.style.visibility = toggle.checked ? 'visible' : 'hidden'
    closing_time.style.visibility = toggle.checked ? 'visible' : 'hidden'
}
}

function initializeOpeningHourBehavior() {
for (i = 0; i < 7; i++) {
    prefix = 'id_opening_hours_' + i + '_'
    toggle = document.getElementById(prefix + '0')
    opening_time = document.getElementById(prefix + '1')
    closing_time = document.getElementById(prefix + '2')
    toggle.addEventListener("change", updateEnable)
}
}
