function updateCurrentYear() {
    var releaseYear = `2025`
    var today = new Date();
    var currentYear = today.getFullYear();
    var yearElement = document.getElementById('current-year');

    if(yearElement){
        if (releaseYear == currentYear)
            yearElement.textContent = currentYear
        else{
            yearElement.textContent = `${releaseYear} - ${currentYear}`
        }
    } else console.error("Element with id 'current-year' not found");
}

document.addEventListener('DOMContentLoaded', updateCurrentYear);