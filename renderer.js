const time = document.getElementById('currentTime');

function updateTime() {
    const currentDate = new Date();
    time.innerHTML = currentDate.getHours() + ':' + currentDate.getMinutes();
}

updateTime();
setTimeout(updateTime, 30000);